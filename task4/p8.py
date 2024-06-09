'''
Write a python program to create a module named mycalc. 
In mycalc module create four functions add(), sub(), 
mult() and div() to find summation, subtraction, 
multiplication and division respectively. 
Now import mycalc module and test these functions.
'''

def mycalc(ch,a,b):
	if ch=='+':
		return(a+b)
	elif ch=='-':
		return(a-b)
	elif ch=='*':
		return(a*b)
	elif ch=='/':
		return(a/b)
	elif ch=='%':
		return(a%b)
	else :
		return 'Invalid Choise'
status=True
while status:
	num1=int(input("Enter first number : "))
	num2=int(input("Enter second number : "))
	ch=input("Choose Operator in given set (+, -, *, /, % ) : ")
	print(mycalc(ch,num1,num2))















