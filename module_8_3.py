"""Объявление класса ошибки IncorrectVinNumber наследуемый от Exception,
   объекты которого обладают атрибутом message"""


class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)  # обязательная строка


"""Объявление класса ошибки IncorrectCarNumbers наследуемый от Exception,
   объекты которого обладают атрибутом message"""


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)  # обязательная строка


class Car:  # объявление класса Car
    def __init__(self, model, vin, numbers):
        self.model = model  # Атрибут объекта model - название автомобиля (строка).
        # присвоение атрибуту self._vin значения vin при корректном номере
        if self.__is_valid_vin(vin):
            self.__vin = vin
        # присвоение атрибуту self._numbers значения numbers при корректном номере
        if self.__is_valid_numbers(numbers):
            self.__numbers = numbers

    def __is_valid_vin(self, vin_number):  # метод __is_valid_vin проверяет корректность vin
        # условие проверки vin_number на целочисленное значение
        if isinstance(vin_number, int) == False:
            # создание класса ошибки при несоответствии условию целочисленного значения
            raise IncorrectVinNumber('Некорректный тип vin номер')
        # условие проверки диапазона vin_number
        if not (1000000 <= vin_number <= 9999999):
            # создание класса ошибки при несоответствии условию диапазона vin_number
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        # возврат при корректном vin_number
        return True

    def __is_valid_numbers(self, numbers):  # метод __is_valid_numbers проверяет корректность numbers
        # условие проверки numbers соответствию строковому значению
        if isinstance(numbers, str) == False:
            # создание класса ошибки при несоответствии условию строкового значения
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        # условие проверки длинны numbers
        if len(numbers) != 6:
            # создание класса ошибки при несоответствии условию длины numbers
            raise IncorrectCarNumbers('Неверная длина номера')
        # возврат при корректном numbers
        return True


# исходные данные

try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')
