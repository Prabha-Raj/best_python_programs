'''
Write a python program to create a class with name ‘MyClass’. 
In MyClass create a function sayHello().In sayHello() 
function pass name of user, and display user 
name with Hello, message. Test class ‘MyClass’.
'''
class MyClass:
	def sayHello(self,name):
		print(name)

name=input("Enter Name : ")
MyClass().sayHello(name)
		





