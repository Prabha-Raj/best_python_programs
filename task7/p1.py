"""
Write a program in python to create a class with name Figure. In Figure class create a single method named area(), by using area() method find area of square and rectangle as an example of method overloading.
"""


class figure():
	def setValue(self,a,b):
		self.a=a
		self.b=b
class square(figure):
	def area(self):
		print("Area of square is: ",self.a*self.a)
class rectangle(square,figure):
	def area(self):
		print("Area of Rectangle is: ",self.a*self.b)
n1=int(input("ENter Length of Figure: "))
n2=int(input("Enter Breadth of Figure: "))
s=square()
s.setValue(n1,n2)
s.area()
r=rectangle()
r.setValue(n1,n2)
r.area()