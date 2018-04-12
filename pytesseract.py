# -*- coding:utf-8 -*-
# ocr光学识别系统
import pytesseract
from PIL import Image

# 使用pil包中Image打开图片文件,返回对象
img = Image.open('test.jpg')
# 调用tesseract识别图片
data = pytesseract.image_to_string(img)
# 输出结果
print(data)
