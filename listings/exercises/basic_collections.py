movies = [(
    "Eternal Sunshine of the Spotless Mind",
    "Michel Gondry",
    2004,
    1_000_000
), ]

new_movie_title = input('Enter movie title: ')
new_movie_director = input('Enter director\'s name: ')
new_movie_release_year = input('Enter release year: ')
new_movie_budget = input('Enter budget: ')

# bad:  we can write like this but it's very UN-readable
# new_movie_info = new_movie_title.title(), new_movie_director.title(), int(new_movie_release_year),
# int(new_movie_budget)

# good: much more better readability
new_movie_info = (
    new_movie_title.title(),
    new_movie_director.title(),
    int(new_movie_release_year),
    int(new_movie_budget)
)

print(f'{new_movie_info[0]} ({new_movie_info[2]})')

movies.append(new_movie_info)

for movie in movies:
    print('-->', movie)

del movies[0]
# movies.pop(0)
# movies.remove(movies[0])

print(movies)
