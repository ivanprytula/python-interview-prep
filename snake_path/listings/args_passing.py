def main():
    ln = [9001]
    print(f"Initial address of n: {id(ln)}")
    increment(ln)
    print(f"Final address of n: {id(ln)}")


def increment(x):
    print(f"Initial address of x: {id(x)}")
    x.extend([100, 200])
    x.pop()
    print(x)
    print(f"Final address of x.: {id(x)}")


main()
