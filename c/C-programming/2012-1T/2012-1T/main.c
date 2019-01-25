#include "stdio.h"
#include "stdlib.h"
#include "string.h"
int main() {
	FILE *fp;
	errno_t err;
	if (err = fopen_s(&fp,"string.in", "r") !=0)
	{
		printf("can not open .in\n");
		system("pause");
		return 0;
	}
	char num1c[20], num2c[20];
	int is1float = 0, is2float = 0;
	fgets(num1c, 20, fp);
	fgets(num2c, 20, fp);
	for (int f = 0; f < (int)strlen(num1c); f++)
		if (num1c[f] == '.')is1float = 1;
	for (int f = 0; f < (int)strlen(num2c); f++)
		if (num2c[f] == '.')is2float = 1;
	if (fclose(fp) != 0)
	{
		printf("can not close .in\n");
		system("pause");
		return 0;
	}


	double num = 0;
	double num1 = 0, num2 = 0;
	num1 = atof(num1c);
	num2 = atof(num2c);
	num = num1 + num2;
	char numbuf[21];
	if (err = fopen_s(&fp,"string.out", "w") != 0)
	{
		printf("can not open .out\n");
		system("pause");
		return 0;
	}
	if (is1float == 1 || is2float == 1)
	{
		sprintf_s(numbuf, 21, "%e", num);
		char dishu[20], zhishu[20];
		int flag = 0, di = 0, zh = 0;
		for (int f = 0; f < (int)strlen(numbuf); f++) {
			if (numbuf[f] == 'e') {
				flag = 1;
				continue;
			}
			if (flag == 0)dishu[di++] = numbuf[f];
			else zhishu[zh++] = numbuf[f];
		}
		dishu[di] = '\0';
		zhishu[zh] = '\0';
		for (int f = (int)strlen(dishu) - 1; f >=0; f--) {
			if (dishu[f] == '0' && dishu[f - 1] == '0')
			{
				dishu[f] = '\0';
				continue;
			}
			if(dishu[f]=='0'&&dishu[f-1]!='0')
			{
				dishu[f] = '\0';
				break;
			}
		}
		int isfuhao = 0;
		int c0 = 0;
		for (int f=0; f < (int)strlen(zhishu)-1; f++) {
			if (f == 0 && (zhishu[0] == '-' || zhishu[0] == '+'))
			{
				isfuhao = 1;
				continue;
			}
			if (zhishu[f] == '0' && zhishu[f + 1] == '0') {
				c0++; 
				continue;
			}
			if (zhishu[f] == '0' && zhishu[f + 1] != '0') {
				c0++;
				break;
			}
			if (zhishu[0] != '0')break;
		}
		if (isfuhao == 0)
		{
			for (int k = 0; k <c0; k++)
				for (int l = 0; l < (int)strlen(zhishu) - 1; l++) {
					zhishu[l] = zhishu[l + 1];
				}
			int point = (int)strlen(zhishu) - c0 - 1;
			zhishu[point] = '\0';
		}
		else
		{
			for(int k=0;k<c0;k++)
				for (int l = 1; l < (int)strlen(zhishu) - 1; l++) {
					zhishu[l] = zhishu[l + 1];
				}
			int point = (int)strlen(zhishu) - c0;
			zhishu[point] = '\0';
		}
		fprintf(fp,"%s", dishu);
		fprintf(fp,"%c", 'e');
		fprintf(fp,"%s", zhishu);
	}
	else
	{
		sprintf_s(numbuf, 20, "%e", num);
		for (int j = (int)strlen(numbuf) - 1; j > 0; j--) {
			if (numbuf[j] == 0 && numbuf[j - 1] == 0)numbuf[j] = '\0';
		}
		fprintf(fp, "%s", numbuf);
	}
	if (fclose(fp) != 0)
	{
		printf("can not close .out\n");
		system("pause");
		return 0;
	}
	return 0;
}