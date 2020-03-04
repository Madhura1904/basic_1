from PIL import Image, ImageChops


ORIG = 'C:/Users/M1049186/Desktop/reciept.jpg'
TEMP = 'temp.jpg'
SCALE = 10


def ELA():
    original = Image.open(ORIG)
    original.save(TEMP, quality=90)
    temporary = Image.open(TEMP)

    diff = ImageChops.difference(original, temporary)
    d = diff.load()
    WIDTH, HEIGHT = diff.size
    for x in range(WIDTH):
        for y in range(HEIGHT):
            d[x, y] = tuple(k * SCALE for k in d[x, y])

    diff.save('fyu.jpg')
