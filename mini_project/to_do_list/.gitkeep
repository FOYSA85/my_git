from customtkinter import *
from PIL import Image
import sqlite3 as sql
import calendar
from datetime import datetime
import re
import random

root = CTk()
root.geometry("390x844")
root.title('TaskMangerApp')
root.iconbitmap()

conn = sql.connect("advanced_to_do_list.db")
cursor = conn.cursor()

blue_white = '#9BB4C4'
black_white = '#757575'
red_white = "#BDBDBD"
BG = '#041955'
FWG = '#97b4ff'
FG = '#3450a1'
PINK = "#FC0FC0"
font = ('Arial', 20, 'bold')

# Main frame
main_frame = CTkFrame(root, width=390, height=764, corner_radius=23, fg_color=FG)
main_frame.pack()
self_category = ''
buttons = []
day_buttons = []
is_running = False
# Global variables to keep track of the current year, month, and today's date
current_year = datetime.now().year
current_month = datetime.now().month
today = datetime.now().day
current_day_name = datetime.now().strftime("%A")
# Set the first day of the week as Sunday
calendar.setfirstweekday(calendar.SUNDAY)

# Implement icons
menu_image = Image.open("C:/Users/MD Foysal/OneDrive/Desktop/to_do_list_icon/menu_icon.png")
task_image = Image.open("C:/Users/MD Foysal/OneDrive/Desktop/to_do_list_icon/task_icon.png")
back_icon = Image.open("C:/Users/MD Foysal/OneDrive/Desktop/to_do_list_icon/back_icon.png")
search_icon = Image.open("C:/Users/MD Foysal/OneDrive/Desktop/to_do_list_icon/search_icon.png")
notification_icon = Image.open("C:/Users/MD Foysal/OneDrive/Desktop/to_do_list_icon/notification_icon.png")
circle_image = Image.open("C:/Users/MD Foysal/OneDrive/Desktop/to_do_list_icon/profile_pic_gemini.png")
cloud_image = Image.open("C:/Users/MD Foysal/OneDrive/Desktop/to_do_list_icon/cloud_icon_gemini.png")
template_icon = Image.open("C:/Users/MD Foysal/OneDrive/Desktop/to_do_list_icon/template_icon.png")
category_icon = Image.open("C:/Users/MD Foysal/OneDrive/Desktop/to_do_list_icon/category_icon.png")
analytics_icon = Image.open("C:/Users/MD Foysal/OneDrive/Desktop/to_do_list_icon/analytics_icon.png")
create_category_icon = Image.open("C:/Users/MD Foysal/OneDrive/Desktop/to_do_list_icon/create_category_icon.png")
project_icon = Image.open("C:/Users/MD Foysal/OneDrive/Desktop/to_do_list_icon/project_icon.png")
delete_icon = Image.open("C:/Users/MD Foysal/OneDrive/Desktop/to_do_list_icon/delete_icon.png")
edit_icon = Image.open("C:/Users/MD Foysal/OneDrive/Desktop/to_do_list_icon/edit_icon.png")
calculator_icon = Image.open("C:/Users/MD Foysal/OneDrive/Desktop/to_do_list_icon/calculator_icon.png")
calender_icon = Image.open("C:/Users/MD Foysal/OneDrive/Desktop/to_do_list_icon/calender_icon.jpg")
clock_icon = Image.open("C:/Users/MD Foysal/OneDrive/Desktop/to_do_list_icon/clock_icon.webp")
age_calculator_icon = Image.open("C:/Users/MD Foysal/OneDrive/Desktop/to_do_list_icon/age_calculator_icon.png")
progress_icon1 = Image.open("C:/Users/MD Foysal/OneDrive/Desktop/to_do_list_icon/progress_icon.png")
progress_icon2 = Image.open("C:/Users/MD Foysal/OneDrive/Desktop/to_do_list_icon/progress_icon.png")
progress_icon3 = Image.open("C:/Users/MD Foysal/OneDrive/Desktop/to_do_list_icon/progress_icon.png")
progress_icon4 = Image.open("C:/Users/MD Foysal/OneDrive/Desktop/to_do_list_icon/progress_icon.png")
calendar_logo = Image.open("C:/Users/MD Foysal/OneDrive/Desktop/to_do_list_icon/calender_icon.jpg")
microphone_logo = Image.open("C:/Users/MD Foysal/OneDrive/Desktop/to_do_list_icon/calender_icon.jpg")
add_icon = Image.open("C:/Users/MD Foysal/OneDrive/Desktop/to_do_list_icon/add_icon.png")


ctk_menu_image = CTkImage(menu_image, size=(33, 30))
ctk_back_icon = CTkImage(back_icon, size=(25, 25))
ctk_task_image = CTkImage(task_image, size=(150, 150))
ctk_search_icon = CTkImage(search_icon, size=(25, 25))
ctk_notification_icon = CTkImage(notification_icon, size=(25, 25))
ctk_circle_image = CTkImage(circle_image, size=(140, 140))
ctk_cloud_image = CTkImage(cloud_image, size=(350, 150))
ctk_template_icon = CTkImage(template_icon, size=(20, 20))
ctk_category_icon = CTkImage(category_icon, size=(20, 20))
ctk_analytics_icon = CTkImage(analytics_icon, size=(20, 20))
ctk_create_category_icon = CTkImage(create_category_icon, size=(50, 50))
ctk_project_icon = CTkImage(project_icon, size=(20, 20))
ctk_delete_icon = CTkImage(delete_icon, size=(25, 25))
ctk_edit_icon = CTkImage(edit_icon, size=(30, 30))
ctk_calculator_icon = CTkImage(calculator_icon, size=(55, 55))
ctk_calender_icon = CTkImage(calender_icon, size=(55, 55))
ctk_clock_icon = CTkImage(clock_icon, size=(55, 55))
ctk_age_calculator_icon = CTkImage(age_calculator_icon, size=(55, 55))
ctk_progress_icon1 = CTkImage(progress_icon1, size=(145, 10))
ctk_progress_icon2 = CTkImage(progress_icon2, size=(145, 10))
ctk_progress_icon3 = CTkImage(progress_icon3, size=(145, 10))
ctk_progress_icon4 = CTkImage(progress_icon4, size=(145, 10))
ctk_calender_logo = CTkImage(calendar_logo, size=(20, 20))
ctk_microphone_logo = CTkImage(microphone_logo, size=(20, 20))
ctk_add_icon = CTkImage(add_icon, size=(35, 35))


def show_date_value(date, month, year, day_button):
    global clicked_day_int, clicked_month_int
    day_color_change(day_button)
    clicked_day_int = date
    clicked_month_int = month
    selected_date = datetime(year, month, date)
    day_name = selected_date.strftime("%A")  # Get the name of the day
    date_entry.delete(0, END)
    date_entry.insert(0, f"{day_name}, {date} {calendar.month_name[month]}")


# Function to update the calendar display
def update_calendar():
    global day_button
    for widget in calendar_frame.winfo_children():
        widget.destroy()

    day_buttons.clear()

    month_name = calendar.month_name[current_month]
    month_year_label.configure(text=f"{month_name} {current_year}", text_color=FG)

    days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    for i, day in enumerate(days):
        CTkLabel(
            calendar_frame,
            text=day,
            fg_color='white',
            text_color='black').grid(row=0, column=i, padx=5, pady=5)

    month_calendar = calendar.monthcalendar(current_year, current_month)

    for week in range(len(month_calendar)):
        for day in range(7):
            day_value = month_calendar[week][day]
            if day_value != 0:
                day_button = CTkButton(
                    calendar_frame,
                    text=str(day_value),
                    width=30,
                    height=30,
                    fg_color='white',
                    text_color='black')
                day_buttons.append(day_button)
                day_button.configure(
                    command=lambda date=day_value,
                                   month=current_month,
                                   year=current_year,
                                   button=day_button: show_date_value(date, month, year, button))
                day_button.grid(row=week + 1, column=day, padx=5, pady=5)

                if (current_year == datetime.now().year and
                        current_month == datetime.now().month and
                        day_value == today):
                    day_button.configure(fg_color="green")  # Highlight today's date

    # Update today's date label with the day name
    today_label.configure(text=f"Today's Date: {today} {month_name}, {current_year} ({current_day_name})")


# Function to move to the previous month
def prev_month():
    global current_month, current_year
    current_month -= 1
    if current_month == 0:
        current_month = 12
        current_year -= 1
    update_calendar()


# Function to move to the next month
def next_month():
    global current_month, current_year
    current_month += 1
    if current_month == 13:
        current_month = 1
        current_year += 1
    update_calendar()


def setup_date(event):
    global month_year_label, today_label, calendar_frame, is_running
    is_running = True
    create_task_btn.configure(command=lambda:
    add_task_in_frame(combo_box.get(), date_entry.get(),
                      clicked_day_int, clicked_month_int))
    # Initialize the main window
    app = CTkFrame(add_task_frame, fg_color='#027EFF')
    back_btn = CTkButton(
        app,
        image=ctk_back_icon,
        text='',
        width=5,
        height=5,
        fg_color='transparent',
        command=lambda: app.place_forget())
    app.place(x=40, y=100)
    back_btn.pack(anchor='nw')

    # Frame for Month and Year Navigation
    nav_frame = CTkFrame(app, fg_color='white')
    nav_frame.pack(pady=10)

    prev_button = CTkButton(nav_frame, text="<<",
                            command=prev_month,
                            width=30, height=20)
    prev_button.grid(row=0, column=0, padx=5)

    month_year_label = CTkLabel(nav_frame, text="")
    month_year_label.grid(row=0, column=1, padx=5)

    next_button = CTkButton(nav_frame, text=">>",
                            command=next_month,
                            width=30, height=20)
    next_button.grid(row=0, column=2, padx=5)

    # Frame for Calendar Grid
    calendar_frame = CTkFrame(app, fg_color='white')
    calendar_frame.pack(pady=10)

    # Label for displaying today's date
    today_label = CTkLabel(app, text="")
    today_label.pack(pady=10)

    add_task_frame.bind('<Button-1>', lambda event: app.place_forget())
    # confermation button
    okay_btn = CTkButton(app, text='Ok', font=font)
    okay_btn.pack(pady=10)

    # Initialize the calendar
    update_calendar()


# create category if not exists
def create_category_database(category):
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?;", (category,))
    table_exists = cursor.fetchone()

    if table_exists == None:
        cursor.execute(
            f"CREATE TABLE IF NOT EXISTS {category} (Tasks text NOT NULL, date_time text, day_month_int integer)")
        cursor.execute("INSERT INTO category_list (category) VALUES (?)", (category,))
        conn.commit()
        create_category_frame(category)

def day_color_change(clicked_button):
    # Reset every button color
    for button in day_buttons:
        button.configure(
            fg_color='transparent',
            hover_color=FG)

    # Changing button color which is clicked
    clicked_button.configure(fg_color=FG)


# A function that works when the button click
def color_change(clicked_button):
    # Reset every button color
    for button in buttons:
        button.configure(
            fg_color='transparent',
            hover_color=FG)
    clicked_button.configure(fg_color=FG)


# all widgets for menu frame
def open_menu_frame():
    global menu_frame
    menu_frame = CTkFrame(
        root,
        width=0,
        height=0,
        corner_radius=23,
        fg_color=BG,
        bg_color=FG
    )
    circle_image_lbl = CTkLabel(
        menu_frame,
        image=ctk_circle_image,
        text=''
    )
    cloud_image = CTkLabel(
        menu_frame,
        image=ctk_cloud_image,
        text=''
    )
    back_icon_btn = CTkButton(
        menu_frame,
        image=ctk_back_icon,
        text='', width=10,
        fg_color=BG,
        command=lambda:
        back_widget(menu_frame)
    )

    name_labal = CTkLabel(
        menu_frame,
        text='Foysal\n      Ahammed',
        font=('Verdana', 25, 'bold')
    )
    my_project_btn = CTkButton(
        menu_frame,
        image=ctk_project_icon,
        width=20,
        text="My Project",
        font=('Verdana', 16, 'bold'),
        fg_color='transparent',
        command=show_my_project
    )
    templates_btn = CTkButton(
        menu_frame,
        image=ctk_template_icon,
        text='Templates',
        font=('Verdana', 16),
        fg_color='transparent',
        width=20
    )
    categories_btn = CTkButton(
        menu_frame,
        image=ctk_category_icon,
        text='Categories',
        font=('Verdana', 16),
        fg_color='transparent',
        width=20,
        command=show_categories_list
    )
    analytics_btn = CTkButton(
        menu_frame,
        image=ctk_analytics_icon,
        text='Analytics',
        font=('Verdana', 16),
        fg_color='transparent',
        width=20
    )

    good_lbl = CTkLabel(
        menu_frame,
        text='Good',
        font=('Arial', 16),
        text_color=FG,
        fg_color='transparent'
    )
    consistancy_lbl = CTkLabel(
        menu_frame,
        text='Consistency',
        font=('Arial', 20),
        fg_color='transparent'
    )

    name_labal.place(x=0, y=210)
    menu_frame.place(x=0, y=0)
    circle_image_lbl.place(x=40, y=50)
    cloud_image.place(x=10, y=500)
    back_icon_btn.place(x=5, y=5)
    my_project_btn.place(x=40, y=280)
    templates_btn.place(x=40, y=320)
    categories_btn.place(x=40, y=360)
    analytics_btn.place(x=40, y=400)
    good_lbl.place(x=40, y=670)
    consistancy_lbl.place(x=40, y=700)
    animate_frame(menu_frame, 390, 850)


def active_digital_watch():
    pass


def show_calculator():
    window = CTk()
    window.mainloop()
    pass


def show_my_project():
    global project_frame
    project_frame = CTkFrame(
        menu_frame,
        width=390,
        height=764,
        corner_radius=23,
        fg_color=BG)
    back_btn = CTkButton(
        project_frame,
        image=ctk_back_icon,
        text='',
        width=5,
        fg_color='transparent',
        command=lambda: back_widget(project_frame))
    calculator_btn = CTkButton(
        project_frame,
        image=ctk_calculator_icon,
        text='',
        font=('Arial', 15),
        width=20,
        fg_color='transparent',
        command=show_calculator)

    calender_btn = CTkButton(
        project_frame,
        image=ctk_calender_icon,
        text='',
        font=('Arial', 20),
        width=20,
        fg_color='transparent'
    )
    digital_watch_btn = CTkButton(
        project_frame,
        image=ctk_clock_icon,
        text='',
        font=('Arial', 20),
        width=20,
        fg_color='transparent',
        command=active_digital_watch
    )
    age_calculator_btn = CTkButton(
        project_frame,
        image=ctk_age_calculator_icon,
        text='',
        font=('Arial', 20),
        width=20,
        fg_color='transparent')

    project_frame.place(x=0, y=0)
    back_btn.place(x=0, y=0)
    calculator_btn.place(x=50, y=40)
    calender_btn.place(x=210, y=40)
    digital_watch_btn.place(x=50, y=130)
    age_calculator_btn.place(x=210, y=130)


def searching_task():
    global search_entry, app
    # Create the main application window
    app = CTkScrollableFrame(main_frame, width=390, height=800, fg_color=FG)
    app.place(x=0, y=50)
    # Create a search entry box
    underline_lbl = CTkLabel(main_frame, text="_________________________________________________",
                             width=50, height=3, bg_color='transparent')
    search_entry = CTkEntry(
        main_frame,
        width=300,
        height=30,
        fg_color=FG,
        placeholder_text='Search',
        border_color=FG,
        font=('Arial', 16))

    search_entry.place(x=80, y=10)
    underline_lbl.place(x=80, y=30)

    # Bind the KeyRelease event to the search entry
    search_entry.bind("<KeyRelease>", update_frame)


# Function to search the database
def search_database(keyword):
    cursor.execute(f"SELECT tasks FROM {c} WHERE tasks LIKE ?", ('%' + keyword + '%',))
    results = cursor.fetchall()
    conn.commit()
    return results


# Function to update the frame with search results
def update_frame(event):
    keyword = search_entry.get().strip()
    results = search_database(keyword)
    # Clear previous resultst
    for widget in app.winfo_children():
        widget.destroy()

    # Display new results
    if results:
        for result in results:
            label_frame = CTkFrame(
                app,
                width=370,
                height=60,
                fg_color=BG,
                corner_radius=12)
            # label = CTkLabel(label_frame, text=result[0], font=('Verdana', 20))
            var = StringVar()
            task_checkbox = CTkCheckBox(
                label_frame,
                text=result[0],
                variable=var,
                font=('Arial', 20),
                width=350,
                height=40,
                corner_radius=32,
                border_width=2,
                border_color=PINK
            )
            task_checkbox.place(x=10, y=15)

            task_checkbox.configure(
                command=lambda frame=label_frame, text=results[0],
                               checkbox=task_checkbox: delete_tasks(text[0], frame, checkbox, '', ''))

            label_frame.pack(pady=5)
    else:
        label = CTkLabel(app, text="No matching items found.")
        label.place(x=0, y=0)


def implement_task_from_db(category, button, t_count):
    global c, tsk_count
    tsk_count = t_count
    task_showing_frame.place_forget()
    color_change(button)
    c = category
    for widget in task_showing_frame.winfo_children():
        widget.destroy()

    cursor.execute(f"SELECT * FROM {category}")
    tasks = cursor.fetchall()
    tasks_list = []
    for task in tasks:
        tasks_list.append(task)
        if task[1] != '':
            show_task_in_frame(task[0], task[1], task[2])

    for task_l in tasks_list:
        if task_l[1] == '':
            show_task_in_frame(task_l[0], task_l[1], task[2])
    task_showing_frame.place(x=0, y=300)

    if task_showing_frame.winfo_children() == []:
        task_empty_lbl = CTkLabel(
            task_showing_frame,
            text=f'List {category} is empty',
            font=('Verdana', 18),
            fg_color='transparent',
            text_color=blue_white
        )
        task_empty_lbl.pack(pady=210)


ctk_menu_btn = CTkButton(
    main_frame,
    image=ctk_menu_image,
    text='',
    fg_color=FG,
    width=10,
    command=open_menu_frame
)
ctk_search_btn = CTkButton(
    main_frame,
    image=ctk_search_icon,
    text='',
    fg_color=FG,
    width=10,
    command=searching_task
)
ctk_notification_btn = CTkButton(
    main_frame,
    image=ctk_notification_icon,
    text='',
    fg_color=FG,
    width=10
)
ctk_menu_btn.place(x=10, y=20)
ctk_search_btn.place(x=290, y=20)
ctk_notification_btn.place(x=330, y=20)
# Designing frame
welcome_label = CTkLabel(
    main_frame,
    text="What's up Foysal!",
    font=('Arial', 30, 'bold'),
    fg_color=FG
)
welcome_label.place(x=20, y=70)
category_text_lbl = CTkLabel(
    main_frame,
    text='Categories',
    font=('Verdana', 20),
    fg_color=FG,
    bg_color=FG,
    text_color=FWG
)
category_text_lbl.place(x=5, y=138)
# Category and task widget frame
main_category_frame = CTkFrame(
    main_frame,
    fg_color=FG,
    bg_color=FG
)
main_category_frame.place(x=0, y=170)
task_showing_frame = CTkScrollableFrame(
    main_frame,
    width=370,
    height=430,
    fg_color=FG,
    bg_color=FG,
    scrollbar_button_color=FWG,
    scrollbar_button_hover_color=BG
)
task_showing_frame.place(x=0, y=300)

# Create a canvas for horizontal scrollable frame
canvas = CTkCanvas(
    main_category_frame,
    width=480,
    height=140,
    bg=FG
)
canvas.pack(side="top", fill="x", padx=10, pady=10)

# Frame with widgets
scrollable_frame = CTkFrame(
    canvas,
    fg_color=FG,
    bg_color=FG
)
scrollable_frame.bind("<Configure>", lambda e:
canvas.configure(scrollregion=canvas.bbox("all")))
canvas.create_window((0, 0),
                     window=scrollable_frame,
                     anchor="nw")
# Horizontal scrollbar
h_scrollbar = CTkScrollbar(
    scrollable_frame,
    orientation="horizontal",
    button_color=FWG,
    command=canvas.xview
)
h_scrollbar.pack(side="bottom", fill="x")
canvas.configure(xscrollcommand=h_scrollbar.set)
frame_list = []


def count_tasks(table_name):
    # global record_count
    table = table_name.replace(' ', '_')
    cursor.execute(f'SELECT COUNT(*) FROM {table}')
    record_count = cursor.fetchone()[0]
    return int(record_count)


# implement_task_from_db
def create_category_frame(category):
    global category_main_frame, frame_list_for_delete
    counting_tasks = count_tasks(category)
    category_main_frame = CTkFrame(
        scrollable_frame,
        width=180,
        height=100,
        corner_radius=19,
        fg_color=BG,
        bg_color=FG,
        border_width=2,
        border_color=PINK
    )
    frame_list_for_delete = {
        "category": category,
        "frame": category_main_frame
    }
    frame_list.append(frame_list_for_delete)
    progress_icon = random.choice([
        ctk_progress_icon2,
        ctk_progress_icon1,
        ctk_progress_icon4,
        ctk_progress_icon3
    ])
    progress_icon_lbl = CTkLabel(
        category_main_frame,
        image=progress_icon,
        text='',
        fg_color='transparent',
        bg_color=BG
    )
    task_count_lbl = CTkLabel(
        category_main_frame,
        text=f'{str(counting_tasks)} Tasks',
        font=font
    )
    category_button = CTkButton(
        category_main_frame,
        text=category.replace("_", " "),
        font=('Verdana', 20),
        fg_color='transparent',
        width=20, command=lambda count=task_count_lbl:
        implement_task_from_db(category, category_button, count)
    )
    buttons.append(category_button)
    category_main_frame.pack(side='left', padx=5)

    task_count_lbl.place(x=10, y=5)
    category_button.place(x=2, y=40)
    progress_icon_lbl.place(x=10, y=68)
    # return category_frame


def load_category_from_db():
    cursor.execute("SELECT * FROM category_list")
    category_name = cursor.fetchall()
    conn.commit()
    for category in category_name:
        cate = category[0]
        create_category_frame(cate)

load_category_from_db()

def animate_frame(frame, target_width, target_height):
    width = frame.winfo_width()
    height = frame.winfo_height()

    if width < target_width or height < target_height:
        if width < target_width:
            width += 20
        if height < target_height:
            height += 20
        frame.configure(width=width, height=height)
        root.after(10, lambda: animate_frame(frame, target_width, target_height))


# adding_task_notificate
def back_widget(frame):
    frame.place_forget()

def add_task_widget():
    global add_task_frame, task_entry, combo_box, category_list, date_entry, create_task_btn
    add_task_frame = CTkFrame(
        main_frame,
        width=0,
        height=0,
        fg_color=BG
    )
    add_task_frame.place(x=0, y=0)
    # Animate the frame
    animate_frame(add_task_frame, 390, 850)
    title = CTkLabel(
        add_task_frame,
        text='New Task',
        font=font
    )
    task_entry = CTkEntry(
        add_task_frame,
        width=300, height=55,
        placeholder_text='Enter Task Here',
        corner_radius=17,
        fg_color='transparent',
        font=('Arial', 20),
        text_color=FWG,
        border_color=FG
    )
    back_btn = CTkButton(
        add_task_frame,
        image=ctk_back_icon,
        text='',
        width=10,
        fg_color='transparent',
        command=lambda: back_widget(add_task_frame)
    )
    cursor.execute("SELECT * FROM category_list")
    category_name = cursor.fetchall()
    conn.commit()
    # Extract category names into a list
    category_list = [category[0].replace('_', ' ') for category in category_name]
    due_date_lbl = CTkLabel(
        add_task_frame,
        text='Due date',
        font=font,
        text_color='#027EFF')
    underlint_lbl = CTkLabel(
        add_task_frame,
        text='_____________________________________________________')
    calender_btn = CTkButton(
        add_task_frame,
        image=ctk_calender_logo,
        text='',
        fg_color='transparent',
        width=10)
    date_entry = CTkEntry(
        add_task_frame,
        width=300,
        height=30,
        placeholder_text='Date not set',
        font=('Arial', 20),
        fg_color='transparent',
        border_color=BG,
        corner_radius=17
    )
    date_entry.bind('<Button-1>', setup_date)
    combo_box = CTkComboBox(
        add_task_frame,
        values=category_list,
        width=300, height=55,
        fg_color=BG, bg_color=BG,
        border_color=FG,
        corner_radius=17,
        dropdown_fg_color=FG,
        button_color=FWG,
        dropdown_hover_color=BG,
        font=('Arial', 20))
    
    task_image_lbl = CTkLabel(
        add_task_frame,
        image=ctk_task_image,
        text=''
    )
    create_task_btn = CTkButton(
        add_task_frame,
        text='Create Task',
        font=('Arial', 20),
        width=300, height=55,
        border_width=2,
        corner_radius=17,
        border_color=FG,
        command=lambda:
        add_task_in_frame(combo_box.get(),
                          date_entry.get(), 0, 0)
    )

    combo_box.place(x=30, y=200)
    back_btn.place(x=5, y=2)
    title.place(x=150, y=20)
    task_entry.place(x=30, y=70)
    task_image_lbl.place(x=240, y=600)
    create_task_btn.place(x=30, y=380)
    # create_category_btn.place(x=330, y=200)
    due_date_lbl.place(x=30, y=265)
    date_entry.place(x=30, y=300)
    calender_btn.place(x=330, y=300)
    underlint_lbl.place(x=30, y=320)


def add_task_in_frame(category, date, click_day, click_month):
    global categ
    clicked_date = f"{click_day} {click_month}"
    categ = category.replace(' ', '_')
    adding_task_notificate()
    create_category_database(categ)
    task = task_entry.get()
    # combo_get_category = combo_box.get()

    if task != '':
        tsk_count.configure(text=str(count_tasks(combo_box.get()) + 1) + ' Tasks')
        # task_count.place_configure(x=10, y=5)
        task_entry.delete(0, END)
        cursor.execute(f'INSERT INTO {categ} (Tasks, date_time, day_month_int) VALUES (?, ?, ?)',
                       (task, date, clicked_date))
        conn.commit()
        if categ == c:
            show_task_in_frame(task, date, clicked_date)

def show_task_in_frame(text, date, clicked_date):
    task_frame = CTkFrame(
        task_showing_frame,
        width=380,
        height=45,
        fg_color=BG,
        corner_radius=12
    )
    task_frame.pack(pady=5)
    var = IntVar()
    task_checkbox = CTkCheckBox(
        task_frame,
        text=text,
        variable=var,
        font=('Arial', 20),
        width=350,
        height=40,
        corner_radius=32,
        border_width=2,
        border_color=PINK)
    task_checkbox.place(x=10, y=0)

    date_lbl = CTkLabel(
        task_frame,
        text=date,
        height=5,
        text_color='#55AAFF')

    pattern = re.compile(r"\d+")
    date_text = re.findall(pattern, clicked_date)
    todays_month = datetime.now().month
    todays_day = datetime.now().day
    if date != '':
        if (todays_month, todays_day) < (int(date_text[1]), int(date_text[0])):
            task_frame.configure(height=60)
            date_lbl.place(x=40, y=35)
        else:
            task_frame.configure(height=60)
            date_lbl.configure(text_color='red')
            date_lbl.place(x=40, y=35)

    task_checkbox.configure(
        command=lambda frame=task_frame,
                       checkbox=task_checkbox:
        delete_tasks(text, date, frame, checkbox, clicked_date))


# Function to animate the checkbox and then delete the task
def animate_checkbox(task_frame, task_checkbox):
    current_x = task_checkbox.winfo_x()
    if current_x < 420:
        new_x = current_x + 2
        task_checkbox.place(x=new_x, y=5)
        task_frame.after(18, lambda: animate_checkbox(task_frame, task_checkbox))
    else:
        task_frame.after(200, task_frame.pack_forget)  # Delay and then delete the task


def delete_tasks(tasks, date, frame, checkbox, clicked_date):
    animate_checkbox(frame, checkbox)
    tsk_count.configure(text=str(count_tasks(c) - 1) + ' Tasks')

    cursor.execute("INSERT INTO Complete_Tasks (Tasks, date_time, day_month_int) VALUES (?, ?, ?)",
                   (tasks, date, clicked_date))
    cursor.execute(f"DELETE FROM {c} WHERE Tasks=?", (tasks,))
    conn.commit()
    # tsk_count.configure(text= str(count_tasks("Complete_Task")+1) + ' Tasks')


# Add button implementation
ctk_add_btn = CTkButton(
    main_frame,
    image=ctk_add_icon,
    text='',
    width=7,
    height=7,
    fg_color=BG,
    bg_color=BG,
    hover_color=PINK,
    corner_radius=88,
    command=add_task_widget
)
ctk_add_btn.place(x=320, y=700)


def delete_category(frame, category):
    for frame_l in frame_list:
        cate = frame_l["category"]
        if cate == category:
            frame_l["frame"].pack_forget()

    frame.grid_forget()
    cursor.execute(f"DELETE FROM category_list WHERE category=?", (category,))
    cursor.execute("DROP TABLE IF EXISTS {0}".format(category))
    conn.commit()


def show_categories_list():
    categories_list_frame = CTkScrollableFrame(
        menu_frame,
        width=390,
        height=764,
        corner_radius=23,
        fg_color=BG
    )
    back_frame = CTkFrame(
        categories_list_frame,
        width=300,
        height=30,
        fg_color=BG
    )
    title = CTkLabel(
        back_frame,
        text='Task List',
        font=font,
        fg_color='transparent'
    )
    back_btn = CTkButton(
        back_frame,
        text='<',
        font=('Arial', 30),
        fg_color='transparent',
        width=5,
        height=1,
        command=lambda:
        back_widget(categories_list_frame))
    cursor.execute("SELECT * FROM category_list")
    category_name = cursor.fetchall()
    conn.commit()
    i = 1
    for category in category_name:
        cate = category[0]
        counting_tasks = count_tasks(cate)
        i += 1
        category_frame = CTkFrame(
            categories_list_frame,
            width=350,
            height=100,
            corner_radius=19,
            fg_color=BG,
            bg_color=BG,
            border_width=2,
            border_color=PINK
        )
        progress_icon = random.choice(
            [
                ctk_progress_icon2,
                ctk_progress_icon1,
                ctk_progress_icon4,
                ctk_progress_icon3
            ])
        progress_icon_lbl = CTkLabel(
            category_frame,
            image=progress_icon,
            text='',
            fg_color='transparent',
            bg_color=BG
        )

        delete_icon_btn = CTkButton(
            category_frame,
            image=ctk_delete_icon,
            text='',
            fg_color='transparent',
            bg_color=BG,
            width=10,
            command=lambda frame=category_frame,
                           ctg=cate: delete_category(
                frame, ctg
            ))
        edit_icon_btn = CTkButton(
            category_frame,
            image=ctk_edit_icon,
            text='',
            fg_color='transparent',
            bg_color=BG,
            width=10
        )
        task_count = CTkLabel(
            category_frame,
            text=f'{str(counting_tasks)} Tasks',
            font=font
        )
        category_button = CTkButton(
            category_frame,
            text=cate,
            font=('Verdana', 20),
            fg_color='transparent',
            width=20
        )
        buttons.append(category_button)
        category_frame.grid(row=i,
                            column=0,
                            pady=5
                            )
        task_count.place(x=10, y=5)
        category_button.place(x=2, y=40)
        progress_icon_lbl.place(x=10, y=68)

        if cate != "Default_":
            delete_icon_btn.place(x=290, y=55)
            edit_icon_btn.place(x=240, y=55)

    categories_list_frame.place(x=0, y=0)
    back_frame.grid(row=0, column=0, rowspan=1)
    back_btn.place(x=0, y=0)
    title.place(x=110, y=0)


# Function to delete the frame
def delete_frame(frame):
    frame.destroy()


# Function to create the frame and schedule its deletion
def adding_task_notificate():
    frame = CTkFrame(
        add_task_frame,
        width=200,
        height=50,
        corner_radius=10,
        fg_color=FG
    )
    adding_task_lbl = CTkLabel(
        frame,
        text='Adding Task',
        font=('Arial', 16, 'bold'),
        fg_color='transparent',
        text_color=FWG
    )
    if task_entry.get() != '':

        frame.place(x=80, y=480)
        adding_task_lbl.place(x=50, y=10)
        root.after(1500, lambda:
        delete_frame(frame)
                   )
    else:
        frame.place(x=80, y=480)
        adding_task_lbl.configure(
            text='Please Enter a Task',
            text_color='red'
        )
        adding_task_lbl.place_configure(x=25, y=15)
        root.after(1500, lambda:
        delete_frame(frame)
                   )
root.mainloop()
