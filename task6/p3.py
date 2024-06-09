'''
Write a python program to create a class Employee. In 
Employee class take two instance variables empid and empname. In Employee class create two methods setEmployee() and getEmployee(). setEmployee() method is used to initialize instance variables empid and empname whereas getEmployee() method is used to display values of empid and empname. 
By inheriting Employee class create a new class Payroll. 
In Payroll class create three instance variables bs, 
hra and da. In Payroll class create two methods setPayroll() 
and getPayroll(). setPayroll() method is used to 
initialize variables bs, hra and da whereas getPayroll()
 method is used to display values of bs, hra and da. 
Now by inheriting Payroll class create a new class Payslip. 
In Payslip class create a method named netSalary() which 
displays net salary with addition of basic 
salary, hra and da. Now test Payslip class. 
This is an example of multilevel inheritance.
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
class Payslip(Payroll):
	def netSalary(self):
		netsal=self.bs+self.hra+self.da
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
obj.netSalary()












