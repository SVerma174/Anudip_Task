# Q 1)
# Program to check if a year is a leap year
year = int(input("Enter a year: ")) # user can enter the year

    # If divisible by 4, but not divisible by 100, or divisible by 400
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.") # print if its leap year 
else:
    print(f"{year} is not a leap year.") # print if its not leap year

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Q2)
#Program to find the largest numberber among three
number1 = float(input("Enter the first numberber: "))
number2 = float(input("Enter the second numberber: "))
number3 = float(input("Enter the third numberber: "))

# Compareing  numbers to find the largest
if number1 >= number2 and number1 >= number3:
    print(f"The largest numberber is {number1}")# here if the num 1 is greater then it will show
elif number2 >= number1 and number2 >= number3:
    print(f"The largest numberber is {number2}")#num2 is greater then it will print 
else:
    print(f"The largest numberber is {number3}")#else num 3 is greater 

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Q 3)
# Program to check if a number is positive, negative, or zero
number = float(input("Enter a number: "))

if number > 0:
    print(f"{number} is a positive number.")
elif number < 0:
    print(f"{number} is a negative number.")
else:
    print(f"The number is zero.")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Q 4)
#Toy Vendor Discount Calculation
product_code = int(input("Enter the product code (1 for Battery Based Toys, 2 for Key-based Toys, 3 for Electrical Charging Based Toys): "))
order_amount = float(input("Enter the order amount: "))

# Initialize discount to 0
discount = 0

# Calculate discount based on product code and order amount
if product_code == 1:  # Battery Based Toys
    if order_amount > 1000:
        discount = 0.10 * order_amount
elif product_code == 2:  # Key-based Toys
    if order_amount > 100:
        discount = 0.05 * order_amount
elif product_code == 3:  # Electrical Charging Based Toys
    if order_amount > 500:
        discount = 0.10 * order_amount
else:
    print("Invalid product code.")
    exit()

# Calculate net amount
net_amount = order_amount - discount

# Output the net amount
print(f"Net amount to be paid: Rs. {net_amount:.2f}")


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Q 5)
# Program to calculate transport fare
distance = float(input("Enter the distance traveled (in km): "))

# Calculate fare based on the distance
if distance <= 50:
    fare = distance * 8  # 8 Rs./km
elif distance <= 100:
    fare = (50 * 8) + ((distance - 50) * 10) # 10 Rs./km
else:
    fare = (50 * 8) + (50 * 10) + ((distance - 100) * 12) # 12 Rs./km

# showing  the fare
print(f"Total fare: Rs. {fare:.2f}")
