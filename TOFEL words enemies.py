import random
from PIL import Image,ImageDraw,ImageFont

f = open("TOFEL words.txt","r")
text = f.read()
TOFEL_words = text.split()

TOFEL_word_enemy = TOFEL_words[random.randint(0,571)]

image = Image.open('enemy2.png')
draw = ImageDraw.Draw(image)
font=ImageFont.truetype('font/msyh.ttc',10)
draw.text((10,30), TOFEL_word_enemy, (0,0,0),font)
image.save("enemy2_now" + ".png")

