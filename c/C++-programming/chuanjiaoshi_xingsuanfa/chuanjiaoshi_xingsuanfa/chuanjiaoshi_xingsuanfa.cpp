// chuanjiaoshi_xingsuanfa.cpp : 此文件包含 "main" 函数。程序执行将在此处开始并结束。
//

#include "pch.h"
#include <iostream>
#include <cstdlib>
using namespace std;



struct S
{
	int p;//左岸传教士人数
	int w;//左岸野人人数
	int b;//船在左岸 b=1；船在右岸 b=0；
}s;

const int M = 5,BM=3;

//计算h(x)
int fh(S a) {
	return a.p + a.w -2*a.b;
}
//计算f(x)
int ff(int d, int h) {
	return d + h;
}

struct mytable
{
	//int id;//当前结点号
	struct mytable *father;//父结点号
	S o;//当前状态
	int d;//实际代价
	int f;//启发函数值
	struct mytable *next;//下一个表内容
}*Oend,*Cend,*rcend;


//判断重复状态
bool isrepead(S t, mytable *rh) {
	mytable *h = new mytable;
	h = rh;
	while (h != NULL) {
		if (t.p == h->o.p&&t.w == h->o.w&&t.b == h->o.b)return true;
		h = h->next;
	}
	return false;
}

void inserttable(mytable *&head, mytable *n) {
	mytable* p = head;
	if (p == NULL) {
		p->next = n;
	}
	else {
		do {
			if (p->next == NULL) {
				p->next = n;
				break;
			}
			if (n->f < p->next->f) {
				n->next = p->next;
				p->next = n;
				break;
			}
			p = p->next;
		} while (p != NULL);
	}
}

//扩展结点
void kuozhan(S op0[],S op1[],mytable* &Ohead,mytable* &Cend,mytable *rchead,mytable *&rcend) {
	//在扩展前，修正open表。将首结点的启发函数值修改为f(x)=d,并排序Open表
	//取出open首结点;放到close中
	mytable *cn = new mytable,*rn=new mytable;
	//cn->d = Ohead->d; cn->f = Ohead->f; cn->o = Ohead->o;
	//cn->father = Ohead->father;
	//cn->next = NULL;
	*cn = { Ohead->father,Ohead->o,Ohead->d,Ohead->f,NULL };
	*rn = { Ohead->father,Ohead->o,Ohead->d,Ohead->f,NULL };
	//船在左岸，开向右岸
	if (cn->o.b == 1) {
		for (int i = 0; i < 9; i++) {
			S temp = cn->o;
			if (cn->o.p >= op0[i].p&&cn->o.w>=op0[i].w) {
				temp.p = temp.p - op0[i].p;
				temp.w = temp.w - op0[i].w;
				temp.b = 0;
				int t = cn->d+1;
				if (temp.w > temp.p&&temp.p!=0);//野人人数大于传教士人数
				else if ((M - temp.w) > (M - temp.p) && (5 - temp.p) != 0);//对岸的野人人数大于传教士人数
				else if (isrepead(temp, rchead));
				else {
					mytable *no = new mytable;
					*no = { cn,temp,t,ff(t,fh(temp)),NULL };
					inserttable(Ohead, no);//把扩展结点放到Open表中
					mytable *nr = new mytable;
					*nr = { cn,temp,t,ff(t,fh(temp)),NULL };
					rcend->next = nr;
					rcend = rcend->next;
				}
				
			}
		}
	}
	//船在右岸，开向左岸
	if (cn->o.b == 0) {
		for (int i = 0; i < 9; i++) {
			S temp = cn->o;
			if ((M-cn->o.p >= op1[i].p)&&(M-cn->o.w >= op1[i].w)) {
				temp.p = temp.p + op1[i].p;
				temp.w = temp.w + op1[i].w;
				temp.b = 1;
				int t = cn->d+1;
				if (temp.w > temp.p&&temp.p != 0);//野人人数大于传教士人数
				else if ((M - temp.w) > (M - temp.p) && (5 - temp.p) != 0);//对岸的野人人数大于传教士人数
				else if (isrepead(temp, rchead));
				else {
					mytable* no = new mytable;
					*no = { cn,temp,t,ff(t,fh(temp)),NULL };
					inserttable(Ohead, no);//把扩展结点放到Open表中
					mytable *nr = new mytable;
					*nr = { cn,temp,t,ff(t,fh(temp)),NULL };
					rcend->next = nr;
					rcend = rcend->next;
				}
			}
		}
	}

	char c = ',';
	int p, w, b;
	p = cn->o.p; w = cn->o.w; b = cn->o.b;
	std::cout << p << c << w << c << b << "  进行扩展" << endl;
	std::cout << "*****************************" << endl;

	Ohead = Ohead->next;
	Cend->next = cn; rcend->next = rn;
	Cend = cn; rcend = rn;
}

void outt(mytable* Oposition,mytable* Cposition) {
	int p, w, b, d, f, h;
	//输出open 表
	std::cout << "\topen表" << endl;
	do {
		if (Oposition == NULL)break;
		p = Oposition->o.p; w = Oposition->o.w; b = Oposition->o.b;
		d = Oposition->d; f = Oposition->f; h = Oposition->f - Oposition->d;
		std::cout << p << ',' <<w << ',' << b << "\t\td=" << d << " h=" << h << " f=" << f << endl;
		Oposition = Oposition->next;
	} while (Oposition!= NULL);
	std::cout << "\tclose表" << endl;
	do {
		if (Cposition == NULL)break;
		p = Cposition->o.p; w = Cposition->o.w; b = Cposition->o.b;
		d = Cposition->d; f = Cposition->f; h = Cposition->f - Cposition->d;
		std::cout << p << ',' << w << ',' << b << "\t\td=" << d << " h=" << h<< " f=" << f << endl;
		Cposition = Cposition->next;
	} while (Cposition!= NULL);
	std::cout << "*****************************" << endl;
}

int main()
{
	//初始化
	S start;
	start.p = start.w = 5;
	start.b = 1;
	S end;
	end.p = end.w = 0;
	end.b = 0;
	S operates_to0[9];//b=1时，去右岸｛0,3,1｝，｛3，0，1｝，｛1,2,1｝，｛2,1,1｝，｛0,2,1｝，｛2,0,1｝，｛1,1,1｝,{0,1.1},{1,0,1}
	operates_to0[0] = { 0,3,1 };
	operates_to0[1] = { 3,0,1 };
	operates_to0[2] = { 1,2,1 };
	operates_to0[3] = { 2,1,1 };
	operates_to0[4] = { 0,2,1 };
	operates_to0[5] = { 2,0,1 };
	operates_to0[6] = { 1,1,1 };
	operates_to0[7] = { 0,1,1 };
	operates_to0[8] = { 1,0,1 };
	S operates_to1[9];//b=0时，回左岸｛1,0,0｝，｛0，1，0｝,{2,0,0},{0,2,0}，｛3,0,0｝，｛0,3,0｝，｛1,1,0｝，｛2,1,0｝，｛1,2,0｝
	operates_to1[0] = { 1,0,0 };
	operates_to1[1] = { 0,1,0 };
	operates_to1[2] = { 2,0,0 };
	operates_to1[3] = { 0,2,0 };
	operates_to1[4] = { 3,0,0 };
	operates_to1[5] = { 0,3,0 };
	operates_to1[6] = { 1,1,0 };
	operates_to1[7] = { 2,1,0 };
	operates_to1[8] = { 1,2,0 };
	mytable *O_head=new mytable;
	O_head->o = start; O_head->father = NULL; O_head->next = NULL; O_head->d = 0; O_head->f = 0;
	Oend = O_head;
	mytable *C_head=new mytable;
	C_head->d = 0; C_head->f = 8; C_head->father = NULL; C_head->next = NULL; C_head->o = { 0,0,0 };
	Cend = C_head;
	mytable *rchead = new mytable;//存放所有出现过的状态
	rchead->next = NULL; rchead->father = NULL; rchead->o.b = -1; rchead->o.p = -1; rchead->o.w = -1;
	rcend = rchead;

	int flag = 0;//是否无解
	while ((O_head->o.p != end.p || O_head->o.w != end.w || O_head->o.b != end.b))//&&(O_head->o.p!=5||O_head->o.w!=5||O_head->o.b!=0))
	{
		kuozhan(operates_to0,operates_to1,O_head,Cend,rchead,rcend);
		outt(O_head, C_head->next);
		if (O_head == NULL||O_head->d >= 100) {
			flag = 1;
			break;
		}
	}
	if (flag) {
		std::cout << "无解" << endl;
	}
	else
	{
		mytable* answer_end = new mytable;
		answer_end = O_head;
		answer_end->next = NULL;
		while (answer_end->father != NULL) {
			mytable* t = new mytable;
			t->o.b = answer_end->o.b; t->o.p = answer_end->o.p; t->o.w = answer_end->o.w;
			t->next = answer_end->next;
			answer_end = answer_end->father;
			answer_end->next = t;
		}
		mytable* answer = new mytable;
		answer = answer_end;
		while (answer != NULL) {
			cout <<'('<< answer->o.p << ',' << answer->o.w << ',' << answer->o.b << ')' << endl;
			answer = answer->next;
		}
	}
	system("pause");
}

// 运行程序: Ctrl + F5 或调试 >“开始执行(不调试)”菜单
// 调试程序: F5 或调试 >“开始调试”菜单

// 入门提示: 
//   1. 使用解决方案资源管理器窗口添加/管理文件
//   2. 使用团队资源管理器窗口连接到源代码管理
//   3. 使用输出窗口查看生成输出和其他消息
//   4. 使用错误列表窗口查看错误
//   5. 转到“项目”>“添加新项”以创建新的代码文件，或转到“项目”>“添加现有项”以将现有代码文件添加到项目
//   6. 将来，若要再次打开此项目，请转到“文件”>“打开”>“项目”并选择 .sln 文件
