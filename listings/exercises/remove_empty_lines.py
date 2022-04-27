# list_with_empty_lines = [1, [], 2, [], 3, [], 4, [], 5, [], ]

empty_lines_list = ['', '', 'abc', '', 'def', 'ghi', '']


def check_is_empty(line):
    return bool(line)


filtered_list = [line for line in empty_lines_list if check_is_empty(line)]

print(empty_lines_list)
print(filtered_list)
