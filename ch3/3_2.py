# Author: Gerardo Hidalgo-Cuellar
# Date: 4/8/2022
# 
# Exercise 3.2 
# Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use input to read a string and float() to convert the string to a number. Do not worry about error checking the user input - assume the user types numbers properly. 
# 
# Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the program. The following shows two executions of the program: 
# 
# Enter Hours: 20
# Enter Rate: nine
# Error, please enter numeric input
# 
# Enter Hours: forty
# Error, please enter numeric input


# Get input from user
try:
    hours = float(input("Hours: "))
    rate = float(input("Rate/Hour: "))

except:
    print("Error, please enter numeric input")
    quit()

if (hours > 40):
    hours_over_40 = hours - 40 # calculate hours worked over 40
    # pay 
    pay_40hrs = 40 * rate
    pay_over_40hrs = hours_over_40 * (rate * 1.5)
    # sum pay
    pay = pay_40hrs + pay_over_40hrs
else:
    pay = hours * rate

print("Pay:", pay)

