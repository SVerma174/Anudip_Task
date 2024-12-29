name=input("Enter the string that you went to check is Palindrome or not ") # create a input the name of variable is = name and here it will take input from user

def isPalindrome(name):                     #create a def fuction called as  which take parameter as = name 
    return name == name[::-1]                               # then returning that parameter and chek the input string is equal to reverese
 
if isPalindrome(name):                              #using if statment here given a condition on parameter is the contiation is right then it will print yes as output 
    print("Yes")
else:                                           # if condition is false it goes to else block code and print No
    print("No")