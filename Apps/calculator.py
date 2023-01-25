import tkinter
from PIL import ImageTk, Image

# import time

def evaluate():
    func = disp.get()
    a = eval(func)
    text = str(a)
    disp.delete(0,'end')
    disp.insert(0,text)


def cleared():
    disp.delete(0,'end')

def backspace():
    func = disp.get()
    # func = func.rstrip(func[-1])
    a = func[:-1]
    disp.delete(0,'end')
    disp.insert(0,a)


def add_char(inp):
    strii = disp.get()
    strii += inp
    disp.delete(0, 'end')
    disp.insert(0, strii)

window = tkinter.Tk()
window.title("calci")
window.geometry('600x800')


expression = "0"

disp = tkinter.Entry(window)
disp.grid(column=0, row=1, columnspan=4)
clear = tkinter.Button(window, text="C",command=cleared)
clear.grid(column=0,row=2, columnspan=3,sticky='nesw')

back = tkinter.Button(window, text="<-",command=lambda:backspace())
back.grid(column=3,row=2, columnspan=1,sticky='nesw')

one = tkinter.Button(window, text="1",command=lambda:add_char('1'))
one.grid(column=0,row=3, columnspan=1,sticky='nesw')
# one.bind("<Button-1>",add_char('1'))

two = tkinter.Button(window, text="2",command=lambda:add_char('2'))
two.grid(column=1,row=3, columnspan=1,sticky='nesw')
three = tkinter.Button(window, text="3",command=lambda:add_char('3'))
three.grid(column=2,row=3, columnspan=1,sticky='nesw')
plus = tkinter.Button(window, text="+",command=lambda:add_char('+'))
plus.grid(column=3,row=3, columnspan=1,sticky='nesw')

four = tkinter.Button(window, text="4",command=lambda:add_char('4'))
four.grid(column=0,row=4, columnspan=1,sticky='nesw')
five = tkinter.Button(window, text="5",command=lambda:add_char('5'))
five.grid(column=1,row=4, columnspan=1,sticky='nesw')
six = tkinter.Button(window, text="6",command=lambda:add_char('6'))
six.grid(column=2,row=4, columnspan=1,sticky='nesw')
minus = tkinter.Button(window, text="-",command=lambda:add_char('-'))
minus.grid(column=3,row=4, columnspan=1,sticky='nesw')

seven = tkinter.Button(window, text="7",command=lambda:add_char('7'))
seven.grid(column=0,row=5, columnspan=1,sticky='nesw')
eight = tkinter.Button(window, text="8",command=lambda:add_char('8'))
eight.grid(column=1,row=5, columnspan=1,sticky='nesw')
nine = tkinter.Button(window, text="9",command=lambda:add_char('9'))
nine.grid(column=2,row=5, columnspan=1,sticky='nesw')
multiply = tkinter.Button(window, text="*",command=lambda:add_char('*'))
multiply.grid(column=3,row=5, columnspan=1,sticky='nesw')

dot = tkinter.Button(window, text=".",command=lambda:add_char('.'))
dot.grid(column=0,row=6, columnspan=1,sticky='nesw')
zero = tkinter.Button(window, text="0",command=lambda:add_char('0'))
zero.grid(column=1,row=6, columnspan=1,sticky='nesw')
equal = tkinter.Button(window, text="=",command=lambda:evaluate())
equal.grid(column=2,row=6, columnspan=1,sticky='nesw')
divide = tkinter.Button(window, text="/",command=lambda:add_char('/'))
divide.grid(column=3,row=6, columnspan=1,sticky='nesw')

# add_char('0')
# cleared()
# add_char('3')

window.mainloop()

