# -*- coding:utf-8 -*-
from PIL import Image
from ascii_char import *
import argparse


parser = argparse.ArgumentParser()

parser.add_argument('file')
parser.add_argument('-o', '--output')
parser.add_argument('--width', type=int, default=80)
parser.add_argument('--height', type=int, default=80)

args = parser.parse_args()

INPUT = args.file
OUTPUT = args.output
WIDTH = args.width
HEIGHT = args.height

if __name__ == '__main__':

	im = Image.open(INPUT)
	if not WIDTH and not HEIGHT:
		(WIDTH,HEIGHT) = im.size
	else:
		im = im.resize((WIDTH,HEIGHT), Image.NEAREST)

	txt = ""

	for i in range(HEIGHT):
		for j in range(WIDTH):
			txt += get_char(*im.getpixel((j,i)))
		txt += "\n"

	if OUTPUT:
		with open(OUTPUT, 'w') as f:
			f.write(txt)
	else:
		with open("output.txt", 'w') as f:
			f.write(txt)