'''
Write a python program to create a tuple of five numbers.
 Now apply len(), max(), min() and sum() functions on tuple.
'''
mytuple=()
print("Enter 5 Elements in Tuple : ")
for i in range(5):
	num=int(input("Enter no : "))
	mytuple+=num,
	
print("Tuple =>> ",mytuple)
print(type(mytuple))
print("Length of Tuple =>> ",len(mytuple))
print("Max value of Tuple =>> ",max(mytuple))
print("Min Value of tuple =>> ",min(mytuple))
print(mytuple[0])
print(mytuple[4])
print(mytuple[1:4])
print("Adding 10,20 at bigning and 2,3 at the end position : ")
print((10,20)+mytuple+(2,3))
print("Multiply by 2 and print : ")
print(mytuple*2)
print("to check 50 in tuple : ")
print(50 in mytuple)
print("print the index of 3 :")
print(mytuple.index(3))
print("How many time present in tuple")
print(mytuple.count(65))
print("The sum of Orignal tuple : ")
print(sum(mytuple))
print("type of sum of tuple : ")
print(type(sum(mytuple)))
print("Sorted tuple : ")
print(sorted(mytuple))
print("Type of Sorted tuple : ")
print(type(sorted(mytuple)))