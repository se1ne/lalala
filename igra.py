import random

print("Добро пожаловать в автомат, дробовик, снайперка ")
def thegame():
    while True:
        weapon = input("Выберите пушку(1 - автомат, 2 - дробовик 3 - снайперка): ")
        if weapon == "1":
            print("Автомат? Неплохой выбор!")
        elif weapon == "2":
            print("Дробовик? Мощно!")
        elif weapon == "3":
            print("Снайперка? Глаз как у орла?)")
        else:
            print("Только 1 2 3")
            continue
        print("Выбираем пушку вашему сопернику...")
        random_weapon = random.randint(1, 3)
        ask1 = input("Готов?(просто +)")
        if ask1 == "+":
            continue
        else:
            break
        print(weapon)
        print(random_weapon)
        if random_weapon == int(weapon):
            print("Ничья, у вас были одинаковые пушки. Переигрываем")
        elif int(weapon) == 1 and random_weapon == 2:
            print("Увы, но противник выбрал дробовик, ты проиграл. Но ты можешь постараться еще раз")
            ask = input("Хочешь?(+,-)")
            if ask == "+":
                print("Окей, летс го")
                continue
            elif ask == "-":
                print("как хочешь(")
                quit()
            else:
                print("только + и -")
            break

thegame()