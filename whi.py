def finding_oddnumber(n):
    odd_number = []
    i = 1
    count = 0
    while count < n:
        odd_number.append(i)
        i += 2
        count += 1
    print("The first", n, "odd numbers are:", odd_number)
    return odd_number


result = finding_oddnumber(100)
print("Returned odd numbers:", result)
