#   Write a program in python to search a substring in given string.

string=input("Enter a string : ")
fw=input("Find what? ")
if fw in string:	
	print("this substring is present in given string.")
else:
	print("this substring is not present in given string")