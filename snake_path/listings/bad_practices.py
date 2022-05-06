"""
Common Python Anti-Patterns to watch out for
"""


def show_bad_ugLiesTFuncEveR_patterns(abc=42, foo=[]):
    """
    this is super cool docs for cool func.
    blah foo spam eggs bar buzz..........


    :param abc: blah blah
    :param foo: blah blah
    :param bar: blah blah
    :return: I dunno what exactly, but many things
    """
    # === Not Using Context Managers for Files ===
    file_obj = open('abc.txt', 'r')
    data = file_obj.read()
    # do something exciting
    file_obj.close()

    # === Using type() to compare types ===
    name = 'Alex'
    if type(name) == str:
        print('It is a string')
    else:
        print('It is not a string')

    # === Use of `exec()` ===
    s = "print(\"Hello, World!\")"
    exec(s)

    # === No exception type(s) specified ===
    try:
        print(5 / 0)
    except:
        print("Exception")

    # === Using map() or filter() instead of list comprehension ===
    values = [1, 2, 3]
    doubles = map(lambda num: num * 2, values)

    # === Using list/dict/set comprehension unnecessarily ===
    my_fav_superheroes = ['sdf', 'sdfdf', 'dfgdfg']
    comma_seperated_names = ','.join([name for name in my_fav_superheroes])

    # === Unnecessary use of generators ===
    squares = dict((i, i ** 2) for i in range(1, 10))

    # === Not using `else` where appropriate in a `for` loop ===
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

    # ===  LBYL: “look before you leap” ===
    dict_ = dict()
    value = None
    if "key" in dict_:
        value += dict_["key"]

    # === Comparing with None/Boolean values in the wrong way ===
    number = None
    flag = True
    # ... many lines after:
    if number == None or flag == True:
        print("This works, but is not the preferred PEP 8 pattern")

    # === Using wildcard imports * ===
    from collections import *

    # === Not using zip() to iterate over a pair of lists ===
    numbers = [1, 2, 3]
    letters = ["A", "B", "C"]
    for index in range(len(numbers)):
        print(numbers[index], letters[index])

    # === Using `key` in `list` to check if key is contained in list ===
    l = [1, 2, 3, 4]
    if 4 in l:
        print("The number 4 is in the list.")
    else:
        print("The number 4 is NOT in the list.")

    # === Not using `get()` to return default values from a dictionary ===
    stocks = {'AMZ': 'Amazon', 'AAPL': 'Apple'}
    if 'AMC' in stocks:
        stock_name = stocks['AMC']
    else:
        stock_name = 'undefined'

    # === Not using items() to iterate over a dictionary ===
    country_map = {'us': "USA", 'uk': "United Kingdom"}
    for code in country_map:
        name = country_map[code]
        # do something with name

    # === Not Using explicit unpacking ===
    cars = ['BMW', 'Mazda', 'Tesla']
    car_1 = cars[0]
    car_2 = cars[1]
    car_3 = cars[2]

    # === Not Using enumerate() in loops ===
    cars = ['BMW', 'Mazda', 'Tesla']
    for ind in range(len(cars)):
        print(ind, cars[ind])

    # === Returning more than one object type in function call ===
    def returning_many_types_from_function_call_bad(name, db=None):
        person = db.get_person(name)
        if person:
            return person.age  # returns an int

        # returns None if person not found

    # === Not using literal syntax to initialize empty list/dict/tuple ===
    my_evans = list()
    my_maps = dict()
    my_tuple = tuple()
    # Add something to this empty list

    # === Pushing debugger in production code ===
    breakpoint()
    # push to prod env
