import math

class Shape:
    def __init__(self):
        pass

    @staticmethod
    def about():
        print("Программа разработана для вычисления объема конуса.")
        print("Команда разработки: AI Assistant Team")

class Cone(Shape):
    def __init__(self, radius, height):
        super().__init__()  # Вызов конструктора родительского класса
        self.__radius = radius  # Приватный атрибут радиуса
        self.__height = height  # Приватный атрибут высоты

    def volume(self):
        return (1/3) * math.pi * (self.__radius ** 2) * self.__height

    @staticmethod
    def about():
        print("Это класс для вычисления объема конуса.")

Shape.about()

try:
    radius = float(input("Введите радиус основания конуса: "))
    height = float(input("Введите высоту конуса: "))

    cone = Cone(radius, height)

    print(f"Объем конуса с радиусом {radius} и высотой {height} составляет: {cone.volume():.2f} кубических единиц.")
except ValueError:
    print("Пожалуйста, введите валидные числовые значения.")