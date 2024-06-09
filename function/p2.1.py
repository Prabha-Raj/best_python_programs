'''
Write a python program to check given number is even or odd.
'''
def check(n):
	if n%2==0:
		return "Even Number"
	else:
		return "Odd Number"
num=int(input("Enter a numbr for checking Even or Odd : "))
print(check(num)) 