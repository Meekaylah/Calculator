import tkinter as tk


class Calculator:
    def __init__(self):
        self.root = tk.Tk()

#       numbersBox is the textbox where numbers are typed and results are shown
        self.numbersBox = tk.Text(self.root, height=5, font=('Arial', 18))
        self.numbersBox.pack(padx=10, pady=10)

        self.numbersframe = tk.Frame(self.root)
        self.numbersframe.columnconfigure(0, weight=1)
        self.numbersframe.columnconfigure(1, weight=1)
        self.numbersframe.columnconfigure(2, weight=1)
        self.numbersframe.columnconfigure(3, weight=1)
        self.numbersframe.columnconfigure(4, weight=1)

        self.button0 = tk.Button(self.root, text="AC", font=('Arial', 18))
        self.button0.grid(row=0, column=0, sticky=tk.W+tk.E)

        self.button1 = tk.Button(self.root, text="7", font=('Arial', 18))
        self.button1.grid(row=1, column=0, sticky=tk.W + tk.E)

        self.button2 = tk.Button(self.root, text="4", font=('Arial', 18))
        self.button2.grid(row=2, column=0, sticky=tk.W + tk.E)

        self.button3 = tk.Button(self.root, text="1", font=('Arial', 18))
        self.button3.grid(row=3, column=0, sticky=tk.W + tk.E)

        self.button4 = tk.Button(self.root, text="0", font=('Arial', 18))
        self.button4.grid(row=4, column=1, sticky=tk.W + tk.E)

        self.button5 = tk.Button(self.root, text="⁺/₋", font=('Arial', 18))
        self.button5.grid(row=0, column=1, sticky=tk.W + tk.E)

        self.button6 = tk.Button(self.root, text="8", font=('Arial', 18))
        self.button6.grid(row=1, column=1, sticky=tk.W + tk.E)

        self.button7 = tk.Button(self.root, text="5", font=('Arial', 18))
        self.button7.grid(row=2, column=1, sticky=tk.W + tk.E)

        self.button8 = tk.Button(self.root, text="2", font=('Arial', 18))
        self.button8.grid(row=3, column=1, sticky=tk.W + tk.E)

        self.button9 = tk.Button(self.root, text="%", font=('Arial', 18))
        self.button9.grid(row=0, column=2, sticky=tk.W + tk.E)

        self.button10 = tk.Button(self.root, text="9", font=('Arial', 18))
        self.button10.grid(row=1, column=2, sticky=tk.W + tk.E)

        self.button11 = tk.Button(self.root, text="6", font=('Arial', 18))
        self.button11.grid(row=2, column=2, sticky=tk.W + tk.E)

        self.button12 = tk.Button(self.root, text="3", font=('Arial', 18))
        self.button12.grid(row=3, column=2, sticky=tk.W + tk.E)

        self.button13 = tk.Button(self.root, text=".", font=('Arial', 18))
        self.button13.grid(row=4, column=2, sticky=tk.W + tk.E)

        self.button14 = tk.Button(self.root, text="÷", font=('Arial', 18))
        self.button14.grid(row=0, column=3, sticky=tk.W + tk.E)

        self.button15 = tk.Button(self.root, text="×", font=('Arial', 18))
        self.button15.grid(row=1, column=3, sticky=tk.W + tk.E)

        self.button16 = tk.Button(self.root, text="-", font=('Arial', 18))
        self.button16.grid(row=2, column=3, sticky=tk.W + tk.E)

        self.button17 = tk.Button(self.root, text="+", font=('Arial', 18))
        self.button17.grid(row=3, column=3, sticky=tk.W + tk.E)

        self.button18 = tk.Button(self.root, text="=", font=('Arial', 18))
        self.button18.grid(row=4, column=3, sticky=tk.W + tk.E)

        self.numbersframe.pack()

        self.root.mainloop()

