salary=float(input("input salary(RMB):"));
revernu =0;
if salary >85000 :
	revernu =revernu+(salary-85000)*0.45;
	salary=85000;
if salary >60000 :
	revernu =revernu+(salary-60000)*0.35;
	salary=60000;
if salary >40000 :
	revernu =revernu+(salary-40000)*0.3;
	salary=40000;
if salary >30000 :
	revernu =revernu+(salary-30000)*0.25;
	salary=30000;
if salary >17000 :
	revernu =revernu+(salary-17000)*0.2;
	salary=17000;
if salary >8000 :
	revernu =revernu+(salary-8000)*0.1;
	salary=8000;
if salary >5000 :
	revernu =revernu+(salary-5000)*0.03;
	salary=5000;
print("revernu:",revernu);
