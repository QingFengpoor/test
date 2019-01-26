#include "stdio.h"
#include "string.h"
#include "stdlib.h"

int main() {
	FILE *fp;
	errno_t err;
	if (err = fopen_s(&fp, "number.in", "r") !=0){
		printf("can not open number.in\n");
		system("pause");
		return 0;
	}
	char nc[3],numc[102];
	fgets(nc, 3, fp);
	fgets(numc, 100, fp);
	int len = (int)strlen(numc);
	numc[len] = '#';
	numc[len+1] = '\0';
	if (fclose(fp) != 0) {
		printf("can not close number.in\n");
		system("pause");
		return 0;
	}

	int n = 0;
	int num[50];
	n = atoi(nc);
	char numbuff[10];
	int np = n;
	for (int i = 0; i < (int)strlen(numc); i++) {
		int j = 0;
		while (numc[i] != ' ') {
			if (numc[i] == '#')break;
			numbuff[j++] = numc[i];
			i++;
		}
		numbuff[j] = '\0';
		num[--np] = atoi(numbuff);
		for (int k = 0; k < (int)strlen(numbuff); k++)
			numbuff[k] = '\0';
	}
	if (np != 0) {
		printf("err:number of number is wrong\n");
		system("pause");
		return 0;
	}

	int min = num[0], max = num[0];
	for (int i = 0; i < n; i++) {
		if (num[i] > max)max = num[i];
		if (num[i] < min)min = num[i];
	}

	int maxGYS = 0;
	for (int i = 1; i <=min; i++) {
		int t = max % i;
		if (t == 0)maxGYS = i;
	}

	if (err = fopen_s(&fp, "number.out", "w") != 0) {
		printf("cannot open number.out\n");
		system("pause");
		return 0;
	}
	fprintf(fp, "%d %d %d", min, max, maxGYS);
	if (fclose(fp) != 0) {
		printf("cannot clse number.out\n");
		system("pause");
		return 0;
	}
	return 0;

}