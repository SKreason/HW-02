# def print_GameBoard():
#     for x in range(3):
#         print("\n+---+---+---+")
#         print("|", end="")
#         for y in range(3):
#             print("", gameBoard[x][y], end=" |")
#     print("\n+---+---+---+")
#
# gameBoard = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print_GameBoard()

# def show():
#     print()
#     print("     0  1  2  ")
#     # print("  --------------- ")
#     for i, row in enumerate(data_field):
#         row_str = f"  {i}  {'  '.join(row)}  "
#         print(row_str)
#         # print("  --------------- ")
#     print()
#
# # field = [[" "] * 3 for i in range(3) ]
# data_field = [["-", "-", "-"] for i in range(3)]
# show()

# def ask():
#     while True:
#         cords = input("         Ваш ход: ").split()
#
#         if len(cords) != 2:
#             print(" Введите 2 координаты! ")
#             continue
#
#         x, y = cords
#
#         if not (x.isdigit()) or not (y.isdigit()):
#             print(" Введите числа! ")
#             continue
#
#         x, y = int(x), int(y)
#
#         if 0 > x or x > 2 or 0 > y or y > 2:
#             print(" Координаты вне диапазона! ")
#             continue
#
#         if field[x][y] != " ":
#             print(" Клетка занята! ")
#             continue
#
#         return x, y
# ask()
# print(cords)
# print(x)
# print(y)

pole = [["-"] * 3] * 3
pole1 = [["-"] * 3 for i in range(3) ]
pole2 = [["-", "-", "-"]] * 3
pole3 = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
print(pole)
print(pole1)
print(pole2)
print(pole3)
print()
pole[1][1] = "O"
pole1[1][1] = "O"
pole2[1][1] = "O"
pole3[1][1] = "O"
print(pole)
print(pole1)
print(pole2)
print(pole3)
