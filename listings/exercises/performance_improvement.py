from timeit import timeit

# TIP 1: range(len(list)) vs Enumerate(list)
animals = ['lizard', 'cat', 'dog', 'snake', 'frog', 'mouse']
rr = timeit(f"""result = [i for i in range(len({animals}))]""", number=10_000_000)
print(rr)
# 3.934364941998865

rr2 = timeit(f"""result = [(i, el) for i, el in enumerate({animals})]""", number=10_000_000)
print(rr2)
# 5.38475575099983

# TIP 1.1: But in case where we need only indexes, the enumarate works faster.
timeit(f"""result = [i for i in range(len({animals}))]""", number=10_000_000)
# 5.1784939990000005
timeit(f"""result = [i for i, _ in enumerate({animals})]""", number=10_000_000)
# 5.061018913999999

timeit(f"""result = [i for i in range(len({animals}))]""", number=1_000_000_000)
# 522.119624852
timeit(f"""result = [i for i, _ in enumerate({animals})]""", number=1_000_000_000)
# 515.48873659

# TIP 2: Create list by List comrehension or by range
timeit("""n = [x for x in range(10)]""", number=10000000)
# 5.0356921020000005

timeit("""n = list(range(10))""", number=10000000)
# 3.0431294699999993

# TIP 3: concatenate multiple dictionaries
cat = {'Vasya': {'type': 'cat', 'family_type': 'mammals'}}
frog = {'Fred': {'type': 'frog', 'family_type': 'amphibians'}}
parrot = {'Kesha': {'type': 'parrot', 'family_type': 'birds'}}
salmon = {'Pepper': {'type': 'salmon', 'family_type': 'fish'}}

# {
# 'Pepper': {'type': 'salmon', 'family_type': 'fish'},
# 'Kesha': {'type': 'parrot', 'family_type': 'birds'},
# 'Fred': {'type': 'frog', 'family_type': 'amphibians'},
# 'Vasya': {'type': 'cat', 'family_type': 'mammals'}
# }

# solution 1
animals_one = {}
animals_one.update(cat)
animals_one.update(frog)
animals_one.update(parrot)
animals_one.update(salmon)

# solution 2. better
from collections import ChainMap

animals_two = dict(ChainMap(cat, frog, parrot, salmon))

# solution 3. better-better
animals_three = {**cat , **frog, **parrot, **salmon}

# solution 4. better-better-better
animals_four = cat | frog | parrot | salmon



