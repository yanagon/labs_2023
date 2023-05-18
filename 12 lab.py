from tkinter import *

def pp1():
    class Rest:
        def __init__(self, name, cuisine):
            self.name = name
            self.cuisine = cuisine

    class IceCream(Rest):
        def __init__(self, name, cuisine, flavors, place, time):
            super().__init__(name, cuisine)
            self.flavors = flavors
            self.place = place
            self.time = time

        class Popsicle:
            def __init__(self, name, flavors):
                self.name = name
                self.flavors = flavors

        class Cone:
            def __init__(self, name, flavors):
                self.name = name
                self.flavors = flavors

        class Sunday:
            def __init__(self, name, flavors):
                self.name = name
                self.flavors = flavors

        def describe_rest(self):
            print('Название рестрорана:', self.name)
            print('Тип кухни:', self.cuisine)
            print('Находится по адресу ', self.place)
            print('Часы работы: ', self.time)

        def add_fvs(self):
            s.append(input('Введите вкусы, которые хотите добавить: '))

        def del_fvs(self):
            s.remove(input('Введите вкус, которые хотите удалить: '))

        def flavs(self):
            print('Список сортов мороженного: ', s)

        def proverka(self):
            if str(input('Введите вкус, который хотите проверить')) in s:
                print('Такой вкус есть')
            else:
                print('Такого вкуса нет')

    s = ['Шоколадное', 'Ванильное']
    res3 = IceCream('Italia', 'Итальянская', s, 'пр. Бакунина, 5', '9:00 - 2:00')

    res3.describe_rest()
    res3.flavs()
    res3.add_fvs()
    res3.del_fvs()
    res3.proverka()
    res3.flavs()


def pp2():
    class IceCreamStand:
        def __init__(self, name, cuisine, flavors, place, time):
            self.name = name
            self.cuisine = cuisine
            self.flavors = flavors
            self.place = place
            self.time = time

        def flavs(self):
            print('Список сортов мороженного: ', s)

    s = ['Шоколадное', 'Ванильное', 'Клубничное', 'Лимонное', 'Фисташковое']
    r = IceCreamStand('Italia', 'Итальянская', s, 'пр. Бакунина, 5', '9:00 - 2:00')
    r.flavs()

    okno = Tk()
    okno['bg'] = 'MistyRose3'
    okno.title('IceCream')
    okno.geometry('300x250')

    f = Frame(okno, bg='RosyBrown3', bd=5)
    f.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.7)
    text = Label(okno, text='Виды мороженного:', bg='RosyBrown3', font=30)
    text.place(relx=0.15, rely=-0.25, relwidth=0.7, relheight=0.7)
    text.pack

    schet = 0.1
    for i in s:
        sl = i
        schet += 0.12
        slovo = Label(okno, text=sl, bg='RosyBrown3', font=25)
        slovo.place(relx=0.15, rely=schet, relwidth=0.7, relheight=0.1)
        slovo.pack

    okno.mainloop()

pp2()