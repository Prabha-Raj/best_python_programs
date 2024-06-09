'''
Write a python program to find area and perimeter of circle.
area=3.14*r*r
perimeter=2*3.14*r
'''

def calc(x,ch):
	if ch==1:
		return float(3.12*x*x)
	elif ch==2:
		return float(2*3.14*x)
	else:
		return 'invalid choice'

choice=int(input("Enter choice (Press 1 for area and 2 for perimeter of circle ) : "))
r=int(input("Enter Radius of Circle : "))
print(calc(r,choice))








