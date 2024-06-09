'''
write a python program to create a class named Shape. 
In Shape class create a method named setValue(), 
this method initialize side of shape. By inheriting 
Shape class create a new class Square. In Square 
class create a method area(), this method return 
area of square. Now by inheriting Shape class create 
a new class Cube. In Cube class create a method volume(), 
this method return volume of cube. Now Test Square and 
Cube classes.
'''
class Shape:
	def setValue(self,side):
		self.s=side
class Square(Shape):
	def area(self):
		return self.s*self.s
class Cube(Shape):
	def volume(self):
		return self.s*self.s*self.s
side1=eval(input("Enter Side of Square : "))
sq=Square()
sq.setValue(side1)
print("The Area of square is  ",sq.area())
side2=eval(input("Enter Side of Cube : "))
cu=Cube()
cu.setValue(side2)
print("The Volume of Cube is ",cu.volume())
