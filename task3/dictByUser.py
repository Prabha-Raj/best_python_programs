#create dictinary by usinng user input.
'''
mydict={}
print("Enter 5 element of dictinary with key and its value : ")
for i in range(5):
	i=i+1
	key=input("Enter no key of dict : ")
	value=input("Enter value of % key of dict : ") 
	mydict[key]=value
print(mydict)
key=input("Enter Key for finding = value in dict : ")
print(mydict[key]) 

'''

mydict2={'parrot': 'tota', 'ram': 'bhagvan', 'dog': 'animal(kutta)', 'cow': 'National animal', 'tiranga': 'National flag'}
key2=input("Enter key for searching in list : ")
print(mydict2[key2])
