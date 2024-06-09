#  Write a program in python to take full name as input. Now display short name of user.

name=input("Enter your full name : ")
shortname=name.split(" ")
print("Your short name :",end="")
for n in range(len(shortname)-1):
	print(shortname[n][0]+".",end="")
print(shortname[len(shortname)-1])