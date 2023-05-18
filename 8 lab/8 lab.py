def l81():
    from PIL import Image

    img = Image.open('happybd.jpg')
    img.show()

    img_cr = img.crop((0, 0, 750, 540))
    img_cr.show()
    img_cr.save('hbd2.jpg')


def l82():
    from PIL import Image
    sl = {'День рождения': 'happybd.jpg', 'Новый год': 'newyear.jpg', '8 марта': '8m.jpg',
          'Доброе утро': 'goodmorning.jpg'}
    n = input('Введите название праздника:')
    img = Image.open(sl[n])
    img.show()


def l83():
    from PIL import Image
    from PIL import ImageFont
    from PIL import ImageDraw

    img = Image.open('hbday.jpg')
    n = input('Введите имя человека, которого хотите поздравить: ')
    fontt = ImageFont.truetype('arial_bold.ttf', 25)
    imgd = ImageDraw.Draw(img)
    imgd.text((30, 60), n + ', поздравляю!!', font=fontt, fill='white')

    img.show()
    img.save('newpp.png')


l82()
l83()
