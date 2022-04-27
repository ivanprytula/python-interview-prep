"""
Common Python Anti-Patterns to watch out for
"""


# === Not Using Context Managers for Files ===

# bad
def open_file_bad():
    file_obj = open('abc.txt', 'r')
    data = file_obj.read()
    # do something exciting
    file_obj.close()


# good
def open_file_good():
    """Context managers in Python help to facilitate proper handling of resources,
    to control what to do when objects are created or destroyed. This removes the
    overhead of handling the creation and deletion of objects."""
    with open('abc.txt', 'r') as file_obj:
        data = file_obj.read()
        # do something exciting


# === Using type() to compare types ===

# bad
def compare_types_bad():
    name = 'Alex'
    if type(name) == str:
        print('It is a string')
    else:
        print('It is not a string')


# good
def compare_types_good():
    """isinstance() is usually the preferred way to compare types. It’s not only
    faster but also considers inheritance, which is often the desired behavior. In
    Python, you typically want to check if a given object behaves like a string or a
    list, not necessarily if it’s exactly a string. So instead of checking for string
    and all its custom subclasses, you can just use `isinstance`."""
    name = 'Alex'
    if isinstance(name, str):
        print('It is a string')
    else:
        print('It is not a string')


# === Use of `exec` ===

# bad
def exec_bad():
    s = "print(\"Hello, World!\")"
    exec(s)


# good
def exec_good():
    """The exec statement enables you to dynamically execute arbitrary Python code
    which is stored in literal strings. Building a complex string of Python code and
    then passing that code to exec results in code that is hard to read and hard to
    test. Anytime the Use of exec error is encountered, you should go back to the
    code and check if there is a clearer, more direct way to accomplish the task."""

    def print_word():
        print("Hello, World!")

    print_word()


# === No exception type(s) specified ===

# bad
def exception_type_specified_bad():
    try:
        5 / 0
    except:
        print("Exception")


# good
def exception_type_specified_good():
    """Not specifying an exception type might not only hide the error but also leads
    to losing information about the error itself. So its better to handle the
    situation with the appropriate error rather than the generic exception otherwise
    as shown below.

    With this pattern, you are able to handle exceptions based on their actual
    exception-type. The first exception type that matches the current error is
    handled first. Thus, it is recommended to handle specific exception types first (
    e.g., ZeroDivisionError) and generic error types (e.g., Exception) towards the
    end of the try-except block.
    """
    try:
        5 / 0
    except ZeroDivisionError as e:
        print("ZeroDivisionError")
    except Exception as e:
        print("Exception")
    else:
        print("No errors")
    finally:
        print('Good day')


# === Using map() or filter() instead of list comprehension ===

# bad
def map_instead_comprehension_bad():
    values = [1, 2, 3]
    doubles = map(lambda num: num * 2, values)


# good
def map_instead_comprehension_good():
    """For simple transformations that can be expressed as a list comprehension,
    its better to use list comprehensions over map() or filter() as map and filter
    are used for expressions that are too long or complicated to express with a list
    comprehension."""
    values = [1, 2, 3]
    doubles = [num * 2 for num in values]


# === Using list/dict/set comprehension unnecessarily ===

# bad
def using_comprehension_unnecessarily_bad():
    my_fav_superheroes = ['sdf', 'sdfdf', 'dfgdfg']
    comma_seperated_names = ','.join([name for name in my_fav_superheroes])


# good
def using_comprehension_unnecessarily_good():
    """Built-in functions like `all`, `any`, `enumerate`, `iter`, `itertools.cycle`,
    `itertools.accumulate`, can work directly with a generator expression. They do not
    require comprehension.

    In addition to them: `all()` and `any()` in Python also support short-circuiting,
    but this behavior is lost if comprehension is used. This affects performance.
    """
    my_fav_superheroes = ['sdf', 'sdfdf', 'dfgdfg']
    comma_seperated_names = ','.join(name for name in my_fav_superheroes)


# === Unnecessary use of generators ===

# bad
def use_of_generators_bad():
    squares = dict((i, i ** 2) for i in range(1, 10))


# good
def use_of_generators_good():
    """It is unnecessary to use a generator expression within a call to list,
    dict or set since there are comprehensions for each of these types. Instead of
    using list/dict/set around a generator expression, they can be written as their
    respective comprehension."""
    squares = {i: i ** 2 for i in range(1, 10)}


# === Not using `else` where appropriate in a `for` loop ===

# bad
def else_is_appropriate_bad():
    numbers = [1, 2, 3]
    n = 4
    found = False
    for num in numbers:
        if num == n:
            found = True
            print("Number found")
            break
    if not found:
        print("Number not found")


# good
def else_is_appropriate_good():
    """Python provides a built-in else clause for for loops. If a for loop completes
    without being prematurely interrupted by a break or return statement, then the
    else clause of the loop is executed."""
    numbers = [1, 2, 3]
    n = 4
    for num in numbers:
        if num == n:
            print("Number found")
            break
    else:
        print("Number not found")


# === Asking for permission instead of forgiveness ===

# bad
def permission_instead_of_forgiveness_bad():
    import os

    my_file = "/path/to/my/abc.txt"

    if os.access(my_file, os.R_OK):
        with open(my_file) as f:
            print(f.read())
    else:
        print("File can't be accessed")


# good
def permission_instead_of_forgiveness_good():
    """The Python community uses an EAFP (easier to ask for forgiveness than
    permission) coding style. This coding style assumes that needed variables, files,
    etc. exist. Any problems are caught as exceptions. This results in a generally
    clean and concise style containing a lot of try and except statements."""
    import os

    my_file = "/path/to/my/abc.txt"
    try:
        f = open(my_file)
    except IOError as e:
        print("File can't be accessed")
    else:
        with f:
            print(f.read())


# === Comparing with None/Boolean Values in the wrong way ===

# bad
def comparing_with_none_bool_bad():
    number = "None"
    flag = True
    if number == None or flag == True:
        print("This works, but is not the preferred PEP 8 pattern")


# good
def comparing_with_none_bool_good():
    """"""
    number = None
    flag = True
    if number is None or flag is True:
        print("PEP 8 Style Guide prefers this pattern")


# === Using wildcard imports ===

# bad
def wildcard_imports_bad():
    from collections import *


# good
def wildcard_imports_good():
    """"""
    from collections import Counter


# === Not using zip() to iterate over a pair of lists ===

# bad
def using_zip_bad():
    numbers = [1, 2, 3]
    letters = ["A", "B", "C"]
    for index in range(len(numbers)):
        print(numbers[index], letters[index])


# good
def using_zip_good():
    """"""
    numbers = [1, 2, 3]
    letters = ["A", "B", "C"]
    for numbers_value, letters_value in zip(numbers, letters):
        print(numbers_value, letters_value)


# === Using `key` in `list` to check if key is contained in list ===

# bad
def check_if_key_is_contained_in_list_bad():
    l = [1, 2, 3, 4]
    if 4 in l:
        print("The number 4 is in the list.")
    else:
        print("The number 4 is NOT in the list.")


# good
def check_if_key_is_contained_in_list_good():
    """Using key in list to iterate through a list can potentially take n iterations
    to complete, where n is the number of items in the list.

    If possible, you should change the list to a set or dictionary instead, because
    Python can search for items in a set or dictionary by attempting to directly
    accessing them without iterations, which is much more efficient (Since set in
    Python
    is implemented as a hash table and time complexity of accessing an element is O(1)).

    This is not applicable if your list has duplicates and you want to find all
    occurrences of the element.
    """
    original_list = [1, 2, 3, 4]
    s = set(original_list)
    if 4 in s:
        print("The number 4 is in the list.")
    else:
        print("The number 4 is NOT in the list.")


# === Not using `get()` to return default values from a dictionary ===

# bad
def using_get_for_dict_value_bad():
    stocks = {'AMZ': 'Amazon', 'AAPL': 'Apple'}

    if 'AMC' in stocks:
        stock_name = stocks['AMC']
    else:
        stock_name = 'undefined'


# good
def using_get_for_dict_value_good():
    """Frequently you will see code create a variable, assign a default value to the
    variable, and then check a dictionary for a certain key. If the key exists,
    then the value of the key is copied into the value for the variable. While there
    is nothing wrong this, it is more concise to use the built-in method dict.get(
    key[, default]) from the Python Standard Library. If the key exists in the
    dictionary, then the value for that key is returned. If it does not exist,
    then the default value specified as the second argument to get() is returned."""
    stocks = {'AMZ': 'Amazon', 'AAPL': 'Apple'}
    stock_name = stocks.get('AMC', 'undefined')


# === Not using items() to iterate over a dictionary ===

# bad
def using_items_iterate_dict_bad():
    country_map = {'us': "USA", 'uk': "United Kingdom"}
    for code in country_map:
        name = country_map[code]
        # do something with name


# good
def using_items_iterate_dict_good():
    """The `items()` method on a dictionary returns an iterable with key-value tuples
    which can be unpacked in a for loop. This approach is idiomatic, and hence
    recommended.
    """
    country_map = {'us': "USA", 'uk': "United Kingdom"}
    for code, name in country_map.items():
        # do something with name
        pass


# === Not Using explicit unpacking ===

# bad
def using_explicit_unpacking_bad():
    cars = ['BMW', 'Mazda', 'Tesla']

    car_1 = cars[0]
    car_2 = cars[1]
    car_3 = cars[2]


# good
def using_explicit_unpacking_good():
    """Unpacking is more concise and less error prone as manually assigning multiple
    variables to the elements of a list is more verbose and tedious to write."""
    cars = ['BMW', 'Mazda', 'Tesla']

    car_1, car_2, car_3 = cars


# === Not Using enumerate() in loops ===

# bad
def enumerate_in_loops_bad():
    cars = ['BMW', 'Mazda', 'Tesla']
    for ind in range(len(cars)):
        print(ind, cars[ind])


# good
def enumerate_in_loops_good():
    """Creating a loop that uses an incrementing index to access each element of a
    list within the loop construct is not the preferred style for accessing each
    element in a list. The preferred style is to use enumerate() to simultaneously
    retrieve the index and list element."""
    cars = ['BMW', 'Mazda', 'Tesla']
    for index, car in enumerate(cars):
        print(index, car)


# === Returning more than one object type in function call ===

# bad
def returning_many_types_from_function_call_bad(name, db=None):
    person = db.get_person(name)
    if person:
        return person.age  # returns an int

    # returns None if person not found


# good
def returning_many_types_from_function_call_good(name=None, db=None):
    """
    Having inconsistent return types in a function makes the code confusing and
    complex to understand, and can lead to bugs which are hard to resolve. If a
    function is supposed to return a given type (e.g. integer constant, list,
    tuple) but can something else as well, the caller of that function will always
    need to check for the type of value being returned. It is recommended to return
    only one type of object from a function.

    If there's a need to return something empty in some failing case, it is recommended
    to raise an exception that can be cleanly caught.
    :return:
    """
    person = db.get_person(name)
    if not person:
        raise Exception(f'No person found with name {name}')
    return person.age  # guaranteed to return int every time


# === Not using literal syntax to initialize empty list/dict/tuple ===

# bad
def using_literal_syntax_initialize_bad():
    my_evans = list()
    # Add something to this empty list


# good
def using_literal_syntax_initialize_good():
    """
    It is relatively slower to initialize an empty dictionary by calling dict() than
    using the empty literal, because the name dict must be looked up in the global
    scope in case it has been rebound. Same goes for the other two types — list() and
    tuple().
    :return:
    """
    my_evans = []
    # Add something to this empty list


# === Pushing debugger in production code ===

# bad
def debugger_in_prod_bad():
    breakpoint()
    # push to prod env


# good
def debugger_in_prod_good():
    """
    Most of us have done this at least once — while debugging code, it may happen
    that you push your code after you found the bug but forgotten to remove the
    debugger. This is critical, and can affect the behavior of the code. It is highly
    recommended to audit the code to remove invocations of debuggers before checking in.
    :return:
    """
    # breakpoint()
    # some business logic
    ...


# ===  ===

# bad
def _bad():
    ...


# good
def _good():
    """"""
    ...


# ===  ===

# bad
def _bad():
    ...


# good
def _good():
    """"""
    ...
