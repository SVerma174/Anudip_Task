# Accept employee details
employee_details = {
    "name": input("Employee Name: "),"no": input("Enter your Mobile No: "),  "dep": input("From Which Department You Are: "),"des": input("Enter your Designation: "),
"DOJ": input("Enter your Date Of Joining (DD/MM/YYYY): "),"DOB": input("Enter your Date Of Birth (DD/MM/YYYY): "),"salary": float(input("Enter your Annual Salary in Lakhs: "))
}

print("\nEmployee Details:")
# Iterate through the dictionary to display key, value, and item
for key, value in employee_details.items():
    print(f"Key: {key}, Value: {value}, Item: ({key}, {value})")
