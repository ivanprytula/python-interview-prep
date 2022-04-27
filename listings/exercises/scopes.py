class TestScopes:
    var1 = 'string'
    var2 = 24
    var3 = 3.14

    # __dict__ = {1: 'a'}

    @staticmethod
    def get_some():
        print(5 * 2)
        return 100


test_ob = TestScopes()


# help(test_ob.get_some())


print(dir(test_ob))
print('--------------')
print(dir())
print('++++++++++++++++++++++=')
print(test_ob.__dir__())
