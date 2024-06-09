#10.	Write a python program to reverse the digits of given number. using for loop
'''
num=int(input("Enter any number are you enter :  "))
num_str=str(num)
num_length=len(num_str)
print("Length of given Number : ",num_length)
for i in range(0,num_length):
	rem=num%10
	print(rem,end="")
	num=num//10
'''

#10.	Write a python program to reverse the digits of given number.uding while loop

num=int(input("Enter any number are you enter :  "))
while num>0:
	rem=num%10
	print(rem,end="")
	num=num//10


 