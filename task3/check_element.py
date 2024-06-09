'''
Write a python program to create a list of ten numbers by taking input from user. 
Now check a number is presented in list or not.
'''

mylist=[]
print("Enter 5 Elements in list :  ")
for i in range(5): #taking input from user
	e=int(input())
	mylist.append(e)
count=0
check=int(input("What's element are chakinng :  "))
for i in mylist: #traversing list
	if i==check:
		count=count+1
if count==0:
	print("The Element is Not Present in this list !")
else:
	print("The Element is Present in this list !")