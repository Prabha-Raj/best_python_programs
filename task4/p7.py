'''
Write a python program to generate Fibonacci series 
up to n terms using ‘Recursion’.
'''
def fib(x):
	term1=0
	term2=1
	fiblist=[term1,term2]
	for i in range(2,x):
		nextTerm=term1+term2
		term1=term2
		term2=nextTerm
		fiblist.append(nextTerm)
	return (fiblist)
num=int(input("Enter Number = "))    	
for i in fib(num):
	print(i,end=" ")