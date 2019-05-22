from tkinter import *

rv=Tk()

def eventx(event):
    print("点击的x和y轴：",event.x,event.y)

fra=Frame(rv,width=100,height=100,bg="red")

fra.bind("<Button-1>",eventx)

fra.pack()

rv.mainloop()
