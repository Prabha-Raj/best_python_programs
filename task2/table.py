'''
7.	Write a python program to print table of given number in given format:-
2*1=2
2*2=4
2*3=6
.
.
2*10=20

'''

num=int(input("Enter Any Number For Table : "))
for i in range(1, 30, 5) :
	#i=i+1
	print(num," X ",i," = ",num*i)