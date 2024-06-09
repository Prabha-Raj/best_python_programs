'''
Write a Python program to calculate electricity bill on following basis:-
Unit	Bill/unit
	   1-150	2.40/unit
For next 151-300	3.00/unit
For next more than 300	3.20/unit

'''

unit=eval(input("Enter Total Units : "))
if unit>=1 and unit<=150:
	bill=unit*2.40
elif unit>=151 and unit<=300:
	bill=(150*2.40)+(unit-150)*3.00
elif unit>300:
	bill=(150*2.40)+(150*3.00)+(unit-300)*3.20
else:
	print("Invalid Input ")
print("Your PayBill Amount is ",bill)


















