def r1():
    from PIL import Image, ImageFilter
    from pathlib import Path

    current_dir = ''
    filenames = Path(current_dir).glob('*')
    Path('new_dir').mkdir(parents=True, exist_ok=True)

    for file in filenames:
        if file.suffix in ['.jpg', '.png']:
            with Image.open(file) as img:
                img.load()
                new_img = img.filter(ImageFilter.EMBOSS)
                new_img.save(Path("new_dir", file))


def r3():
    import csv
    file = open("l9.csv", 'r')
    l = list(csv.reader(file, delimiter=','))
    summ = 0
    for i in l:
        summ = summ + (int(i[1]) * int(i[2]))
    for i in l:
        i.insert(1, ' - ')
        i.insert(3, ' шт. за ')
        i.insert(5, ' руб. ')
        print(*i)

    print('Итоговая сумма:', summ, 'руб.')


r1()
r3()
