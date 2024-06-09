#10.	Write a python program to convert a list into tuple.

mylist=[]
print("Enter 5 Element in list : ")
for i in range(5):
	e=input()
	mylist.append(e)

print(mylist)
mytuple=tuple(mylist)
print(mytuple)
mytuple.append(100)
print(mytuple)



