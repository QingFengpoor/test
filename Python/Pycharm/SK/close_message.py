from tkinter import *

from tkinter import messagebox

rv=Tk()

def closex():
    if messagebox.askokcancel("关闭","确定要关闭该窗口吗？"):
        rv.destroy()

rv.protocol("WM_DELETE_WINDOW",closex())

rv.mainloop()
