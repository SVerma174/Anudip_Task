'''Write a python program and iterate the given tuples
Input:
employee1 = ("John Doe", 101, "Human Resources", 60000)
employee2 = ("Alice Smith", 102, "Marketing", 55000)
employee3 = ("Bob Johnson", 103, "Engineering", 75000)'''



# Input from the user for three employees
employee1 = tuple(input("Enter details for Employee 1 (Name, ID, Department, Salary): ").split(", "))
employee2 = tuple(input("Enter details for Employee 2 (Name, ID, Department, Salary): ").split(", "))
employee3 = tuple(input("Enter details for Employee 3 (Name, ID, Department, Salary): ").split(", "))

# Combine the tuples into a list for iteration
employees = [employee1, employee2, employee3]

# Iterate over the employee details
for emp in employees:
    print("Name:", emp[0])
    print("ID:", emp[1])
    print("Department:", emp[2])
    print("Salary:", emp[3])
    print()  # Add an empty line for better readability
