# Write a python program to demonstrate super keyword.

class A:
	def m(self):
		print("I am Method of Class A")
class B(A):
	def m(self):
		super().m()
		print("I am Method of Class B")
B().m()













