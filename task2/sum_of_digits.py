#9.	Write a python program to find sum of digits of given number.
 
num=int(input("Enter any Number Are you want add : "))
sum_of_digits=0
for i in range(0,num):
	rem=num%10
	sum_of_digits=sum_of_digits+rem
	num = num//10

print("Sum of Digits that You entered : ",sum_of_digits)
 