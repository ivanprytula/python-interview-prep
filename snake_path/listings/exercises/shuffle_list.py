from random import shuffle

moto_words = ['Keep', 'The', 'Blue', 'Flag', 'Flying', 'High']
print(f'Original list: {moto_words}; id == {id(moto_words)}')
shuffle(moto_words)
print(f'Shuffled list: {moto_words}; id == {id(moto_words)}')
