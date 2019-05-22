process_status=["READY","RUN","FINISH"]
class PCB:
    def __init__(self,name,ctime,ntime):
        self.name=name#进程名
        self.next=None
        self.time_slice=2#时间片长度
        self.ctime=ctime#到达时间
        self.take_cpu_time=0#进程已使用的CPU时间长度
        self.process_time=ntime#进程需要运行的总时间
        self.status=""#进程状态

class PCBC:
    def __init__(self):
        self.run=None#运行队列指针
        self.ready=None#准备队列的头指针
        self.tail=None#准备队列的尾指针
        self.finish=None#完成队列指针

def input_process(pcbc):
    pcb=PCB(input("请输入进程名：\n"),int(input("请输入进程到达时间（整数）：\n")),int(input("请输入进程需要的时间(整数):\n")))
    pcb.status=process_status[0]
    if pcbc.ready is None and pcbc.tail is None:#当等待队列为空的时候
        pcbc.ready=pcbc.tail=pcb
        pcb.next=None
    else:
        pcb.next=pcbc.tail.next
        pcbc.tail.next=pcb
        pcbc.tail=pcb

#对刚输入完的等待队列按照FCFS排序
def sortready(pcbc):
    p=pcbc.ready
    if p.next is None :#就只有一个结点
        return
    mc=p.ctime
    while p is not None:#先找到最小的那个值
        if mc>p.ctime:
            mc=p.ctime
        p=p.next
    p=pcbc.ready
    if p.ctime==mc:#当前头结点就是最小的那个
        print("当前头结点就是最小的")
    else:
        while p.next is not None:#把最小的那个值放到头结点，其后的往前移
            c=p.next
            if c.ctime==mc:#当前结点就是最小的那个
                head=PCB(pcbc.ready.name,pcbc.ready.ctime,pcbc.ready.process_time)
                head.status=process_status[0]
                new_head=PCB(c.name,c.ctime,c.process_time)
                new_head.status=process_status[0]
                new_head.next=pcbc.ready.next
                pcbc.ready=new_head#更换头结点
                while p is not None:#找到新的链表中p的位置
                    if id(new_head.next)==id(p.next):
                        p=new_head
                        break
                    new_head=new_head.next
                p.next=head
                head.next=c.next
                break

            p=p.next
    p=pcbc.ready
    #while p.next is not None:#把头结点以后的点从小到大排队
        #p=p.next
    t=pcbc.ready
    while t.next is not None:
        pre=t
        t=t.next
        flo=t.next
        if flo is None:
            break
        if pre.ctime<=flo.ctime and flo.ctime<t.ctime:
            t.next=flo.next
            flo.next=t
            pre.next=flo
    pcbc.taile=pcbc.ready
    while pcbc.tail.next is not None:
        pcbc.tail=pcbc.tail.next

#打印当前控制块的内容
def print_log(pcbc):
    ready=pcbc.ready
    finish=pcbc.finish
    print("----------------------------------------------------\n")
    if pcbc.run is not None:
        print(pcbc.run.name,"\t",pcbc.run.ctime,"\t",pcbc.run.take_cpu_time,"\t",pcbc.run.process_time,"\n")
    else:
        print("Run is empty! \n")
    print("Ready: \n")
    while ready is not None:
        print(ready.name,"   ",ready.ctime,"   ",ready.take_cpu_time,"   ",ready.process_time,"\n")
        ready=ready.next
    print("Finish: \n")
    while finish is not None:
        print(finish.name,"\t",finish.ctime,"\t",finish.take_cpu_time,"\t",finish.process_time,"\n")
        finish=finish.next

#用时间片轮转法调度算法
def timeslice(pcbc):
    ready=pcbc.ready
    tail=pcbc.tail
    finish=pcbc.finish
    leavetime=0
    while 1==1:
        run=PCB(ready.name,ready.ctime,ready.process_time)#把等待队列的队首运行
        run.take_cpu_time=ready.take_cpu_time
        run.status=process_status[1]
        if (run.process_time-run.take_cpu_time)>run.time_slice+leavetime:#时间片用完 没有完成
            leavetime=0
            run.take_cpu_time=run.take_cpu_time+run.time_slice
            run.status=process_status[0]
            ready=ready.next
            tail.next=run
            tail= tail.next
        else:#时间片没用完 已经完成
            finish=run
            run.status=process_status[2]
            leavetime=run.time_slice+run.take_cpu_time-run.process_time#时间片剩余的时间
            ready=ready.next
        pcbc.ready=ready
        #pcbc.finish=finish
        if leavetime==0:#当前时间片没有用完 先不输出
            pcbc.finish.next=finish
        else:
            pcbc.finish=finish
            print_log(pcbc)
            finish=None
        if pcbc.ready is None:
            break






def main():
    pcbc=PCBC()
    pcb_num=int(input("请输入要处理的进程数目:"))
    for i in range(pcb_num):
        input_process(pcbc)
    sortready(pcbc)
    print_log(pcbc)
    timeslice(pcbc)
if __name__ == "__main__":
    main()
