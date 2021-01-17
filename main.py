import random


def thegame1():
    life = 100
    while True:
        random_number1 = random.randint(1, 50)
        random_number2 = random.randint(51, 100)
        random_number = random.randint(random_number1, random_number2)
        print("Попробуй отгадать цифру от", random_number1, "до", random_number2)
        number = input("Пускай будет: ")
        while not int(number) == random_number:
            if int(number) > random_number:
                print("Меньше")
                life -= 10
                print("Жизней осталось:", life)
                if life == 0:
                    print("Жизней не осталось! Ты проиграл((")
                    break
                number = input("Еще раз: ")
            elif int(number) < random_number:
                print("Больше")
                life -= 10
                print("Жизней осталось:", life)
                if life == 0:
                    print("Жизней не осталось! Ты проиграл((")
                    break
                number = input("Еще раз: ")
            else:
                print("ну только цифры, чего непонятного то((")

        print("Конец! Загаданное число равнялось ", random_number)
        ask = " "
        while not ask == "+":
            ask = input("Хочешь продолжить?(+,-)")
            if ask == "+":
                print(" \n" * 100)
                print("Окей, по новой")
                continue
            elif ask == "-":
                print(" \n" * 100)
                print("Ладно, хорошо поиграли! Пока!)")
                break
            else:
                print("особенный слишком? сказал же только + или -")
                continue
        break


def thegame2():
    life = 100
    while True:
        random_number1 = random.randint(1, 500)
        random_number2 = random.randint(501, 1000)
        random_number = random.randint(random_number1, random_number2)
        print("Попробуй отгадать цифру от", random_number1, "до", random_number2)
        number = input("Пускай будет: ")
        while not int(number) == random_number:
            if int(number) > random_number:
                print("Меньше")
                life -= 10
                print("Жизней осталось:", life)
                if life == 0:
                    print("Жизней не осталось! Ты проиграл((")
                    break
                number = input("Еще раз: ")
            elif int(number) < random_number:
                print("Больше")
                life -= 10
                print("Жизней осталось:", life)
                if life == 0:
                    print("Жизней не осталось! Ты проиграл((")
                    break
                number = input("Еще раз: ")
            else:
                print("ну только цифры, чего непонятного то((")

        print("Конец! Загаданное число равнялось ", random_number)
        ask = " "
        while not ask == "+":
            ask = input("Хочешь продолжить?(+/-)")
            if ask == "+":
                print(" \n" * 100)
                print("Окей, по новой")
                continue
            elif ask == "-":
                print(" \n" * 100)
                print("Ладно, хорошо поиграли! Пока!)")
                break
            else:
                print("особенный слишком? сказал же только + или -")
                continue
        break


def thegame3():
    while True:
        life = 100
        random_number1 = random.randint(1, 1000)
        random_number2 = random.randint(1001, 2000)
        random_number = random.randint(random_number1, random_number2)
        print("Попробуй отгадать цифру от", random_number1, "до", random_number2)
        number = input("Пускай будет: ")
        while not int(number) == random_number:
            if int(number) > random_number:
                print("Меньше")
                life -= 10
                print("Жизней осталось:", life)
                if life == 0:
                    print("Жизней не осталось! Ты проиграл((")
                    break
                number = input("Еще раз: ")
            elif int(number) < random_number:
                print("Больше")
                life -= 10
                print("Жизней осталось:", life)
                if life == 0:
                    print("Жизней не осталось! Ты проиграл((")
                    break
                number = input("Еще раз: ")
            else:
                print("ну только цифры, чего непонятного то((")

        print("Конец! Загаданное число равнялось ", random_number)
        ask = " "
        while not ask == "+":
            ask = input("Хочешь продолжить?(+/-)")
            if ask == "+":
                print(" \n" * 100)
                print("Окей, по новой")
                continue
            elif ask == "-":
                print(" \n" * 100)
                print("Ладно, хорошо поиграли! Пока!)")
                break
            else:
                print("особенный слишком? сказал же только + или -")
                continue
        break


ask1 = " "
while not ask1 == "+":
    ask1 = input("Привет, сыграем в игру?(+/-)")
    if ask1 == "+":
        print("Тогда погнали")
    elif ask1 == "-":
        print("Ну ладно... 'зачем я это все писал...((('")
        exit()
    else:
        print("только плюс и минус, в чем проблема?")
        continue

while True:
    level = input("Выбери уровень сложности (1 - легко, 2 - средне 3 - сложно, - - выйти из игры)")
    if level == "1":
        thegame1()
    elif level == "2":
        thegame2()
    elif level == "3":
        thegame3()
    elif level == "-":
        print("Ок, скоро увидимся, пока!")
        break
    else:
        print("1,2,3,-, в чем трабл?")
        continue
