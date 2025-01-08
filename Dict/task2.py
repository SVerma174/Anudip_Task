# Take input from the user to define dictionaries
dic1 = {int(input("Key for dic1: ")): int(input("Value for dic1: "))}
dic2 = {int(input("Key for dic2: ")): int(input("Value for dic2: "))}
dic3 = {int(input("Key for dic3: ")): int(input("Value for dic3: "))}

# Concatenate dictionaries using the | operator
result = dic1 | dic2 | dic3
print("Concatenated dictionary:", result)

