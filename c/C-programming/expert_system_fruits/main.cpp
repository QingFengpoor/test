#include <string.h>
#include <iostream>
using namespace std;
#define True 1
#define False 0
#define DontKnow -1
int main()
{
	const char * str[] = { "圆球体","小球体","类似圆球","大球体","心状" ,
		"橙色","紫色、绿色","近似土灰色","绿色黑纹","红色有斑点",
		"酸、甜","甜","果皮不能食用","许多个在一起","果皮有毛毛",
		"大，皮不能吃","小","桔子","葡萄","猕猴桃","西瓜","草莓"};
	int rulep[][6] = { {1,6,11,13,0,0},{2,7,11,14,0,0},{3,8,11,15,0,0},{4,9,12,16,0,0},{5,10,11,17,0,0} };
	int rulc[] = { 18,19,20,21,22 };
	class fact //事实类
	{
	private:
		int Number;//事实的编号
		char Content[21];//事实的内容
		int Active;
		int Succ;
	public:
		fact *Next;
		fact(int Num, char *L)
		{
			strcpy(Content, L);
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
			strcpy(L, Content);
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
}
