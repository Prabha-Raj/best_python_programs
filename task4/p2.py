'''
Write a python program to create a function calc(), 
write code to find summation, subtraction, multiplication 
and division and return result in form of list.
Now test calc() function.
'''

def calc(x,y):
	return [x+y,x-y,x*y,x/y,x%y]
a=eval(input("Enter first Number : "))
b=eval(input("Enter second Number : "))
print("Summation = ",calc(a,b)[0])
print("Subtraction = ",calc(a,b)[1])
print("Multiplecation = ",calc(a,b)[2])
print("Division = ",calc(a,b)[3])
print("Remender = ",calc(a,b)[4])













