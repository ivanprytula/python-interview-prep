"""Application that asks the user for their age in years, and prints back the number of seconds they've lived for.
Try to use f-strings if possible.
Optionally, extend it so it prints months, days, hours, and seconds."""
import math

user_age_years = int(input("Enter your age: "))
user_age_months = user_age_years * 12
user_age_days = user_age_years * 365
user_age_hours = user_age_days * 24
user_age_minutes = user_age_hours * 60
user_age_seconds = user_age_minutes * 60

print(f"That's {user_age_months} months.")
print(f"Or {user_age_days} days.")
print(f"Or {user_age_hours} hours.")
print(F"Or {user_age_minutes} minutes.", F"Or {user_age_seconds} seconds.", sep=' - ')


# Secondary task: Calculate and print the area of a circle with a radius of 5 units


def calc_circle_area(radius):
    return math.pi * radius ** 2
    # return math.pi * pow(radius, 2)


print('\nCircle area:', calc_circle_area(5))
