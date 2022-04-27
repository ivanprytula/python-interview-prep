# import os

# Cause issues with functions which have been overridden.
from os import *

rename('some_filename.txt', 'new_name.txt')
