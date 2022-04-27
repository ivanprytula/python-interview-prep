def get_function():
    print("inside get_function")

    def returned_function():
        print("inside returned_function")
        return 1

    print("outside returned_function")
    return returned_function


# returned_function()
x = get_function()
# print(x)
y = x()
print(y)



