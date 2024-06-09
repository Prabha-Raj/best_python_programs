'''
3.	Write a python program to find roots of quadratic equation ax2+bx+c=0.
root1=(-b+math.sqrt(b*b-4*a*c))/(2*a)
root2=(-b-math.sqrt(b*b-4*a*c))/(2*a)
'''
import math
a=int(input("Enter value of a : "))
b=int(input("Enter value of b : "))
c=int(input("Enter value of c : "))
root=math.sqrt(b*b-4*a*c)
root1=(-b+root)/(2*a)
root2=(-b-root)/(2*a)
print("There are two Square root value -- ")
print("First one is  ",root1)
print("secont one is  ",root2)