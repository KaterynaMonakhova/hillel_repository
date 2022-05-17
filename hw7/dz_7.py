class Vehicle:
    def __init__(self, color, model, year, price):
        self.__color = color
        self.__model = model
        self.__year = year
        self.__price = price

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, col):
        self.__color = col

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, m):
        self.__model = m

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, y):
        self.__year = y

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price


    def info(self):
       print("Vehicle")
       print("Color: " + str(self.__color))
       print("Model: " + str(self.__model))
       print("Year: " + str(self.__year))
       print('Price - ', self.__price)

class Car(Vehicle):
    def __init__(self, color, model, year, price, body):
        super().__init__(color, model, year, price)
        self.__body = body

    @property
    def body(self):
        return self.__body

    @body.setter
    def body(self, b):
        self.__body = b

    def info(self):
        print("Car")
        print("Color: " + str(self.color))
        print("Model: " + str(self.model))
        print("Year: " + str(self.year))
        print("Price: " + str(self.price))
        print("Body: " + str(self.body))

class Bus(Vehicle):
    def __init__(self, color, model, year, price, seats):
        super().__init__(color, model, year, price)
        self.__seats = seats

    @property
    def seats(self):
        return self.__seats

    @seats.setter
    def seats(self, s):
        self.__seats = s

    def info(self):
        print("Bus")
        print("Color: " + str(self.color))
        print("Model: " + str(self.model))
        print("Year: " + str(self.year))
        print("Price: " + str(self.price))
        print("Seats: " + str(self.seats))

result = Vehicle("red", "Sedan", 2018, 10000)
result.info()
result2 = Car("blue", "audi", 2008, 20000, "sedan")
result2.info()
result3 = Bus("green", "mercedes", 2010, 70000, 30)
result3.info()



