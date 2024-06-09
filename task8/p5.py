#       Write a program in python to take a sentence as input. 
#         Now count occurrence of ‘The’ word in given sentence.


sentence=input("Enter a sentence : ")
print("Your sentence is : ",sentence)
s=sentence.split(" ")
print(s)
count="the"
n=0
for i in s:
	if count=="the" :
		n=n+1

if n==0:
	print("The Is Not Present ")
else:
	print("The is Present no of time =>>> ",n,count)
		