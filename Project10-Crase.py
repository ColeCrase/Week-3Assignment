"""
Program: Project10
Author: Cole Crase
This program is to take the hourly wages, total regualr hours, and total
overtime hours and displays the employee's total weekly pay.
"""

hourly_wages = float(input("Enter your hourly wages: "))
total_regular_hours = int(input("Enter your total regular hours: "))
total_overtime_hours = int(input("Enter your total overtime hours: "))

overtime_result = total_overtime_hours * 1.5 * hourly_wages
result = hourly_wages * total_regular_hours + overtime_result

print("Your total weekly pay is", "$", result)
