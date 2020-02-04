# импорт всегда первый
import random


# Создаем список с заданными параметрами
def create_list(count, maximum):
    # возвращаем список от 1 до заданного числа с заданным количеством элементов
    return [random.randint(1, maximum) for i in range(count)]


# пользователь вводит количество элементов
inputCount = int(input("Введите количество элементов списка : "))
# пользователь вводит максимальное число в списке
inputMaximum = int(input("Введите максимальное число : "))

# вывести список
print(create_list(inputCount, inputMaximum))
