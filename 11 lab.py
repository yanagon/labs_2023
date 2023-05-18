def p1u2():
    class Rest:
        def __init__(self, name, cuisine):
            self.name = name
            self.cuisine = cuisine

        def describe_rest(self):
            print('Название рестрорана:', self.name)
            print('Тип кухни:', self.cuisine)

        def open_rest(self):
            print('Ресторан "', self.name, '" открыт')

    new_rest = Rest(input('Введите название ресторана:'), input('Введите тип кухни:'))

    print(new_rest.name)
    print(new_rest.cuisine)
    new_rest.describe_rest()
    new_rest.open_rest()

    res1 = Rest('Токио Сити', 'Японская')
    res2 = Rest('Кореана', 'Корейская')
    res3 = Rest('Camorra Chimerica', 'Итальянская')

    res1.describe_rest()
    res2.describe_rest()
    res3.describe_rest()

def p3():
    class Rest:
        def __init__(self, name, cuisine, rating):
            self.name = name
            self.cuisine = cuisine
            self.rating = rating

        def describe_rest(self):
            print('Название рестрорана:', self.name)
            print('Тип кухни:', self.cuisine)

        def res_rating(self):
            print('Рейтинг ресторана: ', self.rating)

        def new_rating(self):
            self.rating = int(input('Введите новый рейтинг ресторана: '))
            print('Обновленный рейтинг ресторана: ', self.rating)

    res2 = Rest('Кореана', 'Корейская', '3')

    res2.describe_rest()
    res2.res_rating()
    res2.new_rating()

p3()