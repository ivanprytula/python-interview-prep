r"""
Python Regular Expression Quick Guide

^        Matches the beginning of a line
$        Matches the end of the line
.        Matches any character
\s       Matches whitespace
\S       Matches any non-whitespace character
*        Repeats a character zero or more times
*?       Repeats a character zero or more times
         (non-greedy)
+        Repeats a character one or more times
+?       Repeats a character one or more times
         (non-greedy)
[aeiou]  Matches a single character in the listed set
[^XYZ]   Matches a single character not in the listed set
[a-z0-9] The set of characters can include a range
(        Indicates where string extraction is to start
)        Indicates where string extraction is to end
"""

import re

text_line = 'My 2 favorite numbers are 19 and 42'
# + means 'one or more times'
found_numbers = re.findall(r'[0-9]+', text_line)
absent_substring = re.findall(r'[AEIOU]', text_line)
print(found_numbers)
print(absent_substring)

# Warning: Greedy Matching
# The repeat characters (* and +) push outward in both directions
# (greedy) to match the largest possible string
text_line_2 = 'From: Using the : character'
found_numbers_2 = re.findall(r'^F.+:', text_line_2)
print(found_numbers_2)  # -> ['From: Using the :']

# Non-Greedy Matching
# Not all regular expression repeat codes are greedy!
# If you add a "?" character, the + and * chill out a bit...
found_numbers_2 = re.findall(r'^F.+?:', text_line_2)
print(found_numbers_2)  # -> ['From:']

# Fine-Tuning String Extraction
# \S+ - at least one non-whitespace character
str_with_email = "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
found_numbers_3 = re.findall(r'\S+@\S+', str_with_email)
print(found_numbers_3)  # -> ['stephen.marquard@uct.ac.za']

# Parentheses are not part of the match - but they tell where
# to start and stop what string to extract
found_numbers_4 = re.findall(r'^From (\S+@\S+)', str_with_email)
print('found_numbers_4:', found_numbers_4)

# [^ ] - means "everything except blank"
found_numbers_5 = re.findall(r'@([^ ]*)', str_with_email)
print('found_numbers_5:', found_numbers_5)  # -> ['uct.ac.za']

# even cooler/refined regex version: extract only from the line which starts with
# "From ..."
# like "if" statement
found_numbers_6 = re.findall(r'^From .*@([^ ]*)', str_with_email)
print('found_numbers_6:', found_numbers_6)  # -> ['uct.ac.za']

# Escape Character
cookies_str = 'We just received $10.00 for cookies.'
cookies_match_all = re.findall(r'\$[0-9.]+', cookies_str)
print('cookies_match_all', cookies_match_all)  # ['$10.00']
