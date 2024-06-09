'''
Write a program in python to calculate gross salary.
In this program take basic salary as input then calculate HRA and DA.
HRA should be 10% of basic salary and DA should be 50% of basic salary. 
Then find gross salary as sum of basic salary, HRA and DA.
'''

bs=int(input("Enter Basic Salary : "))
hra=bs*10/100
da=bs*50/100
gs=bs+hra+da
print("Gross Salary = ",gs)

















