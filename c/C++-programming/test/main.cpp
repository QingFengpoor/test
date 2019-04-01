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
}*Oend,*Cend;


/*void correct(mytable* &position,int d) {
	mytable* father = new mytable; father = position;
	mytable* temp = new mytable; temp = position;
	position->f = d;
	do {
		if (position->next == NULL) {
			break;
		}
		if (position->f > position->next->f);
		position = position->next;
	} while (position != NULL);
}*/

//判断重复状态
bool isrepead(S t, mytable *oh, mytable *ch) {
	mytable *h = new mytable;
	h = oh;
	while (h != NULL) {
		if (t.p == h->o.p&&t.w == h->o.w&&t.b == h->o.b)return true;
		h = h->next;
	}
	h = ch;
	do {
		if (t.p == h->o.p&&t.w == h->o.w&&t.b == h->o.b)return true;
		h = h->next;
	} while (h != NULL);
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
			}
			p = p->next;
		} while (p != NULL);
	}
}

//扩展结点
void kuozhan(S op0[],S op1[],mytable* &Ohead,mytable* &Cend,mytable *Chead) {
	//在扩展前，修正open表。将首结点的启发函数值修改为f(x)=d,并排序Open表
	//取出open首结点;放到close中
	mytable *cn = new mytable;
	*cn = *Ohead;
	//cn->father = Ohead->father;
	cn->next = NULL;
	Cend->next = cn;
	Cend = cn;

	std::cout << cn->o.p << ',' << cn->o.w << ',' << cn->o.b << "  进行扩展" << endl;
	std::cout << "**************************" << endl;
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
				else if (isrepead(temp, Ohead,Chead));
				else {
					mytable *no = new mytable;
					*no = { cn,temp,t,ff(t,fh(temp)),NULL };
					inserttable(Ohead, no);//把扩展结点放到Open表中
				}

			}
		}
	}
	//船在右岸，开向左岸
	if (cn->o.b == 0) {
		for (int i = 0; i < 4; i++) {
			S temp = cn->o;
			if ((5-cn->o.p >= op1[i].p)&&(5-cn->o.w >= op1[i].w)) {
				temp.p = temp.p + op1[i].p;
				temp.w = temp.w + op1[i].w;
				temp.b = 1;
				int t = cn->d+1;
				if (temp.w > temp.p&&temp.p != 0);//野人人数大于传教士人数
				else if ((M - temp.w) > (M - temp.p) && (5 - temp.p) != 0);//对岸的野人人数大于传教士人数
				else if (isrepead(temp, Ohead,Chead));
				else {
					mytable* no = new mytable;
					*no = { cn,temp,t,ff(t,fh(temp)),NULL };
					inserttable(Ohead, no);//把扩展结点放到Open表中
				}
			}
		}
	}
	Ohead = Ohead->next;
}

void outt(mytable* Oposition,mytable* Cposition) {
	//输出open 表
	std::cout << "\topen表" << endl;
	do {
		if (Oposition == NULL)break;
		std::cout << Oposition->o.p << ',' << Oposition->o.w << ',' << Oposition->o.b << "\t\td=" << Oposition->d << " h=" << Oposition->f - Oposition->d << " f=" << Oposition->f << endl;
		Oposition = Oposition->next;
	} while (Oposition!= NULL);
	std::cout << "\tclose表" << endl;
	do {
		if (Cposition == NULL)break;
		std::cout << Cposition->o.p << ',' << Cposition->o.w << ',' << Cposition->o.b << "\t\td=" << Cposition->d << " h=" << Cposition->f - Cposition->d << " f=" << Cposition->f << endl;
		Cposition = Cposition->next;
	} while (Cposition!= NULL);
	std::cout << "**************************" << endl;
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
	S operates_to1[4];//b=0时，回左岸｛1,0,0｝，｛0，1，0｝,{2,0,0},{0,2,0}
	operates_to1[0] = { 1,0,0 };
	operates_to1[1] = { 0,1,0 };
	operates_to1[2] = { 2,0,0 };
	operates_to1[3] = { 0,2,0 };
	mytable *O_head=new mytable;
	O_head->o = start; O_head->father = NULL; O_head->next = NULL; O_head->d = 0; O_head->f = 0;
	Oend = O_head;
	mytable *C_head=new mytable;
	C_head->d = 0; C_head->f = 8; C_head->father = NULL; C_head->next = NULL; C_head->o = { 0,0,0 };
	Cend = C_head;
	mytable *r = new mytable;//存放所有出现过的状态
	r->next = NULL;

	int flag = 0;//是否无解
	while (O_head->o.p != end.p || O_head->o.w != end.w || O_head->o.b != end.b)
	{
		kuozhan(operates_to0,operates_to1,O_head,Cend,C_head);
		outt(O_head, C_head->next);
		if (O_head == NULL||O_head->d >= 100) {
			flag = 1;
			break;
		}
	}
	if (flag) {
		std::cout << "无解" << endl;
	}
	else std::cout << "有解" << endl;
	/*else
	{
		mytable* answer_head = new mytable;
		answer_head = O_head;
		mytable* answer_end = new mytable;
		answer_end = O_head;
		while (answer_head->father != NULL) {
			answer_head->next = answer_head;
			answer_head = answer_head->father;
		}
		mytable* answer = new mytable;
		answer = answer_head;
		while (answer != NULL) {
			cout <<'('<< answer->o.p << ',' << answer->o.w << ',' << answer->o.b << ')' << endl;
			answer = answer->next;
		}
	}*/
	system("pause");
}
