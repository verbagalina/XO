#Выигрышные комбинации
victory = [
    [
        [1, 1, 1],
        [0, 0, 0],
        [0, 0, 0]
    ],
    [
        [0, 0, 0],
        [1, 1, 1],
        [0, 0, 0]
    ],
    [
        [0, 0, 0],
        [0, 0, 0],
        [1, 1, 1]
    ],
    [
        [1, 0, 0],
        [1, 0, 0],
        [1, 0, 0]
    ],
    [
        [0, 1, 0],
        [0, 1, 0],
        [0, 1, 0]
    ],
    [
        [0, 0, 1],
        [0, 0, 1],
        [0, 0, 1]
    ],
    [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ],
    [
        [0, 0, 1],
        [0, 1, 0],
        [1, 0, 0]
    ]
]

#преобразователь
def trans_xo(a, r):
    b = []
    for i in a:
        if i == r:
            b.append(1)
        else:
            b.append(0)
    return b

#есть ли ходы
def play_off(p):
    for z in p:
        if "_" in z:
            return True
    return False

#игровое поле
def decor(a):
    print("_|0|1|2")
    print("0|{}|{}|{}".format(a[0][0], a[0][1], a[0][2]))
    print("1|{}|{}|{}".format(a[1][0], a[1][1], a[1][2]))
    print("2|{}|{}|{}".format(a[2][0], a[2][1], a[2][2]))

#поверка победы
def winner(a):
    for g in range(len(victory)):
        count = 0
        for i in range(len(a)):
            for j in range(len(a[i])):
                if a[i][j] == victory[g][i][j] and a[i][j] == 1:
                    count += 1
        if count == 3:
            return True
    return False


#функция для ввода коррдинат
def vvod(a):
    while True:
        koord = input("Введите координаты через пробел либо введите Z для выхода из программы:")
        koord = koord.lower()
        if len(koord) == 1 and koord[0] == "z":
            return False
        else:
            koord = koord.split()
            if len(koord) == 2:
                if koord[0].isdigit() and koord[1].isdigit():
                    koord = list(map(int, koord))
                    if 0 <= koord[0] <= 2 and 0 <= koord[1] <= 2 and a[koord[0]][koord[1]] == "_":
                        return koord

            print("Введено некорректное значение.")

#игровой цикл
def play():
    A =  [
        ["_", "_", "_"],
        ["_", "_", "_"],
        ["_", "_", "_"]
    ]
    round = 1
    while True:
        decor(A)
        if round % 2 == 0:
            print("Ходит 0")
        else:
            print("Ходит х")
        k = vvod(A)
        if not k:
            break
        elif round % 2 == 1:
            A[k[0]][k[1]] = "X"
            if winner(list(map(lambda X: trans_xo(X, "X"), A))):
                print("Выиграл Х")
                break
        else:
            A[k[0]][k[1]] = "0"
            if winner(list(map(lambda X: trans_xo(X, "0"), A))):
                print("Выиграл 0")
                break
        if not play_off(A):
            print("Ничья")
            break
        else:
            round+= 1

play()
