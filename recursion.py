
# Python Recursive Function
# We know that in Python, a function can call other functions. It is even possible for the 
# function to call itself. These type of construct are termed as recursive functions.
# Factorial of a number is the product of all the integers from 1 to that number. For example, 
# the factorial of 6 (denoted as 6!) is 1*2*3*4*5*6 = 720.
# Following is an example of recursive function to find the factorial of an integer.
# Write a program to factorial using recursion
def fact(x):
 if x==0:
    result = 1
 else :
    result = x * fact(x-1)
 return result
print("zero factorial",fact(0))
print("five factorial",fact(5))

# zip() is an recursive function
colors=('red','green','blue')
fruits=['orange','banana','cherry']
zip(colors,fruits)
li = list(zip(colors,fruits))
print(li)

