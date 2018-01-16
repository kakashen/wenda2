# -*- coding: utf-8 -*-
from PIL import Image
import os
import matplotlib.pyplot as plt


def pull_screenshot():
    os.system('adb shell screencap -p /sdcard/screenshot.png')
    os.system('adb pull /sdcard/screenshot.png .')

pull_screenshot()
img = Image.open("./screenshot.png")

# 用 matplot 查看测试分辨率，切割问题和选项区域
# region = img.crop((75, 315, 1167, 789))

question  = img.crop((40, 450, 1050, 680))
choices = img.crop((75, 735, 990, 1270))
print(question)
plt.subplot(221)
im = plt.imshow(img, animated=True)
plt.subplot(222)
im2 = plt.imshow(question, animated=True)
plt.subplot(212)
im3 = plt.imshow(choices, animated=True)
plt.show()