'''
WAP to find greatest Number with in three numbers 
without using and operator 
you can use only decision control statements.
'''



a=int(input("Enter first no : "))
b=int(input("Enter second no : "))
c=int(input("Enter third no : "))
if a>b:
	if a>c:
		print("A is Greatest !",a)
	else :
		print("C is Greatest !",c)
else:
	if b>c:
		print("B is Greatest !",b)
	else:
		print("C is greatest !",c)	
