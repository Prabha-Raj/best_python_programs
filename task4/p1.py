''''
 Write a python program to create two functions 
area() and peri() to find area and perimeter of rectangle.
'''
def area(a,b):
	return (a*b)
def peri(a,b):
	return (2*(a+b))
l=eval(input("Enter Length of rectangle : "))
b=eval(input("Enter breadth of rectangle : "))
print("The area of rectangle = ",area(l,b))
print("The perimeter of rectangle = ",peri(l,b))




















