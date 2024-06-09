'''
6.	Write a python program to calculate electricity bill based on following parameters:-

Units				Bill/unit
1-150				2.40
For next 151-300		3.00
For next more than 300		3.20

'''

units=int(input("Enter total Consumed Electrity in Units : "))
if units<=0:
	print("You are Trying Enter zero / Less than Zero electricity unit That is not possible. ")
elif units>=1 and units<=150:
	bill = (units*2.40)
elif units>150 and units<=300:
	bill=((150*2.40)+(units-150)*3.00)
else :
	bill=((150*2.40)+(150*3.00)+(units-300)*3.20)

print("Your total Amount of Electricity Bill = ",bill)
