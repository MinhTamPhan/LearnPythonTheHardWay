import Tkinter
import time
from Tkconstants import *
# if you are working under Python 3, comment the previous line and comment out the following line
#from tkinter import *
tk = Tkinter.Tk()
frame = Tkinter.Frame(tk, relief=RIDGE, borderwidth=2)
frame.pack(fill=BOTH,expand=1)
label = Tkinter.Label(frame, text="Hello, World")
label.pack(fill=X, expand=1)
button = Tkinter.Button(frame,text="Exit",command=tk.destroy)
button.pack(side=BOTTOM)
tk.mainloop()
