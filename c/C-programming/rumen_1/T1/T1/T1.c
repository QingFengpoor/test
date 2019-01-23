#include "stdio.h"
#include "stdlib.h"

int main() {
	int n = 0, i = 0, s = 0;
	scanf_s("%d", &n);
	for (; i <= n; i++)
		s += i;
	printf("%d", s);
	system("pause");
	return 0;
}