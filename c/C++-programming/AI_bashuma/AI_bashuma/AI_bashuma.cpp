// AI_bashuma.cpp : 此文件包含 "main" 函数。程序执行将在此处开始并结束。
//

#include "pch.h"
#include "stdio.h"
#include<cstdio>
#include<cstring>
#include<ctime>
char temp_sc[11], kaishizhuangtai[10];
int jieshuzhuangtai = 123804765;
const int M = 400000; 
int zhuangtaikongjian[M], zongshu = 0;
bool shiyongbiaozhi[11];
bool zhuangtaibiaozhi[M];
int zhuangtai[M][3];
//空格0的可能位置，及移动结果{上，左，下，右}，-1表示不允许移动
int yidong[9][4] = { {-1,-1,3,1},{-1,0,4,2},{-1,1,5,-1},
					{0,-1,6,4},{1,3,7,5},{2,4,8,-1},
					{3,-1,-1,7},{4,6,-1,8},{5,7,-1,-1}
};
void huhuan(char *s, int a, int b) {
	char t = s[a];
	s[a] = s[b];
	s[b] = t;
}

int zheban(int r, int n, int l) {
	int mid_point = l + (r - l) / 2;
	if (zhuangtaikongjian[mid_point] == n)return mid_point;
	else if (l<r&&zhuangtaikongjian[mid_point]>n)return zheban(l, mid_point - 1, n);
	else if (l < r&&zhuangtaikongjian[mid_point] < n) return zheban(mid_point + 1, r, n);
	return -1;
}

int sousuo(int n, int p) {
	int head = 0, tail = 1, temp;
	zhuangtai[head][0] = n, zhuangtai[head][1] = p, zhuangtai[head][2] = head; 
	while (head != tail) {
		int  position0 = zhuangtai[head][1];
		char dq[10];
		sprintf_s(dq, "%09d", zhuangtai[head][0]);
		for (int i = 0; i < 4; i++) {
			int jh = yidong[position0][i];
			if (jh != -1) {				
				huhuan(dq, position0, jh);
				sscanf_s(dq, "%d", &temp);
				if (temp == jieshuzhuangtai)
					return zhuangtai[head][2] + 1;
				int k = zheban(zongshu, temp,0);
				if (!zhuangtaibiaozhi[k]) {
					zhuangtai[tail][2] = zhuangtai[head][2] + 1;
					zhuangtai[tail][1] = jh;
					zhuangtai[tail][0] = temp;
					zhuangtaibiaozhi[k] = 1;
					tail++;
				}
				huhuan(dq, position0, jh);
			}
		}
		head++;
	}
}

void chansheng(int n, int k) {
	for (int i = 0; i < n; i++) {
		if (!shiyongbiaozhi[i]) {
			temp_sc[k] = i + '0';
			shiyongbiaozhi[i] = 1;
			if (k == n) {
				temp_sc[k + 1] = '\0';
				sscanf_s(temp_sc + 1, "%d", &zhuangtaikongjian[zongshu++]);
			}
			else
				chansheng(n, k + 1);
			shiyongbiaozhi[i] = 0;
		}
	}
}

int main() {
	int n, i = -1, steps = 0;
	scanf_s("%s", kaishizhuangtai, 10);
	while (kaishizhuangtai[++i] != '0');
	sscanf_s(kaishizhuangtai, "%d", &n);
	chansheng(9, 1);
	if (n != jieshuzhuangtai)
		steps = sousuo(n, i);
	printf("%d\n", steps);
	return 0;
}

