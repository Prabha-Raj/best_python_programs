'''
7.	Write a python program to take number of days
 as input now display years, weeks and days. 
E.g. If user input 375 days then output
 will be 1 years, 1 weeks and 3 days.
 In this program ignore leap year.
'''
import math
days=int(input("Enter Total No of Days : "))
years=days/365
days=days%365
months=days/30
days=days%30
weeks=days/7
days=days%7
print("Years = ",int(years) ," Months = ",int(months),"Weeks = ",int(weeks), " Days = ",days)