'''
5.	Write a python program to find simple interest.
si=(p*n*r)/100

'''

p=float(input("Enter Principle Amount : "))
r=int(input("Enter Rate of Intrest / year : "))
t=int(input("Enter Time duration in year : "))

si=(p*r*t)/100

print("Simple Intrest = ",si)