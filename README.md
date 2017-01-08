# PyCharpixel

**Python Final Project**: *replace pixels with ASCII characters*  

### Depedency

+ Pillow 3.0.0  
+ Lib/argparser

### Design

+   `ascii_char.py`
     **var** `ASCII_CHAR`: a list of 70 ASCII characters with decreasing gray scale values  
    **class** `Processor`  
    - constructor `__init__(_INPUT,_WIDTH,_HEIGHT)`: open an image file using `PIL.Image.open` and resize the image if needed  
    - staticmethod `get_char(r,g,b,alpha)`: a linear transformation used for mapping between gray scale values and characters  
    - method `generate_text()`: replace each pixel with proper character using `Processor.get_char`, join them and return the result text string  

+ `charpixel.py`
    **var** `parser`: initialized with `argparse.ArgumentParser`  
    **var** `args`: parser's arguments with 4 members  
    - `INPUT` the path of input file, image, positional  
    - `OUTPUT` the path of output file, text, optional  
    - `WIDTH` the processing width of pixels, optional  
    - `HEIGHT` the processing height of pixels, optional  

    **\_\_main\_\_**: create and initialize a processor with `INPUT`, `WIDTH` and `HEIGHT`, generate the replaced text string and output the text

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

---

### 依赖

+ Pillow 3.0.0 图像处理库  
+ Lib/argparser 终端参数引导  

###  设计

+   `ascii_char.py`
     **var** `ASCII_CHAR`: 依据字符所占点阵的点数降序排列，得到了70个字符的list作为替换备选  
    **class** `Processor`  
    - 构造函数 `__init__(_INPUT,_WIDTH,_HEIGHT)`: 使用 `PIL.Image.open` 打开指定图片文件  
    - 静态方法 `get_char(r,g,b,alpha)`: 将RGB图片多通道值转换为单色灰度值，并对灰度值进行线性变换映射到备选字符list中  
    - 方法 `generate_text()`: 逐行逐列替换图片中每个像素，并拼接出完整字符串  

+ `charpixel.py`
    **var** `parser`: 用 `argparse.ArgumentParser` 初始化一个parser实例  
    **var** `args`: 调用 `parser.parse_args()` 方法获得4个参数成员  
    - `INPUT` 输入图片的文件路径 必需参数  
    - `OUTPUT` 输出文本的文件路径 可选参数  
    - `WIDTH` 一次处理的图片宽度 可选参数  
    - `HEIGHT` 一次处理的图片高度 可选参数  

    **\_\_main\_\_**: 用 `INPUT`, `WIDTH` and `HEIGHT` 初始化一个Processor类的实例 生成灰度映射字符串`txt`并输出至文本文件  

### 用法

	charpixel.py [-h] [-o OUTPUT] [--width WIDTH] [--height HEIGHT] file  

	必需参数: 输入图片文件路径  
	  file  
	可选参数: 
	  -o, -output 输出文件路径 默认值为output.txt  
	  -width 处理像素宽度 默认值为全图宽度  
	  -height 处理像素高度 默认值为全图高度  

例如，在终端输入：  

```bash
$ python charpixel.py test.jpeg -o result.txt
```

输入`test.jpeg`图片，依据像素灰度映射为不同字符并输出至`result.txt`文件。考虑到显示效果，不推荐使用尺寸过大的图片进行测试；同时，由于文本编辑器的字符显示宽度不尽相同，在“等宽显示”且单个字符高度和宽度相近的显示设置下视觉效果最佳。  

