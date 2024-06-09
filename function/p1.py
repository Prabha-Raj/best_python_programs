def calc(x,y):
	return x+y,x-y,x*y,x/y,x%y
a=int(input("Enter First no: "))
b=int(input("Enter Second no: "))
print("Summation = ",calc(a,b)[0])
print("Subtract = ",calc(a,b)[1])
print("Multiplecation = ",calc(a,b)[2])
print("Division = ",calc(a,b)[3])
print("Remender = ",calc(a,b)[4])