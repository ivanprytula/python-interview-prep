from itertools import zip_longest

actors_names = ['Peter Parker', 'Clark Kent', 'Wade Wilson', 'Bruce Wayne']
heroes_name = ['Spiderman', 'Superman', 'Deadpool', 'Batman']
universes = ['Marvel', 'DC', 'Marvel', 'DC']

# Long way with enumerate object
# for index, name in enumerate(actors_names):
#     hero = heroes_name[index]
#     print(f'{name} is actually {hero}')

# NB: Better use zip()
# for actor, hero, universe in zip(actors_names, heroes_name, universes):
for value in zip(actors_names, heroes_name, universes):
    # print(f'{actor} is actually {hero} from {universe}')
    print('single tuple returned from zip() -->', value)

zip_object = zip(actors_names, heroes_name, universes)
print(zip_object)  # <zip object at 0x7efe869cadc0>, Iterator
print(zip_object.__next__())  # ('Peter Parker', 'Spiderman', 'Marvel')

# NB: zip_longest()
foo_data = [100, 200, 300, 400]
daily_data = list(zip_longest(range(10), foo_data))
print(daily_data)
