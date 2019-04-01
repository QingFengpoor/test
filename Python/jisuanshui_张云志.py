a=float(input("输入工资:"));
shuishou =0;
if a >85000 :
	shuishou =shuishou+(a-85000)*0.45;
	a=85000;
if a >60000 :
	shuishou =shuishou+(a-60000)*0.35;
	a=60000;
if a >40000 :
	shuishou =shuishou+(a-40000)*0.3;
	a=40000;
if a >30000 :
	shuishou =shuishou+(a-30000)*0.25;
	a=30000;
if a >17000 :
	shuishou =shuishou+(a-17000)*0.2;
	a=17000;
if a >8000 :
	shuishou =shuishou+(a-8000)*0.1;
	a=8000;
if a >5000 :
	shuishou =shuishou+(a-5000)*0.03;
	a=5000;
print("税收:",shuishou);
