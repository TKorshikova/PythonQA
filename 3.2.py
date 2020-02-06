import random


def intersection_lists(count1, max1, count2, max2):
    # создаем два списка случайных чисел
    list1 = [random.randint(1, max1) for i in range(count1)]
    list2 = [random.randint(1, max2) for i in range(count2)]
    # список3 состоит из элементов, общих для списка1 и списка2
    list3 = list(set(list1) & set(list2))
    print(list3)

    # если общих элементов нет
    if len(list3) == 0:
        print("Совпадений нет")


inputCount1 = int(input("Введите количество элементов списка 1 : "))
inputMax1 = int(input("Введите максимальное число списка 1 : "))
inputCount2 = int(input("Введите количество элементов списка 2 : "))
inputMax2 = int(input("Введите максимальное число списка 2 : "))

intersection_lists(inputCount1, inputMax1, inputCount2, inputMax2)
