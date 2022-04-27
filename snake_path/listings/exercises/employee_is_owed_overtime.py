employee_name = input("Enter the employee's name: ")
hours_worked = float(input(f"How many hours did {employee_name} work this week? "))
hourly_wage = float(input(f"What is {employee_name}'s hourly wage? "))

if hours_worked > 40:
    regular_pay = 40 * hourly_wage
    overtime_pay = (hours_worked - 40) * hourly_wage * 1.1
    owed_pay = int(regular_pay + overtime_pay)
else:
    owed_pay = int(hours_worked * hourly_wage)

print(f"{employee_name} is owed ${owed_pay}.")
