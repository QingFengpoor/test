// K-means.cpp : 此文件包含 "main" 函数。程序执行将在此处开始并结束。
//

#include "pch.h"
#include <iostream>
#include <ctime>
#include <cstdlib>
#include <cmath>

struct xn
{
	int id;
	int h=0;
	int w = 0;
	xn *next;
};

int determinec(xn *h, double **idk, double **dk,int r,int c) {
	xn *pi = h,*pj=h;
	while (pi != NULL) {//记录每个点距离中心点的距离
		int i = pi->id;
		for (int j = 0; j < c; j++) {
			double t = -1;
			t = sqrt(pow(pi->h - idk[j][0], 2) + pow(pi->w - idk[j][1], 2));
			dk[i][j] = t;
		}
		pi = pi->next;
	}
	struct idl
	{
		int id;
		idl *next;
	};
	idl **kid = new idl *[c];//记录每一个中心点所包含的点
	for (int i = 0; i < c; i++) {
		kid[i] = new idl;
		kid[i]->next = NULL;
	}
	for (int i = 0; i < r; i++) {
		int a = i, b = 0;
		double tmin = dk[a][0];
		for (int j = 0; j < c; j++) {//找到每一个点距离最近的中心点
			if (tmin > dk[i][j]) {
				b = j;
				tmin = dk[i][j];
			}
		}
		//把该点添加到对应的类中
		idl *pidl = kid[b];
		while (pidl->next != NULL)pidl = pidl->next;
		idl *nw = new idl;
		nw->id = a;
		nw->next = NULL;
		pidl->next = nw;
	}
	for (int i = 0; i < c; i++)kid[i] = kid[i]->next;
	//更新中心点
	int f = 0;//是否停止更新 更新前后如果相差不超过3 停止
	for (int i = 0; i < c; i++) {
		double nh = 0, nw = 0;
		int count = 0;
		idl *pidl = kid[i];
		while (pidl != NULL) {
			count++;
			pi = h;
			while (pi->id != pidl->id)pi = pi->next;
			nh = nh + pi->h;
			nw = nw + pi->w;
			pidl = pidl->next;
		}
		nh = nh / count;
		nw = nw / count;
		if (abs(nh - idk[i][0]) < 3 && abs(nw - idk[i][1]) < 3)f = f + 1;
		idk[i][0] = nh;
		idk[i][1] = nw;
	}
	if (f == c)
		f = 1;
	else 
		f = 0;
	//结束更新 输出最后答案
	if (f == 1) {
		for (int i = 0; i < c; i++) {
			std::cout << "第" << i+1 << "类：";
			idl *pidl = kid[i];
			while (pidl != NULL) {
				pi = h;
				while (pi->id != pidl->id) pi = pi->next;
				std::cout << "(" << pi->h << "," << pi->w << ")  ";
				pidl = pidl->next;
			}
			std::cout << "\n";
		}
	}
	return f;
}

int main()
{
	std::cout << "人数:";
	int n;
	std::cin >> n;
    std::cout << "Input x :\n";
	xn *X = new xn;
	xn *p = X;
	for (int i = 0; i < n; i++) {
		xn *nw = new xn;
		nw->next = NULL;
		std::cout << "第" << i+1 << "位：\nh(cm)=";
		std::cin >> nw->h;
		std::cout << "w(斤)=";
		std::cin >> nw->w;
		nw->id = i;
		p->next = nw;
		p = p->next;
	}
	X = X->next;
	int k;
	std::cout << "\n\n输入k:";
	std::cin >> k;
	if (k > n) {
		std::cout << "分类不能完成，类的数目大于人的数目\n";
		exit(1);
	}
	double **dk = new double*[n];//一张二维表 行数等于所有点数，列数等于中心点数，值为非中心点到中心点的距离
	for (int i = 0; i < n ; i++)
		dk[i] = new double[k];

	srand((unsigned)time(NULL));
	double **idk = new double*[k];//用来存放初始的随机中心点 第一列是h 第二列是w
	for (int i = 0; i < k; i++)
		idk[i] = new double[3];
	for (int i = 0; i < k; i++) {
		p = X;
		int t = rand() % n;
		for (int j = 0; j < i; j++)//排除重复的随机值
			if (idk[j][2] == t) 
			{ 
				i--; 
				continue; 
			}
		idk[i][2] = t;
		while (p->id != t)p = p->next;
		idk[i][0] = p->h;
		idk[i][1] = p->w;
	}

	int f = 0;
	while (!f)
		f = determinec(X, idk, dk, n, k);
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
