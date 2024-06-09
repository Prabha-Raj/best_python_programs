'''
WAP to find greatest Number with in three numbers 
without using and operator 
you can use only decision control statements.
'''



a=int(input("Enter first no : "))
b=int(input("Enter second no : "))
c=int(input("Enter third no : "))
if a>b:
	num=a
else:
	num=b
if b>c:
	num1=b
else:
	num1=c
if num>num1:
	if num==a:
		print("A is Greatest !",a)
	else :
		print("B is Greatest !",b)
else:
	if num1==b:
		print("B is Greatest !",b)
	else:
		print("C is greatest !",c)	
