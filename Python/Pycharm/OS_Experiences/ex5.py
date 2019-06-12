import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog
import numpy as np

class Application(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.pack()
        self.create_widgets()
        self.Init()

    def create_widgets(self):
        self.entryrequest=tk.Entry(self)
        self.entryrequest.grid(row=0,column=0,sticky="W")
        self.bankbutton=tk.Button(self,text="确认请求",command=self.bank)
        self.bankbutton.grid(row=0,column=1,sticky="W")

    def Init(self):
        self.m=simpledialog.askinteger("输入","进程数目：")
        self.n=simpledialog.askinteger("输入","资源种类数：")
        self.maxneed=[]#最大所需
        self.allocation=[]#当前已分配
        self.available=[]#现有可得
        i=0
        while  i<self.m:
            spn=simpledialog.askstring("第%d个进程最多所需资源数"%(i+1),"共有%d种资源 用空格隔开:"%self.n).strip().split()
            spg=simpledialog.askstring("第%d个进程已分配的资源数"%(i+1),"共有%d种资源 用空格隔开:"%self.n).strip().split()
            if len(spn)!=self.n or len(spg)!=self.n:
                messagebox.showerror("错误提示","输入有误，重新输入")
                continue
            spn=[int(i) for i in spn]
            self.maxneed.append(spn)
            spg=[int(i) for i in spg]
            self.allocation.append(spg)
            i+=1
        i=0
        while i<self.n:
            avaliable=simpledialog.askinteger("资源%d:"%i,"资源现有数目：")
            self.available.append(avaliable)
            i+=1
    def bank(self):
        self.show(self.maxneed)
        self.show(self.allocation)
        R=self.entryrequest.get().strip().split()
        id=simpledialog.askinteger("REQUEST","第几个进程")-1
        R=[int(i) for i in R]
        if len(R)!=self.n:
            messagebox.showinfo("错误提示","输入有误,重新输入")
            self.entryrequest.delete(0,len(self.entryrequest.get()))
            return
        NEED=[self.maxneed[id][i]-self.allocation[id][i] for i in range(self.n)]
        if not R<=NEED :
            messagebox.showinfo("错误提示","请求资源数超过需要数")
            self.entryrequest.delete(0,len(self.entryrequest.get()))
            return
        if not R<=self.available:
            messagebox.showinfo("错误提示","请求资源数超过可得数")
            self.entryrequest.delete(0,len(self.entryrequest.get()))
            return
        self.available=[self.available[i]-R[i] for i in range(self.n)]
        self.allocation[id]=[self.allocation[id][i]+R[i] for i in range(self.n)]
        if not self.safe():
            messagebox.showinfo("错误提示","请求被拒绝")
            self.available=[self.available[i]-R[i] for i in range(self.n)]
            self.allocation[id]=[self.allocation[id][i]+R[i] for i in range(self.n)]
            self.entryrequest.delete(0,len(self.entryrequest.get()))
            return
        messagebox.showinfo("提示","同意分配请求")
    def safe(self):
        Work=self.available
        Finish=np.zeros(self.m)
        ALLNEED=[[self.maxneed[i][j]-self.allocation[i][j] for j in range(self.n)] for i in range(self.m)]
        i=0
        route=[]
        while i<self.m:
            if Finish[i]==0 and ALLNEED[i]<=Work:
                Work=[Work[p]+self.allocation[i][p] for p in range(self.n)]
                Work+=self.allocation[i]
                Finish[i]=1
                route.append(i)
                i=0
                continue
            i+=1
        if any(Finish==1):
            route=[str(i) for i in route]
            messagebox.showinfo("提示","安全序列:"+','.join(route))
            return True
        else:
            messagebox.showinfo("提示","系统是不安全的")
            return False
    def show(self,LT):
        tmptk=tk.Toplevel(self)
        if LT==self.maxneed:
            tmptk.title("进程最多所需资源数")
        if LT==self.allocation:
            tmptk.title("进程已分配资源数")
        columns=["进程id"]
        for i in range(self.n):
            columns.append("资源%d数目"%i)
        treeview=ttk.Treeview(tmptk,height=18,show="headings",columns=columns)
        for i in range(len(columns)):
            treeview.column(columns[i],width=66,anchor="center")
            treeview.heading(columns[i],text=columns[i])
        treeview.pack()
        for i in range(self.m):
            values=[i]
            for j in range(self.n):
                values.append(LT[i][j])
            treeview.insert('',i,values=values)









def main():
    root=tk.Tk()
    root.geometry("+120+120")
    app=Application(master=root)
    app.mainloop()

if __name__=="__main__":
    main()
