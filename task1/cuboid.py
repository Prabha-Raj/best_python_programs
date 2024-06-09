'''
4.	Write a python program to find volume and surface area of cuboid.
v=l*b*h
sa=2*(l*b+b*h+h*l)

'''

length=int(input("Enter Length of Cuboid : "))
height=int(input("Enter Height of Cuboid : "))
breadth=int(input("Enter Breadth of Cuboid : "))

volume=length*breadth*height
surface_area=2*(length*breadth+breadth*height+height*length)
print("Volume of Circle =  ",volume)
print("Surface Area of The Circle = ",surface_area)