#WAP to find Prime or Non prime.

num=int(input("Enter a Number For checking Prime or Non Prime : "))
flag=1
num1=num
for i in range(1,num1):
	if num%i==0:
		flag=flag+1
if flag==2:
	print("Prime Number and your Number is = ",num)
else:
	print("Non Prime No and your Number is = ",num)
	