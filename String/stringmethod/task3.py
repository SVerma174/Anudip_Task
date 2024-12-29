#  Write a Python program to count Uppercase, Lowercase, special character and numeric values in a given string
import random

magic_number = random.randint(0, 20)

print("Welcome to the Magic Number Guessing Game!")
print("I have chosen a number between 0 and 20. Can you guess what it is?")

while True:
  
    try:
        guess = int(input("Enter your guess: "))
        
      
        if guess == magic_number:
            print("Congratulations! You guessed the magic number.")
            break
        elif guess < magic_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
    except ValueError:
        print("Invalid input! Please enter a whole number.")
