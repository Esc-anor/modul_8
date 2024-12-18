module_8_1
    Домашнее задание по уроку "Try и Except".
    
    Задание "Программистам всё можно":
    Пора разрушать шаблоны привычного нам Python! Вот вас раздражает, что мы не можем сложить число(int) и строку(str)? Давайте исправим это недоразумение!
    
    Реализуйте следующую функцию:
    add_everything_up, будет складывать числа(int, float) и строки(str)
    
    Описание функции:
    add_everything_up(a, b) принимает a и b, которые могут быть как числами(int, float), так и строками(str).
    TypeError - когда a и b окажутся разными типами (числом и строкой), то возвращать строковое представление этих двух данных вместе (в том же порядке). Во всех остальных случаях выполнять стандартные действия.
    
    Пример кода:
    print(add_everything_up(123.456, 'строка'))
    print(add_everything_up('яблоко', 4215))
    print(add_everything_up(123.456, 7))
    
    Вывод в консоль:
    123.456строка
    яблоко4215
    130.456
    
    Примечания:
    Конструкции try-except в функции выполняют строго ту обработку, которая написана в задании (обращайте на важность порядка передачи данных).
    Если хотите дополнить функции своими исключениями или написать отдельно дополнительно собственные функции - это не запрещено, мы не против, чтобы вы больше экспериментировали. Но в первую очередь выполните поставленную задачу.

module_8_2
    Цель: понять как работают исключения внутри функций и как обрабатываются эти исключения на практике при помощи try-except.
    
    Задача "План перехват":
    Напишите 2 функции:
    Функция personal_sum(numbers):
    Должна принимать коллекцию numbers.
    Подсчитывать сумму чисел в numbers путём перебора и увеличивать переменную result.
    Если же при переборе встречается данное типа отличного от числового, то обработать исключение TypeError, увеличив счётчик incorrect_data на 1.
    В конечном итоге функция возвращает кортеж из двух значений: result - сумма чисел, incorrect_data - кол-во некорректных данных.
    Функция calculate_average(numbers)
    Среднее арифметическое - сумма всех данных делённая на их количество.
    Должна принимать коллекцию numbers и возвращать: среднее арифметическое всех чисел.
    Внутри для подсчёта суммы используйте функцию personal_sum написанную ранее.
    Т.к. коллекция numbers может оказаться пустой, то обработайте исключение ZeroDivisionError при делении на 0 и верните 0.
    Также в numbers может быть записана не коллекция, а другие типы данных, например числа. Обработайте исключение TypeError выводя строку 'В numbers записан некорректный тип данных'. В таком случае функция просто вернёт None.
    
    Пункты задачи:
    Создайте функцию personal_sum на основе условий задачи.
    Создайте функцию calculate_average на основе условий задачи.
    Вызовите функцию calculate_average несколько раз, передав в неё данные разных вариаций.
    Пример результата выполнения программы:
    Пример выполнения программы:
    print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
    print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
    print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
    print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать
    
    Вывод на консоль:
    Некорректный тип данных для подсчёта суммы - 1
    Некорректный тип данных для подсчёта суммы - ,
    Некорректный тип данных для подсчёта суммы -
    Некорректный тип данных для подсчёта суммы - 2
    Некорректный тип данных для подсчёта суммы - ,
    Некорректный тип данных для подсчёта суммы -
    Некорректный тип данных для подсчёта суммы - 3
    Результат 1: 0
    Некорректный тип данных для подсчёта суммы - Строка
    Некорректный тип данных для подсчёта суммы - Ещё Строка
    Результат 2: 2.0
    В numbers записан некорректный тип данных
    Результат 3: None
    Результат 4: 26.5

module_8_3
    Цель: освоить навык создания пользовательских исключений и использовать его в решении задачи. Повторить тему ООП и принцип инкапсуляции.
    
    Задача "Некорректность":
    
    Создайте 3 класса (2 из которых будут исключениями):
    Класс Car должен обладать следующими свойствами:
    Атрибут объекта model - название автомобиля (строка).
    Атрибут объекта __vin - vin номер автомобиля (целое число). Уровень доступа private.
    Метод __is_valid_vin(vin_number) - принимает vin_number и проверяет его на корректность. Возвращает True, если корректный, в других случаях выбрасывает исключение. Уровень доступа private.
    Атрибут __numbers - номера автомобиля (строка).
    Метод __is_valid_numbers(numbers) - принимает numbers и проверяет его на корректность. Возвращает True, если корректный, в других случаях выбрасывает исключение. Уровень доступа private.
    Классы исключений IncorrectVinNumber и IncorrectCarNumbers, объекты которых обладают атрибутом message - сообщение, которое будет выводиться при выбрасывании исключения.
    
    Работа методов __is_valid_vin и __is_valid_numbers:
    __is_valid_vin
    Выбрасывает исключение IncorrectVinNumber с сообщением 'Некорректный тип vin номер', если передано не целое число. (тип данных можно проверить функцией isinstance).
    Выбрасывает исключение IncorrectVinNumber с сообщением 'Неверный диапазон для vin номера', если переданное число находится не в диапазоне от 1000000 до 9999999 включительно.
    Возвращает True, если исключения не были выброшены.
    __is_valid_numbers
    Выбрасывает исключение IncorrectCarNumbers с сообщением 'Некорректный тип данных для номеров', если передана не строка. (тип данных можно проверить функцией isinstance).
    Выбрасывает исключение IncorrectCarNumbers с сообщением 'Неверная длина номера', переданная строка должна состоять ровно из 6 символов.
    Возвращает True, если исключения не были выброшены.
    
    ВАЖНО!
    Методы __is_valid_vin и __is_valid_numbers должны вызываться и при создании объекта (в __init__ при объявлении атрибутов __vin и __numbers).
    
    Пример результата выполнения программы:
    Пример выполняемого кода:
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
    Вывод на консоль:
    Model1 успешно создан
    Неверный диапазон для vin номера
    Неверная длина номера
    
    Примечания:
    Для выбрасывания исключений используйте оператор raise
