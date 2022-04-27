import re
file_name = input('Enter file: ')
try:
    if len(file_name) < 1:
        file_name = 'test.md'
    handle = open(file_name)
except IOError:
    print('File cannot be opened:', file_name)
    quit()

counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        word = word.strip('.,')
        counts[word] = counts.get(word, 0) + 1
handle.close()

# Option 1
big_count = None
big_word = None
for word, count in counts.items():
    if big_count is None or count > big_count:
        big_word = word
        big_count = count

print(f'Word "{big_word}" has {big_count} count.')


# Option 2: one-liner
# words_with_max_counts = {k: v for k, v in counts.items() if v == max(counts.values())}
# print('words_with_max_counts:', words_with_max_counts)

# Playground cases
# sorted_counts = {k: v for k, v in sorted(counts.items(), key=lambda item: item[1])}
# sorted_counts = collections.OrderedDict(counts)

# Any number of spaces is valid. But convention/PEP 8 says that the indentation needs to be multiple of four
# for _ in range(5):
#  print('spam eggs')
