# PyCharpixel

**Python Final Project**: *replace pixels with ASCII characters*  

### Depedency

+ Pillow 3.0.0  
+ Lib/argparser

### Usage

	charpixel.py [-h] [-o OUTPUT] [--width WIDTH] [--height HEIGHT] file  

	positional arguments:  
	  file  
	optional arguments:  
	  -o OUTPUT, --output OUTPUT  
	  --width WIDTH  
	  --height HEIGHT  

For example, we input a file called `test.jpeg` and output the result into `result.txt`.

```bash
$ python charpixel.py test.jpeg -o result.txt
```
