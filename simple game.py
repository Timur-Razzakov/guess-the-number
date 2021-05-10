import random

print("Игра 'Угадай число'\n")

i = random.randint(1, 100)  # указываем диапазон
user_num = 0  # число пользователя
cnt = 0  # количество попыток за которое угадает пользователь
name = input('Как тебя зовут?')
print(f'Привет  {name}!')

print('Я загадал число от 1 до 100. Тебе нужно угадать его!')
while True:
    try: 
        user_num = int(input("Введи число:"))
        cnt += 1  # cnt = cnt + 1
        if user_num == i:
            print(f"Поздравляем. Ты угадали число!!! за {cnt} попыток")
            if input('Может ещё раз? " Да|Нет ":') == 'Да':
                print("Ты мне нравишься всё больше и больше;)")
                i = random.randint(1, 100)
                cnt = 0
            else:
                print("ЭЭх, а жаль! )=")
                break
        elif user_num > i:
            print(f'Моё число меньше.')
        else:
            print("Моё число больше")
    except Exception:
        print("Вводить можно только целые числа!!")
