# Write a program in python to find division of two numbers. Also handle ValueError and ZeroDivisionError in same program.

try:
	n=int(input("Enter first no: "))
	m=int(input("Enter second no: "))
	o=n/m
	print("Division= ",o)
except ValueError:
	print("Enter only Inteser Value.")
except ZeroDivisionError:
	print("Don't try to divide 0")