#   Write a program in python to take a string as input. Now check given string is palindrome or not.


string=input("Enter a string : ")
reverse_string="".join(reversed(string))
print(reverse_string)
if string==reverse_string:
	print("String is palindrome")
else:
	print("String is non-palindrome")