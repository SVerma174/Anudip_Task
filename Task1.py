# Q1) Cal the multi and sum of two numbers

# Taking Input from User
number11 =int(input("Enter the first Number:"))
number22 = int(input("Enter the second number:"))

Multification = number11 * number22  # numuber11 ko mul ker diya hai Number22 sa
print(Multification )
addition = number11 + number22
print (addition)

#Q2) cal the which number is greater using ternary Operator

a = int(input("enter the first number: "))
b = int(input("Enter the second number :"))

largest = a if a> b else b  # a and b mai sa jo bada hoga wo print hoga
print(largest)


# Q3)con Tempture to Degree 
# input tempture from celcius from user
celsius = float(input("Enter the Temperature in Celsius :"))

#converting celcius to fahrenheit
fahrenheit = (celsius * 9/5) + 32

print(" Temperature Conversion (Celsius to Fahrenheit)")
print("{celsius}°C is equivalent to {fahrenheit}°F")

#Q4) Find the area of a triangle whose sides are given

# Input sides of the triangle from user
side1 = float(input("Enter the first side of the triangle: "))
side2 = float(input("Enter the second side of the triangle: "))
side3 = float(input("Enter the third side of the triangle: "))

# Calculate semi-perimeter adding two three side and divided by 2
s = (side1 + side2 + side3) / 2

# Ucalculating Traing area using side 
area = (s * (s - side1) * (s - side2) * (s - side3))**0.5

# printing  result
print(" Area of a Triangle",area)




