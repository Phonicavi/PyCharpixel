# -*- coding:utf-8 -*-
from PIL import Image
ASCII_CHAR = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'.")


class Processor():

	@staticmethod
	def get_char(r,g,b,alpha=256):
		if alpha == 0:
			return ' '
		grayscale = int(.2126 * r + .7152 * g + .0722 * b)
		unit = (256.0 + 1)/len(ASCII_CHAR)
		return ASCII_CHAR[int(grayscale/unit)]


	"""image processor"""
	def __init__(self,_INPUT,_WIDTH,_HEIGHT):
		self.__im = Image.open(_INPUT)
		(self.__width,self.__height) = (_WIDTH, _HEIGHT)
		if not _WIDTH and not _HEIGHT:
			(self.__width,self.__height) = self.__im.size
		else:
			self.__im = self.__im.resize((self.__width,self.__height), Image.NEAREST)


	def generate_text(self):
		txt = ""
		for i in range(self.__height):
			for j in range(self.__width):
				txt += Processor.get_char(*self.__im.getpixel((j,i)))
			txt += "\n"
		return txt