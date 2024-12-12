class ElementФамилия:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

    def dump(self):
        print(f'Name: {self.name}')
        print(f'Symbol: {self.symbol}')
        print(f'Number: {self.number}')

# Создание объекта класа с данными для водорода
hydrogen = ElementФамилия("Hydrogen", "H", 1)

# Вывод информации об объекте с использованием метода dump
hydrogen.dump()