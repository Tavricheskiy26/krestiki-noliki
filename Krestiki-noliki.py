field = list(range(1, 10))

win_cord = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]

player = "X", "O"

counter = 0


def draw_board():
    print("-------------")
    for i in range(3):
        print('|', field[0 + i * 3], '|', field[1 + i * 3], '|', field[2 + i * 3], '|')
        print("-------------")


def take_input(player):
    while True:
        value = input(f"Ваш ход мистер {player} ")
        if not (value in "123456789"):
            print("Промахнулись, повторите ход")
            continue
        value = int(value)
        if str(field[value - 1]) in "XO":
            print("Это клетка уже занята")
            continue
        field[value - 1] = player
        break


def check_win():
    for result in win_cord:
        if (field[result[0] - 1]) == (field[result[1] - 1]) == (field[result[2] - 1]):
            return True
    else:
        return False


def main():
    counter = 0
    while True:
        draw_board()
        if counter % 2 == 0:
            take_input('X')
        else:
            take_input('O')
        if check_win():
            print(f"Победа!!!")
            return True
        counter += 1
        if counter > 8:
            draw_board()
            print("Ничья")
            break


main()
