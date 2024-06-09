'''
Write a python program to find volume and surface area of cuboid.
v=l*b*h
sa=2*(l*b+b*h+h*l)
'''

def calc(l,b,h,ch):
	if ch==1:
		return l*b*h
	elif ch==2:
		return 2*(l*b+b*h+h*l)
	else:
		return 'Invalid Choice'
print("Press 1 for volume of Cuboid : ")
print("Press 2 for volume of Cuboid : ")
choice=int(input("Enter Choice : "))
l=eval(input("Enter Length of cuboid : "))
b=eval(input("Enter Breadth of cuboid : "))
h=eval(input("Enter Height of cuboid : "))
print(calc(l,b,h,choice))








