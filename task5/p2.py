'''
Write a python program to create a class with name 
‘Employee’. In Employee class take three instance 
variables empid, empname and salary. Create 
two methods in Employee class first setEmployee()
 and second display(). setEmployee() method 
initialize instance variables empid, empname, salary
and display() method display value of empid, 
empname and salary. Now test Employee class.
'''

class Employee:
	def setEmployee(self,eId,eName,eSal):
		self.eId=eId
		self.eName=eName
		self.eSal=eSal
	def getEmployee(self):
		print("Employee Id = ",self.eId)
		print("Employee Name =",self.eName)
		print("Employee Salary =",self.eSal)
eid=int(input("Enter Employee Id : "))
name=input("Enter Employee Name : ")
salary=eval(input("Enter Employee Salary : "))
obj=Employee()
obj.setEmployee(eid,name,salary)
obj.getEmployee()




















