def p1():
    a = input()
    b = input()

    if a = b:
        print("Пароль совпадает")
    else:
        print("Пароль не совпадает")
def p2():
    n = int(input())

    if n % 2:
        if n <= 36:
            print("Ваше место - верхее, не боковое")
        elif (n > 36) and (n <= 54):
            print("Ваше место - верхее, боковое")
    else:
        if n <= 36:
            print("Ваше место - нижнее, не боковое")
        elif (n > 36) and (n <= 54):
            print("Ваше место - нижнее, боковое")

def p3():
    n = int(input())

    if ((n % 4 == 0) and (n % 100 != 0)) or (n % 400 ==0):
        print('Год ', n, ' - високосный')
    else:
        print('Это год не високосный')

def p4():
    cv1 = input()
    cv2 = input()

    r = 'красный'
    y = 'желтый'
    b = 'синий'

    if (cv1 == r) or (cv1 == y) or (cv1 == b):
        if (cv2 == r) or (cv2 == y) or (cv2 == b):
            if cv1 == cv2:
                print('Цвет не изменился')
            if ((cv1 == r) and (cv2 == y)) or ((cv2 == r) and (cv1 == y)):
                print('Цвет: оранжевый')
            if ((cv1 == b) and (cv2 == y)) or ((cv2 == b) and (cv1 == y)):
                print('Цвет: зеленый')
            if ((cv1 == r) and (cv2 == b)) or ((cv2 == r) and (cv1 == b)):
                print('Цвет: фиолетовый')
        else:
            print('Проверьте введенные цвета')
    else:
        print('Проверьте введенные цвета')

def p5():
    n = int(input())
    stroka = ''

    for i in range(1, n + 1):
        slovo = input()
        stroka = stroka + slovo + ' '
        slovo =''

    print(stroka)

