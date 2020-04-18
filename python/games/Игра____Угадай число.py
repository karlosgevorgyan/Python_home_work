import random

tries = 0
number = random.randint(1,10)
print("Угадай число до 6 раз....")
while tries < 3:
    guess = int(input('Введите число -'))
    tries += 1
    if guess < number:
        print("Число меньше...")
    if guess > number:
        print("Число больше...")
    if guess == number:
        print("Вы угадали число...")
        break
    if guess != number and tries == 3:
        print('Вы проиграли!!!')
        break