import random
import os
ask1 = "a"
while not ask1 == "+":
    ask1 = input("Привет, сыграем в игру?(+/-)" )
    if ask1 == "+":
        print("Тогда погнали")
    elif ask1 == "-":
        print("Ну ладно... 'зачем я это все писал...((('")
        exit()
    else:
        print("только плюс и минус, в чем проблема?")
        continue


while True:
    random_number1 = random.randint(1, 500)
    random_number2 = random.randint(501, 1000)
    random_number = random.randint(random_number1, random_number2)
    print("Попробуй отгадать цифру от", random_number1, "до", random_number2)
    number = input("Пускай будет: ")
    while not int(number) == random_number:

        if int(number) > random_number:
            print("Меньше")
            number = input("Еще раз: ")
        elif int(number) < random_number:
            print("Больше")
            number = input("Еще раз: ")
        else:
            print("ну только цифры, чего непонятного то((")


    print("Красавчик! Загаданное число равнялось ", random_number)

    ask = input("Хочешь продолжить?(+/-)")

    if ask == "+":
        print(" \n" * 100)
        print("Окей, по новой")
        continue
    elif ask == "-":
        print(" \n" * 100)
        print("Ладно, хорошо поиграли! Пока!)")
        break
    