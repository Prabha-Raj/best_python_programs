'''
Write a python program to take number of days as input 
now display years, weeks and days. 
E.g. If user input 375 days then output will be
1 years, 1 weeks and 3 days.
In this program ignore leap year.
'''
def calendar(days):
	years=days//365
	days=days%365
	months=days//30
	days=days%30
	weeks=days//7
	days=days%7
	return years,months,weeks,days
days=int(input("Enter First Number : "))
cdict={
'Years':calendar(days)[0],
'Months':calendar(days)[1],
'Weeks':calendar(days)[2],
'Days':calendar(days)[3]
}
print(cdict)
print(cdict['Months'])















