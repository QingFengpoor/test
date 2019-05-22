from tkinter import *
from PIL import Image,ImageTk
import cv2
#PIL 的导入必须在tkinter 之后 不然报错
#AttributeError: type object 'Image' has no attribute 'open'

tux=cv2.imread("C:/Users/feng/Pictures/psbNJNK3QUI.bmp")
cv2image = cv2.cvtColor(tux, cv2.COLOR_BGR2RGBA)  # 转换颜色从BGR到RGBA
print(type(cv2image))
current_image = Image.fromarray(cv2image)  # 将图像转换成Image对象
tv=Tk()
imgx = ImageTk.PhotoImage(image=current_image)
label = Label(tv,image=imgx)
label.image = imgx
label.grid(row=1, column=0, rowspan=4, sticky=W + E + N + S, padx=10, pady=10)  # sticky=W + E + N + S 表示填充控件
tv.mainloop()
