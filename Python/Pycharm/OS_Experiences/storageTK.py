import tkinter as tk
from tkinter import ttk
import time

areastatus=["未分配","已分配"]
class ACB:
    def __init__(self,size):
        self.order=1
        self.size=size#单位为kb
        self.star=0
        self.status=areastatus[0]#0表示未分配，1表示已分配

class JCB:
    def __init__(self,name,size):
        self.name=name
        self.size=size
        self.areaorder=-1#所属分区号

class Application(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.pack()
        self.area=[]
        self.jcb0=[]
        self.jcb1=[]
        self.create_widgets()

    def create_widgets(self):
        self.sizelabel=tk.Label(self,text="输入分区大小(单位k,共62k)")
        self.sizelabel.grid(row=0,column=0,sticky="W")
        self.sizevar=tk.StringVar()
        self.sizevar.set("剩余64kb")
        self.sizeentry=tk.Entry(self,textvariable=self.sizevar)
        self.sizeentry.grid(row=0,column=1,sticky="W")
        self.sizebutton=tk.Button(self,text="提交分区",command=self.addarea)
        self.sizebutton.grid(row=0,column=2,sticky="W")
        self.areashowbutton=tk.Button(self,text="显示分区",command=self.showarea)
        self.areashowbutton.grid(row=0,column=3,sticky="W")
        self.joblabel=tk.Label(self,text="输入作业(作业名 作业大小(单位k))")
        self.joblabel.grid(row=1,column=0,sticky="W")
        self.jobvar=tk.StringVar()
        self.jobentry=tk.Entry(self,textvariable=self.jobvar)
        self.jobentry.grid(row=1,column=1,sticky="W")
        self.jobbutton=tk.Button(self,text="提交作业",command=self.addjcb)
        self.jobbutton.grid(row=1,column=2,sticky="W")
        self.jobshowbutton=tk.Button(self,text="显示作业",command=self.showjcb)
        self.jobshowbutton.grid(row=1,column=3,sticky="W")
        self.areadjobbutton=tk.Button(self,text="按序分配一个作业",command=self.distribut)
        self.areadjobbutton.grid(row=2,column=0,sticky="W")
        self.areacjobbutton=tk.Button(self,text="按序撤销一个作业",command=self.cancle)
        self.areacjobbutton.grid(row=2,column=2,sticky="W")




    def addarea(self):
        try:
            size=int(self.sizeentry.get())
        except:
            print("分区输入有错")
            return
        acb=ACB(size)
        if len(self.area)==0:
            if acb.star+acb.size>62:
                print("分区大小过大")
                self.sizevar.set("剩余62kb")
            else:
                self.area.append(acb)
                self.sizevar.set("剩余"+str(62-acb.star-acb.size)+"kb")
        else:
            last=self.area[len(self.area)-1]
            acb.order=last.order+1
            acb.star=last.star+last.size
            if acb.star+acb.size>62:
                print("分区大小过大")
                self.sizevar.set("剩余"+str(62-last.star-last.size)+"kb")
            else:
                self.area.append(acb)
                self.sizevar.set("剩余"+str(62-acb.star-acb.size)+"kb")

    def showarea(self):
        columns=("分区号","分区大小","起址","状态")
        treeview=ttk.Treeview(self,height=18,show="headings",columns=columns)
        treeview.column("分区号",width=66,anchor="center")
        treeview.column("分区大小",width=66,anchor="center")
        treeview.column("起址",width=66,anchor="center")
        treeview.column("状态",width=66,anchor="center")

        treeview.heading("分区号",text="分区号")
        treeview.heading("分区大小",text="分区大小")
        treeview.heading("起址",text="起址")
        treeview.heading("状态",text="状态")
        treeview.grid(row=3,column=0,rowspan=len(self.area)+1,columnspan=3)
        try:
            for i in range(len(self.area)):
                j=self.area[i]
                treeview.insert('',i,values=(j.order,j.size,j.star,j.status))
        except:
            print("分区插入表格出错")

    def addjcb(self):
        s=self.jobentry.get().split()
        if len(s)!=2:
            print("输入有错")
            return
        try:
            s[1]=int(s[1])
        except:
            print("作业大小有误")
            return
        if int(s[1])>62:
            print("不能接受的作业")
            print(s)
            return
        job=JCB(s[0],int(s[1]))
        jf=0
        for i in self.jcb0:
            if s[0]==i.name:
                print("作业名重复")
                jf=1
        if jf==0:
            self.jcb0.append(job)
        self.jobentry.delete(0,len(self.jobentry.get()))


    def showjcb(self):
        columns=("作业名","作业大小","分配到的分区号")
        treeview=ttk.Treeview(self,height=18,show="headings",columns=columns)
        treeview.column("作业名",width=77,anchor="center")
        treeview.column("作业大小",width=88,anchor="center")
        treeview.column("分配到的分区号",width=99,anchor="center")

        treeview.heading("作业名",text="作业名")
        treeview.heading("作业大小",text="作业大小")
        treeview.heading("分配到的分区号",text="分配到的分区号")
        treeview.grid(row=3, column=0, rowspan=len(self.jcb0)+len(self.jcb1)+1, columnspan=3)
        try:
            for i in range(len(self.jcb0)):
                j=self.jcb0[i]
                treeview.insert('',i,values=(j.name,j.size,j.areaorder))
            for i in range(len(self.jcb1)):
                j=self.jcb1[i]
                treeview.insert('',i,values=(j.name,j.size,j.areaorder))
        except:
            print("作业插入表格出错")

    def distribut(self):#使用类似最佳适应分配,把作业队列中的第一个分配到内存
        if len(self.jcb0)==0:
            print("当前没有要分配的作业")
            return
        cr=self.jcb0[0]
        smin=62
        sa=-1
        for i in self.area:
            if i.status==areastatus[0] and i.size>=cr.size and i.size-cr.size<smin:
                smin=i.size-cr.size
                sa=i.order
        if sa!=-1:
            cr.areaorder=sa
            self.jcb1.append(cr)
            del self.jcb0[0]
            for i in self.area:
                if i.order==sa:
                    i.status=areastatus[1]
        else:
            print("目前还不能分配")

    def cancle(self):
        if len(self.jcb1)==0:
            print("当前没有可撤销的作业")
            return
        cr=self.jcb1[0]
        for i in self.area:
            if i.order==cr.areaorder:
                i.status=areastatus[0]
        del self.jcb1[0]








def main():
    root=tk.Tk()
    app=Application(master=root)
    app.mainloop()

if __name__=="__main__":
    main()
