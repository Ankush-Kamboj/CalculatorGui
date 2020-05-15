import tkinter as tk
import tkinter.font as font

class Calculator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("327x330")
        self.root.title("Calculator")
        self.root.resizable("false", "false")
        self.root.configure(background = "white")

        self.cal_textbox = tk.StringVar()
        self.special_char = ['+', '-', '/', '*', '.']   
        buttonFont = font.Font(size = "15", weight = "bold")

        # Calculator Layout
        self.calEntry = tk.Entry(self.root, textvariable = self.cal_textbox,bd = 8, font = buttonFont, state = "readonly", relief = "groove" )
        self.calEntry.grid(column = 0, row = 0, columnspan = 3, ipady = 10)

        buttonDel = tk.Button(self.root, text = "Del",bg = "grey",fg = "white", font = buttonFont, height = 2, width = 6, relief = "flat", command = lambda : self.cal_textbox.set(self.cal_textbox.get()[0:len(self.cal_textbox.get())-1]))
        buttonDel.grid(column = 3, row = 0)

        button7 = tk.Button(self.root, text = "7",bg = "black",fg = "white",font = buttonFont, height = 2, width = 6, relief = "flat", command = lambda : self.cal_textbox.set(self.cal_textbox.get() + "7"))
        button7.grid(column = 0, row = 1)

        button6 = tk.Button(self.root, text = "8",bg = "black",fg = "white",font = buttonFont, height = 2, width = 6, relief = "flat", command = lambda : self.cal_textbox.set(self.cal_textbox.get() + "8"))
        button6.grid(column = 1, row = 1)

        button9 = tk.Button(self.root, text = "9",bg = "black",fg = "white",font = buttonFont, height = 2, width = 6, relief = "flat", command = lambda : self.cal_textbox.set(self.cal_textbox.get() + "9"))
        button9.grid(column = 2, row = 1)

        buttondiv = tk.Button(self.root, text = "/",bg = "grey",fg = "white",font = buttonFont, height = 2, width = 6, relief = "flat", command = lambda : self.operator("/"))
        buttondiv.grid(column = 3, row = 1)

        button4 = tk.Button(self.root, text = "4",bg = "black",fg = "white",font = buttonFont, height = 2, width = 6, relief = "flat", command = lambda : self.cal_textbox.set(self.cal_textbox.get() + "4"))
        button4.grid(column = 0, row = 2)

        button5 = tk.Button(self.root, text = "5",bg = "black",fg = "white",font = buttonFont, height = 2, width = 6, relief = "flat", command = lambda : self.cal_textbox.set(self.cal_textbox.get() + "5"))
        button5.grid(column = 1, row = 2)

        button6 = tk.Button(self.root, text = "6",bg = "black",fg = "white",font = buttonFont, height = 2, width = 6, relief = "flat", command = lambda : self.cal_textbox.set(self.cal_textbox.get() + "6"))
        button6.grid(column = 2, row = 2)

        buttonmul = tk.Button(self.root, text = "x",bg = "grey",fg = "white",font = buttonFont, height = 2, width = 6, relief = "flat", command = lambda : self.operator("*"))
        buttonmul.grid(column = 3, row = 2)

        button1 = tk.Button(self.root, text = "1",bg = "black",fg = "white",font = buttonFont, height = 2, width = 6, relief = "flat", command = lambda : self.cal_textbox.set(self.cal_textbox.get() + "1"))
        button1.grid(column = 0, row = 3)

        button2 = tk.Button(self.root, text = "2",bg = "black",fg = "white",font = buttonFont, height = 2, width = 6, relief = "flat", command = lambda : self.cal_textbox.set(self.cal_textbox.get() + "2"))
        button2.grid(column = 1, row = 3)

        button3 = tk.Button(self.root, text = "3",bg = "black",fg = "white",font = buttonFont, height = 2, width = 6, relief = "flat", command = lambda : self.cal_textbox.set(self.cal_textbox.get() + "3"))
        button3.grid(column = 2, row = 3)

        buttonmin = tk.Button(self.root, text = "-",bg = "grey",fg = "white",font = buttonFont, height = 2, width = 6, relief = "flat", command = lambda: self.operator("-"))
        buttonmin.grid(column = 3, row = 3)

        buttondec = tk.Button(self.root, text = ".",bg = "black",fg = "white",font = buttonFont, height = 2, width = 6, relief = "flat", command = lambda : self.operator("."))
        buttondec.grid(column = 0, row = 4)

        button0 = tk.Button(self.root, text = "0",bg = "black",fg = "white",font = buttonFont, height = 2, width = 6, relief = "flat", command = lambda : self.cal_textbox.set(self.cal_textbox.get() + "0"))
        button0.grid(column = 1, row = 4)

        buttoneq = tk.Button(self.root, text = "=",bg = "red",fg = "white", font = buttonFont, height = 2, width = 6, relief = "flat", command = self.result)
        buttoneq.grid(column = 2, row = 4)

        buttonplus = tk.Button(self.root, text = "+", bg = "grey",fg = "white", font = buttonFont, height = 2, width = 6, relief = "flat", command = lambda: self.operator("+"))
        buttonplus.grid(column = 3, row = 4)


    # Checks if there is a special charactor at last, if not then adds the pressed special character
    def operator(self, op):
        try:
            if not self.cal_textbox.get()[-1] in self.special_char:
                self.cal_textbox.set(self.cal_textbox.get() + op)
        except IndexError:
            pass


    # Calculates the final result
    def result(self):
        try:
            self.cal_textbox.set(str(eval(self.cal_textbox.get())))
        except SyntaxError:
            pass


    def showDialog(self):
        self.root.mainloop()


if __name__ == "__main__":
    Calculator().showDialog()