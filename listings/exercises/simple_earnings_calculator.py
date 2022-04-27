name = input("Please enter the employee's name: ").strip().title()
hourly_wage = input("What is their hourly wage? ")
hours_worked = input("How many hours have they worked this week? ")

try:
    hourly_wage = float(hourly_wage)
except ValueError:
    print('You entered non-numeric value for hourly wage')

try:
    hours_worked = float(hours_worked)
except ValueError:
    print('You entered non-numeric value for hours worked')

try:
    earnings = hourly_wage * hours_worked
    print(f"{name} earned ${earnings:.2f} this week.")
except TypeError:
    print('You are doing wrong calculation!')

# NB: Precision
x = 4863.4343091  # example float to format

print(f"{x:.6f}")  # f-string version
print("{:.6f}".format(x))  # format method version
print(f"{x:.3}")  # 4.86e+03
print(f"{x:.3f}")  # 4863.434
print(f"{x:f}")  # 4863.434309, f on its own as well, which defaults to 6 digits of precision

# NB: Separators
y = 1000000

print(f"{y:,}")  # 1,000,000
print(f"{y:_}")  # 1_000_000

# NB: Percentages
questions = 30
correct_answers = 23

print(f"You got {correct_answers / questions :.2%} correct!")
# You got 76.67% correct!
