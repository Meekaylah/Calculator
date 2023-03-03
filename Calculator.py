import tkinter as tk

calculation = ""


def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)


def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "Error")


def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")
    pass


root = tk.Tk()
root.geometry("191x270")

text_result = tk.Text(root, height=1, width=8, font=("Arial", 32))
text_result.grid(columnspan=5)

btn_0 = tk.Button(root, text="0", command=lambda: add_to_calculation(0), height=1, width=3, font=("Arial", 16))
btn_0.grid(row=5, column=1, columnspan=2, sticky="nsew")
btn_1 = tk.Button(root, text="1", command=lambda: add_to_calculation(1), height=1, width=3, font=("Arial", 16))
btn_1.grid(row=4, column=1, sticky="nsew")
btn_2 = tk.Button(root, text="2", command=lambda: add_to_calculation(2), height=1, width=3, font=("Arial", 16))
btn_2.grid(row=4, column=2, sticky="nsew")
btn_3 = tk.Button(root, text="3", command=lambda: add_to_calculation(3), height=1, width=3, font=("Arial", 16))
btn_3.grid(row=4, column=3, sticky="nsew")
btn_4 = tk.Button(root, text="4", command=lambda: add_to_calculation(4), height=1, width=3, font=("Arial", 16))
btn_4.grid(row=3, column=1, sticky="nsew")
btn_5 = tk.Button(root, text="5", command=lambda: add_to_calculation(5), height=1, width=3, font=("Arial", 16))
btn_5.grid(row=3, column=2, sticky="nsew")
btn_6 = tk.Button(root, text="6", command=lambda: add_to_calculation(6), height=1, width=3, font=("Arial", 16))
btn_6.grid(row=3, column=3, sticky="nsew")
btn_7 = tk.Button(root, text="7", command=lambda: add_to_calculation(7), height=1, width=3, font=("Arial", 16))
btn_7.grid(row=2, column=1, sticky="nsew")
btn_8 = tk.Button(root, text="8", command=lambda: add_to_calculation(8), height=1, width=3, font=("Arial", 16))
btn_8.grid(row=2, column=2, sticky="nsew")
btn_9 = tk.Button(root, text="9", command=lambda: add_to_calculation(9), height=1, width=3, font=("Arial", 16))
btn_9.grid(row=2, column=3, sticky="nsew")
btn_AC = tk.Button(root, text="AC", command=clear_field, height=1, width=3, font=("Arial", 16))
btn_AC.grid(row=1, column=1, sticky="nsew")
btn_plus_or_minus = tk.Button(root, text="⁺/₋", command="", height=1, width=3, font=("Arial", 16))
btn_plus_or_minus.grid(row=1, column=2, sticky="nsew")
btn_percent = tk.Button(root, text="%", command=lambda: add_to_calculation("%"), height=1, width=3, font=("Arial", 16))
btn_percent.grid(row=1, column=3, sticky="nsew")
btn_divide = tk.Button(root, text="÷", command=lambda: add_to_calculation("/"), height=1, width=3, font=("Arial", 16))
btn_divide.grid(row=1, column=4, sticky="nsew")
btn_multiply = tk.Button(root, text="×", command=lambda: add_to_calculation("*"), height=1, width=3, font=("Arial", 16))
btn_multiply.grid(row=2, column=4, sticky="nsew")
btn_subtract = tk.Button(root, text="-", command=lambda: add_to_calculation("-"), height=1, width=3, font=("Arial", 16))
btn_subtract.grid(row=3, column=4, sticky="nsew")
btn_add = tk.Button(root, text="+", command=lambda: add_to_calculation("+"), height=1, width=3, font=("Arial", 16))
btn_add.grid(row=4, column=4, sticky="nsew")
btn_decimal = tk.Button(root, text=".", command=lambda: add_to_calculation("."), height=1, width=3, font=("Arial", 16))
btn_decimal.grid(row=5, column=3, sticky="nsew")
btn_equal = tk.Button(root, text="=", command=evaluate_calculation, height=1, width=3, font=("Arial", 16))
btn_equal.grid(row=5, column=4, sticky="nsew")
root.mainloop()
