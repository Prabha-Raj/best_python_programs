#Write a program in python to open a file for read operation. Also handle FileNotFoundError.


f=None
try:
	filename=input("Enter filename to be open : ")
	f=open(filename,"r")
	contents=f.read()
	print(contents)
except FileNotFoundError:
	print("File doesn't exists")
finally:
	f.close()