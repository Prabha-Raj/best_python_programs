'''
Write a python program to create a list of five students by taking input from user. 
Now display name of students in ascending and descending order.
'''

mylist=[]

print("Enter 5 Element for list : ")
for i in range(5):
	e=input()
	mylist.append(e)
print("Normal List :=> ",mylist)
mylist.sort()
print("List in Ascending Order :=> ",mylist)
mylist.reverse()
print("List in Descending Order :=> ",mylist) 


