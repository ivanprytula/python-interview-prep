countries = []

print("Welcome to the countries app.")
print("You have visited 0 countries so far.")

user_input = input("Enter 'a' to add a country you've visited, or 'q' to quit: ")

while user_input != "q":
    # Do stuff here
    if user_input == "a":
        name = input("Country name: ")
        date = input("Date visited: ")
        countries.append([name, date])
    elif user_input == "l":
        print(f"You have visited {len(countries)} countries:")
        for data in countries:
            print(f"--> {data[0]}, visited on {data[1]}")
    # At the end of the loop, ask the user whether they want to go again
    user_input = input("Enter 'a' to add another country, 'l' to list the countries you've visited, or 'q' to quit: ")
