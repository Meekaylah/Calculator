import tkinter as tk
import ast as ast

calculation = ""

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

def evaluate_calculation():
    global calculation
    try:
        tree = ast.parse(calculation, mode='eval')
    except SyntaxError:
        return  # not a Python expression
    if not all(isinstance(node, (ast.Expression,
                                 ast.UnaryOp, ast.unaryop,
                                 ast.BinOp, ast.operator,
                                 ast.Num)) for node in ast.walk(tree)):
        return  # not a mathematical expression (numbers and operators)

    try:
        result = eval(compile(tree, filename='', mode='eval'))
        calculation = ""
        text_result.delete(1.0, "end")
        text_result.insert(1.0, result)
    except:
        clear_field()
        text_result.insert(1.0, "Error")
        pass

def clear_field():
    global calculation
    calculation = ""
    text_result  .delete(1.0, "end")
    pass


root = tk.Tk()
root.geometry("275x325")

text_result = tk.Text(root, height=2, width=16, font=("Arial", 24))
text_result.grid(columnspan=4)

btn_0 = tk.Button(root, text="0", command=lambda: add_to_calculation(0), width=5, )
btn_1 = tk.Button(root, text="1", command=lambda: add_to_calculation(1))
btn_2 = tk.Button(root, text="2", command=lambda: add_to_calculation(2))
btn_3 = tk.Button(root, text="3", command=lambda: add_to_calculation(3))
btn_4 = tk.Button(root, text="4", command=lambda: add_to_calculation(4))
btn_5 = tk.Button(root, text="5", command=lambda: add_to_calculation(5))
btn_6 = tk.Button(root, text="6", command=lambda: add_to_calculation(6))
btn_7 = tk.Button(root, text="7", command=lambda: add_to_calculation(7))
btn_8 = tk.Button(root, text="8", command=lambda: add_to_calculation(8))
btn_9 = tk.Button(root, text="9", command=lambda: add_to_calculation(9))
btn_AC = tk.Button(root, text="AC", command=lambda: clear_field())
btn_plus_or_minus = tk.Button(root, text="⁺/₋", command="")
btn_percent = tk.Button(root, text="%", command="")
btn_divide = tk.Button(root, text="÷", command="")
btn_multiply = tk.Button(root, text="×", command="")
btn_subtract = tk.Button(root, text="-", command="")
btn_add = tk.Button(root, text="+", command="")
btn_decimal = tk.Button(root, text=".", command="")
btn_equal = tk.Button(root, text="=", command="")
root.mainloop()

