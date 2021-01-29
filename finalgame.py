import random
play_game = True
while play_game:
    number_from = random.randint(1, 100)
    distance = random.randint(30, 40)
    if number_from < 1:
        number_to = number_from + distance
    else:
        number_to, number_from = number_from, number_from - distance
    random_number = random.randint(number_from, number_to)
    print(f"\nЗагаданно целое число от {number_from} до {number_to}")
    print("Попробуйте отгадать")
    print("С каждой попыткой здоровье меняется")
    health = 100
    is_guessed = False
    while not is_guessed and health > 0:
        health_text = f"Здоровье: {health}"
        delimiter = "*" * len(health_text)
        print(delimiter)
        print(health_text)
        print(delimiter)
        number = ""
        number_is_digit = False
        while not number_is_digit:
            number = input(f"Введите целое число в диапозоне от {number_from} до {number_to}:")
            number_is_digit = number.isdigit()
            if not number_is_digit:
                print("Ошибка. Это не число.", end=" ")
            elif int(number) > number_to or int(number) < number_from:
                print("Ошибка. Число вне диапазона.", end=" ")
                number_is_digit = False
        number = int(number)
        if number != random_number:
            if number > random_number:
                print(f"Загаданное число меньше {number}",)
            else:
                print(f"Загаданное число больше {number}",)
            interval = abs(number - random_number)
            if interval < 3:
                if health <= 93:
                    health += 5
                    print("Очень горячо. +5 к здоровью")
                else:
                    print("Очень горячо.")
            elif interval < 10:
                print("Горячо.")
            elif interval < 15:
                health -= 10
                print("Холодноватенько")
            else:
                print("Мороз. Бррр")
                health -= 20
            if health <= 0:
                print(delimiter)
                print("Долгий путь ты прожил. Но... Наступила смерть")
                print(delimiter)
        else:
            is_guessed = True
            print(delimiter)
            print(f"Ну что ж, победа! Загаданоое число равнялось: {random_number}")

    else:
        print("Игра окончена.")
        print(delimiter)
        if input("ENTER - сыграть снова, 0 - выход")== 0:
            play_game = False
        else:
            is_guessed = False
print("Ну что ж, до встречи! Пока!")