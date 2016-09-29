#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-09-23 15:49:58
# @Author  : waitingChow (zhouzt52@qq.com)
# @Link    : https://github.com/StephinChou/

# 将图像转化为字符画 
# convert a image to a char-img

from PIL import Image

chars = list("A-%,+1n&M-B/\?<8&WM#$_+~*|(){}[]>i!lI;:,\"^`'. ")

# 图像整体使用多少个字符来表示？ 必须为2的指数倍2,4,6,8,16,32最大
# 对于只想看轮廓的图,2或4显示效果较好，对稍微追求细节的图稍微弄大一点
num = 2;
chars = chars[:num]
# isThumb = True
isThumb = False
width,height =80,40

#分节因子
factor = int(256 / len(chars))

# 依据灰度值阶梯返回不同的字符
def get_char(pix):
    for i in range(0,len(chars)):
        if pix < factor * (i+1):
            return chars[i]

# img = Image.open('laugh.jpg')
# img = Image.open('look.jpg')
# img = Image.open('cry.jpg')
img = Image.open('flower.jpg')
# img = Image.open('girl.jpg')
# img = Image.open('wm.png')
# img = Image.open('lengmo.jpg')
# img = Image.open('lufei.jpg')
if img.mode=='P' or img.mode =='RGBA':
     im=Image.new('RGB',img.size,'white')
     im.paste(img.convert('RGBA'),img.convert('RGBA'))
     img= im
# 转化为灰度图
img = img.convert("L")
w,h = 0,0
# 进行图片大小的变换
if isThumb:
    w,h = width,height
    img=img.resize((w,h),Image.NEAREST)
else:
    w,h = img.size
    img = img.resize((w,int(h/2)),Image.NEAREST)
    h= int(h/2)


data=[]
pix = img.load()
length = len(chars)
data = ""
#扫描整个图片，按灰度置换图片
for i in range(0,h):
    line = ""
    for j in range(0,w):
        line += get_char(pix[j,i])
    data += line+"\n"

with open("a.txt",'w') as f:
    f.write(data)
