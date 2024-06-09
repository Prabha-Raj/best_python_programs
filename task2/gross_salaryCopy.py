"""
5. Write a python program to compute gross salary based on following parameters:-
Basic Salary	HRA	DA
01 - 4000	10%	50%
4001-8000	15%	60%
8001-12000	20%	70%
More than 12000	25%	80%

gs=bs+hra+da

"""
bs=eval(input("Enter Your Basic Salary : "))
if bs<1:
	Print("Invalid Salary !")
elif bs>=1 and bs<=4000:
	hra=(bs*10)/100
	da=(bs*50)/100
elif bs>4000 and bs<=8000:
	hra=((4000*10)/100)+(((bs-4000)*15)/100)
	da=((4000*50)/100)+(((bs-4000)*60)/100)
elif bs>8000 and bs<=12000:
	hra=((4000*10)/100)+((4000*15)/100)+(((bs-8000)*20)/100)
	da=((4000*50)/100)+((4000*60)/100)+(((bs-8000)*70)/100)
else:
	hra=((4000*10)/100)+((4000*15)/100)+((4000*20)/100)+(((bs-12000)*25)/100)
	da=((4000*50)/100)+((4000*60)/100)+((4000*70)/100)+(((bs-12000)*80)/100)
gross_salary = bs + hra + da
print("Your Totale / Gross Salary = ",gross_salary)