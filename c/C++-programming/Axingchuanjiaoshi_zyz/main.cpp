#include<vector>
#include<algorithm>
#include<stdio.h>
#include<stdlib.h>
using namespace std;

#define MAX 5

typedef struct Node {
    int M, N, B;
    int g, h, f;
    int  parent;//记录父节点在tree中的下标
}Node;
vector<Node> open;
vector<Node> close;
vector<Node> tree;

Node boat[8] = {
    { 0,1,1,0,0,0,-1 },
    { 0,2,1,0,0,0,-1 },
    { 0,3,1,0,0,0,-1 },
    { 1,0,1,0,0,0,-1 },
    { 1,1,1,0,0,0,-1 },
    { 2,0,1,0,0,0,-1 },
    { 2,1,1,0,0,0,-1 },
    { 3,0,1,0,0,0,-1 }
};
void show_open() {//显示open表
    vector<Node>::iterator ite;
    ite = open.end()-1;
    for (; ite >=open.begin(); ite--) {
        printf("%d,%d,%d \t\t g=%d h=%d f=%d\n", (*ite).M, (*ite).N, (*ite).B, (*ite).g, (*ite).h, (*ite).f);
        if (ite == open.begin()) break;
    }
}
void show_close() {//显示close表
    vector<Node>::iterator ite;
    ite = close.begin();
    for (; ite < close.end(); ite++) {
        printf("%d,%d,%d \t\t g=%d h%d f%d)\n", (*ite).M, (*ite).N, (*ite).B, (*ite).g, (*ite).h, (*ite).f);
    }
}
bool operator ==(Node a, Node b) {
    return(a.M == b.M&&a.N == b.N&&a.B == b.B);
}
bool comp(Node a, Node b) {
    return a.f > b.f;//降序排列
}

void kuozhan(Node p) {//对节点p进行扩展
    Node n;
    printf(" %d,%d,%d 进行扩展\n", p.M, p.N, p.B);
    printf(".............................................\n");
    for (int i = 0; i < 8; i++) {
        if (p.B == 1) {//p船在左岸
            n.M = p.M - boat[i].M;
            n.N = p.N - boat[i].N;
            n.B = p.B - boat[i].B;
        }
        else {//p船在右岸
            n.M = p.M + boat[i].M;
            n.N = p.N + boat[i].N;
            n.B = p.B + boat[i].B;
        }
        bool ju;
        if (n.M > MAX || n.N > MAX || n.M < 0 || n.N < 0)//不在范围内。不合法
            ju=false;
        else if (n.M != 0 && n.M < n.N)//左岸传教士人数不为0 并且小于野人数
            ju=false;
        else if (MAX - n.M != 0 && MAX - n.M < MAX - n.N)//右岸传教士人数不为0 并且小于野人数
            ju=false;
        else ju=true;
        bool jo;
        if(find(open.begin(), open.end(), n)==open.end())
            jo=false;
        else
            jo=true;
        bool jc;
        if (find(close.begin(), close.end(), n) == close.end())
            jc=false;
        else
            jc=true;
        if (ju && !jo && !jc) {//避免死循环  已经扩展过的结点不再扩展
            n.g = p.g + 1;
            n.h = n.M + n.N - 2 * n.B;
            n.f = n.g + n.h;
            int pos = find(tree.begin(), tree.end(), p)-tree.begin();
            n.parent = pos;
            open.push_back(n);
            sort(open.begin(), open.end(), comp);
            tree.push_back(n);
        }
    }
    close.push_back(p);
    printf("\t open表 \n");
    show_open();
    printf("\t close表 \n");
    show_close();
    printf(".............................................\n");
}

void path(Node p) {
    vector<Node> temp;
    while (p.parent!=-1) {
        temp.push_back(p);
        p = tree[p.parent];
    }
    temp.push_back(p);
    vector<Node>::iterator ite1 = temp.end() - 1;
    for (; ite1 >= temp.begin(); ite1--) {
        printf("%d,%d,%d \t g=%d h=%d f%d\n", (*ite1).M, (*ite1).N, (*ite1).B, (*ite1).g, (*ite1).h, (*ite1).f);
        if (ite1 == temp.begin()) break;
    }
}
int main() {
    Node t,x;
    Node start;
    start.M=5;start.N=5;start.B=1;
    start.g=0;start.h=10;start.f=10;
    start.parent=-1;
    open.push_back(start);
    tree.push_back(start);
    while (open.size() != 0) {
        x = *(open.end() - 1);//从open表中取出一个进行扩展
        if (x.M == 0 && x.N == 0 && x.B == 0) {
                t=x;
                break;
        }
        open.pop_back();//从open中删除
        kuozhan(x);//扩展该结点
    }

    printf("解为：\n");
    path(t);
}
