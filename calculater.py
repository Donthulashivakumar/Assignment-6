from tkinter import *
def button_click(value):
    current = e.get()
    e.delete(0, END)
    e.insert(END, current + str(value))
def clear_entry():
    e.delete(0, END)
def evaluate():
    try:
        result = eval(e.get())
        e.delete(0, END)
        e.insert(END, str(result))
    except:
        e.delete(0, END)
        e.insert(END, "Error")
window = Tk()
window.geometry('300x400')
window.title("Calculator")
e = Entry(window, width=24, font=('Arial', 18), bd=5, relief=RIDGE, justify='right')
e.place(x=10, y=10)
buttons = [
    ('1', 10, 60), ('2', 80, 60), ('3', 150, 60),
    ('4', 10, 110), ('5', 80, 110), ('6', 150, 110),
    ('7', 10, 160), ('8', 80, 160), ('9', 150, 160),
    ('0', 10, 210), ('+', 80, 210), ('-', 150, 210),
    ('*', 10, 260), ('/', 80, 260), ('=', 150, 260),
    ('clear', 10, 310)
]

for (text, x, y) in buttons:
    if text == '=':
        cmd = evaluate
    elif text == 'clear':
        cmd = clear_entry
    else:
        cmd = lambda x=text: button_click(x)
    
    Button(window, text=text, width=5, height=2, font=('Arial', 12), command=cmd).place(x=x, y=y)

window.mainloop()
