class ElementФамилия:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

    def __str__(self):
        return f'Element: {self.name}, Symbol: {self.symbol}, Number: {self.number}'

# Создание объекта класса с данными для водорода
hydrogen = ElementФамилия("Hydrogen", "H", 1)

# Вывод информации об объекте
print(hydrogen)