import cProfile
import sys
from datetime import datetime

a = []
before = datetime.now()
for _ in range(10_000_000):
    a.append(_)
print(sys.getsizeof(a), 'bytes')
after = datetime.now()
print(f'Elapsed time = {after - before}')

print('---------------------------------------------------')

before = datetime.now()
new_list_lc = [_ for _ in range(10_000_000)]
print(sys.getsizeof(new_list_lc), 'bytes')
after = datetime.now()
print(f'Elapsed time = {after - before}')

print('---------------------------------------------------')

before = datetime.now()
new_list_gc = (_ for _ in range(10_000_000))
print(sys.getsizeof(new_list_gc), 'bytes')
after = datetime.now()
print(f'Elapsed time = {after - before}')

cProfile.run('sum(a)')
cProfile.run('sum([_ for _ in range(10_000_000)])')
cProfile.run('sum((_ for _ in range(10_000_000)))')
