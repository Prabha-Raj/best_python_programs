'''
Write a python program to find simple interest.
si=(p*n*r)/100
'''

def siCalc(p,t,r):
	return (p*t*r)/100
p=int(input("Enter Principle Amount : "))
t=int(input("Enter Time Period : "))
r=int(input("Enter Rate of Intrest : "))
print("Simple Intrest : ",siCalc(p,t,r))










