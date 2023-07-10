<!--
.. title: Show Me The Code
.. slug: show-me-the-code
.. date: 2022-04-27 11:23:57 UTC+03:00
.. type: text
-->

# Syntax - all in one

```python
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
  bar = foo.function_bar()
"""

# ####### 1. Standard Library imports
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

# fyi: Such import style will cause issues with built-in funcs -
#  if names match, they'll be overridden.
# from os import *

# ####### 3. your own packages
# import < model_name > from < models_package >

GRAVITATIONAL_CONSTANT: float = 9.81

# Write a full sentence in one-line comment with a period in the end.
multiline_comment = '''
  Not a Module docstring \t but comment assigned to variable.\n This will be
  a second line if printed.
  '''
```
