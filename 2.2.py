import random

a = random.randint(0,10)
b = random.randint(0,10)
c = random.randint(0,10)

if a > b:
    print("Я обожаю Питон")
elif a < b:
    print("Я ненавижу Питон")
else:
    print(c, "Теперь эта")

if a + b < c:
    print("Какое счастье!")
elif a + b > c:
    print("Какая печаль!")
else:
    print("Страдание")



