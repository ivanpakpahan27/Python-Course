from tkinter import *
MainWindow = Tk()

counter = 0

def fungsi_1():
	global counter
	counter +=1
	print('hello world ',counter)
	Label1.config(text=counter)

def fungsi_2():
	global counter
	counter -=1
	print('hello world ',counter)
	Label1.config(text=counter)

Button1   = Button(MainWindow, text='+', command=fungsi_1)
Button2   = Button(MainWindow, text='-', command=fungsi_2)
Label1    = Label(MainWindow,  text = '0')

Label1.pack()
Button1.pack(side = LEFT)
Button2.pack(side = LEFT)
MainWindow.geometry('400x400+200+200')
MainWindow.mainloop()