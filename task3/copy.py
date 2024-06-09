'''
Write a python program to create a list of ten numbers by taking input from user named AR.
 Now copy even numbers in list EAR and odd numbers in list OAR.
 Now display elements of EAR and OAR.
'''

AR=[]

#taking input from user
print("Enter 10 Numbers for list")
for i in range(10):
	e=int(input())
	AR.append(e)
print("AR ===>>>>> ",AR)
EAR=[]
OAR=[]
#traversing list
for i in AR:
	if i%2==0:
		EAR.append(i)
	else:
		OAR.append(i)

print("EAR ===>>>>> ", EAR)
print("OAR ===>>>>> ",OAR)


