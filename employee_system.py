# Employee system ( activity 42)
print("*** Employee system")

# Request data to user
employee_name =input("Enter name:")
employee_age = int(input("Enter age:"))
employee_salary = float(input("Enter salary:"))
is_boss = input("Enter if is departament boss (yes/no):")

#convert to bool is_boss
is_boss = is_boss.lower() == "yes"

# Print employee values
print(f"Name: {employee_name}")
print(f"Age: {employee_age}")
print(f"Salary: {employee_salary:.2f}")
print(f"Is boss?: {is_boss}")