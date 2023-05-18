def a1():
    from PIL import Image

    filename = "sobaken.jpg"
    with Image.open(filename) as img:
        img.load()
    img.show()
    w, h = img.size
    f = img.format
    m = img.mode

    print('Ширина: ', w)
    print('Высота: ', h)
    print('Формат: ', f)
    print('Цветовая модель: ', m)


def a2():
    from PIL import Image
    filename = "sobaken.jpg"
    with Image.open(filename) as img:
        img.load()

    new_img = img.resize((img.width // 3, img.height // 3))
    new_img.save("newsobaken.jpg")

    conv_img = img.rotate(180)
    conv_img.save("180sobaken.jpg")

    conv_img = img.transpose(Image.FLIP_LEFT_RIGHT)
    conv_img.save("sobaken_left_right.jpg")


def a3():
    from PIL import Image, ImageFilter
    files = ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg"]
    for f in files:
        with Image.open(f) as img:
            img.load()
            n_img = img.filter(ImageFilter.EMBOSS)
            n_img.show()
            n_img.save('n' + f)


def a4():
    from PIL import Image, ImageFilter
    files = ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg"]

    for f in files:
        watermark = Image.open("wmark.jpg")
        with Image.open(f) as img:
            img.paste(watermark)
            img.save('new' + f)


a1()
a2()
a3()
