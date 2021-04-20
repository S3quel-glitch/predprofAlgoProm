mine1 = []
mine2 = []
mine3 = []
mine4 = []
mine5 = []

# READING FILE
with open("Ершов_2.txt") as file:
    data = file.readlines()

for line in data:
    mine1.append(line.split(" ")[0])
    mine2.append(line.split(" ")[1])
    mine3.append(line.split(" ")[2])
    mine4.append(line.split(" ")[3])
    mine5.append(line.split(" ")[4])


# Средняя производительность в год
# Округлено до сотых
def midMineYear(mine):
    mid = 0
    for x in range(0, len(mine1)):
        mid += int(mine[x])
    mid = mid / len(mine1)
    return round(mid, 2)


def efficientIn3months(mine1, mine2, mine3, mine4, mine5):
    # MINE 1
    total = 0
    totals1 = []
    for x in range(0, 3):
        total += int(mine1[x])
    totals1.append(total)
    total = 0
    for x in range(3, 6):
        total += int(mine1[x])
    totals1.append(total)
    total = 0
    for x in range(6, 9):
        total += int(mine1[x])
    totals1.append(total)
    total = 0
    for x in range(9, 12):
        total += int(mine1[x])
    totals1.append(total)
    total = 0

    # MINE 2
    total = 0
    totals2 = []
    for x in range(0, 3):
        total += int(mine2[x])
    totals2.append(total)
    total = 0
    for x in range(3, 6):
        total += int(mine2[x])
    totals2.append(total)
    total = 0
    for x in range(6, 9):
        total += int(mine2[x])
    totals2.append(total)
    total = 0
    for x in range(9, 12):
        total += int(mine2[x])
    totals2.append(total)
    total = 0

    #MINE 3
    total = 0
    totals3 = []
    for x in range(0, 3):
        total += int(mine3[x])
    totals3.append(total)
    total = 0
    for x in range(3, 6):
        total += int(mine3[x])
    totals3.append(total)
    total = 0
    for x in range(6, 9):
        total += int(mine3[x])
    totals3.append(total)
    total = 0
    for x in range(9, 12):
        total += int(mine3[x])
    totals3.append(total)
    total = 0

    #MINE 4
    total = 0
    totals4 = []
    for x in range(0, 3):
        total += int(mine4[x])
    totals4.append(total)
    total = 0
    for x in range(3, 6):
        total += int(mine4[x])
    totals4.append(total)
    total = 0
    for x in range(6, 9):
        total += int(mine4[x])
    totals4.append(total)
    total = 0
    for x in range(9, 12):
        total += int(mine4[x])
    totals4.append(total)
    total = 0

    #MINE 5
    total = 0
    totals5 = []
    for x in range(0, 3):
        total += int(mine5[x])
    totals5.append(total)
    total = 0
    for x in range(3, 6):
        total += int(mine5[x])
    totals5.append(total)
    total = 0
    for x in range(6, 9):
        total += int(mine5[x])
    totals5.append(total)
    total = 0
    for x in range(9, 12):
        total += int(mine5[x])
    totals5.append(total)
    total = 0

    # Вычисление самой эффективной шахты за квартал
    maximum = 0
    for x in range(1, 5):
        if totals1[x-1] > maximum:
            maximum = totals1[x-1]
        if totals2[x-1] > maximum:
            maximum = totals2[x - 1]
        if totals3[x-1] > maximum:
            maximum = totals3[x-1]
        if totals4[x-1] > maximum:
            maximum = totals4[x - 1]

        if maximum in totals1:
            print(f"Самая эффективная шахта за квартал {x}: Шахта 1")
        if maximum in totals2:
            print(f"Самая эффективная шахта за квартал {x}: Шахта 2")
        if maximum in totals3:
            print(f"Самая эффективная шахта за квартал {x}: Шахта 3")
        if maximum in totals4:
            print(f"Самая эффективная шахта за квартал {x}: Шахта 4")


def sumInAllMines(mine1, mine2, mine3, mine4, mine5):
    # MINE 1
    total = 0
    totals1 = []
    for x in range(0, 3):
        total += int(mine1[x])
    totals1.append(total)
    total = 0
    for x in range(3, 6):
        total += int(mine1[x])
    totals1.append(total)
    total = 0
    for x in range(6, 9):
        total += int(mine1[x])
    totals1.append(total)
    total = 0
    for x in range(9, 12):
        total += int(mine1[x])
    totals1.append(total)
    total = 0

    # MINE 2
    total = 0
    totals2 = []
    for x in range(0, 3):
        total += int(mine2[x])
    totals2.append(total)
    total = 0
    for x in range(3, 6):
        total += int(mine2[x])
    totals2.append(total)
    total = 0
    for x in range(6, 9):
        total += int(mine2[x])
    totals2.append(total)
    total = 0
    for x in range(9, 12):
        total += int(mine2[x])
    totals2.append(total)
    total = 0

    # MINE 3
    total = 0
    totals3 = []
    for x in range(0, 3):
        total += int(mine3[x])
    totals3.append(total)
    total = 0
    for x in range(3, 6):
        total += int(mine3[x])
    totals3.append(total)
    total = 0
    for x in range(6, 9):
        total += int(mine3[x])
    totals3.append(total)
    total = 0
    for x in range(9, 12):
        total += int(mine3[x])
    totals3.append(total)
    total = 0

    # MINE 4
    total = 0
    totals4 = []
    for x in range(0, 3):
        total += int(mine4[x])
    totals4.append(total)
    total = 0
    for x in range(3, 6):
        total += int(mine4[x])
    totals4.append(total)
    total = 0
    for x in range(6, 9):
        total += int(mine4[x])
    totals4.append(total)
    total = 0
    for x in range(9, 12):
        total += int(mine4[x])
    totals4.append(total)
    total = 0

    # MINE 5
    total = 0
    totals5 = []
    for x in range(0, 3):
        total += int(mine5[x])
    totals5.append(total)
    total = 0
    for x in range(3, 6):
        total += int(mine5[x])
    totals5.append(total)
    total = 0
    for x in range(6, 9):
        total += int(mine5[x])
    totals5.append(total)
    total = 0
    for x in range(9, 12):
        total += int(mine5[x])
    totals5.append(total)
    total = 0

    # Вычисление общего объёма добычи в каждом квартале
    for x in range(0, 4):
        allSum = totals1[x] + totals2[x] + totals3[x] + totals4[x] + totals5[x]
        print(f"Суммарный объём добычи угля в квартале {x+1} во всех шахтах:", allSum)
        allSum = 0


def theMostLargeAmount(mine1, mine2, mine3, mine4, mine5):
    # MINE 1
    total = 0
    totals1 = []
    for x in range(0, 3):
        total += int(mine1[x])
    totals1.append(total)
    total = 0
    for x in range(3, 6):
        total += int(mine1[x])
    totals1.append(total)
    total = 0
    for x in range(6, 9):
        total += int(mine1[x])
    totals1.append(total)
    total = 0
    for x in range(9, 12):
        total += int(mine1[x])
    totals1.append(total)
    total = 0

    # MINE 2
    total = 0
    totals2 = []
    for x in range(0, 3):
        total += int(mine2[x])
    totals2.append(total)
    total = 0
    for x in range(3, 6):
        total += int(mine2[x])
    totals2.append(total)
    total = 0
    for x in range(6, 9):
        total += int(mine2[x])
    totals2.append(total)
    total = 0
    for x in range(9, 12):
        total += int(mine2[x])
    totals2.append(total)
    total = 0

    # MINE 3
    total = 0
    totals3 = []
    for x in range(0, 3):
        total += int(mine3[x])
    totals3.append(total)
    total = 0
    for x in range(3, 6):
        total += int(mine3[x])
    totals3.append(total)
    total = 0
    for x in range(6, 9):
        total += int(mine3[x])
    totals3.append(total)
    total = 0
    for x in range(9, 12):
        total += int(mine3[x])
    totals3.append(total)
    total = 0

    # MINE 4
    total = 0
    totals4 = []
    for x in range(0, 3):
        total += int(mine4[x])
    totals4.append(total)
    total = 0
    for x in range(3, 6):
        total += int(mine4[x])
    totals4.append(total)
    total = 0
    for x in range(6, 9):
        total += int(mine4[x])
    totals4.append(total)
    total = 0
    for x in range(9, 12):
        total += int(mine4[x])
    totals4.append(total)
    total = 0

    # MINE 5
    total = 0
    totals5 = []
    for x in range(0, 3):
        total += int(mine5[x])
    totals5.append(total)
    total = 0
    for x in range(3, 6):
        total += int(mine5[x])
    totals5.append(total)
    total = 0
    for x in range(6, 9):
        total += int(mine5[x])
    totals5.append(total)
    total = 0
    for x in range(9, 12):
        total += int(mine5[x])
    totals5.append(total)
    total = 0

    # Вычисление наибольшего квартального объёма в каждой шахте
    maximum = 0
    index = 0
    for x in range(0, 4):
        if totals1[x] > maximum:
            maximum = totals1[x]
            index = x+1
    print(f"Наибольший квартальный объём добычи угля в Шахте 1 был в {index} квартале и составил: {maximum}")

    maximum = 0
    index = 0
    for x in range(0, 4):
        if totals2[x] > maximum:
            maximum = totals2[x]
            index = x + 1
    print(f"Наибольший квартальный объём добычи угля в Шахте 2 был в {index} квартале и составил: {maximum}")

    maximum = 0
    index = 0
    for x in range(0, 4):
        if totals3[x] > maximum:
            maximum = totals3[x]
            index = x + 1
    print(f"Наибольший квартальный объём добычи угля в Шахте 3 был в {index} квартале и составил: {maximum}")

    maximum = 0
    index = 0
    for x in range(0, 4):
        if totals4[x] > maximum:
            maximum = totals4[x]
            index = x + 1
    print(f"Наибольший квартальный объём добычи угля в Шахте 4 был в {index} квартале и составил: {maximum}")

    maximum = 0
    index = 0
    for x in range(0, 4):
        if totals5[x] > maximum:
            maximum = totals5[x]
            index = x + 1
    print(f"Наибольший квартальный объём добычи угля в Шахте 5 был в {index} квартале и составил: {maximum}")


# Основной цикл
while True:
    comm = input("\nСписок доступных команд:\n"
                 "1.Средняя добыча угля в год\n"
                 "2.Самая эффективная в каждом квартале\n"
                 "3.Суммарный объём добычи угля в каждом квартале года суммарно во всех шахтах\n"
                 "4.Наибольший квартальный объём добычи угля по шахтам холдинга\n"
                 "5.Выход из программы\n\n"
                 "Введите команду: ")
    comm = int(comm)
    if comm == 1:
        print(f"Средняя добыча угля шахты 1 в год: ", midMineYear(mine1))
        print(f"Средняя добыча угля шахты 2 в год: ", midMineYear(mine2))
        print(f"Средняя добыча угля шахты 3 в год: ", midMineYear(mine3))
        print(f"Средняя добыча угля шахты 4 в год: ", midMineYear(mine4))
        print(f"Средняя добыча угля шахты 5 в год: ", midMineYear(mine5))
    elif comm == 2:
        efficientIn3months(mine1, mine2, mine3, mine4, mine5)
    elif comm == 3:
        sumInAllMines(mine1, mine2, mine3, mine4, mine5)
    elif comm == 4:
        theMostLargeAmount(mine1, mine2, mine3, mine4, mine5)
    elif comm == 5:
        print("Выходим из программы...")
        break
    else:
        print("Неправильная команда. Повторите ввод. \n")


