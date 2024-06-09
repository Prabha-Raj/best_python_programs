#print all prime number in given range.

limit=int(input("Enter Number : "))
print("<<<<<<=====  All Prime Numbers are as given range :=====>>>>>> ")  
for i in range(1,limit+1):
	count=0
	for j in range(1,i+1):
		#print(j)
		if i%j==0:
			count=count+1
		#print(count)
	if i==1:
		print(i,end=" ")
	if count==2:
		print(i,end=" ")
print()
print("End of Program !")
