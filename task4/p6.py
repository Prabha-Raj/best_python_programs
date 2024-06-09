'''
Write a python program to find factorial of 
given number using ‘Recursion’.
'''

def fact(n):
	if n==0 or n==1:
		return 1
	else:
		return n*fact(n-1)
num=int(input("Enter Number : "))
print("Factorial = ",fact(num))





