#ConverT Binary to Decimal Number : 

num=int(input("Enter binary  Number : "))
power=0

len=len(str(num))
for i in range(len):
	num1=num%10
	bnum=num1+2**power
	power+=1
	num//=10
print(bnum)