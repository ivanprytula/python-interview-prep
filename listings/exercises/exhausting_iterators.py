actors_names = ['Peter Parker', 'Clark Kent', 'Wade Wilson', 'Bruce Wayne']
heroes_name = ['Spiderman', 'Superman', 'Deadpool', 'Batman']

identities = zip(actors_names, heroes_name)
print(identities)

print(list(identities))  # at this moment iterator has been exhausted
next(identities)  # --> StopIteration

# so this code cannot be executed
for identity in identities:
    print(f'{identity[0]} is actually {identity[1]}')
