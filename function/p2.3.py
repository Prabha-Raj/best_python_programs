'''
Write a python program to find roots of 
quadratic equation ax2+bx+c=0.
root1=(-b+math.sqrt(b*b-4*a*c))/(2*a)
root2=(-b-math.sqrt(b*b-4*a*c))/(2*a)

'''
import math
def rt(a,b,c):
	root1=(-b+ math.sqrt(b*b-4*a*c))//(2*a)
	root2=(-b- math.sqrt(b*b-4*a*c))//(2*a)
	return (root1,root2)
print("A python program to find roots of quadratic equation ax2+bx+c=0.")
a=int(input("Enter the value of a = "))
b=int(input("Enter the value of b = "))
c=int(input("Enter the value of c = "))
x=rt(a,b,c)
print("the value of x by using shree dharacharya vidhi ==>>")
print("x =",x[0])
print("x =",x[1])











