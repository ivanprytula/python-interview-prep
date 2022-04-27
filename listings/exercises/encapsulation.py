class Computer:

    def __init__(self):
        self.__maxprice = 800

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price


c = Computer()
c.sell()

# change the price
c._Computer__maxprice = 1000
c.sell()

# using setter function
c.setMaxPrice(2500)
c.sell()
