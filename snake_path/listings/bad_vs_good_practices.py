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



def show_best_practices(pos1, pos2, /, pos_or_kwd=True, *, kwd1, kwd2=""):
    """
    Shows good and best practices for getting clean & idiomatic code.

    # https://deepsource.io/blog/python-positional-only-arguments/
    PEP 570

    :param pos1: 1st positional `only` argument
    :param pos2: 2nd positional `only` argument
    :param pos_or_kwd: after '/' -> positional `or` keyword args
    :param kwd1: after '*' -> keyword `only` argument
    :param kwd2: 2nd keyword `only` argument
    :return:
    """

    # fyi: === Using `Context Managers` for Files ===
    with open('abc.txt', 'r') as file_obj:
        """
        Context managers in Python help to facilitate proper handling of resources,
        to control what to do when objects are created or destroyed. This removes the
        overhead of handling the creation and deletion of objects.
        """
        data = file_obj.read()
        # do something exciting

    # === Using isinstance() to compare types ===
    name = 'Alex'
    if isinstance(name, str):
        """isinstance() is usually the preferred way to compare types. It’s not only
        faster but also considers inheritance, which is often the desired behavior. In
        Python, you typically want to check if a given object behaves like a string or a
        list, not necessarily if it’s exactly a string. So instead of checking for 
        string
        and all its custom subclasses, you can just use `isinstance`."""
        print('It is a string')
    else:
        print('It is not a string')

    # === Use of `exec()` ONLY in very specific case ===
    def print_word():
        """The exec statement enables you to dynamically execute arbitrary Python code
        which is stored in literal strings. Building a complex string of Python code and
        then passing that code to exec results in code that is hard to read and hard to
        test. Anytime the use of exec error is encountered, you should go back to the
        code and check if there is a clearer, more direct way to accomplish the task."""
        print("Hello, World!")
    print_word()

    # === Use exception type(s) specified ===
    try:
        """Not specifying an exception type might not only hide the error but also leads
        to losing information about the error itself. So its better to handle the
        situation with the appropriate error rather than the generic exception otherwise
        as shown below.

        With this pattern, you are able to handle exceptions based on their actual
        exception-type. The first exception type that matches the current error is
        handled first. Thus, it is recommended to handle specific exception types 
        first (
        e.g., ZeroDivisionError) and generic error types (e.g., Exception) towards the
        end of the try-except block.
        """
        print(5 / 0)
    except ZeroDivisionError as e:
        print(f"ZeroDivisionError: {e}")
    except Exception as e:
        print(F"Exception: {e}")
    else:
        print("No errors")
    finally:
        print('Good day')

    # === Using map() or filter() instead of list comprehension ===
    """For simple transformations that can be expressed as a list comprehension,
    it is better to use list comprehensions over map() or filter() as map and filter
    are used for expressions that are too long or complicated to express with a list
    comprehension."""
    values = [1, 2, 3]
    doubles = [num * 2 for num in values]

    # === Use generator expression directly, w/o unnecessary comprehension ===
    """Built-in functions like `all`, `any`, `enumerate`, `iter`, `itertools.cycle`,
    `itertools.accumulate`, can work directly with a generator expression. They do not
    require comprehension.
    In addition to them: `all()` and `any()` in Python also support short-circuiting,
    but this behavior is lost if comprehension is used. This affects performance.
    """
    my_fav_superheroes = ['sdf', 'sdfdf', 'dfgdfg']
    comma_seperated_names = ','.join(name for name in my_fav_superheroes)

    # === Use respective comprehension instead of unnecessary use of generators ===
    """It is unnecessary to use a generator expression within a call to list,
    dict or set since there are comprehensions for each of these types. Instead of
    using list/dict/set around a generator expression, they can be written as their
    respective comprehension."""
    squares = {i: i ** 2 for i in range(1, 10)}

    # === Using `else` where appropriate in a `for` loop ===
    """Python provides a built-in `else` clause for `for` loops. If a `for` loop completes
    without being prematurely interrupted by a `break` or `return` statement, then the
    `else` clause of the loop is executed."""
    numbers = [1, 2, 3]
    n = 4
    for num in numbers:
        if num == n:
            print("Number found")
            break
    else:
        print("Number not found")

    # === EAFP: “it’s easier to ask for forgiveness than permission”. ===
    """The Python community uses an EAFP (easier to ask for forgiveness than
    permission) coding style. This coding style assumes that needed variables, files,
    etc. exist. Any problems are caught as exceptions. This results in a generally
    clean and concise style containing a lot of try and except statements."""
    dict_ = {}
    value = None
    try:
        value += dict_["key"]
        print(value)
    except KeyError:
        pass

    # === Comparing with None/Boolean values in the Correct way ===
    number = None
    flag = True
    # ... many lines after:
    if number is None or flag is True:
        print("PEP 8 Style Guide prefers this pattern")

    # === Using wildcard imports * ===
    from collections import Counter

    # === Use zip() to iterate over a pair of lists ===
    numbers = [1, 2, 3]
    letters = ["A", "B", "C"]
    for numbers_value, letters_value in zip(numbers, letters):
        print(numbers_value, letters_value)

    # === Using set/dict to check if key is in list (especially very long) ===
    """Using key in list to iterate through a list can potentially take n iterations
    to complete, where n is the number of items in the list.

    If possible, you should change the list to a set or dictionary instead, because
    Python can search for items in a set or dictionary by attempting to directly
    accessing them without iterations, which is much more efficient (Since set in
    Python
    is implemented as a hash table and time complexity of accessing an element is O(1)).

    This is not applicable if your list has duplicates, and you want to find all
    occurrences of the element.
    """
    original_list = [1, 2, 3, 4]
    s = set(original_list)
    if 4 in s:
        print("The number 4 is in the list.")
    else:
        print("The number 4 is NOT in the list.")

    # === Use `get()` to return default values from a dictionary ===
    """Frequently you will see code create a variable, assign a default value to the
    variable, and then check a dictionary for a certain key. If the key exists,
    then the value of the key is copied into the value for the variable. While there
    is nothing wrong this, it is more concise to use the built-in method dict.get(
    key[, default]) from the Python Standard Library. If the key exists in the
    dictionary, then the value for that key is returned. If it does not exist,
    then the default value specified as the second argument to get() is returned."""
    stocks = {'AMZ': 'Amazon', 'AAPL': 'Apple'}
    stock_name = stocks.get('AMC', 'undefined')

    # === Use items() to iterate over a dictionary ===
    """The `items()` method on a dictionary returns an iterable with key-value tuples
    which can be unpacked in a `for` loop. This approach is idiomatic, and hence
    recommended.
    """
    country_map = {'us': "USA", 'uk': "United Kingdom"}
    for code, name in country_map.items():
        # do something with name
        pass

    # === Use explicit unpacking ===
    """Unpacking is more concise and less error-prone as manually assigning multiple
    variables to the elements of a list is more verbose and tedious to write."""
    cars = ['BMW', 'Mazda', 'Tesla']
    cars2 = ['BMW', 'Mazda', 'Tesla']
    cars3 = ('BMW', 'Mazda', 'Tesla', 'Audi')
    car_1, car_2, car_3 = cars
    car_1, car_2, _ = cars2  # _ -> if we don't need variable name for other values
    car_1, car_2, *car_3 = cars3  # car_1='BMW', car_2='Mazda', car_3=('Tesla', 'Audi')

    # === Use enumerate() in loops ===
    """Creating a loop that uses an incrementing index to access each element of a
    list within the loop construct is not the preferred style for accessing each
    element in a list. The preferred style is to use enumerate() to simultaneously
    retrieve the index and list element."""
    cars = ['BMW', 'Mazda', 'Tesla']
    for index, car in enumerate(cars):
        print(index, car)

    # === Prefer returning one object type in function call ===
    def returning_many_types_from_function_call_good(name=None, db=None):
        """
        Having inconsistent return types in a function makes the code confusing and
        complex to understand, and can lead to bugs which are hard to resolve. If a
        function is supposed to return a given type (e.g. integer constant, list,
        tuple) but can something else as well, the caller of that function will always
        need to check for the type of value being returned. It is recommended to return
        only one type of object from a function.

        If there's a need to return something empty in some failing case,
        it is recommended to raise an exception that can be cleanly caught.
        :return:
        """
        person = db.get_person(name)
        if not person:
            raise Exception(f'No person found with name {name}')
        return person.age  # guaranteed to return int every time

    # === Use literal syntax to initialize empty list/dict/tuple ===
    """
    It is relatively slower to initialize an empty dictionary by calling dict() than
    using the empty literal, because the name dict must be looked up in the global
    scope in case it has been rebound. Same goes for the other two types — list() and
    tuple().
    """
    my_evans = []
    my_maps = {}
    my_tuple = ()
    my_set = set()  # because there is no literal syntax for set
    # Add something to this empty list

    # === Audit code thoroughly! in production code ===
    """
    Most of us have done this at least once — while debugging code, it may happen
    that you push your code after you found the bug but forgotten to remove the
    debugger. This is critical, and can affect the behavior of the code. It is highly
    recommended to audit the code to remove invocations of debuggers before checking in.
    :return:
    """
    # remove all breakpoint()/print()/pdb
    # ...some ready for dev/qa/stage/prod envs business logic...
