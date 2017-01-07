# -*- coding:utf-8 -*-
ASCII_CHAR = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'.")

def get_char(r,g,b,alpha=256):
	if alpha == 0:
		return ' '
	grayscale = int(.2126 * r + .7152 * g + .0722 * b)
	unit = (256.0 + 1)/len(ASCII_CHAR)
	return ASCII_CHAR[int(grayscale/unit)]