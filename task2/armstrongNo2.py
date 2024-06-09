#all armstrong number of given range.

i=int(input("Enter last rang for printing Armstrong Number (1 to 10000000 ) :  "))
print("<<<<<<<<<<<<==============All armstrong Numbers are acording to your range ===============>>>>>>>>>>>>>>>>>")
#for when range in 1 digits from 1 to 9 than print armstrong number
if i>0 and i<10:
	num=1
	while i>=num:
		temp=0
		num2=num
		while num2>0:
			rem=num2%10
			temp=temp+rem
			num2=num2//10
		if temp==num:
			print(num)
		num=num+1

#for when range in 2 digits from 10 to 99 than print armstrong number
elif i>=10 and i<100:
	num=1
	while i>=num:
		temp=0
		temp1=0
		num2=num
		while num2>0:
			rem=num2%10
			temp=temp+rem
			temp1=temp1+rem*rem
			num2=num2//10
		if temp==num or temp1==num:
			print(num)
		num=num+1
#for when range in 3 digits from 100 to 999 than print armstrong number
elif i>=100 and i<1000:
	num=1
	while i>=num:
		temp=0
		temp1=0
		temp2=0
		temp3=0
		num2=num
		while num2>0:
			rem=num2%10
			temp=temp+rem
			temp1=temp1+rem*rem
			temp2=temp2+rem*rem*rem
			temp3=temp3+rem*rem*rem*rem
			num2=num2//10
		if temp==num or temp1==num or temp2==num or temp3==num:
			print(num)
		num=num+1
#for when range in 4 digits from 1000 to 9999 than print armstrong number
elif i>=1000 and i<10000:
	num=1
	while i>=num:
		temp=0
		temp1=0
		temp2=0
		temp3=0
		num2=num
		while num2>0:
			rem=num2%10
			temp=temp+rem
			temp1=temp1+rem*rem
			temp2=temp2+rem*rem*rem
			temp3=temp3+rem*rem*rem*rem
			num2=num2//10
		if temp==num or temp1==num or temp2==num or temp3==num:
			print(num)
		num=num+1

#for when range in 5 digits from 10000 to 99999 than print armstrong number
elif i>=10000 and i<100000:
	num=1
	while i>=num:
		temp=0
		temp1=0
		temp2=0
		temp3=0
		temp4=0
		num2=num
		while num2>0:
			rem=num2%10
			temp=temp+rem
			temp1=temp1+rem*rem
			temp2=temp2+rem*rem*rem
			temp3=temp3+rem*rem*rem*rem
			temp4=temp4+rem*rem*rem*rem*rem
			num2=num2//10
		if temp==num or temp1==num or temp2==num or temp3==num or temp4==num:
			print(num)
		num=num+1
#for when range in 6 digits from 100000 to 999999 than print armstrong number
elif i>=100000 and i<1000000:
	num=1
	while i>=num:
		temp=0
		temp1=0
		temp2=0
		temp3=0
		temp4=0
		temp5=0
		num2=num
		while num2>0:
			rem=num2%10
			temp=temp+rem
			temp1=temp1+rem*rem
			temp2=temp2+rem*rem*rem
			temp3=temp3+rem*rem*rem*rem
			temp4=temp4+rem*rem*rem*rem*rem
			temp5=temp5+rem*rem*rem*rem*rem*rem
			num2=num2//10
		if temp==num or temp1==num or temp2==num or temp3==num or temp4==num or temp5==num:
			print(num)
		num=num+1
#for when range in 7 digits from 1000000 to 9999999 than print armstrong number
elif i>=1000000 and i<10000000:
	num=1
	while i>=num:
		temp=0
		temp1=0
		temp2=0
		temp3=0
		temp4=0
		temp5=0
		temp6=0
		num2=num
		while num2>0:
			rem=num2%10
			temp=temp+rem
			temp1=temp1+rem*rem
			temp2=temp2+rem*rem*rem
			temp3=temp3+rem*rem*rem*rem
			temp4=temp4+rem*rem*rem*rem*rem
			temp5=temp5+rem*rem*rem*rem*rem*rem
			temp6=temp6+rem*rem*rem*rem*rem*rem*rem
			num2=num2//10
		if temp==num or temp1==num or temp2==num or temp3==num or temp4==num or temp5==num or temp6==num:
			print(num)
		num=num+1
#for when range in 8 digits from 10000000 to 99999999 than print armstrong number
elif i>=10000000 and i<100000000:
	num=1
	while i>=num:
		temp=0
		temp1=0
		temp2=0
		temp3=0
		temp4=0
		temp5=0
		temp6=0
		temp7=0
		num2=num
		while num2>0:
			rem=num2%10
			temp=temp+rem
			temp1=temp1+rem*rem
			temp2=temp2+rem*rem*rem
			temp3=temp3+rem*rem*rem*rem
			temp4=temp4+rem*rem*rem*rem*rem
			temp5=temp5+rem*rem*rem*rem*rem*rem
			temp6=temp6+rem*rem*rem*rem*rem*rem*rem
			temp7=temp7+rem*rem*rem*rem*rem*rem*rem
			num2=num2//10
		if temp==num or temp1==num or temp2==num or temp3==num or temp4==num or temp5==num or temp6==num or temp7==num:
			print(num)
		num=num+1
else :
	print("Invalid Range !")











