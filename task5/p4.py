'''
write a python program to create a class with name
‘Student’.In Student class take 
three instance variables rollno, name and fee. 
Now create a parameterized constructor to 
initialize variables and create a method display() 
which display values of instance variables. 
Test the class ‘Student’.
'''

class Student:
	def __init__(self,rollno,name,fee):
		self.rollno=rollno
		self.name=name
		self.fee=fee
	def display(self):
		print("Student Roll No : ",self.rollno)
		print("Student Name :   ",self.name)
		print("Student Fee :   " ,self.fee)
rol=input("Enter Roll No : ")
name=input("Enter Name : ")
fee=eval(input("Enter Fee Amount : "))
obj=Student(rol,name,fee)
obj.display()











