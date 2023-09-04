from tkinter import *
from PIL import ImageTk, Image
from ctypes import windll

calculation = ""
z = 0
has_style = False


def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    if calculation != "0":
        btn_AC.config(text="C", command=clear_string)
    text_result.delete(0, END)
    text_result.insert(0, calculation)


def functions(operator):
    global calculation

    calculation += str(operator)


def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        btn_AC.config(text="AC", command=clear_field)
        text_result.delete(0, END)
        text_result.insert(0, calculation)
    except:
        clear_field()
        text_result.insert(0, "Error")


def add_minus(minus):
    global calculation
    calculation = str(calculation)
    if minus not in calculation:
        calculation = calculation[:0] + str(minus) + calculation[0:]
    else:
        calculation = calculation.replace(minus, "")
    text_result.delete(0, END)
    text_result.insert(0, calculation)


def calculate_percent():
    global calculation
    calculation = str(float(calculation) / 100)
    text_result.delete(0, END)
    text_result.insert(0, calculation)


def clear_field():
    global calculation
    calculation = ""
    text_result.delete(0, END)
    text_result.insert(0, "0")
    pass


def clear_string():
    global calculation
    calculation = calculation[0:-1]
    text_result.delete(0, END)
    text_result.insert(0, calculation)
    if calculation == "":
        btn_AC.config(text="AC", command=clear_field)
        text_result.delete(0, END)
        text_result.insert(0, "0")


def set_appwindow():
    global has_style
    GWL_EXSTYLE = -20
    WS_EX_APPWINDOW = 0x00040000
    WS_EX_TOOLWINDOW = 0x00000080
    if not has_style:
        hwnd = windll.user32.GetParent(root.winfo_id())
        style = windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
        style = style & ~WS_EX_TOOLWINDOW
        style = style | WS_EX_APPWINDOW
        res = windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, style)
        root.withdraw()
        root.after(10, lambda: root.wm_deiconify())
        has_style = False


def move_app(e):
    root.geometry(f'+{e.x_root}+{e.y_root}')


def frame_mapped(e):
    global z
    root.overrideredirect(True)
    if z == 1:
        set_appwindow()
        z = 0


def minimize(event):
    global z
    root.state('withdrawn')
    root.overrideredirect(False)
    root.state('iconic')
    z = 1


def quitter(e):
    root.destroy()


# Create window
root = Tk()
root.geometry('234x323+500+200')
root.bind("<Map>", frame_mapped)
root.resizable(width=False, height=False)
root.overrideredirect(True)
root.update_idletasks()
root.after(10, lambda: set_appwindow())

# Create icon for app
# root.tk.call('wm', 'iconphoto', root.w, PhotoImage(file='icons/icons8-calculator-48.ico'))


# Create title bar
title_bar = Frame(root, bg="#57504d", relief="raised", height=20, width=234, padx=0)
title_bar.grid(columnspan=4, sticky="nsew", ipady=4)

# Bind the title bar
title_bar.bind("<B1-Motion>", move_app)

# Create close button on title bar
icon_red = Image.open('icons/icons8-red-circle-48.png')
resized_icon_red = icon_red.resize((14, 14), Image.LANCZOS)
red = ImageTk.PhotoImage(resized_icon_red)
close_label = Label(title_bar, bg="#57504d", fg="white", image=red)
close_label.pack(side=LEFT, padx=2)
close_label.bind("<Button-1>", quitter)

# Create minimize button on title bar
icon_yellow = Image.open('icons/icons8-yellow-circle-48.png')
resized_icon_yellow = icon_yellow.resize((14, 14), Image.LANCZOS)
yellow = ImageTk.PhotoImage(resized_icon_yellow)
hide_label = Label(title_bar, bg="#57504d", fg="white", image=yellow)
hide_label.pack(side=LEFT)
hide_label.bind("<Button-1>", minimize)


# Create Entry bar for text input
text_result = Entry(root, width=9, font=("Arial", 34), relief=FLAT, justify=RIGHT, bg="#57504d", bd=0, fg="white")
text_result.config(insertbackground="#57504d")
text_result.insert(0, '0')
text_result.grid(row=1, columnspan=4, ipadx=3.5, ipady=5)


# Create buttons for numbers and other functions
btn_0 = Button(root, text="0", command=lambda: add_to_calculation(0), height=1, width=3, font=("Arial", 18),
               bg="#837e7d", fg="white")
btn_0.grid(row=6, column=0, columnspan=2, sticky="nsew")
btn_1 = Button(root, text="1", command=lambda: add_to_calculation(1), height=1, width=3, font=("Arial", 18),
               bg="#837e7d", fg="white")
btn_1.grid(row=5, column=0, sticky="nsew")
btn_2 = Button(root, text="2", command=lambda: add_to_calculation(2), height=1, width=3, font=("Arial", 18),
               bg="#837e7d", fg="white")
btn_2.grid(row=5, column=1, sticky="nsew")
btn_3 = Button(root, text="3", command=lambda: add_to_calculation(3), height=1, width=3, font=("Arial", 18),
               bg="#837e7d", fg="white")
btn_3.grid(row=5, column=2, sticky="nsew")
btn_4 = Button(root, text="4", command=lambda: add_to_calculation(4), height=1, width=3, font=("Arial", 18),
               bg="#837e7d", fg="white")
btn_4.grid(row=4, column=0, sticky="nsew")
btn_5 = Button(root, text="5", command=lambda: add_to_calculation(5), height=1, width=3, font=("Arial", 18),
               bg="#837e7d", fg="white")
btn_5.grid(row=4, column=1, sticky="nsew")
btn_6 = Button(root, text="6", command=lambda: add_to_calculation(6), height=1, width=3, font=("Arial", 18),
               bg="#837e7d", fg="white")
btn_6.grid(row=4, column=2, sticky="nsew")
btn_7 = Button(root, text="7", command=lambda: add_to_calculation(7), height=1, width=3, font=("Arial", 18),
               bg="#837e7d", fg="white")
btn_7.grid(row=3, column=0, sticky="nsew")
btn_8 = Button(root, text="8", command=lambda: add_to_calculation(8), height=1, width=3, font=("Arial", 18),
               bg="#837e7d", fg="white")
btn_8.grid(row=3, column=1, sticky="nsew")
btn_9 = Button(root, text="9", command=lambda: add_to_calculation(9), height=1, width=3, font=("Arial", 18),
               bg="#837e7d", fg="white")
btn_9.grid(row=3, column=2, sticky="nsew")
btn_AC = Button(root, text="AC", command=clear_field, height=1, width=3, font=("Arial", 18),
                bg="#6a6563", fg="white")
btn_AC.grid(row=2, column=0, sticky="nsew")
btn_plus_or_minus = Button(root, text="⁺/₋", command=lambda: add_minus("-"), height=1, width=3, font=("Arial", 18),
                           bg="#6a6563", fg="white")
btn_plus_or_minus.grid(row=2, column=1, sticky="nsew")
btn_percent = Button(root, text="%", command=calculate_percent, height=1, width=3, font=("Arial", 18),
                     bg="#6a6563", fg="white")
btn_percent.grid(row=2, column=2, sticky="nsew")
btn_divide = Button(root, text="÷", command=lambda: add_to_calculation("/"), height=1, width=3, font=("Arial", 18),
                    bg="#fea00f", fg="white")
btn_divide.grid(row=2, column=3, sticky="nsew")
btn_multiply = Button(root, text="×", command=lambda: add_to_calculation("*"), height=1, width=3, font=("Arial", 18),
                      bg="#fea00f", fg="white")
btn_multiply.grid(row=3, column=3, sticky="nsew")
btn_subtract = Button(root, text="-", command=lambda: add_to_calculation("-"), height=1, width=3, font=("Arial", 18),
                      bg="#fea00f", fg="white")
btn_subtract.grid(row=4, column=3, sticky="nsew")
btn_add = Button(root, text="+", command=lambda: add_to_calculation("+"), height=1, width=3, font=("Arial", 18),
                 bg="#fea00f", fg="white")
btn_add.grid(row=5, column=3, sticky="nsew")
btn_decimal = Button(root, text=".", command=lambda: add_to_calculation("."), height=1, width=3, font=("Arial", 18),
                     bg="#837e7d", fg="white")
btn_decimal.grid(row=6, column=2, sticky="nsew")
btn_equal = Button(root, text="=", command=evaluate_calculation, height=1, width=3, font=("Arial", 18),
                   bg="#fea00f", fg="white")
btn_equal.grid(row=6, column=3, sticky="nsew")


root.mainloop()
