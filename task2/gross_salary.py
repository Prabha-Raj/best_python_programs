'''
5.  Write a python program to compute gross salary based on following parameters:-
Basic Salary	HRA	DA
1-4000	 	10%	50%
4001-8000	15%	60%
8001-12000	20%	70%
More than 12000	25%	80%

gs=bs+hra+da

'''

salary=int(input("Enter Basic Salary : "))
if salary<=0:
	print("Your Salary is Negative formate / Zero, That is not Possible. ")
elif salary>=1 and salary<=4000 :
	hra=(salary*10)/100
	da=(salary*50)/100
	gs=salary+hra+da
	print("Gross Salary =  ",gs)
elif salary>4000 and salary<=8000 :
	hra=(salary*15)/100
	da=(salary*60)/100
	gs=salary+hra+da
	print("Gross Salary =  ",gs)
elif salary>8000 and salary<=12000 :
	hra=(salary*20)/100
	da=(salary*70)/100
	gs=salary+hra+da
	print("Gross Salary =  ",gs)
else :
	hra=(salary*25)/100
	da=(salary*80)/100
	gs=salary+hra+da
	print("Gross Salary =  ",gs)