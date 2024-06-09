'''
Write a python program to create a dictionary and 
traverse elements of dictionary using for loop.
'''

mydict={'1':'Prabhakar Rajput', '2':'Shailendra Kumar', '3':'Sourabh Rajput', '4':'Kaushal Kumar'}
print(mydict)
print("Traversing By using for loop ===>>>>")
for i in mydict:
	i=str(i)
	print(mydict[i])