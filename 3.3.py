import random


def key_value(username, minimum, maximum):
    return {username: random.randint(minimum, maximum)}


user = str(input("Введите вашу фамилию : "))

print(key_value(user, 10000, 1000000))
