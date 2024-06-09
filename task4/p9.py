'''
Write a python program to create a module named tempconv. 
In tempconv module create two function ctof() and ftoc(). 
ctof() function converts temperature from centigrade to 
Fahrenheit  and ftoc() function converts temperature 
from Fahrenheit to centigrade. Now import tempconv 
module and test ctof() and ftoc() functions.
'''

def tempConv(ch,temp):
	if ch=='f':
		result=((temp*9)/5)+32
	elif ch=='c':
		result=(((temp-32)/9)*5)
	else :
		result='Invalid Choise'
	return result
ch=input("Press 'f' for c to f and 'c' for f to c : ")
if ch=='f':
	temp=eval(input("Enter tempreatur in C : "))
	print("Temprature in Fahrenheit =",tempConv(ch,temp))
	
elif ch=='c':
	temp=eval(input("Enter tempreatur in F : "))
	print("Temprature in Celsius =",tempConv(ch,temp))
else:
	print("Invalid Input")
