movies = [
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)
]

new_movie_count = int(input("Enter how many new movies you wish to add: "))

for _ in range(new_movie_count):
    name = input("Enter new movie name: ")
    budget = int(input("Enter new movie budget: "))
    new_movie = (name, budget)
    movies.append(new_movie)

high_budget_movies = []
total_budget = 0

for movie in movies:
    total_budget += movie[1]

average_budget = int(total_budget / len(movies))

for movie in movies:
    if movie[1] > average_budget:
        high_budget_movies.append(movie)
        over_average_cost = movie[1] - average_budget
        print(f"{movie[0]} cost ${movie[1]}: ${over_average_cost} over average.")

print(f"There were {len(high_budget_movies)} movies with over average budgets.")
