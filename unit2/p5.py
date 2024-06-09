'''
write a python program to calculate gross salary on following basis.
Basic Salary	HRA	DA
   1-4000	10%	50%
4001-8000	20%	60%
8001-12000	25%	75%
More than 12000	30%	80%

'''

bs=int(input("Enter Your basic Salary : "))
if bs>=1 and bs<4000:
	hra=bs*10/100
	da=bs*50/100
elif bs>=4000 and bs<8000:
	hra=bs*20/100
	da=bs*60/100
elif bs>=8000 and bs<12000:
	hra=bs*25/100
	da=bs*75/100
elif bs>=12000:
	hra=bs*30/100
	da=bs*80/100
else:
	print("Invalid Salary ")
print("Basic Salary : ",bs)
print("House Rant Alowance (hra) : ",hra)
print("Dearness Alowance (da) : ",da)
gs=bs+hra+da
print("Gross Salary : ",gs)











