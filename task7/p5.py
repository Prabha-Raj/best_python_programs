# Write a program in python to take a decimal number as input and convert it into binary, octal and hexa-decimal equivalent.




n=int(input("Enter Number: "))
print("Binary is: ",bin(n).replace("0b",""))
print("Octal is: ",oct(n).replace("0o",""))
print("Hexa is: ",hex(n).replace("0x",""))