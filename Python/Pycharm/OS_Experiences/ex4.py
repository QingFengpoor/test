import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
class MDFNode:
    def __init__(self,name,filedir):
        self.username=name#用户名
        self.filedir=filedir#文件目录指针

class UFDNode:
    def __init__(self,filename,protectnum,size):
        self.filename=filename
        self.protectnum=protectnum#一共有三位，分别表示读写和执行。例如：111表示可读可写可执行。
        self.size=size

class AFDNode:
    def __init__(self,filename,protectnum,readwrite):
        self.filename=filename
        self.protectnum=protectnum
        self.readwrite=readwrite


class Application(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.pack()
        self.MDF=[]
        self.UFD=[]#二维的 长度跟MDF保持一致，一一对应
        self.AFD=[]
        self.create_widgets()

    def create_widgets(self):
        self.userlabel=tk.Label(self,text="用户名")
        self.userlabel.grid(row=0,column=0,sticky="W")
        self.userentry=tk.Entry(self)
        self.userentry.grid(row=0,column=1,sticky="W")
        self.userbutton=tk.Button(self,text="添加",command=self.useradd)
        self.userbutton.grid(row=0,column=2,sticky="W")
        self.curuserlabel=tk.Label(self,text="当前用户")
        self.curuserlabel.grid(row=1,column=0,sticky="W")
        self.curuser=tk.StringVar()
        self.curuserentry=tk.Entry(self,textvariable=self.curuser)
        self.curuserentry.grid(row=1,column=1,sticky="W")
        self.curuserbutton=tk.Button(self,text="确认/打印",command=self.curuserconfirm)
        self.curuserbutton.grid(row=1,column=2,sticky="W")
        self.commandlock=0
        self.commandlabel=tk.Label(self,text="选择一个命令")
        self.commandlabel.grid(row=2,column=0,sticky="W")
        self.Createcheckbutton=tk.Checkbutton(self,text="Create",command=self.Create)
        self.Createcheckbutton.grid(row=3,column=0,sticky="W")
        self.Deletecheckbutton=tk.Checkbutton(self,text="Delete",command=self.Delete)
        self.Deletecheckbutton.grid(row=3,column=1,sticky="W")
        self.Opencheckbutton=tk.Checkbutton(self,text="Open",command=self.Open)
        self.Opencheckbutton.grid(row=3,column=2,sticky="W")
        self.Closecheckbutton=tk.Checkbutton(self,text="Close",command=self.Close)
        self.Closecheckbutton.grid(row=4,column=0,sticky="W")
        self.Readcheckbutton=tk.Checkbutton(self,text="Read",command=lambda :self.ReadWrite("r","READADDR"))
        self.Readcheckbutton.grid(row=4,column=1,sticky="W")
        self.Writecheckbutton=tk.Checkbutton(self,text="Write",command=lambda :self.ReadWrite("w","WRITEADDR"))
        self.Writecheckbutton.grid(row=4,column=2,sticky="W")
        self.Byecheckbutton=tk.Checkbutton(self,text="Bye",command=self.Bye)
        self.Byecheckbutton.grid(row=5,column=0,sticky="W")

    def useradd(self):
        m=[self.userentry.get().strip(),len(self.MDF)]
        if m[0] in \
                [x.username for x in self.MDF]:
            messagebox.showinfo("ERROR","用户名重复")
            return
        M=MDFNode(m[0],m[1])
        self.MDF.append(M)
        self.UFD.append([])
        self.userentry.delete(0,len(self.userentry.get()))

    def isuserexist(self):
        filedir=-1
        for i in self.MDF:
            if i.username==self.curuserentry.get():
                filedir=i.filedir
        return filedir

    def curuserconfirm(self):
        if len(self.curuserentry.get())==0:
            messagebox.showinfo("ERROR","输入为空")
            return
        filedir=self.isuserexist()
        if filedir==-1:
            messagebox.showinfo("ERROR","无此用户文件")
            return
        else:
            columns=("文件名")
            treeview=ttk.Treeview(self,height=18,show="headings",columns=columns)
            treeview.column("文件名",width=166,anchor="center")
            treeview.heading("文件名",text="文件名")
            treeview.grid(row=6,column=0)
            for i in range(len(self.UFD[filedir])):
                tmp=self.UFD[filedir][i]
                treeview.insert('',i,values=(tmp.filename))

    def Create(self):
        from tkinter.simpledialog import askstring,askinteger
        if self.commandlock!=0:
            messagebox.showinfo("ERROR","已经选择另外的命令了")
            self.Createcheckbutton.toggle()
            return
        filename=askstring("新建文件","文件名:")
        protectnum=askstring("新建文件","安全码(共三位0/1，表示读写执行，例如111表示可读可写可执行")
        size=askinteger("新建文件","文件大小(单位kb)")
        filedir=self.isuserexist()
        self.Createcheckbutton.toggle()
        self.commandlock=0
        if filedir==-1:
            messagebox.showinfo("ERROR","当前用户不存在，文件添加失败")
            return
        else:
            if filename in [x.filename for x in self.UFD[filedir]]:
                messagebox.showinfo("ERROR","文件名重复")
                return
            U=UFDNode(filename,protectnum,size)
            self.UFD[filedir].append(U)

    def Delete(self):
        from tkinter.simpledialog import askstring
        if self.commandlock!=0:
            messagebox.showinfo("ERROR","已经选择别的命令了")
            self.Deletecheckbutton.toggle()
            return
        filename=askstring("删除文件","文件名")
        filedir=self.isuserexist()
        self.Deletecheckbutton.toggle()
        self.commandlock=0
        if filedir==-1:
            messagebox.showinfo("ERROR","当前用户不存在")
            return
        else:
            if filename not in [x.filename for x in self.UFD[filedir]]:
                messagebox.showinfo("ERROR","文件不存在")
                return
            else:
                j=-1
                for i in range(len(self.UFD[filedir])):
                    if self.UFD[filedir][i].filename==filename:
                        j=i
                if j!=-1:
                    del self.UFD[filedir][j]

    def Open(self):
        from tkinter.simpledialog import askstring
        if self.commandlock!=0:
            messagebox.showinfo("ERROR","已经选择别的命令")
            self.Opencheckbutton.toggle()
            return
        filename=askstring("打开文件","文件名")
        filedir=self.isuserexist()
        self.Opencheckbutton.toggle()
        self.commandlock=0
        if filedir==-1:
            messagebox.showinfo("ERROR","当前用户不存在")
            return
        else:
            if filename not in [x.filename for x in self.UFD[filedir]]:
                messagebox.showinfo("ERROR","文件不存在")
                return
            else:
                ufd=None
                for i in range(len(self.UFD[filedir])):
                    if self.UFD[filedir][i].filename==filename:
                        ufd=self.UFD[filedir][i]
                if int(ufd.protectnum[2])!=1:
                    messagebox.showinfo("ERROR","没有执行权限")
                else:
                    tmp=AFDNode(filename,ufd.protectnum,None)
                    self.AFD.append(tmp)
                    messagebox.showinfo("Info","打开完毕")

    def Close(self):
        from tkinter.simpledialog import askstring
        if self.commandlock!=0:
            messagebox.showinfo("ERROR","已经选择别的命令")
            self.Closecheckbutton.toggle()
            return
        filename=askstring("关闭文件","文件名")
        filedir=self.isuserexist()
        self.Closecheckbutton.toggle()
        self.commandlock=0
        if filedir==-1:
            messagebox.showinfo("ERROR","当前用户不存在")
            return
        else:
            if filename not in [x.filename for x in self.UFD[filedir]]:
                messagebox.showinfo("ERROR","文件不存在")
                return
            else:
                if filename not in [x.filename for x in self.AFD]:
                    messagebox.showinfo("ERROR","文件未打卡")
                    return
                else:
                    for i in range(len(self.AFD)):
                        if self.AFD[i].filename==filename:
                            del self.AFD[i]
                            messagebox.showinfo("Info","关闭完成")

    def ReadWrite(self,rorw,read_writeaddr):
        from tkinter.simpledialog import askstring
        if self.commandlock!=0:
            messagebox.showinfo("ERROR","已经选择别的命令")
            if rorw=="r":
                self.Readcheckbutton.toggle()
            else:
                self.Writecheckbutton.toggle()
            return
        filename=askstring("读文件","文件名")
        filedir=self.isuserexist()
        self.Readcheckbutton.toggle()
        self.commandlock=0
        if filedir==-1:
            messagebox.showinfo("ERROR","当前用户不存在")
            return
        else:
            if filename not in [x.filename for x in self.UFD[filedir]]:
                messagebox.showinfo("ERROR","文件不存在")
                return
            else:
                if filename not in [x.filename for x in self.AFD]:
                    messagebox.showinfo("ERROR","文件未打卡")
                    return
                else:
                    for i in range(len(self.AFD)):
                        if self.AFD[i].filename==filename:
                            if rorw=="r":
                                if int(self.AFD[i].protectnum[0])==1:
                                    self.AFD[i].readwrite=read_writeaddr
                                    messagebox.showinfo("Info","正在读")
                                else:
                                    messagebox.showinfo("ERROR","没有读的权限")
                            else:
                                if int(self.AFD[i].protectnum[1])==1:
                                    self.AFD[i].readwrite=read_writeaddr
                                    messagebox.showinfo("Info","正在写")
                                else:
                                    messagebox.showinfo("ERROR","没有写的权限")

    def Bye(self):
        for i in range(len(self.AFD)):
            del self.AFD[i]
        self.commandlock=1
        self.destroy()

def main():
    root=tk.Tk()
    app=Application(master=root)
    app.mainloop()

if __name__=="__main__":
    main()
