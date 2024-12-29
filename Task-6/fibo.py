 # 4. Get the Fibonacci series between 0 to 50
print("Fibonacci series between 0 and 50:")
a, b = 0, 1                 # Initializing the first two numbers of the Fibonacci sequence
while a <= 50:              # Looping until the current number exceeds 50
    print(a, end=" ")            # Printing the current number in the sequence
    a, b = b, a + b             # Updating a and b to the next two numbers in the sequence
