def add_everything_up(a, b):  # будет складывать числа(int, float) и строки(str)
    try:
        # возврат работы функции когда ошибки нет, суммы чисел с округлением до 3 знаков после запятой
        return round(a + b, 3)
    except TypeError:
        # возврат работы функции при разных типах входных данных
        return str(a) + str(b)


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
print(add_everything_up('Hello', 'Python'))
print(add_everything_up(15, 20))
