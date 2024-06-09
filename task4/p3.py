'''
Write a python program to create a function search(), 
in search function pass two parameters first, 
a list of ten numbers and second, a number to search. 
If number is present in list return index of list
otherwise return false.
'''

def search(x,y):
	n1="This Element is Present in list"
	n2="This Element is Not Present in list"
	for i in x:
		if i==y:
			return n1
		else :
			return n2
li=[40,10,30,50,100,5,20,30,30,48]
num=int(input("Enter Number for Searching in list : "))
print(search(li,num))
print(num in li)