'''
Write  a python program to create a function named substr(), 
in substr() function pass a string and substring. 
If substring is presented in string then 
return true or return false.
'''

def substr(st,subst):
	return (subst in st)
st=input("Enter string : ")
subst=input("Enter sub string :")
print("substring Present in string : ",substr(st,subst))