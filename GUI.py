import tkinter.font
from tkinter import *
from stackCalculator import *
windowbgcolor = "#769FCD"
textfgcolor = "#F9F7F7"
buttonbgcolor = "#DBE2EF"
calline = []
answer = None
class Window:
    window = None
    font1 = None
    font2 = None
    font3 = None
    frame1 = None
    frame2 = None
    calculation = None

    buttons = [
        "C", "(", ")", "<",
        "7", "8", "9", "/",
        "4", "5", "6", "*",
        "1", "2", "3", "-",
        ".", "0", "=", "+"
    ]
    def __init__(self):
        self.window = Tk()
        self.window.title("Calculator")
        self.window.geometry("300x420")
        self.window.resizable(False, False)
    def create_frame(self, filltype):
        self.frame = tkinter.Frame(self.window, bg=windowbgcolor)
        self.frame.pack(fill=filltype, padx=5, pady=5)
        return self.frame

    def create_label(self, frame, rowIndex, colInex, font, text):
        self.label = Label(frame, font=font, text=text, bg=windowbgcolor, fg=textfgcolor)
        self.label.grid(row=rowIndex, column=colInex, padx=5, pady=5, sticky="e")
        return self.label

    def set_window_bgcolor(self, bg):
        self.window.configure(bg=bg)

    def window_loop(self):
        self.window.mainloop()

    def create_numpad(self, frame, root):
        rowindex = 0
        colindex = 0
        button_width = 5
        button_height = 2
        for i in self.buttons:
            Button(frame, bg=buttonbgcolor, text=i, width=button_width, height=button_height, font=font3,
                   command=lambda c=i: root.click_button(c)).grid(
                row=rowindex, column=colindex, padx=5, pady=5, sticky="nsew")
            colindex += 1
            if colindex == 4:
                colindex = 0
                rowindex += 1

    def click_button(self, value):
        if IsDigit(value):
            calline.append(value)
            cal_text()
        elif (value in priority) or value == "(" or value == ")" or value == ".":
            calline.append(value)
            cal_text()
        elif value == "<":
            calline.pop()
            cal_text()
        elif value == "C":
            print("모두 지우기")
            output_stack.Clear()
            stack.Clear()
            calline.clear()
            num.clear()
            label_clear()
        elif value == "=":
            result = PostFix(calline)
            output_stack.Clear()
            stack.Clear()
            calline.clear()
            num.clear()
            answer_text(result)
def cal_text():
    calculation.config(text="".join(calline))
def label_clear():
    calculation.config(text="")
    answer.config(text="")

def answer_text(answervalue):
    answer.config(text=answervalue)
#def main_window():
if __name__ == "__main__":
    root = Window()
    root.set_window_bgcolor(windowbgcolor)
    font1 = tkinter.font.Font(size=25, weight="bold")
    font2 = tkinter.font.Font(size=13)
    font3 = tkinter.font.Font(weight="bold")

    frame1 = root.create_frame("both")
    calculation = root.create_label(frame1, 0, 0, font2, "")
    answer = root.create_label(frame1, 1, 0, font1, "")

    frame1.columnconfigure(0, weight=1)

    frame2 = root.create_frame("none")
    root.create_numpad(frame2, root)

    root.window_loop()
