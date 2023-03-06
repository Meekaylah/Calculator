from tkinter import *
from PIL import ImageTk, Image

calculation = ""


def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(0, END)
    text_result.insert(0, calculation)


def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(0, END)
        text_result.insert(0, calculation)
    except:
        clear_field()
        text_result.insert(0, "Error")


def clear_field():
    global calculation
    calculation = ""
    text_result.delete(0, END)
    pass


def move_app(e):
    root.geometry(f'+{e.x_root}+{e.y_root}')


def quitter(e):
    root.quit()


root = Tk()
root.geometry('234x323+400+300')

root.overrideredirect(True)

title_bar = Frame(root, bg="white", relief="raised", height=20, width=234, padx=0)
title_bar.grid(columnspan=4, sticky="nsew", ipady=4)

# Bind the title bar
title_bar.bind("<B1-Motion>", move_app)

# Create close button on title bar

icon_red = Image.open('icons/icons8-red-circle-48.png')
resized_icon_red = icon_red.resize((14, 14), Image.LANCZOS)
red = ImageTk.PhotoImage(resized_icon_red)
icon_yellow = Image.open('icons/icons8-yellow-circle-48.png')
resized_icon_yellow = icon_yellow.resize((14, 14), Image.LANCZOS)
yellow = ImageTk.PhotoImage(resized_icon_yellow)
close_label = Label(title_bar, bg="white", fg="white", image=red)
close_label.pack(side=LEFT, padx=2)
close_label.bind("<Button-1>", quitter)
hide_label = Label(title_bar, bg="white", fg="white", image=yellow)
hide_label.pack(side=LEFT)
hide_label.bind("<Button-1>", quitter)


text_result = Entry(root, width=9, font=("Arial", 34), relief=RAISED, justify=RIGHT)
text_result.grid(row=1, columnspan=4, ipadx=3, ipady=4)

btn_0 = Button(root, text="0", command=lambda: add_to_calculation(0), height=1, width=3, font=("Arial", 18))
btn_0.grid(row=6, column=0, columnspan=2, sticky="nsew")
btn_1 = Button(root, text="1", command=lambda: add_to_calculation(1), height=1, width=3, font=("Arial", 18))
btn_1.grid(row=5, column=0, sticky="nsew")
btn_2 = Button(root, text="2", command=lambda: add_to_calculation(2), height=1, width=3, font=("Arial", 18))
btn_2.grid(row=5, column=1, sticky="nsew")
btn_3 = Button(root, text="3", command=lambda: add_to_calculation(3), height=1, width=3, font=("Arial", 18))
btn_3.grid(row=5, column=2, sticky="nsew")
btn_4 = Button(root, text="4", command=lambda: add_to_calculation(4), height=1, width=3, font=("Arial", 18))
btn_4.grid(row=4, column=0, sticky="nsew")
btn_5 = Button(root, text="5", command=lambda: add_to_calculation(5), height=1, width=3, font=("Arial", 18))
btn_5.grid(row=4, column=1, sticky="nsew")
btn_6 = Button(root, text="6", command=lambda: add_to_calculation(6), height=1, width=3, font=("Arial", 18))
btn_6.grid(row=4, column=2, sticky="nsew")
btn_7 = Button(root, text="7", command=lambda: add_to_calculation(7), height=1, width=3, font=("Arial", 18))
btn_7.grid(row=3, column=0, sticky="nsew")
btn_8 = Button(root, text="8", command=lambda: add_to_calculation(8), height=1, width=3, font=("Arial", 18))
btn_8.grid(row=3, column=1, sticky="nsew")
btn_9 = Button(root, text="9", command=lambda: add_to_calculation(9), height=1, width=3, font=("Arial", 18))
btn_9.grid(row=3, column=2, sticky="nsew")
btn_AC = Button(root, text="AC", command=clear_field, height=1, width=3, font=("Arial", 18))
btn_AC.grid(row=2, column=0, sticky="nsew")
btn_plus_or_minus = Button(root, text="⁺/₋", command="", height=1, width=3, font=("Arial", 18))
btn_plus_or_minus.grid(row=2, column=1, sticky="nsew")
btn_percent = Button(root, text="%", command=lambda: add_to_calculation("%"), height=1, width=3, font=("Arial", 18))
btn_percent.grid(row=2, column=2, sticky="nsew")
btn_divide = Button(root, text="÷", command=lambda: add_to_calculation("/"), height=1, width=3, font=("Arial", 18))
btn_divide.grid(row=2, column=3, sticky="nsew")
btn_multiply = Button(root, text="×", command=lambda: add_to_calculation("*"), height=1, width=3, font=("Arial", 18))
btn_multiply.grid(row=3, column=3, sticky="nsew")
btn_subtract = Button(root, text="-", command=lambda: add_to_calculation("-"), height=1, width=3, font=("Arial", 18))
btn_subtract.grid(row=4, column=3, sticky="nsew")
btn_add = Button(root, text="+", command=lambda: add_to_calculation("+"), height=1, width=3, font=("Arial", 18))
btn_add.grid(row=5, column=3, sticky="nsew")
btn_decimal = Button(root, text=".", command=lambda: add_to_calculation("."), height=1, width=3, font=("Arial", 18))
btn_decimal.grid(row=6, column=2, sticky="nsew")
btn_equal = Button(root, text="=", command=evaluate_calculation, height=1, width=3, font=("Arial", 18))
btn_equal.grid(row=6, column=3, sticky="nsew")
root.mainloop()
