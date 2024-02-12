class Guitar:
    def __init__(self, brand, model, year, color, strings, price):
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.__color = color
        self.__strings = strings
        self.__price = price

    def get_brand(self):
        return self.__brand

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    def get_color(self):
        return self.__color

    def get_strings(self):
        return self.__strings

    def get_price(self):
        return self.__price

    def set_brand(self, brand):
        self.__brand = brand

    def set_model(self, model):
        self.__model = model

    def set_year(self, year):
        self.__year = year

    def set_color(self, color):
        self.__color = color

    def set_strings(self, strings):
        self.__strings = strings

    def set_price(self, price):
        self.__price = price

    def __str__(self):
        return f"{self.__brand} {self.__model} {self.__color}, ({self.__strings}), ({self.__year}): ${self.__price}"

    def __eq__(self, other):
        if isinstance(other, Guitar):
            return self.__brand == other.get_brand() and \
                   self.__model == other.get_model() and \
                   self.__year == other.get_year() and \
                   self.__color == other.get_color() and \
                   self.__strings == other.get_strings() and \
                   self.__price == other.get_price()
        return False