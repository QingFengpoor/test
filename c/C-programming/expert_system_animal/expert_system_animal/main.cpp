#include <string.h>
#include <math.h>
#include <stdlib.h>
#include <stdio.h>
#include <iostream>
using namespace std;
#define True 1
#define False 0
#define DontKnow -1
char *str[] = { "chew_cud反刍动物","hooves蹄类动物","mammal哺乳动物","forward_eyes眼盯前方",
"claws有爪","pointed_teeth有犬齿","eat_meat吃肉","lay_eggs会下蛋","fly会飞",
"feathers有羽毛","ungulate有蹄","carnivore食肉动物","bird鸟","give_milk能产奶",
"has_hair有毛发","fly_well善飞","black&white_color黑白色","can_swim会游泳",
"long_legs长腿","long_neck长脖子","black_stripes黑条纹","dark_spots黑斑点",
"tawny_color黄褐色","albatross信天翁","penguin企鹅","ostrich驼鸟","zebra斑马",
"giraffe长颈鹿","tiger老虎","cheetah猎豹",0 };
int rulep[][6] = { {22,23,12,3,0,0},{21,23,12,3,0,0},{22,19,20,11,0,0},
{21,11,0,0,0,0},{17,19,20,13,-9,0},{17,18,13,-9,0,0},{16,13,0,0,0,0},
{15,0,0,0,0,0},{14,0,0,0,0,0},{10,0,0,0,0,0},{8,7,0,0,0,0},
{7,0,0,0,0,0},{4,5,6,0,0,0},{2,3,0,0,0,0},{1,3,0,0,0,0} };
int rulec[] = { 30,29,28,27,26,25,24,3,3,13,13,12,12,11,11,0 };
class fact
{
private:
	int Number;
	char Name[21];
	int Active;
	int Succ;
public:
	fact *Next;
	fact(int Num, char *L)
	{
		strcpy(Name, L);
		Number = Num;
		Active = False;
		//-1 是已经推理，不符合。1 是已经推理，符合。
		Succ = DontKnow; //0 是无，-1 是不知道，1 是有。
		Next = NULL;
	}
	char *GetName()
	{
		char *L;
		L = new char[21];
		strcpy(L, Name);
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
class rule
{
	char *Name;
	list *Pre;
	int Conc;
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
	strcpy(Name, N);
	i = 0;
	while (P[i] != 0)
	{
		L = new list(P[i++]);
		L->Next = Pre;
		Pre = L;
	}
	Conc = C;
}
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
			if ((F->GetSucc()) == true) { L = L->Next; continue; }
			if ((F->GetSucc()) == false) return false;
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
		cout << F->GetName() << "(Y/N)" << endl;
		c = getchar();//事实断言为不知道的时候，向用户询问
		cin.ignore(20);
		//flushall();
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
	if (Conc < 24)
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
		if (Conc < 24)
		{
			F->PutAct(1, True);
			return False;
		}
		cout << "\nThis aniamal is " << F->GetName() << endl;
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
		F = new fact(i, str[i - 1]);
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
	for (i = 0; i < 15; i++) //初始化规则库。
	{
		R = new rule(ch, rulep[i], rulec[i]);
		R->Next = Rule;
		Rule = R;
		ch[5]++;
	}
	R = Rule;
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