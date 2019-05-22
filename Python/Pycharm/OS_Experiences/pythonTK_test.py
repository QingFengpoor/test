import tkinter as tk
from tkinter import ttk

timeslice=2
process_status=["Ready","Run","Finish"]

class PCB:
    def __init__(self,name,ctime,ntime):
        self.name=name
        self.ctime=ctime#到达时间
        self.ntime=ntime#所需时间
        self.status=process_status[0]#状态为等待
        self.takecpu=0#已用时间


class Application(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.pack()
        self.Ready=[]
        self.Finish=[]
        self.Run=None
        self.leavetime=0
        self.create_widgets()

    def create_widgets(self):
        self.pcbentry=tk.Entry(self)
        self.pcbentry.grid(row=0,column=0)
        self.pcbbutton=tk.Button(self,text="进程(进程名 到达时间 需要时间",command=self.inputPCB)
        self.pcbbutton.grid(row=0,column=1,sticky="W")
        self.pcbclearbutton=tk.Button(self,text="清空",command=self.clearpcb)
        self.pcbclearbutton.grid(row=0,column=2,sticky="W")
        self.pcbbutton.grid(row=0,column=1,sticky="W")
        self.showRunbutton=tk.Button(self,text="显示运行队列",command=lambda :self.showPCB([self.Run]))
        self.showRunbutton.grid(row=1,column=0,sticky="W")
        self.showReadybutton=tk.Button(self,text="显示等待队列",command=lambda :self.showPCB(self.Ready))
        self.showReadybutton.grid(row=1,column=1,sticky="W")
        self.showFinishbuton=tk.Button(self,text="显示完成队列",command=lambda :self.showPCB(self.Finish))
        self.showFinishbuton.grid(row=1,column=2,sticky="W")
        self.runontime=tk.Button(self,text="运行一个时间片",command=self.runoenslice)
        self.runontime.grid(row=2,column=0,sticky="W")

    def inputnum(self):
        self.num=0
        if self.numentry.get() != '':
            self.num=int(self.numentry.get().strip())
        print(self.num)

    def clearnum(self):
        self.numentry.delete(0,len(self.numentry.get()))

    def inputPCB(self):
        s=self.pcbentry.get().split()
        print(s)
        try:
            P=PCB(s[0],int(s[1]),int(s[2]))
            self.Ready.append(P)
        except:
            print("ERROR")
        self.sortPCB()

    def clearpcb(self):
        self.pcbentry.delete(0,len(self.pcbentry.get()))

    def sortPCB(self):#采用冒泡排序法
        for i in range(len(self.Ready)):
            for j in range(len(self.Ready)-1):
                if self.Ready[j].ctime>self.Ready[j+1].ctime:
                    tmp=self.Ready[j]
                    self.Ready[j]=self.Ready[j+1]
                    self.Ready[j+1]=tmp

    def showPCB(self,LPCB):
        columns=("进程名","到达时间","需要时间","进程状态")
        treeview=ttk.Treeview(self,height=18,show="headings",columns=columns)
        treeview.column("进程名",width=66,anchor="center")
        treeview.column("到达时间",width=66,anchor="center")
        treeview.column("需要时间",width=66,anchor="center")
        treeview.column("进程状态",width=66,anchor="center")

        treeview.heading("进程名",text="进程名")
        treeview.heading("到达时间",text="到达时间")
        treeview.heading("需要时间",text="需要时间")
        treeview.heading("进程状态",text="进程状态")
        treeview.grid(row=3,column=0,columnspan=3,rowspan=len(LPCB)+1)
        try:
            for i in range(len(LPCB)):
                treeview.insert('',i,values=(LPCB[i].name,LPCB[i].ctime,LPCB[i].ntime,LPCB[i].status))
        except:
            print("ERROR showPCB")

    def runoenslice(self):
        if len(self.Ready)==0:
            print("没有等待进程了")
            self.Run=None
            return
        self.Run=self.Ready[0]
        #del LReady[0]
        self.Run.status=process_status[1]
        print("Running:\n",self.Run.name,"\t",self.Run.ctime,"\t",self.Run.status)
        if self.leavetime ==0:#运行一个完整的时间片
            if self.Run.ntime>self.Run.takecpu+timeslice:#还未完成
                self.Run.takecpu=self.Run.takecpu+timeslice
                self.Run.status=process_status[0]#送回等待队列尾
                self.Ready.append(self.Run)
                self.Run.status=process_status[1]
                del self.Ready[0]
            else:
                self.leavetime=self.Run.takecpu+timeslice-self.Run.ntime
                self.Run.takecpu=self.Run.ntime
                self.Run.status=process_status[2]
                self.Finish.append(self.Run)
                self.Run.status=process_status[1]
                del self.Ready[0]
        else :#运行剩余的时间片
            if self.Run.ntime>self.Run.takecpu+self.leavetime:
                self.Run.takecpu=self.Run.takecpu+self.leavetime
                self.leavetime=0
                self.Run.status=process_status[0]
                self.Ready.append(self.Run)
                self.Run.status=process_status[1]
                del self.Ready[0]
            else:
                self.leavetime=self.Run.takecpu+self.leavetime-self.Run.ntime
                self.Run.status=process_status[2]
                self.Run.takecpu=self.Run.ntime
                self.Finsh.append(self.Run)
                self.Run.status=process_status[1]
                del self.Ready[0]
    def say_hi(self):
        print("hi there, everyone!")

def main():
    root=tk.Tk()
    app=Application(master=root)
    app.mainloop()

if __name__=="__main__":
    main()
