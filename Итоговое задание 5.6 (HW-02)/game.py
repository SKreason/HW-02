# Итоговое задание 5.6 (HW-02)

# данные поля
board = [["-"] * 3 for i in range(3)]


# вывод игрового поля
def board_output(data):
    print()
    print("  X| 0 | 1 | 2 |")
    print(" Y |---+---+---|")
    for y_coord, x_coord in enumerate(data):
        line = f" {y_coord} | {' | '.join(x_coord)} | "
        print(line)
        print(" --+---+---+---+")
    print()


# Ввод координат для хода
def input_coord():
    while True:
        # Запрашиваем по очереди координаты
        x_input = input("\nВедите номер столбца: ")
        y_input = input("Ведите номер строки: ")
        if not (x_input.isdigit()) or not (y_input.isdigit()):  # 1 проверка - на ввод только цифр
            print("\nНужно вводить только целые цифры!\nПопробуйте снова!")
            continue
        x, y = int(x_input), int(y_input)  # преобразуем ввод в целые числа
        if 0 > x or x > 2 or 0 > y or y > 2:  # 2 проверка на диапазон
            print("\nВведены неверные координаты! \nПопробуйте снова!")
            continue
        if board[y][x] != "-":  # 3 проверка на свободную ячейку
            print("\nПоле занято!\nВведите другие координаты")
            continue
        return x, y


def check_win():
    # проверка по горизонтали
    for y_coord_win in range(3):
        combination = []
        for x_coord_win in range(3):
            combination.append(board[y_coord_win][x_coord_win])
        if combination == ["X", "X", "X"]:
            print("""Победил игрок "X" \n Поздравляю!""")
            return True
        if combination == ["O", "O", "O"]:
            print("""Победил игрок "O" \n Поздравляю!""")
            return True
    # проверка по вертикали
    for x_coord_win in range(3):
        combination = []
        for y_coord_win in range(3):
            combination.append(board[y_coord_win][x_coord_win])
        if combination == ["X", "X", "X"]:
            print("""Победил игрок "X" \n Поздравляю!""")
            return True
        if combination == ["O", "O", "O"]:
            print("""Победил игрок "O" \n Поздравляю!""")
            return True
    # проверка диагонали 1
    combination = []
    for coord_win in range(3):
        combination.append(board[coord_win][coord_win])
    if combination == ["X", "X", "X"]:
        print("""Победил игрок "X" \n Поздравляю!""")
        return True
    if combination == ["O", "O", "O"]:
        print("""Победил игрок "O" \n Поздравляю!""")
        return True
    # проверка диагонали 2
    combination = []
    for coord_win in range(3):
        combination.append(board[2 - coord_win][coord_win])
    if combination == ["X", "X", "X"]:
        print("""Победил игрок "X" \n Поздравляю!""")
        return True
    if combination == ["O", "O", "O"]:
        print("""Победил игрок "O" \n Поздравляю!""")
        return True


def start():
    print("""Добро пожаловать в игру "Крестики - нолики"\nИгроки ходят по очереди.\n""")
    command_start = input("""Ведите "yes" чтобы начать игру \n """)
    if command_start == "yes":
        return True
    else:
        print("До свидания!")


if start():
    for step in range(9):
        step += 1
        board_output(board)
        print(f"Ход {step}")
        if step % 2 == 0:
            print("""Ход игрока "O" !""")
            x, y = input_coord()
            board[y][x] = "O"
        if step % 2 != 0:
            print("""Ход игрока "X"!""")
            x, y = input_coord()
            board[y][x] = "X"
        if check_win():
            break
        if step == 9:
            print("Ничья!")
