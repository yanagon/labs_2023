def l41():
    try:
        a = int(input('Введите число: '))
        b = a % 3
    except ValueError:
        print('Введено не число')
    else:
        if b == 0 and a != 0:
            print('Число делится на 3')
        elif a == 0:
            print('Введен ноль')
        else:
            print('Число не делится на 3')

def l42():
    try:
        a = int(input('Введите делитель: '))
        b = 100 / a
    except ZeroDivisionError:
        print('Введен 0')
    except ValueError:
        print('Введено не число')
    else:
        print('Результат деления равен: ', b)

def l43():
    date = input('Введите дату(дд.мм.гггг)')
    date = date.split(".")
    if int(date[0]) * int(date[1]) == int(date[2][2:]):
        print('Эта дата магическая!!!')
    else:
        print('Эта дата не магическая:(')

def l44():
    nomer = input('Введите номер билета: ')
    a = 0
    b = 0
    if len(nomer) % 2 == 0:
        for i in nomer[0:int(len(nomer) / 2)]:
            a = a + int(i)
        for i in nomer[int(len(nomer) / 2):int(len(nomer))+1]:
            b = b + int(i)
        if a == b:
            print('Вам попался счастливый билетик!!')
        else:
            print('К сожалению, этот билет не счастливый:(')
    else:
        print('Количество цифр нечетное')

l41()
l42()
l43()
l44()