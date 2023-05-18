def proc1():
    n = int(input())
    stroka = ''

    for i in range(1, n + 1):
        slovo = input()
        stroka = stroka + slovo + ' '
        slovo = ''

    print(stroka)


def proc2():
    stroka = ''
    slovo = input()

    while slovo != 'stop':
        stroka = stroka + slovo + ' '
        slovo = input()
    print(stroka)

def proc3():
    slovo = input()
    letter1 = 'ф'
    letter2 = 'Ф'

    while slovo!= 'stop':
        if (letter1 in slovo) or (letter2 in slovo):
            print("Ого! Это редкое слово!")
        else:
            print("Эх, это не очень редкое слово...")
        slovo = input()

def proc4():
    import random
    n = 0
    v = 0
    while n != 3:
        a = random.randint(1, 9)
        b = random.randint(1, 9)
        res = a + b
        otvet = input(str(a) + "+" + str(b) + "= ")

        if otvet == str(res):
            print("Правильно!")
            v += 1
        else:
            print("Ответ неверный")
            n += 1
    print("Количество правильных ответов: ", v)

proc4()