def personal_sum(numbers):  # Должна принимать коллекцию numbers.
    # присвоение переменным значений 0 перед вычислением
    result = 0
    incorrect_data = 0
    # цикл перебора значений numbers
    for i in numbers:
        # блок проверки на ошибки
        try:
            # вычисление суммы чисел в numbers
            result += i
        # блок подсчета ошибок типа данных
        except TypeError:
            # подсчет количества выявленных ошибок типов данных
            incorrect_data += 1
            print(f'Некорректный тип данных для подсчёта суммы - {i}')
    # возврат полученных результатов в виде кортежа
    return result, incorrect_data


def calculate_average(numbers):  # Должна принимать коллекцию numbers и возвращать: среднее арифметическое всех чисел.
    # блок проверки на ошибки вычислений
    try:
        # обращение за данными к функции personal_sum()(кортеж)
        per_sum = personal_sum(numbers)
        # подсчет среднего арифметического через индексы кортежа per_sum
        avg = per_sum[0] / (len(numbers) - per_sum[1])
        # возврат avg
        return avg
    # блок обработки ошибок деления на 0
    except ZeroDivisionError:
        return 0
    # блок обработки ошибок типа данных
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None


# print(f'Результат 0: {calculate_average([10, 'sTr', 15, 8, 33, "СтРоКа"])}')
print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать
