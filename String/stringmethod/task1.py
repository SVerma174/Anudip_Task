 # Write a Python program to Count all letters, digits, and special nsymbols from the given string
apl=(input("enter the input :"))
def apl_char(apl):
    count_char=0
    count_digit=0
    count_symb=0

    for char in apl:
        if char.isalpha():
            count_char+=1
        elif char.isdigit():
            count_digit+=1
        else:
            count_symb+=1

    print("char = ",count_char,"Digits =",count_digit,"symobls =",count_symb)

#apl="P@#yn26at^&i5ve"

print("Total count of char , digit,symbols")

apl_char(apl)