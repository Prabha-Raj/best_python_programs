""" 
Write a program in python to create a class with name Bank. In Bank class create a method interest() which return 0 value. Now override interest method in class Sbi and Pnb.
"""


class bank:
	def setValue(self,bs,t):
		self.bs=bs
		self.t=t
		
class sbi(bank):
	def interest(self):
		self.int=(self.bs*10*self.t)/100
		print("Sbi Intrest is: ",self.int)
class pnb(sbi,bank):
	def interest(self):
		super().interest()
		self.int=(self.bs*9*self.t)/100
		print("Pnb Intrest is: ",self.int)


print("Sbi intrest rate is 10%")
print("Pnb intrest rate is 9%")
n1=int(input("Enter amount: "))
n2=int(input("Enter Time: "))
p=pnb()
p.setValue(n1,n2)
p.interest()