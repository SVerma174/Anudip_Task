 # 5. Check the validity of password input by users
import re                           # Importing regular expressions module for password validation
password = input("Enter a password: ")                       # Taking password input from the user
if (len(password) >= 8 and                          # Checking if password length is at least 8
    re.search("[A-Z]", password) and                        # Checking for at least one uppercase letter
    re.search("[a-z]", password) and                     # Checking for at least one lowercase letter
    re.search("[0-9]", password) and                 # Checking for at least one digit
    re.search("[!@#$%^&*(),.?\":{}|<>]", password)):                      # Checking for at least one special character
    print("Password is valid.")                             # If all conditions are met, print password is valid
else:
    print("Password is invalid. It must contain at least 8 characters, including an uppercase letter, a lowercase letter, a number, and a special character.")  # If conditions fail, print password is invalid

'''if __name__ == "__main__":
    main() '''                             # Calling the main function to execute the program