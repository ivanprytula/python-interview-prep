# By adding the line #!/usr/bin/python3 on the top of the script, we can run the file.py
# on a Unix system & automatically will understand that this is a python script.
# !/usr/bin/python3
"""A one line summary of the module or program, terminated by a period.

Leave one blank line.  The rest of this docstring should contain an
overall description of the module or program.  Optionally, it may also
contain a brief description of exported classes and functions and/or usage
examples.
PEP = Python Enhancement Proposal

  Typical usage example:

  foo = ClassFoo()
  bar = foo.get_bar()
"""

# ####### 1. STL imports
import datetime
import importlib
import math
import os
import platform
import random
import sys
from copy import copy, deepcopy
from pprint import pprint

# ####### 2. 3rd-party packages
from colorama import Fore, Back, Style
import requests

# fyi: Such import style will cause issues with built-in funcs - if names match, they will be overridden.
# from os import *

# ####### 3. Your own packages
# import model_name from models_package


GRAVITATIONAL_CONSTANT: float = 9.81

# Write a full sentence in one-line comment with a period in the end.
multiline_comment = '''
    Not a Module docstring \t but comment assigned to variable.\n This will be a second line if printed.

'''


def explore_file_handling():
    main_dir: str = os.path.split(os.path.abspath(path=__file__))[0]
    data_dir: str = os.path.join(main_dir, 'data')
    test_data_file = 'test_data.txt'
    test_data_path = f'{data_dir}/{test_data_file}'

    try:
        # context manager
        with open(file=test_data_path, mode='x') as file_obj:
            antigravity_trial = random.randint(a=8, b=10)
            if 8 < antigravity_trial <= int(GRAVITATIONAL_CONSTANT):
                import antigravity

                print(antigravity.__name__)
            else:
                module_path = importlib.import_module('exercises/python_zen')
                file_obj.write(str(module_path))
    except FileExistsError as file_error:
        os.remove(test_data_path)
        print(f'Existed file was removed', file_error)
    else:
        print("This code will execute if no exception happened.")
        print("\nLet's try to overcome gravity!\n")
    finally:
        print('*' * 20)
        print('Ok, double-check your current directory:\n')
        os.system('ls -l')


def explore_data_types():
    """Remember LEGB rule."""
    # Note: Avoid + operator for string concatenation. Prefer string formatting.
    data_types_question = 'data types in Python. Write corresponding classes (separated by space): '
    entered_immutable_data_types = input(f'Name immutable {data_types_question}').strip().split()
    entered_mutable_data_types = input(f'Name mutable {data_types_question}').strip().split()

    # Define function with parameters
    def check_data_types(user_input: list = None, data=None) -> bool:
        """Test user knowledge of basic data types."""

        # TIP: check list for emptiness
        if not user_input:
            user_input = []

        # shorthand instead of if... statement
        data = data or []

        #     int float bool str bytes tuple frozenset
        #     list dict set bytearray

        immutable_data_types = (int, float, bool, str, bytes, tuple, frozenset)
        mutable_data_types = (list, dict, set, bytearray,)
        builtins_data_types = immutable_data_types + mutable_data_types
        print('builtins_data_types:', builtins_data_types)

        # Create generator and convert it to tuple
        builtins_data_types_as_strings = tuple((dt.__name__ for dt in builtins_data_types))
        print('builtins_data_types_as_strings:', builtins_data_types_as_strings)

        unique_entered_types = set(user_input)
        print('unique_entered_types:', unique_entered_types)
        correct_types = list(filter(lambda dt: dt in builtins_data_types_as_strings, unique_entered_types))

        print('correct_types:', correct_types)

        # aka double-check
        if len(correct_types) == int('11', base=10):
            print(f'You named all data types!')
            return True
        elif len(correct_types) > int('11', base=10):
            print('Do you know more than me?')
            return bool(0)
        else:
            missed_types = set(builtins_data_types_as_strings) - unique_entered_types
            print(f'You\'ve missed {missed_types}')
            return False

    check_data_types(user_input=entered_immutable_data_types + entered_mutable_data_types)


def show_basic_operators():
    first_name = 'Ivan'
    last_name = 'Prytula'

    # print('{first_name} {last_name}'.format())
    print('{0} {1}'.format(first_name, last_name))

    # f-string format datetime
    now = datetime.datetime.now()
    print(f'{now:%Y-%m-%d %H:%M}')

    user_age = 33
    admin_age = 35
    user_salary = 1_000_000
    admin_salary = 2_000_000.5

    total_salary = (user_salary + admin_salary) ** 2 % 7 // 2 / 2.0 * 4000 + 100 - 4  # -> 4096.0
    total_salary += 200
    total_salary -= 400
    total_salary *= 5
    total_salary /= 3
    total_salary //= 3
    total_salary **= 2
    total_salary %= 3
    is_lost = None
    funny_list = ['is_lost' * 5]
    print(funny_list)
    del is_lost
    # print(id(is_lost))  # UnboundLocalError: local variable 'is_lost' referenced before assignment

    print('Final salary:', round(total_salary, 3))  # -> 6493.333

    # f-string format floats
    print(f'Final age: {user_age / admin_age:.5f}', )  # -> 0.94286
    #  P  E  M  IntDiv  D  M  A  S
    # ()  ** %  //      /  *  +  -

    # Operators    _Operation_          _Example_
    # **            Exponent            2 ** 3 = 8
    # %             Modulus/Remainder   22 % 8 = 6
    # //            Integer division    22 // 8 = 2
    # /             Division            22 / 8 = 2.75
    # *             Multiplication      3 * 3 = 9
    # -             Subtraction         5 - 2 = 3
    # +             Addition            2 + 2 = 4

    # f-string format width
    for x in range(1, 11):
        print(f'{x:002} {x * x:3} {x * x * x:4}')

    # f-string justify string
    s1 = 'a'
    s2 = 'ab'
    s3 = 'abc'
    s4 = 'abcd'

    print(f'{s1:>10}')
    print(f'{s2:>10}')
    print(f'{s3:>10}')
    print(f'{s4:>10}')

    # f-string numeric notations
    numeric_notation = numeric_notation_two = 300

    # hexadecimal
    print(f"{numeric_notation:x}")  # 12c

    # octal
    print(f"{numeric_notation:o}")  # 453

    # scientific
    print(f"{numeric_notation:e}")  # 3.000000e+02


def show_comprehensions():
    numbers_one = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
    numbers_two = copy(numbers_one)

    test_str2 = "let's do more Python!".title()  # Let'S Do More Python!

    # TIP: "".join(<iterable_of_substrings>) is 2-3 times faster than "for-loop s += subsrings"
    res2 = ''.join([str(ord(elem)) for elem in test_str2])  # 76101116398332681113277111114101328012111610411111033
    doubled_numbers = [num * 2 for num in numbers_one]
    doubled_numbers_tuple = tuple(doubled_numbers)
    stringified_numbers_dict = {str(num): num for num in numbers_two if 0 < num < 10}
    stringified_numbers_dict.update(doubled_numbers_tuple=doubled_numbers_tuple)
    pprint(stringified_numbers_dict, indent=2, width=100, depth=2, compact=True)


def explore_builtins():
    """Sandbox to play with builtins."""
    print(abs(-40))  # 40
    will_be_eliminated_from_set = 1
    seq_to_test = {1, 4, will_be_eliminated_from_set, 'abc', None, sys.copyright}
    print(all(seq_to_test), any(seq_to_test), sep='\n')

    # TIP:
    a_1 = sys.intern('hello')
    b_1 = sys.intern('hello' + 'd')
    print(a_1 is b_1)  # True

    import keyword

    print('keyword.kwlist:', keyword.kwlist)

    # help()

    keywords = """
        False               break               for                 not
        None                class               from                or
        True                continue            global              pass
        __peg_parser__      def                 if                  raise
        and                 del                 import              return
        as                  elif                in                  try
        assert              else                is                  while
        async               except              lambda              with
        await               finally             nonlocal            yield
    """

    modules = '''
    PIL                 _weakrefset         hmac                remove_empty_lines
    __future__          _xxsubinterpreters  html                reprlib
    _abc                _xxtestfuzz         http                resource
    _aix_support        _zoneinfo           imaplib             rlcompleter
    _ast                abc                 imghdr              runfiles
    _asyncio            aifc                imp                 runpy
    _bisect             antigravity         importing_with_asterisk sched
    _blake2             argparse            importlib           scopes
    _bootlocale         args_passing        inspect             secrets
    _bootsubprocess     array               interpreterInfo     select
    _bz2                ascii_transformation io                  selectors
    _codecs             ast                 ipaddress           setattr_getattr
    _codecs_cn          asynchat            iterators_vs_lists  setup_cython
    _codecs_hk          asyncio             itertools           setuptools
    _codecs_iso2022     asyncore            json                shelve
    _codecs_jp          atexit              json_demos          shlex
    _codecs_kr          audioop             keyword             shuffle_list
    _codecs_tw          backend_interagg    lib2to3             shutil
    _collections        base64              linecache           signal
    _collections_abc    basic_collections   locale              site
    _compat_pickle      bdb                 logging             sitecustomize
    _compression        binascii            lzma                smtpd
    _contextvars        binhex              mailbox             smtplib
    _crypt              bisect              mailcap             sndhdr
    _csv                bs4                 marshal             socket
    _ctypes             builtins            math                socketserver
    _ctypes_test        bz2                 mimetypes           soupsieve
    _curses             cProfile            mmap                spwd
    _curses_panel       calendar            modulefinder        sqlite3
    _datetime           cgi                 monkey_path_module_func sqlite_demos
    _dbm                cgitb               most_frequent_word  sre_compile
    _decimal            check_palindrome    multiprocessing     sre_constants
    _distutils_hack     chunk               mutable_default_args sre_parse
    _elementtree        cmath               netrc               ssl
    _functools          cmd                 network_programming_demos stat
    _gdbm               code                nis                 statistics
    _hashlib            codecs              nntplib             string
    _heapq              codeop              ntpath              string_of_numbers
    _imp                collections         nturl2path          stringprep
    _io                 colorama            numbers             struct
    _json               colorsys            oop_demos           subprocess
    _locale             compileall          opcode              sunau
    _lsprof             concurrent          operator            switch_implementation
    _lzma               configparser        optparse            symbol
    _markupbase         context_managers    os                  symtable
    _md5                contextlib          ossaudiodev         sys
    _multibytecodec     contextvars         parser              sysconfig
    _multiprocessing    copy                pass_keyword        syslog
    _opcode             copying_objects     pathlib             tabnanny
    _operator           copyreg             pdb                 tarfile
    _osx_support        count_capital_letters pickle              telnetlib
    _peg_parser         crypt               pickletools         tempfile
    _pickle             csv                 pip                 termios
    _posixshmem         ctypes              pipes               ternary_conditionals
    _posixsubprocess    curses              pkg_resources       test
    _py_abc             dash_m_option_shell pkgutil             textwrap
    _pydecimal          dataclasses         platform            this
    _pydev_bundle       datalore            plistlib            threading
    _pydev_comm         datetime            polymorphism        time
    _pydev_imps         dbm                 poplib              timeit
    _pydev_runfiles     decimal             posix               tkinter
    _pydevd_bundle      difflib             posixpath           tkinter_demos
    _pydevd_frame_eval  dis                 pprint              token
    _pyio               distutils           prep_jr_strong      tokenize
    _queue              doctest             print_closer_look   trace
    _random             email               print_star_triangle traceback
    _sha1               encapsulation       profile             tracemalloc
    _sha256             encodings           pstats              tty
    _sha3               ensurepip           pty                 turtle
    _sha512             enum                pwd                 type_hinting
    _shaded_ply         enumerate_demo      py_compile          types
    _shaded_thriftpy    errno               pyclbr              typing
    _signal             exhausting_iterators pycompletionserver  underscore_placeholders
    _sitebuiltins       faulthandler        pydev_app_engine_debug_startup unicodedata
    _socket             fcntl               pydev_console       unittest
    _sqlite3            file1               pydev_coverage      unpacking_sequences
    _sre                file_for_importing  pydev_ipython       urllib
    _ssl                filecmp             pydev_pysrc         uu
    _stat               fileinput           pydev_test_pydevd_reload uuid
    _statistics         fnmatch             pydev_tests         venv
    _string             formatter           pydev_tests_mainloop warnings
    _strptime           fractions           pydev_tests_python  wave
    _struct             ftplib              pydevconsole        weakref
    _symtable           functools           pydevd              webbrowser
    _sysconfigdata__linux_x86_64-linux-gnu gc                  pydevd_concurrency_analyser wsgiref
    _sysconfigdata__x86_64-linux-gnu genericpath         pydevd_file_utils   xdrlib
    _testbuffer         get_pass_from_input pydevd_plugins      xml
    _testcapi           getopt              pydevd_pycharm      xml_demos
    _testimportmultiple getpass             pydevd_tracing      xmlrpc
    _testinternalcapi   gettext             pydoc               xxlimited
    _testmultiphase     glob                pydoc_data          xxsubtype
    _thread             gorilla_lib         pyexpat             zip()_demo
    _threading_local    graphlib            queue               zipapp
    _tkinter            grp                 quopri              zipfile
    _tracemalloc        gzip                random              zipimport
    _uuid               hashlib             re                  zlib
    _warnings           heapq               readline            zoneinfo
    _weakref            help_dir            regex_demos
    '''

    symbols = """
        !=                  +                   <=                  __
        "                   +=                  <>                  `
        \"\"\"                 ,                   ==                  b"
        %                   -                   >                   b'
        %=                  -=                  >=                  f"
        &                   .                   >>                  f'
        &=                  ...                 >>=                 j
        '                   /                   @                   r"
        '''                 //                  J                   r'
        (                   //=                 [                   u"
        )                   /=                  \\                  u'
        *                   :                   ]                   |
        **                  <                   ^                   |=
        **=                 <<                  ^=                  ~
        *=                  <<=                 _
    """


def explore_control_flow():
    """The else clause in the while else statement will execute when the condition of the while loop is False and
    the loop runs normally without encountering the break or return statement."""
    lemon = acidity = 0
    money = 90
    while acidity < 100:
        if acidity < 50:
            break
        elif lemon == 10:
            continue
        acidity = lemon + 2 if money >= 50 else lemon + 1
        lemon += 1
    else:
        print('Whoah!')


def unpacking_assignment():
    pairs = [(10, 5, math.pi), (8, 100, math.tau)]
    for left, middle, right in pairs:
        print(left * middle - right)

    # "swap variables" == collection unpacking
    # x, y = [35, 15]
    # x, y = (35, 15)
    # x, y = {35, 15}

    numbers_one = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
    numbers_two = copy(numbers_one)
    print(id(numbers_one), id(numbers_two))

    animals = {
        'dog': {
            'type': 'good',
            'family': 'long_hair'
        }
    }

    animals_deep_copy = deepcopy(animals)
    print(id(animals), id(animals_deep_copy))

    part_a, *part_b = numbers_one
    *part_c, part_d, _ = numbers_one

    # part_c == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # part_d == 11
    # _ == rest which we don't need
    # print('part_c', part_c, 'part_d', part_d)
    # print(numbers_one[1:11:2])


def bitwise_operators():
    # print(bitwise_operators.__name__)  # bitwise_operators
    # print(bin(42))  # 0b101010
    # print((42).bit_length())  # 6
    # a = bin(156)  # '0b10011100'
    # b = bin(52)  # '0b110100'
    # (a & b) = a x b
    res_and = 156 & 52
    res_or = 150 | 51
    res_shift_left = 15 << 2
    print('res_and:', res_and)  # 20 == 10100
    print('res_or:', res_or)  # 183 == 10110111
    print('res_shift_left:', res_shift_left)  # 15 == 1111, added two zeros 60 == 111100
    print(f"{42:032b}")  # Print 42 in binary on 32 zero-padded digits
    print(42 == 0b101010 == 0x2a == 0o52)  # True
    pprint(dir(dict))


def explore_f_string_with_colors():
    platform_python_version = platform.python_version()
    if platform_python_version < '3':
        print(f'Am I {id(platform_python_version)} joke to you? {100_500}????')
    elif platform_python_version < '3.8':
        print(Fore.RED + '\nUpgrade you \'Python\', bro!' + Style.RESET_ALL,
              Back.GREEN + f'New {platform_python_version} has cool features!' + Style.RESET_ALL)
    else:
        print(f'\n\tYou already know how deep is a rabbit hole, bro... ', sys.float_info.max,
              sep='\b-->\b', end=' yeah!\n')


def check_palindrome():
    importlib.import_module('check_palindrome')


def explore_scopes():
    item_list = [1, 2, 3, 5]

    def add_item_to_list(item):
        item_list.append(item)

    add_item_to_list(8)  # will work

    # Won't work
    # def add_item_to_list(item):
    #     item_list += [item]

    # Won't work. need use global keyword
    # counter = 0
    # def add_item_to_counter():
    #     counter += 1
    #
    # add_item_to_counter()


# TIP: Modify A List During Iteration
def modify_list_during_iteration():
    my_items = [1, 4, 6, 7, 9, 12, 15]
    for idx, el in enumerate(my_items):
        if not (el % 2):
            del my_items[idx]

    # [1, 4, 6, 7, 9, 12, 15]
    # [1, 6, 7, 9, 12, 15]
    # [1, 6, 7, 9, 12, 15]
    # [1, 6, 7, 9, 12, 15]
    # [1, 6, 7, 9, 15]

    #     case 2
    # my_items = [1, 4, 6, 7, 9, 12, 15]
    # for idx in range(len(my_items)):
    #     if not(my_items[idx] % 2):
    #         del my_items[idx]
    #
    # [1, 6, 7, 9, 15]
    # [1, 7, 9, 15]
    # [1, 7, 9, 15]
    # [1, 7, 9, 15]
    # IndexError: list index out of range

    # BETTER: is to use comprehension
    # my_items = [1, 4, 6, 7, 9, 12, 15]
    # my_items = [el for _, el in enumerate(my_items) if el % 2]
    # [1, 7, 9, 15]


# TIP: defaultdict vs dict
# history = {'stud_1': 5, 'stud_2': 4, 'stud_3': 4}
# biology = {'stud_1': 3, 'stud_2': 4, 'stud_3': 4}
# english = {'stud_1': 4, 'stud_2': 3, 'stud_3': 5}
#
#
# students_points = {}
# for sub in (history, biology, english):
#     for student, grade in sub.items():
#         if student not in students_points:
#             students_points[student] = []
#         students_points[student].append(grade)
#
#
# students_points['stud_4'] # KeyError: 'stud_4’
# {'stud_1': [5, 3, 4], 'stud_2': [4, 4, 3], 'stud_3': [4, 4, 5]}

# from collections import defaultdict
#
# history = {'stud_1': 5, 'stud_2': 4, 'stud_3': 4}
# biology = {'stud_1': 3, 'stud_2': 4, 'stud_3': 4}
# english = {'stud_1': 4, 'stud_2': 3, 'stud_3': 5}
#
#
# students_points = defaultdict(list)
# for sub in (history, biology, english):
#     for student, grade in sub.items():
#         students_points[student].append(grade)
#
#
#
#
# students_points['stud_4'] # []
# # defaultdict(<class 'list'>, {'stud_1': [5, 3, 4], 'stud_2': [4,4, 3],
#  'stud_3': [4, 4, 5]})

# TIP: List vs set
# lst1 = ['a', 'b', 'c', 'd']
# lst2 = ['b', 'd', 'f', 'l']
# lst3 = ['a', 'f', 'k', 'n']
#
# unique_element = []
# for lst in (lst1, lst2, lst3):
#     for el in lst:
#         if el not in unique_element:
#             unique_element.append(el)
# ['a', 'b', 'c', 'd', 'f', 'l', 'k', 'n']

# lst1 = ['a', 'b', 'c', 'd']
# lst2 = ['b', 'd', 'f', 'l']
# lst3 = ['a', 'f', 'k', 'n']
#
# unique_element = set(lst1 + lst2 + lst3)
# {'d', 'b', 'k', 'c', 'a', 'l', 'n', 'f'}

# TIP: Tuple vs namedtuple
# __problem

# animals = [
#     ('Vasya', 'cat', 'mammals', False, False),
#     ('Fred', 'frog', 'amphibians', True, False),
#     ('Kesha', 'parrot', 'birds', False, True),
#     ('Pepper', 'salmon', 'fish', True, False)
# ]
#
# for animal in animals:
#     print((animal[0], animal[1], animal[2], animal[3], animal[4]))

# __solution
from collections import namedtuple

# characteristics = [
#     'name', 'type', 'family_type', 'cold_blooded', 'can_fly’
# ]
# animals = [
#     ('Vasya', 'cat', 'mammals', False, False),
#     ('Fred', 'frog', 'amphibians', True, False),
#     ('Kesha', 'parrot', 'birds', False, True),
#     ('Pepper', 'salmon', 'fish', True, False)
# ]
#
#
# Animal = namedtuple('Animal', characteristics)
# # ----------------------------------------------------
# named_animals = [Animal(*animal) for animal in animals]
# # or
# named_animals = [Animal._make(animal) for animal in animals]
# # ----------------------------------------------------
# for animal in named_animals :
#     print(animal._asdict())

# TIP: Dictionary as an Alternative to If-Else

# __problem
# def search_tree_for_price_by_product_number(product_num):
#     if product_num >= 0 and product_num < 100:
#         price = 6575
#     elif product_num >= 100 and product_num < 200:
#         price = 343
#     elif product_num >= 200 and product_num < 300:
#         price = 52424
#     elif product_num >= 300 and product_num < 400:
#         price = 8424
#     elif product_num >= 400 and product_num < 500:
#         price = 1342
#     elif product_num >= 500 and product_num < 600:
#         price = 2144
#     elif product_num >= 600 and product_num < 700:
#         price = 342424
#     elif product_num >= 700 and product_num < 800:
#         price = 554
#     elif product_num >= 800 and product_num < 900:
#         price = 89
#     elif product_num >= 900 and product_num < 1000:
#         price = 144424
#     else:
#         price = 0
#     return price

# __solution
# def search_tree_for_price_by_product_number(product_num):
#     keys = [el for el in range(0, 1100, 100)]
#     values = [6575, 343, 52424, 8424, 1342, 2144, 342424, 554, 89, 144424]
#     price_dict = {(keys[i], keys[i+1]): values[i] for i in range(len(keys) - 1)}
#     for k, v in price_dict.items():
#         if product_num in range(*k):
#             return v
#     return 0

# TIP: The magic of itertools
# __problem
# predators = ["fox", "owl"]
# preys = ["rabbit", "mouse", "squirrel"]
#
# combimations = []
# for predator in predators:
# for prey in preys:
# combimations.append((predator, prey))
#
# [
# ('fox', 'rabbit'),
# ('fox', 'mouse'),
# ('fox', 'squirrel'),
# ('owl', 'rabbit'),
# ('owl', 'mouse'),
# ('owl', 'squirrel')
# ]

# __solution
# import itertools
# predators = ["fox", "owl"]
# preys = ["rabbit", "mouse", "squirrel"]
#
# combimations = list(itertools.product(predators, preys))
#
#
# [
# ('fox', 'rabbit'),
# ('fox', 'mouse'),
# ('fox', 'squirrel'),
# ('owl', 'rabbit'),
# ('owl', 'mouse'),
# ('owl', 'squirrel')
# ]

# __problem2
# numbers = [1, 3, 5, 7, 4, 9, 11, 12, 13, 15, 6]
# dropwhile = []
# for idx, numb in enumerate(numbers):
# if not numb%2:
# dropwhile = numbers[idx:]
# break
# [4, 9, 11, 12, 13, 15, 6]


# __solution_2
# import itertools
# numbers = [1, 3, 5, 7, 4, 9, 11, 12, 13, 15, 6]
# dropwhile = list(itertools.dropwhile(lambda x : x%2, numbers))

# [4, 9, 11, 12, 13, 15, 6]


# TIP: Pandas & numpy
# __problem
# rules = [
#     {'dealer': "AC", 'utility': "MP", 'product': "UC12", "tax": 0.1},
#     {'dealer': "AC", 'utility': "KL", 'product': "UC12", "tax": 0.15},
#     {'dealer': "AC", 'utility': None, 'product': "UC12", "tax": 0.20},
#     {'dealer': None, 'utility': None, 'product': "UC12", "tax": 0.25},
# ]
#
# filter_rule = {
#     "dealer": 'AC',
#     "utility": "not_exist",
#     'product': "UC12"
# }

# __solution

# import pandas as pd
# import numpy as np
#
#
# def filter_dataframe_by_column(rules_df, column):
#
#
#     rules_df = rules_df.loc[np.select(
#         [rules_df[column].isin([filter_rule[column]]).any()],
#         [rules_df[column] == filter_rule[column]], rules_df[column].isnull()
#     )]
# return rules_df
#
#
# def get_tax_from_rules(filter_rule):
#
#
#     rules_df = pd.DataFrame(rules)
# for col in ('utility', 'dealer'):
#     rules_df = filter_dataframe_by_column(rules_df, col)
# tax = rules_df['tax'].iloc[0]
# return tax
#
# print(get_tax_from_rules(filter_rule))
# # 0.2


# TIP: Catch any error
# Don’t catch any error. Always specify which exceptions you are prepared to recover from and only catch those.
# Try to avoid passing in except blocks. Unless explicitly desired, this is usually not a good sign.
# try:
#     # something
# except:
#     pass

# TIP: Test coverage
# - Coverage.py is a tool for measuring code coverage of Python programs. It monitors your program, noting which parts
# of the code have been executed, then analyzes the source to identify code that could have been executed but was not.
# - That exact # pragma: no cover is the hint that the part of code should be ignored by the tool.

if __name__ == '__main__':  # Runs main() if file wasn't imported.
    # explore_file_handling()
    # explore_data_types()
    # show_basic_operators()
    # show_comprehensions()
    # explore_builtins()
    # explore_control_flow()
    # unpacking_assignment()
    # bitwise_operators.__call__()
    # explore_f_string_with_colors()
    # check_palindrome()
    pass
