// HAC.cpp : 此文件包含 "main" 函数。程序执行将在此处开始并结束。
//
//还未完成 还有全连接 和最短连接 未完成
#include "pch.h"
#include <iostream>
#include <stdlib.h>
#include <cmath>

struct StudentClass
{
	int v = 0;//类是否有效 0无效，1有效
	int id = 0;//类的代号
	int h = 0;//身高
	int w = 0;//体重
	StudentClass* next;
	StudentClass* subnext;
};

//计算距离
void CD(double **d, StudentClass *h,int c) {
	StudentClass *pi = h, *pj = h;
	for (int i = 0; i < c; i++) {
		for (int j = 0; j < c; j++) {
			while (pj->id != j)
				pj = pj->next;
			double t = sqrt(pow((pi->h - pj->h), 2) + pow((pi->w - pj->w), 2));
			d[i][j] = t;
			pj = h;
		}
		pi = pi->next;
	}
}

//查询最小距离 ab为返回值 Single-linkage
void SRD(StudentClass* h,double **d,int len,int *ab) {
	StudentClass *pi = h, *pj = h;
	int a = 0, b = 1;
	double min = d[0][1];
	while (pi != NULL) {
		int i = pi->id;
		for(int j=0;j<len;j++){
			int f = 0;//判断是不是同一类的 0不是，1是
			while (pj->id != i && pj != NULL)
				pj = pj->next;
			if (pj->subnext != NULL) {
				pj = pj->subnext;
				while (pj != NULL) {
					if (pj->id == j) {
						f = 1;
						break;
					}
					pj = pj->next;
				}
			}
			if (min > d[i][j]&&f==0&&d[i][j]!=0) {
				min = d[i][j];
				a = i, b = j;
			}
			pj = h;
		}
		pi = pi->next;
	}
	ab[0] = a; //确定a
	pi = h;
	pj = h;
	int t = -1;
	while (pi != NULL) {
		if (pi->id == b) {
			t = pi->id;
			break;
		}
		pj = pi->subnext;
		while (pj != NULL) {
			if (pj->id == b) {
				t = pi->id;
				break;
			}
			pj = pj->next;
		}
		pi = pi->next;
	}
	ab[1] = t;//确定b
}

//查询最大距离 ab为返回值 Complete-linkage
void CRD(StudentClass* h, double **d, int len, int *ab) {
	StudentClass *pi = h, *pj = h;
	int a = 0, b = 1;
	double max = d[0][1];
	while (pi != NULL) {
		int i = pi->id;
		for (int j = 0; j < len; j++) {
			int f = 0;//判断是不是同一类的 0不是，1是
			while (pj->id != i && pj != NULL)
				pj = pj->next;
			if (pj->subnext != NULL) {
				pj = pj->subnext;
				while (pj != NULL) {
					if (pj->id == j) {
						f = 1;
						break;
					}
					pj = pj->next;
				}
			}
			if (max < d[i][j] && f == 0 && d[i][j] != 0) {
				max = d[i][j];
				a = i, b = j;
			}
			pj = h;
		}
		pi = pi->next;
	}
	ab[0] = a; //确定a
	pi = h;
	pj = h;
	int t = -1;
	while (pi != NULL) {
		if (pi->id == b) {
			t = pi->id;
			break;
		}
		pj = pi->subnext;
		while (pj != NULL) {
			if (pj->id == b) {
				t = pi->id;
				break;
			}
			pj = pj->next;
		}
		pi = pi->next;
	}
	ab[1] = t;//确定b
}

//合并两个类 把b合并到a
void merge(int *ab, StudentClass *h) {
	StudentClass *pa = h, *pb = h, *pp = h;
	while (pa->id != ab[0] && pa != NULL)
		pa = pa->next;
	while (pb->id != ab[1] && pb != NULL)
		pb = pb->next;
	if (pa == NULL || pb == NULL) { std::cout << "出错，未找到A B\n"; return; }
	while (pp->next->id != ab[1] && pp != NULL)
		pp = pp->next;
	pp->next = pb->next;
	if (pa->subnext != NULL) {
		pa = pa->subnext;
		while (pa != NULL)
			pa = pa->next;
		pa = pb;
		pa->next = pa->subnext;
		pa = pa->subnext;
	}
	else {
		pa->subnext = pb;
		pa = pa->subnext;
		pa->next = pa->subnext;
	}
}

void HACout(StudentClass *h) {
	StudentClass *pi = h, *pj = h;
	int i=1;
	while (pi != NULL) {
		std::cout << "第" << i << "类：\n";
		std::cout << '(' << pi->h<< ',' << pi->w << ")   ";
		pj = pi->subnext;
		while (pj != NULL) {
			std::cout << '(' << pj->h << ',' << pj->w << ")   ";
			pj = pj->next;
		}
		std::cout << '\n';
		i++;
		pi = pi->next;
	}
}

//Sigal-linkage alograthm
void Sigal_linkage(StudentClass *head,int n,double **d) {
	int ab[2] = { -1,-1 };//存放返回值
	int count=n;//类的数目
	StudentClass *heads = head;
	std::cout << "\nSingle-linkage:\n";
	while (count > 2) {
		SRD(heads, d, n, ab);
		if (ab[0] == -1 || ab[1] == -1) {
			std::cout << "查询最小值出错，终止\n";
			break;
			exit(1);
		}
		merge(ab, heads);
		count--;
	}
	HACout(heads);
}

int main()
{
    std::cout << "Input：a training saple\n"; 
	std::cout << "人数:n=";
	int n;//数据数量
	std::cin >> n;
	//Inuput and Initialize
	StudentClass* head=new StudentClass;
	head->next = NULL;
	head->subnext = NULL;
	StudentClass* p = head;
	for (int i = 0; i < n; i++) {
		StudentClass* t = new StudentClass;
		t->next = NULL;
		t->subnext = NULL;
		t->v = 1; t->id = i;
		std::cout << "输入第" << i+1 << "位:\n";
		std::cout << "身高（cm）h=";
		std::cin >> t->h;
		std::cout << "体重（斤) w=";
		std::cin >> t->w;
		p->next = t;
		p = p->next;
	}
	head = head->next;

	int count;//类的数目
	double **d;//存放距离的表 初始值为-1；
	d= new double *[n];
	for (int i = 0; i < n; i++) {
		d[i] = new double[n];
	}
	for (int i = 0; i < n; i++) 
		for (int j = 0; j < n; j++) 
			d[i][j] = -1;
	CD(d, head, n);
	int ab[2] = { -1,-1 };//存放返回值

	std::cout << "\nSingle-linkage:\n";
	count = n;
	StudentClass *heads = head;
	while (count > 2) {
		SRD(heads, d, n, ab);
		if (ab[0] == -1 || ab[1] == -1) {
			std::cout << "查询最小值出错，终止\n";
			break;
			exit(1);
		}
		merge(ab, heads);
		count--;
	}
	HACout(heads);
	//Sigal_linkage( head,  n,  d);

	/*std::cout << "\nComplete-linkage:\n";
	count = n;
	ab[0] = -1;
	ab[1] = -1;
	StudentClass *headc = head;
	while (count > 2) {
		CRD(headc, d, n, ab);
		if (ab[0] == -1 || ab[1] == -1) {
			std::cout << "查询最大值出错，终止\n";
			break;
			exit(1);
		}
		merge(ab, headc);
		count--;
	}
	HACout(headc);*/

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
