from tkinter import *

#making window

root = Tk()

root.title("skalculator")

root.resizable(0,0)

#making i/o fields

inputfield = Entry(root , width = 50)
inputfield.grid(row = 0 ,column = 0 , columnspan = 4)
inputfield.focus()

outputfield = Entry(root , width = 50)
outputfield.grid(row = 1  , column =  0  , columnspan = 4)


#button actions

def addnum(number):
	current = number
	already = inputfield.get()
	inputfield.delete(0 , END)
	inputfield.insert(0 , str(already) + str(current))


def evaluate():
	outputfield.delete(0, END)
	outputfield.insert(0 , eval(inputfield.get()))

#making buttons

b1 = Button(root , text = "1" , command = lambda : addnum(1) )
b1.grid(row = 2 , column = 0 )

b2 = Button(root , text = "2" , command = lambda : addnum(2) )
b2.grid(row = 2 , column = 1 )

b3 = Button(root , text = "3" , command = lambda : addnum(3) )
b3.grid(row = 2 , column = 2 )

bplus = Button(root , text = "+" , command = lambda : addnum("+"))
bplus.grid(row = 2 , column = 3 )

b4 = Button(root , text = "4" , command = lambda : addnum(4) )
b4.grid(row = 3 , column = 0 )

b5 = Button(root , text = "5" , command = lambda : addnum(5) )
b5.grid(row = 3 , column = 1)

b6 = Button(root , text = "6" , command = lambda : addnum(6) )
b6.grid(row = 3 , column = 2)

bminus = Button(root , text = "-"   , command = lambda : addnum("-"))
bminus.grid(row = 3 , column = 3)

b7 = Button(root , text = "7" , command = lambda : addnum(7) )
b7.grid(row = 4 , column = 0)

b8 = Button(root , text = "8" , command = lambda : addnum(8) )
b8.grid(row = 4 , column = 1)

b9 = Button(root , text = "9" , command = lambda : addnum(9) )
b9.grid(row = 4 , column = 2)

bmultiply = Button(root , text = "x"  , command = lambda : addnum("*"))
bmultiply.grid(row = 4 , column = 3)

b0 = Button(root , text = "0" , command = lambda : addnum(0) )
b0.grid(row = 5 , column = 0 )

bclear = Button(root , text = "clear" , command = lambda : inputfield.delete(0,END))
bclear.grid(row = 5 , column = 1)

bequals = Button(root  , text = "=" , command = evaluate)
bequals.grid(row = 5 , column = 2)

bdivide = Button(root  , text = "/" , command = lambda : addnum("/"))
bdivide.grid(row = 5 , column = 3)




root.mainloop()
