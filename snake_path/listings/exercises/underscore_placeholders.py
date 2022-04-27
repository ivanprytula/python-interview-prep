# underscore can be put between triple zeros to denote thousands, billions etc.
num1 = 1_000_000_000
num2 = 10_000_000

total_sum = num1 + num2

print(f'{total_sum}')
print(f'{total_sum:,}')
print(f'{total_sum:.2f}')
