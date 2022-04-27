# def main():
#     n = 9001
#     print(f"Initial address of n: {id(n)}")
#     increment(n)
#     print(f"  Final address of n: {id(n)}")
#
#
# def increment(x):
#     print(f"Initial address of x: {id(x)}")
#     x += 1
#     print(f"  Final address of x: {id(x)}")
#
#
# main()
def some():
    for i in [1, 3, 'sds', 4, 5, ]:
        print(locals())
        print(globals())
        print(i)


print(locals())
print('dfdfdf---------------------------')
some()
