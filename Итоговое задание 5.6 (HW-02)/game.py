# Итоговое задание 5.6 (HW-02)

# данные поля
pole = [["-"] * 3 for i in range(3)]
print(pole)


# функция вывода поля
def out_pole():
    print()
    print("   X| 0 | 1 | 2 |")
    print("  Y |---+---+---|")
    for vert, horiz in enumerate(pole):
        stroka = f"  {vert} | {' | '.join(horiz)} | "
        print(stroka)
        print("  --+---+---+---+")
    print()


out_pole()
x = int(input("Ведите номер столбца: "))
y = int(input("Ведите номер строки: "))

print(x, y)
pole[x][y] = "O"
# pole[1][1] = "O"
print(pole)
out_pole()
