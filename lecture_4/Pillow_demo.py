# encoding=utf-8

from PIL import Image

im1 = Image.open('plt.jpg')
print(im1.size, im1.format, im1.mode)
Image.open('plt.jpg').save('plt1.png')
im2 = Image.open('plt1.png')
size = (288, 180)
im2.thumbnail(size)
out = im2.rotate(45)
im1.paste(out, (50, 50))
im1.save('plt2.png')
