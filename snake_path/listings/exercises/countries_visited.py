"""Create a program that asks the user for a country. Then it should tell the user
whether we've visited that country or not. We'll need a list of known countries first,
and then ask the user for their country. Then check if their country is in our list."""

countries = ["Spain", "Italy", "Germany", "United States", "United Kingdom"]

user_country = input("Enter a country you have visited: ")

if user_country in countries:
    print("I have also visited that country!")
else:
    print("I want to go there one day too.")

# Secondary task
friends = ["Rolf", "Bob", "Anne"]

# copy() creates independent copy of original object, but only "shallow copy",
# i.e. only for first-level list but not for nested lists
friends_abroad = friends.copy()
friends_abroad.remove("Bob")
print(id(friends), id(friends_abroad))  # ids are different
