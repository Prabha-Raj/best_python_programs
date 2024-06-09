#4.	Write a python program to take coordinates of a point as input and determine its quadrant.

print("Enter Coordinates of a point : ")
x=int(input("Enter Value of x-exes : "))
y=int(input("Enter Value of y-exes : "))
if x>0 and y>0 :
	print("First Quardrant ")
elif x<0 and y>0 :
	print("Second Quardrant")
elif x<0 and y== y<0 :
	print("Third Quardrant")
else :
	print("Forth Quardrant")