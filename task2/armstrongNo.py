#Armstrong Number.

num=int(input("Enter a number : "))
temp=num
arm=0
while temp>0:
	rem=temp%10
	arm=rem*rem*rem+arm
	temp=temp//10 
#print(arm)
if num==arm:
	print("Your Number is Armstrong Number ")
else:
	print("Your Number is Non Armstrong Number") 