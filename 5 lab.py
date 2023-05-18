def l51():
    import random
    l = [1, 2, 3, 4, 5]
    a = int(input('Введите число: '))
    if a in l:
        print('Поздравляю, вы угадали число!')
    else:
        print('Нет такого числа!')

def l52():
    l = [1, 2, 3, 3, 2]
    a = ''
    n = 0
    for i in range(0, len(l)):
        for j in range(1, len(l)):
            if i != j and l[i] == l[j]:
                if str(l[i]) not in a:
                    a = a + str(l[i]) + ' '
                    n += 1
    print('Количество повторений: ', n)
    print('Повторяющиеся элементы: ', a)

def l53():
    days = ('Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье')
    k = int(input('Введите желаемое число выходных: '))
    v = []
    r = []
    for i in range(0, k):
        v.insert(i, input('Введите выходной: '))
    for i in range(0, len(days)):
        for j in range(0, k):
            if days[i] != v[j]:
                if not days[i] in r:
                    r.append(days[i])
    print('Ваши выходные:', v, 'Кол-во:', k)
    print('Ваши рабочие дни:', r, 'Кол-во:', (7 - k))

def l54():
    s1 = ['Костин', 'Соловьев', 'Аршинова']
    s2 = ['Круглов', 'Анисимова', 'Лебедь']
    a = (s1[:2] + s2[:2])

    print('Первая группа: ', *s1)
    print('Вторая группа: ', *s2)
    print('Команда:', *a)
    print('Длина:', len(a))

    a = tuple(sorted(a))

    print('Сортированная команда:', *a)

    name = input('Введите проверяемую фамилию: ')
    if name in a:
        print('Этот человек есть в команде')
    else:
        print('Этого человека нет в команде')

l51()
l52()
l53()
l54()