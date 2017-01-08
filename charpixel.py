# -*- coding:utf-8 -*-
from ascii_char import Processor
import argparse


parser = argparse.ArgumentParser()

parser.add_argument('file')
parser.add_argument('-o', '--output')
parser.add_argument('--width', type=int, default=50)
parser.add_argument('--height', type=int, default=50)

args = parser.parse_args()

INPUT = args.file
OUTPUT = args.output
WIDTH = args.width
HEIGHT = args.height

if __name__ == '__main__':

	processor = Processor(INPUT, WIDTH, HEIGHT)

	txt = processor.generate_text()

	if OUTPUT:
		with open(OUTPUT, 'w') as f:
			f.write(txt)
	else:
		with open("output.txt", 'w') as f:
			f.write(txt)