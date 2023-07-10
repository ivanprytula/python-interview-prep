<!--
.. title: Naming Convention
.. slug: naming-convention
.. date: 2022-04-17 15:42:21 UTC+03:00
.. description:
.. type: text
-->

# Clean code is ...?

focused
: Each function, class, or module should do one thing and do it well

easy to read and speak about
: Clean code is read like well-written prose

easy to debug
: The logic should be straightforward to make it hard for bugs to hide

easy to maintain
: That is it can easily be read and enhanced by other developers

highly performant
: performance close to optimal so as not to tempt people to make the code messy with unprincipled optimizations


# Python Naming Conventions

## 1. General
- Avoid using names that are too general or too wordy. Strike a good balance between the two. Use descriptive names that are easy to read.
    * Bad: `data_structure`, `my_list`, `info_map`, `dictionary_for_the_purpose_of_storing_data_representing_word_definitions`
    * Good: `user_profile`, `menu_options`, `word_definitions`
- Don’t be a jackass and name things "O", "l", "O1" or "I". Avoid using ambiguous shorthand.
- When using CamelCase names, capitalize all letters of an abbreviation (e.g. HTTPServer)
- Always use the same vocabulary
- Don’t use magic numbers

```python
# Not recommended
# The au variable is the number of active users
au = 105
c = ["UK", "USA", "UAE"]
fn = 'John'
Ln = 'Doe'
cre_tmstp = 1621535852
client_first_name = 'John'
customer_last_name = 'Doe'
from random import random
def roll_dice():
    return random.randint(0, 4)  # what is 4 supposed to represent?


# Recommended
total_active_users = 105
countries = ["UK", "USA", "UAE"]
first_name = 'John'
Las_name = 'Doe'
creation_timestamp = 1621535852
client_first_name = 'John'
client_last_name = 'Doe'

DICE_SIDES = 4
def roll_dice():
    return random.randint(0, DICE_SIDES)
```


## 2. Packages
- Package names should be all lower case
- When multiple words are needed, an underscore should separate them
- It is usually preferable to stick to 1 word names

## 3. Modules
- Module names should be all lower case
- When multiple words are needed, an underscore should separate them
- It is usually preferable to stick to 1 word names
```python
# pyramid.py
# [or]
# pyramid_giza.py
```

## 4. Classes
- Class names should follow the UpperCaseCamelCase convention
- Python’s built-in classes, however are typically lowercase words
- Exception classes should end with “Error”
- Do not add redundant context
```python
class PyramidGiza:
    pass

class InputError(Exception): # custom exception
    pass

# Not recommended
class PersonBad:
    def __init__(self, person_username, person_email, person_phone, person_address):
        self.person_username = person_username
        self.person_email = person_email
        self.person_phone = person_phone
        self.person_address = person_address

# Recommended
class PersonGood:
    """Since we are already inside the Person class, there's no need to add the person_ prefix to every class variable."""
    def __init__(self, username, email, phone, address):

        self.username = username
        self.email = email
        self.phone = phone
        self.address = address
```

## 5. Global (module-level) Variables
- Global variables should be all lowercase
- Words in a global variable name should be separated by an underscore

## 6. Instance Variables
- Instance variable names should be all lower case
- Words in an instance variable name should be separated by an underscore
- Non-public instance variables should begin with a single underscore
- If an instance name needs to be mangled, two underscores may begin its name
```python
pyramid_giza = "pyramid of giza" # Public
_pyramid_giza = "pyramid of giza" # Protected
__pyramid_giza = "pyramid of giza" # Private
```

## 7. Methods
- Method names should be all lower case
- Words in a method name should be separated by an underscore
- Non-public method should begin with a single underscore
- If a method name needs to be mangled, two underscores may begin its name
```python
def draw_pyramid_giza(): # Public
    pass
def _draw_pyramid_giza(): # Protected
    pass
def __draw_pyramid_giza(): # Private
    pass
```

## 8. Method Arguments
- Instance methods should have their first argument named ‘self’.
- Class methods should have their first argument named ‘cls’
```python
class PyramidGiza(object):
        def instance_method(self):
            print(f'Hello from {self.__class__.__name__}')

        @classmethod
        def class_method(cls):
            print(f'Hello from {cls.__name__}')

        @staticmethod
        def static_method():
            print(f'Hello from {PyramidGiza.static_method.__name__}')
```

## 9. Functions
- Function names should be all lower case
- Words in a function name should be separated by an underscore

## 10. Constants
- Constant names must be fully capitalized
- Words in a constant name should be separated by an underscore
```python
TOTAL = 100
# [or]
MAX_CAPACITY = 200
```
