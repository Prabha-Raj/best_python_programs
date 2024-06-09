#Operator Precedence.
a=20
b=10
c=15
d=5
e=(a*b)*c/d
print("value of (a*b)*c/d is ",e)
e=(a*b)*c/d
print("value of ((a*b)*c)/d is ",e)
e=(a*b)*(c/d)
print("value of (a*b)*(c/d) is ",e)
e=a+(b*c)/d
print("value of a+(b*c)/d is ",e)