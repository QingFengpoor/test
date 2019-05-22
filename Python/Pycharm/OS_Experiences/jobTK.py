import tkinter as tk
from tkinter import ttk
process_status=["Ready","Run","Finish"]

class PCB:
    def __init__(self,name,ctime,ntime):
        self.name=name
        self.ctime=ctime#到达时间
        self.ntime=ntime#所需时间
        self.status=process_status[0]#状态为等待

class Application(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.pack()
        self.Ready=[]
        self.Run=None
        self.method=""
        self.T=0
        self.create_widgets()

    def create_widgets(self):
        self.FCFScheckbutton=tk.Checkbutton(self,text="FCFS",command=self.FCFSclick)
        self.FCFScheckbutton.grid(row=0,column=0,sticky="W")
        self.SJFcheckbutton=tk.Checkbutton(self,text="SJF",command=self.SJFclick)
        self.SJFcheckbutton.grid(row=0,column=1,sticky="W")
        self.HRNcheckbuton=tk.Checkbutton(self,text="HRN",command=self.HRNclick)
        self.HRNcheckbuton.grid(row=0,column=2,sticky="W")
        self.entrylabel=tk.Label(self,text="格式:进程名 到达时间 需要时间")
        self.entrylabel.grid(row=1,column=0)
        self.pcbentry=tk.Entry(self)
        self.pcbentry.grid(row=2,column=0)
        self.pcbbutton=tk.Button(self,text="确认输入",command=self.inputPCB)
        self.pcbbutton.grid(row=2,column=1,sticky="W")
        #self.pcbclearbutton=tk.Button(self,text="清空",command=self.clearpcb)
        #self.pcbclearbutton.grid(row=2,column=2,sticky="W")
        self.comfirmbutton=tk.Button(self,text="完成录入",command=lambda :self.sortPCB(self.method))
        self.comfirmbutton.grid(row=2,column=2)
        self.runontime=tk.Button(self,text="运行一个进程",command=self.run)
        self.runontime.grid(row=3,column=0,sticky="W")
        self.showbutton=tk.Button(self,text="显示等待队列",command=lambda :self.showPCB(self.Ready))
        self.showbutton.grid(row=3,column=1)

    def FCFSclick(self):
        if self.method=="":
            self.method="FCFS"
        else:
            print("ERROR method FCFSclick")

    def SJFclick(self):
        if self.method=="":
            self.method="SJF"
        else:
            print("ERROR method SJFclick")

    def HRNclick(self):
        if self.method=="":
            self.method="HRN"
        else:
            print("ERROR method HRNclick")

    def inputPCB(self):
        s=self.pcbentry.get().split()
        print(s)
        try:
            P=PCB(s[0],int(s[1]),int(s[2]))
            self.Ready.append(P)
        except:
            print("ERROR")
        #self.sortPCB(method=self.method)
        self.pcbentry.delete(0,len(self.pcbentry.get()))

    def clearpcb(self):
        self.pcbentry.delete(0,len(self.pcbentry.get()))

    def sortPCB(self,method="FCFS"):#采用冒泡排序法
        if method=="FCFS":
            for i in range(len(self.Ready)):
                for j in range(len(self.Ready)-1):
                    if self.Ready[j].ctime>self.Ready[j+1].ctime:
                        tmp=self.Ready[j]
                        self.Ready[j]=self.Ready[j+1]
                        self.Ready[j+1]=tmp
        elif method=="SJF":#先按照FCFS排序然后按照sjf调整顺序
            for i in range(len(self.Ready)):
                for j in range(len(self.Ready)-1):
                    if self.Ready[j].ctime>self.Ready[j+1].ctime:
                        tmp=self.Ready[j]
                        self.Ready[j]=self.Ready[j+1]
                        self.Ready[j+1]=tmp
            for i in range(len(self.Ready)):
                for j in range(i+1,len(self.Ready)):
                    if (self.Ready[i].ctime+self.Ready[i].ntime>self.Ready[j].ctime)and\
                        (self.Ready[i+1].ntime>self.Ready[j].ntime):
                        tmp=self.Ready[j]
                        self.Ready[j]=self.Ready[i+1]
                        self.Ready[i+1]=tmp
        elif method=="HRN":#高相应比 先按照FCFS排序 然后调整 按照相应比调整
            for i in range(len(self.Ready)):
                for j in range(len(self.Ready)-1):
                    if self.Ready[j].ctime>self.Ready[j+1].ctime:
                        tmp=self.Ready[j]
                        self.Ready[j]=self.Ready[j+1]
                        self.Ready[j+1]=tmp
            i=0
            while i<len(self.Ready):
                p=1
                j=i+1
                while j<len(self.Ready):
                    print(p,j)
                    if (self.Ready[i].ctime+self.Ready[i].ntime>self.Ready[j].ctime)and\
                            ((self.Ready[i].ctime+self.Ready[i].ntime-self.Ready[i+p].ctime+self.Ready[i+p].ntime)/self.Ready[i+p].ntime<\
                             (self.Ready[i].ctime+self.Ready[i].ntime-self.Ready[j].ctime+self.Ready[j].ntime)/self.Ready[j].ntime):
                        tmp=self.Ready[j]
                        print("替换前")
                        for r in self.Ready:
                            print(r.name,r.ctime,r.ntime)
                        self.Ready[j]=self.Ready[i+p]
                        self.Ready[i+p]=tmp
                        print("替换后")
                        for r in self.Ready:
                            print(r.name,r.ctime,r.ntime)
                    j=j+1
                    if j==len(self.Ready):
                        if(self.Ready[i].ctime+self.Ready[i].ntime<self.Ready[i+p].ctime):
                            break
                        else:
                            p=p+1
                            j=i+p
                i=i+p+1
                for r in self.Ready:
                    print(r.name,r.ctime,r.ntime)
                print("\n")
        else:
            print("method=\"\"")

    def run(self):
        if len(self.Ready)!=0:
            self.Run=self.Ready[0]
        else:
            self.Run=PCB("没有进程了",0,-1)
        self.Run.status=process_status[1]
        if self.T<self.Run.ctime:
            self.T=self.Run.ctime
        self.T=self.T+self.Run.ntime
        Ti=self.T-self.Run.ctime
        Wi=Ti/self.Run.ntime
        columns=("进程名","完成时刻","周转时间","带权周转时间")
        treeview=ttk.Treeview(self,height=18,show="headings",columns=columns)
        treeview.column("进程名",width=66,anchor="center")
        treeview.column("完成时刻",width=66,anchor="center")
        treeview.column("周转时间",width=66,anchor="center")
        treeview.column("带权周转时间",width=66,anchor="center")

        treeview.heading("进程名",text="进程名")
        treeview.heading("完成时刻",text="完成时刻")
        treeview.heading("周转时间",text="周转时间")
        treeview.heading("带权周转时间",text="带权周转时间")
        treeview.grid(row=4,column=0,columnspan=3,rowspan=2)
        try:
            treeview.insert('',0,values=(self.Run.name,self.T,Ti,Wi))
        except:
            print("ERROR show self.Run")
        if len(self.Ready)!=0:
            del(self.Ready[0])


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
        treeview.grid(row=4,column=0,columnspan=3,rowspan=len(LPCB)+1)
        try:
            for i in range(len(LPCB)):
                treeview.insert('',i,values=(LPCB[i].name,LPCB[i].ctime,LPCB[i].ntime,LPCB[i].status))
        except:
            print("ERROR showPCB")

def main():
    root=tk.Tk()
    app=Application(master=root)
    app.mainloop()

if __name__=="__main__":
    main()
