'''
Write a python program to create a function random(). 
This function return random number from 1-10.
'''
from random import randint

def computer(l,u):
	num=randint(l,u)	
	return num
low=int(input("Enter lower Limit : "))
up=int(input("Enter upper Limit : "))
print("Cumputer Genrated Number :",computer(low,up))
















