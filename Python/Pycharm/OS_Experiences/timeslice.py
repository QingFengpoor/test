from tkinter import *

timeslice=2
process_status=["Ready","Run","Finish"]
class PCB:
    def __init__(self,name,ctime,ntime):
        self.name=name
        self.ctime=ctime#到达时间
        self.ntime=ntime#所需时间
        self.status=process_status[0]#状态为等待
        self.takecpu=0#已用时间

def inputPCB(k,Ready):
    for i in range(k):
        P=PCB(input("进程名：\n"),int(input("进程到达时间（整数）：\n")),int(input("进程需要的时间(整数):\n")))
        Ready.append(P)
def sortPCB(LPCB):#采用冒泡排序法
    for i in range(len(LPCB)):
        for j in range(len(LPCB)-1):
            if LPCB[j].ctime>LPCB[j+1].ctime:
                tmp=LPCB[j]
                LPCB[j]=LPCB[j+1]
                LPCB[j+1]=tmp
    return LPCB

def showPCB(LPCB):
    L=LPCB
    for P in L:
        print(P.name,"\t",P.ctime,"\t",P.ntime,"\t",P.status,"\n")
        #P=P.next

def runtimeslice(LReady):
    Run=None
    Finsh=[]
    leavetime=0
    while len(LReady) != 0:
        Run=LReady[0]
        #del LReady[0]
        Run.status=process_status[1]
        print("Running:\n",Run.name,"\t",Run.ctime,"\t",Run.status)
        if leavetime ==0:#运行一个完整的时间片
            if Run.ntime>Run.takecpu+timeslice:#还未完成
                Run.takecpu=Run.takecpu+timeslice
                Run.status=process_status[0]#送回等待队列尾
                LReady.append(Run)
                del LReady[0]
            else:
                leavetime=Run.takecpu+timeslice-Run.ntime
                Run.takecpu=Run.ntime
                Run.status=process_status[2]
                Finsh.append(Run)
                del LReady[0]
        else :#运行剩余的时间片
            if Run.ntime>Run.takecpu+leavetime:
                Run.takecpu=Run.takecpu+leavetime
                leavetime=0
                Run.status=process_status[0]
                LReady.append(Run)
                del LReady[0]
            else:
                leavetime=Run.takecpu+leavetime-Run.ntime
                Run.status=process_status[2]
                Run.takecpu=Run.ntime
                Finsh.append(Run)
                del LReady[0]
        print("Ready:\n")
        showPCB(LReady)
        print("Finish:\n")
        showPCB(Finsh)

def main():
    Ready=[]#等待队列头结点
    num=int(input("输入进程数："))
    inputPCB(num,Ready)
    sortPCB(Ready)
    showPCB(Ready)
    runtimeslice(Ready)
if __name__=="__main__":
    main()
