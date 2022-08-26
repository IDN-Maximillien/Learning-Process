from cgitb import text
import tkinter

mainWindow = tkinter.Tk()

label1 = tkinter.Label(mainWindow, text = 'Login')
label2 = tkinter.Label(mainWindow, text = 'Register')

button1 = tkinter.Button(mainWindow, text = 'Button 1')
button2 = tkinter.Button(mainWindow, text = 'Button 2')

label1.pack()
label2.pack()
button1.pack()
button2.pack()

mainWindow.mainloop()