age=int(input("enter your age"))
if age >=18:
    print ("You are eligible to vote.")


age = int(input("Enter your age: "))

if age >= 18:
    if age == 18:
        print("Congratulations on your first vote!")
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote yet.")


Take a look at the following code snippet.
It is NOT printing as expected, what could be going wrong?

if age >=18:
print ("You are eligible to vote.")