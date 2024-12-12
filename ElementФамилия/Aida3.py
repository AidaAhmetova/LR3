class ElementФамилия:
    def __init__(self, name, symbol, number):
        self.__name = name  # Приватный атрибут name
        self.__symbol = symbol  # Приватный атрибут symbol
        self.__number = number  # Приватный атрибут number

    @property
    def name(self):
        return self.__name  # Свойство для получения значения name

    @property
    def symbol(self):
        return self.__symbol  # Свойство для получения значения symbol

    @property
    def number(self):
        return self.__number  # Свойство для получения значения number

    def dump(self):
        print(f'Name: {self.name}')   # Используем свойство для получения name
        print(f'Symbol: {self.symbol}')  # Используем свойство для получения symbol
        print(f'Number: {self.number}')  # Используем свойство для получения number


# Создание объекта класса с данными для водорода
hydrogen = ElementФамилия("Hydrogen", "H", 1)

# Вывод информации об объекте с использованием метода dump
hydrogen.dump()