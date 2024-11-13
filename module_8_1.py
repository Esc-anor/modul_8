def add_everything_up(a, b):  # будет складывать числа(int, float) и строки(str)
    # блок try проверки работы кода на ошибки и если ошибки нет, вернет result
    try:
        # условие проверки, что a и b - числа
        if (isinstance(a, (int, float))) is True and (isinstance(b, (int, float))) is True:
            # присвоение переменной result суммы чисел с округлением до 3 знаков после запятой
            result = round(a + b, 3)
        else:
            result = a + b
        # возврат работы функции когда ошибки нет
        return result
    # блок except вернет строковое значение в случае разных типов переменных на входе
    except TypeError:
        # присвоение переменной result строковых значений суммы a, b
        result = (str(a) + str(b))
        # возврат работы функции при разных типах входных данных
        return result


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
print(add_everything_up('Hello', 'Python'))
print(add_everything_up(15, 20))
