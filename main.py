import random


def thegame(d_from, d_to, n_1):
    """

    :param d_from: число до которого будет создаватся первое число, и +1 от какого второе
    :param d_to: число до которого будет создаватся второе число
    :param n_1: расстояние между числами которое недопустимо, будет увеличено в 3 раза
    :return:
    """
    life = 100
    while True:

        random_number1 = random.randint(1, d_from)
        random_number2 = random.randint(d_from+1, d_to)
        print(random_number1, random_number2)

        if random_number2 - random_number1 <= n_1:
            print("числа маленькие, увеличиваю...")
            random_number1 -= n_1
            random_number2 += n_1
        random_number = random.randint(random_number1, random_number2)
        print("Попробуй отгадать цифру от", random_number1, "до", random_number2)
        number = input("Пускай будет: ")
        while not int(number) == random_number:
            if int(number) < random_number1:
                print("Ну тебе же написано что минимальное", random_number1)
            elif int(number) > random_number2:
                print("Ну тебе же написано, что максимальное", random_number2)
            elif int(number) > random_number:
                print("Меньше")
                life -= 0
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
        thegame(50, 100, 20)
    elif level == "2":
        thegame(500, 1000, 200)
    elif level == "3":
        thegame(1000, 2000, 400)
    elif level == "-":
        print("Ок, скоро увидимся, пока!")
        break
    else:
        print("1,2,3,-, в чем трабл?")
        continue













