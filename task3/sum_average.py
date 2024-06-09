#1.	Write a python program to create a list of ten numbers by taking input from user. Now find sum and average of numbers.

mylist=[]
sum=0
print("Enter 10 Number in List : ")
for i in range(10):
	e=int(input())
	mylist.append(e)
	sum=sum+e
print("Sum of list Elements =  ",sum)
print("Average of list elements = ",sum//len(mylist))