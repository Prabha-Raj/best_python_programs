# 8.	Write a python program to find factorial of given number.
num=int(input("Enter a number : "))
fact=1
for i in range(1,num+1):
	fact=fact*i	
print(fact)
