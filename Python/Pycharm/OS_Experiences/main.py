from tkinter import *
from ex1 import *
from ex2 import *
from PIL import Image,ImageTk

tf=Tk()
canvas=tk.Canvas(tf,width=500,height=500,bg="white")
img=Image.open('我与船.gif')
photo=ImageTk.PhotoImage(img)

print(img.size)
print(photo.__sizeof__())
canvas.create_image(0,0,image=photo)
canvas.pack()
tf.title("操作系统实验")
#tf.geometry("500x500")
#tf.geometry("+250+200")
button1=Button(tf,text="实验一 进程调度实验-简单轮转法",font=("宋体",14),command=main)
#button1.grid(row=0,column=0)
button1.pack()
button2=Button(tf,text="实验二 作业调度实验-单道处理系统",font=("宋体",14),command=main)
#button2.grid(row=2,column=0)
button2.pack()
tf.mainloop()
