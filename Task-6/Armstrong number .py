num = int(input("Enter a number to check if it's an Armstrong number: "))
sum = 0            # Initializing sum to 0
temp = num          # Copying the input number to a temporary variable
while temp > 0:        # Looping while temp is greater than 0
   digit = temp % 10      # Extracting the last digit of the number
   sum += digit ** len(str(num))         # Adding the power of the digit to the sum based on number length
   temp //= 10             # Removing the last digit from temp
if num == sum:              # Checking if the sum is equal to the original number
   print(f"{num} is an Armstrong number.")         # If true, print it's an Armstrong number
else:
   print(f"{num} is not an Armstrong number.")     # If false, print it's not an Armstrong number
 