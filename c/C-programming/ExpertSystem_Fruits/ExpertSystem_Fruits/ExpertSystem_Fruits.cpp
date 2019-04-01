#include "pch.h"
#include <string.h>
#include <iostream>
using namespace std;
#define True 1
#define False 0
#define DontKnow -1
//事实
const char * str[] = { "圆球体","小球体","类似圆球","大球体","心状" ,
	"橙色","紫色、绿色","近似土灰色","绿色黑纹","红色有斑点",
	"酸、甜","甜","果皮不能食用","许多个在一起","果皮有毛毛",
	"大，皮不能吃","小","桔子","葡萄","猕猴桃","西瓜","草莓",0 };
//规则前提
int rulep[][6] = { {1,6,11,13,0,0},{2,7,11,14,0,0},{3,8,11,15,0,0},{4,9,12,16,0,0},{5,10,11,17,0,0} };
//规则对应结论
int rulec[] = { 18,19,20,21,22 ,0};
//事实类
class fact 
{
private:
	int Number;//事实的编号
	char Content[21];//事实的内容
	int Active;//事实是否已判断符合
	int Succ;//是否有结论
public:
	fact *Next;
	fact(int Num, char *L)
	{
		strcpy_s(Content,21, L);
		Number = Num;
		Active = False;
		//-1 是已经推理，不符合。1 是已经推理，符合。
		Succ = DontKnow; //0 是无，-1 是不知道，1 是有。
		Next = NULL;
	}
	char *GetContent()
	{
		char *L;
		L = new char[21];
		strcpy_s(L,21, Content);
		return L;
	}
	int GetNumber()
	{
		return Number;
	}
	int GetAct()
	{
		return Active;
	}
	int GetSucc()
	{
		return Succ;
	}
	void PutAct(const int Act0, int Suc0)
	{
		Active = Act0;
		Succ = Suc0;
	}
};
fact *Fact;
//规则前提列表类
class list
{
private:
	int Number;
public:
	list *Next;
	list(int Num)
	{
		Number = Num;
		Next = NULL;
	}
	int GetNumber()
	{
		return Number;
	}
};
//规则类
class rule
{
	char *Name;//规则名
	list *Pre;//规则的前提
	int Conc;//规则的结论
public:
	rule *Next;
	rule(char *N, int P[], int C);
	~rule();
	int Query();
	void GetName()
	{
		cout << Name;
	}
};
rule::~rule()
{
	list *L;
	while (Pre)
	{
		L = Pre->Next;
		delete Pre;
		Pre = L;
	}
	delete Name;
}
rule::rule(char *N, int P[], int C)
{
	int i;
	list *L;
	Pre = NULL;
	Next = NULL;
	Name = new char[strlen(N) + 1];
	strcpy_s(Name,21, N);
	i = 0;
	while (P[i] != 0)
	{
		L = new list(P[i++]);
		L->Next = Pre;
		Pre = L;
	}
	Conc = C;
}
//规则的查询
int rule::Query()
{
	char c;
	int Tag = 0;
	list *L;
	fact *F;
	F = Fact;
	L = Pre;
	if (L == NULL)
		cout << "\nError";
	while (L != NULL)
	{
		F = Fact;
		for (;;)
		{
			if (abs(L->GetNumber()) == F->GetNumber())
				break;
			F = F->Next;//查找与规则前提链中前提号相同的事实
		}
		if (L->GetNumber() > 0)
		{
			if ((F->GetSucc()) == True) { L = L->Next; continue; }
			if ((F->GetSucc()) == False) return false;
		}//如果事实的断言为真则判断下一个前提，为假，则表示该规则不适合
		else
		{
			if ((F->GetSucc()) == True)
				return False;
			if ((F->GetSucc()) == False)
			{
				L = L->Next;
				continue;
			}
		}
		cout << F->GetContent() << "(Y/N)" << endl;
		c = getchar();//事实断言为不知道的时候，向用户询问
		getchar();
		if ((c == 'Y') || (c == 'y'))
		{
			if (L->GetNumber() > 0)
				F->PutAct(1, True);//设置事实的断言和激活标志
			if (L->GetNumber() < 0)
			{
				F->PutAct(1, True);
				Tag = -1;
				return False;
			}
		}
		else
		{
			if (L->GetNumber() < 0)
				F->PutAct(-1, False);
			else
			{
				F->PutAct(-1, False);
				Tag = -1; //已经推理，不符合。
				return False;
			}
		}
		L = L->Next;
	}
	F = Fact;
	for (;;)
	{
		if (Conc == F->GetNumber())
			break;//查找结论断言对应的事实
		F = F->Next;
	}
	if (Conc < 18)
	{
		F->PutAct(1, True);
		return False;
	}
	if (Tag != -1)
	{
		F = Fact;
		for (;;)
		{
			if (Conc == F->GetNumber())
				break;
			F = F->Next;
		}
		if (Conc < 18)
		{
			F->PutAct(1, True);
			return False;
		}
		cout << "\nThis fruit is " << F->GetContent() << endl;
		return True;
	}
	return False;
}

int main()
{
	fact *F, *T;
	rule *Rule, *R;
	char ch[8];
	int i = 1;
	Fact = NULL;
	while (str[i - 1]) //初始化事实库，倒序排列。
	{
		F = new fact(i, (char*)str[i-1]);
		F->Next = Fact;
		Fact = F;
		i++;
	}
	F = Fact;
	Fact = NULL;
	while (F) //把倒序排列正过来。
	{
		T = F;
		F = F->Next;
		T->Next = Fact;
		Fact = T;
	}
	i = 0;
	ch[0] = 'R';
	ch[1] = 'U';
	ch[2] = 'L';
	ch[3] = 'E';
	ch[4] = '_';
	ch[5] = 'a';
	ch[6] = '\0';
	Rule = NULL;
	for (i = 0; i < 5; i++) //初始化规则库。
	{
		R = new rule(ch, rulep[i], rulec[i]);
		R->Next = Rule;
		Rule = R;
		ch[5]++;
	}
	R = Rule;
	//进行判断
	for (;;)
	{
		i = R->Query();
		if ((i == 1) || (i == -1))
			break;
		R = R->Next;
		if (!R)
			break;
	}
	if (!R)
		cout << "I don't know." << endl;
	cout << "press any key to exit." << endl;
	getchar();
	return True;
}
