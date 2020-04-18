number_of_sticks = 10
player_turn = 1

# while number_of_sticks > 0:
#     print('Сколко палочек вы берете?')
#     taken = int(input())
#
#     if taken < 1 or taken > 3:
#         print(f'Вы хотели взять {taken}. Но разрещено 1,2,3 полочек.')
#         continue
#     number_of_sticks -= taken
#     print(f'Вы взяли {taken}\n')
#
#     if number_of_sticks <= 0:
#         print(f'Полочек больше нету.\n{player_turn} игрок проиграл!!!')
#         break
#
#     player_turn = 1 if player_turn == 2 else 2


def can_take(sticks_taken,remaining_sticks):  # Количество полочек
    return 1 <= sticks_taken <= 3 and sticks_taken <= remaining_sticks


def switch_player_turn(turn):  # Переключенние очереди
    return 1 if turn == 2 else 2


def end_of_game(sticks):  # Конец игры
    return sticks <= 0


while not end_of_game(number_of_sticks):
    print(f'Сколко палочек вы берете? Remaining{number_of_sticks}')
    taken = int(input())

    if not can_take(taken, number_of_sticks):
        if taken > number_of_sticks:
            print('Вы пытались взять больше, чем на столе')
        else:
            print(f'Вы хотели взять {taken}. Но разрещено 1,2,3 полочек.')
        continue
    number_of_sticks -= taken
    print(f'Вы взяли {taken}\n')

    if end_of_game(number_of_sticks):
        print(f'Полочек больше нету.\n{player_turn} игрок проиграл!!!')
        break

    player_turn = switch_player_turn(player_turn)


class Character:
    def __init__(self, armor: int, power: int):
        self.power = power
        self.armor = armor
        self.health = 10

    def hit(self, damage)-> bool:
        self.health -= damage

    def is_alive(self):
        return self.health > 0

c1 = Character(10, 20)
c1.hit(30)