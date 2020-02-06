import random


def key_value(username, minimum, maximum):
    return {user: random.randint(minimum, maximum)}


user = str(input("Введите вашу фамилию : "))

print(key_value(user, 10000, 1000000))
