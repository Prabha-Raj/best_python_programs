'''
In program (3) create a class Loan 
before the code of Payslip class. In Loan class create a 
method setLoan() which is used to initialize amt variable. 
Now inherit Loan class in Payslip class and in netSalary() 
method also print salary on hand as (bs+hra+da-amt). 
This is an example of hybrid inheritance.
'''

class Employee:
	def setValue(self,id,name):
		self.empid=id
		self.empname=name
class Payroll(Employee):
	def setPayroll(self,bs,hra,da):
		self.bs=bs
		self.hra=hra
		self.da=da
	def getPayroll(self):
		print("Employee Id : ",self.empid)
		print("Employee Name : ",self.empname)
		print("Basic Salary : ",self.bs)
		print("Hra : ",self.hra)
		print("Da : ",self.da)
class Loan:
	def setLoan(self,loan_amount):
		self.amt=loan_amount
class Payslip(Payroll,Loan):
	def netSalary(self):
		netsal=self.bs+self.hra+self.da-self.amt
		print("Employee Id : ",self.empid)
		print("Employee Name : ",self.empname)
		print("Net Salary is : ",netsal)
			
id=int(input("Enter Employee Id : "))
name=input("Enter Employee Name : ")
bs=eval(input("Enter Basic Salary : "))
hra=eval(input("Enter House Rant allowances (hra) : "))
da=eval(input("Dearness Allowances : "))
obj=Payslip()			
obj.setValue(id,name)
obj.setPayroll(bs,hra,da)
obj.getPayroll()
loan_amount=eval(input("Enter Loan Amount : "))
obj.setLoan(loan_amount)
obj.netSalary()












