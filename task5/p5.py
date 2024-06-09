'''
Write a python program to create a class with name ‘Bank’. 
In Bank class take three instance variables acno, name 
and balance. Create a parameterized constructor to 
initialize instance variables. Now create 
following methods in Bank class:-
i.	deposit() – This method is used to deposit() 
	money in account.
ii.	withdraw() – This method is used to withdraw 
	money from account after checking balance.
iii.	enquiry():- This method provide balance enquiry.

'''
class Bank:
	def __init__(self,acNO,name,bal):
		self.acNo=acNo
		self.name=name
		self.balance=bal
	def deposit(self,d_amount):
		self.balance=self.balance+d_amount
		print("Your deposit balance is ",d_amount)
		print("Your Total balance after deposit is ",self.balance)
	def withdraw(self,w_amount):
		self.balance=self.balance-w_amount
		print("Your Withdrowl balance is ",w_amount)
		print("Your Total balance after withdrawl is ",self.balance)
acNo=int(input("Enter Acount No : "))
name=input("Enter Name of Acount Holder : ")
bal=eval(input("Enter Initial(Opening amount) Balance : "))
obj=Bank(acNo,name,bal)
d_bal=eval(input("Enter Deposit balance : "))
obj.deposit(d_bal)
w_bal=eval(input("Enter Withdrawl balance : "))
obj.withdraw(w_bal)










