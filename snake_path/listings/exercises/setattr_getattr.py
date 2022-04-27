class Person:
    pass


person = Person()

# person.first = 'John'
# person.last = 'Prytula'
# print(person.first)
# print(person.last)

first_key = 'first'
first_val = 'John'

# setattr(person, 'first', 'John')
setattr(person, first_key, first_val)  # we can also pass variables

first = getattr(person, first_key)

# print(person.first)
# print(first)

# Example of using
person_info = {'first': 'Johnny', 'last': 'Prytula'}
for key, value in person_info.items():
    setattr(person, key, value)

print(person.first)

for key in person_info.keys():
    print(getattr(person, key))
