#include<stdio.h>
#include<algorithm>
#include<vector>
#include<iostream>
using namespace std;

struct JCB {
	char name[10];
	int comet;
	int needt;
	int sourceid;
	int status;//0 表示等待,1表示运行，2表示结束
	int sf;
	int waitt;//已经等待的时间
	//JCB* next;

	bool operator> (const JCB& a) const
	{
		if(sf==1)
			if (comet != a.comet)
				return comet > a.comet;
			else
			{
				cout << "同时到达,出错.*****************************" << endl;
				return false;
			}
		else if(sf==2)
			if (needt != a.needt) {
				return needt > a.needt;
			}
			else
			{
				if (comet != a.comet)
					return comet > a.comet;
				else
				{
					cout << "所需时间一样长，且同时到达，出错.*****************" << endl;
					return false;
				}
			}
		else if (sf == 3) 
		{
			int hrn = (waitt + needt) / needt;
			int hrna = (a.waitt + a.needt) / a.needt;
			if (hrn != hrna) 
			{
				return hrn > hrna;
			}
			else
			{
				if (needt != a.needt)
					return needt > a.needt;
				else 
				{
					cout << "最高相应比相同，而且作业一样长，出错.*************" << endl;
					return false;
				}
			}
		}
		else {
			cout << "此时的判断类型有误";
		}
	}
};

bool Comp(JCB& a, JCB& b) {
	return a > b;
}

void show(JCB& a) {
	cout << "\t" << a.waitt + a.comet << "\t" << a.waitt + a.comet + a.needt << "\t" << a.waitt + a.needt << endl;
}

void showJCB(JCB& a) {
	cout << a.name << "\t" << a.comet << "\t" << a.needt << "\t" << a.sourceid << "\t" << a.status << "\t" << a.sf << "\t" << a.waitt << endl;
}

int main()
{
	vector<JCB> vecw,vecf;
	int n = 0;
	int sf ;
	cout << "选择哪种方法 (1表示 FCFS ， 2表示SJF， 3 表示HRN):" << endl;
	cin >> sf;
	JCB jcb;
	cout << "输入作业个数:" << endl;
	cin >> n;
	cout << "作业个数为" << n << endl;
	for (int i = 0; i < n; i++) 
	{
		cout << "输入第" << i+1 << "个作业的" << "作业名(长度不超过9)" << endl;
		cin >> jcb.name;
		cout << "输入第" << i+1 << "个作业的" << "到达时间(整数)" << endl;
		cin >> jcb.comet;
		cout << "输入第" << i+1 << "个作业的" << "需要的时间(整数)" << endl;
		cin >> jcb.needt;
		cout << "输入第" << i+1 << "个作业的" << "需要的资源(整数)" << endl;
		cin >> jcb.sourceid;
		jcb.status = 0;
		jcb.sf = 1;
		jcb.waitt = 0;
		vecw.push_back(jcb);
	}
	//vector<JCB>::iterator jhead = vec.begin();
	sort(vecw.begin(), vecw.end(), Comp);//先按照fcfs排队 降序排列
	int ct = vecw[vecw.size()-1].comet;//ct 表示当前时刻 也就是第一个作业到达的时间
	for (int i = 0; i < n; i++)
	{
		vecw[i].waitt = vecw[i].comet - ct;
		vecw[i].sf = sf;
	}
	JCB temp = vecw[vecw.size() - 1];//无论怎样都是第一个到的先运行 所以第一个到的一定是队尾
	vecw.pop_back();
	sort(vecw.begin(), vecw.end(), Comp);//重新按照选择方法排队 降序排列
	vecw.push_back(temp);
	for (int i = 0; i < vecw.size(); i++)
		showJCB(vecw[i]);
	int sumzhouzhuan = 0, sumdaiquan = 0;
	while (vecw.size()!=0)
	{
		if (vecw[vecw.size() - 1].comet >= ct)//当等待列表的下一个未到达时
		{
			for (int i = 0; i < vecw.size(); i++) {
				vecw[i].sf = 1;
			}
			sort(vecw.begin(), vecw.end(), Comp);//再次用FCFS排序
			JCB temp = vecw[vecw.size() - 1];//无论怎样都是第一个到的先运行 所以第一个到的一定是队尾
			vecw.pop_back();
			sort(vecw.begin(), vecw.end(), Comp);//重新按照选择方法排队 降序排列
			vecw.push_back(temp);
			for (int i = 0; i < vecw.size(); i++) {
				vecw[i].sf = sf;
			}
		}
		JCB run = vecw[vecw.size() - 1];//把当前队列的最后一个运行
		if(ct<run.comet)
			ct = run.comet;
		vecw.pop_back();//删除等待队列中的该元素
		run.waitt = ct - run.comet;//当前作业的等待时间为当前时间减去到来的时间
		run.status = 3;//当前作业标记未完成
		vecf.push_back(run);//已完成的加入到完成队列
		cout << "作业" << run.name << endl;
		sumdaiquan = sumdaiquan + (run.waitt + run.needt) / run.needt;
		sumzhouzhuan = sumzhouzhuan + (run.waitt + run.needt);
		cout << "开始时间" << ct << "\t完成时刻" << ct + run.needt << "\t周转时间" << run.waitt + run.needt << "\t带权周转时间" << (run.waitt + run.needt) / run.needt << endl;
		ct = ct + run.needt;//当前作业结束的时刻为当前时刻
	}
	cout << endl << "平均周转时间" << sumzhouzhuan / n << "\t 平均带权周转时间" << sumdaiquan / n << endl;
}

