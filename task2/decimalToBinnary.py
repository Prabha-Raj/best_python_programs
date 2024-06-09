#Decimal  to Binary Conversion.

dec_number=eval(input("Enter Decimal Number : "))
print("Decimal Number= ",dec_number)
#print(bin(dec_number)[2:])
bin_number=str()
while dec_number>0:
	bin_number=str(str(dec_number%2)+(bin_number))
	dec_number=dec_number//2
#print(bin_number)
print("Binary Number : ",int(bin_number))