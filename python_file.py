import pandas
import requests
from bs4 import BeautifulSoup
import sqlite3
import threading
import logging
import time
from queue import Queue

# Logging setup
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

# Shared resources
book_queue = Queue()  # (index, url)
book_data = []
book_data_lock = threading.Lock()

headers = {
    "User-Agent": "Mozilla/5.0"
}

def setup_db():
    con = sqlite3.connect('rokomari_ordered_books0.db')
    cur = con.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS books_info (
            Rank INTEGER,
            Name TEXT,
            Author TEXT,
            Original_Price TEXT,
            Sell_Price TEXT,
            In_Stock TEXT,
            Category TEXT
        )
    """)
    con.commit()
    return con, cur

# Step 1: Collect book links with index
def collect_book_links(pages=4):
    index = 0
    for i in range(1, pages + 1):
        url = f"https://www.rokomari.com/book/category/32/self-help-motivational-and-meditation?sort=SOLD_COUNT_DESC&page={i}"
        logging.info(f"Fetching book links from page {i}: {url}")
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, 'html.parser')
        books = soup.find_all('div', class_='books-wrapper__item')
        logging.info(f"  -> {len(books)} books found on page {i}")
        for book in books:
            a_tag = book.find('a', href=True)
            if a_tag:
                full_url = 'https://www.rokomari.com' + a_tag['href']
                book_queue.put((index, full_url))
                index += 1
    logging.info(f"🔗 All pages fetched. Total links collected: {book_queue.qsize()}")


# Step 2: Worker threads
def book_scraper():
    while not book_queue.empty():
        try:
            idx, url = book_queue.get_nowait()
        except:
            break
        try:
            r = requests.get(url, headers=headers)
            soup = BeautifulSoup(r.text, 'html.parser')
            main = soup.find('div', id='ts--desktop-details-book-main-info')

            name = main.find('h1').text.strip()
            author = ', '.join(a.text.strip() for a in main.find_all('a', href=True))
            category = main.find('p', class_='bookCategory_category__giRM1').text.strip()

            price_div = soup.find('div', class_='priceDetails_priceAndDiscount__oEFMK')
            sell_price = price_div.find('span', class_='sell-price').text.strip()
            original_price = price_div.find('del', class_='original-price').text.strip() if price_div.find('del') else sell_price

            stock = soup.find('figure', class_='flex gap-2')
            stock_text = stock.span.text.strip() if stock and stock.span else 'N/A'

            with book_data_lock:
                book_data.append((idx, {
                    'Name': name,
                    'Author': author,
                    'Original_Price': original_price,
                    'Sell_Price': sell_price,
                    'In_Stock': stock_text,
                    'Category': category
                }))
            logging.info(f"[{idx}] ✅ Scraped: {name}")
        except Exception as e:
            logging.warning(f"❌ Failed [{idx}] {url} | {e}")
        finally:
            book_queue.task_done()

# Step 3: Save to DB in order
def save_to_db():
    con, cur = setup_db()
    for idx, data in sorted(book_data, key=lambda x: x[0]):
        cur.execute("""
            INSERT INTO books_info VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
            idx + 1,
            data['Name'], data['Author'], data['Original_Price'],
            data['Sell_Price'], data['In_Stock'], data['Category']
        ))
    con.commit()
    con.close()
    logging.info("💾 Saved to database.")

# Runner
if __name__ == "__main__":
    start = time.perf_counter()
    pages_to_scrape = 4  # অথবা তুমি যত পেইজ স্ক্র্যাপ করতে চাও
    collect_book_links(pages=pages_to_scrape)
    logging.info(f"📚 Total book links found: {book_queue.qsize()}")

    threads = []
    for _ in range(10):
        t = threading.Thread(target=book_scraper)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    save_to_db()
    logging.info(f"✅ Done in {time.perf_counter() - start:.2f} seconds.")
