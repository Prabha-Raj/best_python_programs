'''
Write a python program to create a function named rev(), in 
rev() function pass a string and this function return
reverse string.
'''

def rev(str):
	str1=''
	for i in str:
		str1=i+str1
	return (str1)
str=input("Enter string : ")
print("Reverse String is = ",rev(str))

















