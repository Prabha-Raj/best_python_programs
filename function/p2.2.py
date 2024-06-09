'''
Write a python program to check given number is even or odd.

Without using And Operator.
'''

def greatest1(a,b):
	if a>b:
		return "A is Greatest Number that is =>> ",a
	else:
		return "B is Greatest Number that is =>>",b

def greatest2(a,b,c):
	if a>b:
		num=a
	else:
		num=b
	if c>a:
		num1=c
	else:
		num1=a
	if num>num1:
		if num==a:
			return "A is Greatest Number that is =>> ",num
		else:
			return "B is Greatest Number that is =>> ",num
	else:
		if  num1==c:
			return "C is Greatest Number that is =>> ",num1
		else:
			return "A is Greatest Number that is =>> ",num1
print("Enter 1 for check Greatest Number with in two Numbers : ")
print("Enter 2 for check Greatest Number with in three Numbers : ")
choice=int(input("Enter choice : "))
if choice==1:
	a=int(input("Enter First Number : "))
	b=int(input("Enter Second Number : "))
	print(greatest1(a,b)[0],greatest1(a,b)[1])
elif choice==2:
	a=int(input("Enter First Number : "))
	b=int(input("Enter Second Number : "))
	c=int(input("Enter third Number : "))
	print(greatest2(a,b,c)[0],greatest2(a,b,c)[1])
	#greatest(a,b,c)
else:
	print("Invalid Choice !")










