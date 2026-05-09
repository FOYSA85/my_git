from customtkinter import *

root = CTk()
root.geometry('300x500')
root.title('calculator')
font = 'Arial', 17

BG = '#041955'
FWG = '#97b4ff'
FG = '#3450a1'
PINK = '#eb06ff'

display = CTkEntry(root, font=font, width=297, height=45, border_width=2, fg_color='black', border_color='yellow')
display.grid(row=0, column=0)

def calculator(number) :
    global num
    if number == 'C' :
        display.delete(0, END)
    if number != 'C' :
        num = display.get()
        display.delete(0, END)
        display.insert(0, str(num)+str(number))

def delete_key(event) :
    display.delete(0, END)

def equal() :
    operators = display.get()
    cross_operator = None

    try :
        if operators == 'Error':
            display.delete(0, END)
            display.bind("<KeyRelease>", delete_key)
        for cross in operators :
            if cross == 'X' :
                print("into :", cross)
                cross_operator = '*'
        if cross_operator == '*' :
            operators1 = operators.replace(' X ', '*')
            add1 = eval(str(operators1))

            display.delete(0, END)
            display.insert(0, add1)

        else :
            add = eval(str(operators))
            display.delete(0, END)
            display.insert(0,add)

    except Exception as e :
        display.delete(0, END)
        display.insert(0, 'Error')

nine  = CTkButton(root, text='9', font=font, width=45, height=50, fg_color='black', hover_color='gray', border_width=2, border_color='#FFCC70', corner_radius=40, command=lambda: calculator(9))
eight = CTkButton(root, text='8', font=font, width=45, height=50, fg_color='black', hover_color='gray', border_width=2, border_color='#FFCC70', corner_radius=40, command=lambda: calculator(8))
seven = CTkButton(root, text='7', font=font, width=45, height=50, fg_color='black', hover_color='gray', border_width=2, border_color='#FFCC70', corner_radius=40, command=lambda: calculator(7))
six   = CTkButton(root, text='6', font=font, width=45, height=50, fg_color='black', hover_color=FWG, border_width=2, border_color='#FFCC70',corner_radius=40, command=lambda: calculator(6))
five  = CTkButton(root, text='5', font=font, width=45, height=50, fg_color='black', hover_color=FWG, border_width=2, border_color='#FFCC70',corner_radius=40, command=lambda: calculator(5))
four  = CTkButton(root, text='4', font=font, width=45, height=50, fg_color='black', hover_color=FWG, border_width=2, border_color='#FFCC70',corner_radius=40, command=lambda: calculator(4))
three = CTkButton(root, text='3', font=font, width=45, height=50, fg_color='black', hover_color=FWG, border_width=2, border_color='#FFCC70',corner_radius=40, command=lambda: calculator(3))
two   = CTkButton(root, text='2', font=font, width=45, height=50, fg_color='black', hover_color=FWG, border_width=2, border_color='#FFCC70',corner_radius=40, command=lambda: calculator(2))
one   = CTkButton(root, text='1', font=font, width=45, height=50, fg_color='black', hover_color=FWG, border_width=2, border_color='#FFCC70',corner_radius=40, command=lambda: calculator(1))
zero  = CTkButton(root, text='0', font=font, width=45, height=50, fg_color='black', hover_color=FWG, border_width=2, border_color='#FFCC70',corner_radius=40, command=lambda: calculator(0))
point = CTkButton(root, text='.', font=font, width=45, height=50, fg_color='black', hover_color=FWG, border_width=2, border_color='#FFCC70',corner_radius=40, command=lambda: calculator('.'))

#operators area
fst_brkt_l = CTkButton(root, text='(', font=font, width=45,height=50, fg_color='black',hover_color=FWG, border_width=2, border_color='#FFCC70',corner_radius=40, command= lambda: calculator('('))
fst_brkt_r = CTkButton(root, text=')', font=font, width=45,height=50, fg_color='black',hover_color='green', border_width=2, border_color='#FFCC70',corner_radius=40, command= lambda: calculator(')'))

clear = CTkButton(root, text='C', font=font, width=45, height=50, fg_color='black',hover_color='green', border_width=2, border_color='#FFCC70',corner_radius=40, command= lambda: calculator('C'))
add   = CTkButton(root, text='+', font=font, width=45, height=50, fg_color='black',hover_color='green', border_width=2, border_color='#FFCC70',corner_radius=40, command= lambda: calculator('+'))
minus = CTkButton(root, text='-', font=font, width=45, height=50, fg_color='black',hover_color='green', border_width=2, border_color='#FFCC70',corner_radius=40, command= lambda: calculator('-'))
cross  = CTkButton(root, text='X', font=font, width=45, height=50, fg_color='black',hover_color='green', border_width=2, border_color='#FFCC70',corner_radius=40, command= lambda: calculator(' X '))
divide= CTkButton(root, text='/', font=font, width=45, height=50, fg_color='black',hover_color='green', border_width=2, border_color='#FFCC70',corner_radius=40, command= lambda: calculator('/'))
equal = CTkButton(root, text='=', font=font, width=45, height=50, fg_color='black',hover_color='green', border_width=2, border_color='#FFCC70',corner_radius=40, command= equal)

#build widget
seven.place(x=5, y=100)
eight.place(x=80, y=100)
nine.place(x=155, y=100)
clear.place(x=230, y=100)

four.place(x=5, y=170)
five.place(x=80, y=170)
six.place(x=155, y=170)
minus.place(x=230, y=170)
#
one.place(x=5, y=240)
two.place(x=80, y=240)
three.place(x=155, y=240)
add.place(x=230, y=240)

point.place(x=5, y=310)
zero.place(x=80, y=310)
equal.place(x=155, y=380)
cross.place(x=230, y=310)

fst_brkt_l.place(x=5, y=380)
fst_brkt_r.place(x=80, y=380)
divide.place(x=155, y=310)

root.mainloop()
