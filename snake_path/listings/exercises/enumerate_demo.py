nice_words = ['Keep', 'The', 'Blue', 'Flag', 'Flying', 'High']

# for word in nice_words:
#     print(word)

# NB: Enumerate use in Pythonic way
for index, word in enumerate(nice_words, start=1):
    print(index, word)
