
# 答题辅助

## 具体实现

1. ADB 获取手机截屏
```
adb shell screencap -p /sdcard/screenshot.png
adb pull /sdcard/screenshot.png .
```
2. OCR 识别题目与选项文字

3. 搜索判断

## 结果判断方式

1. 直接打开浏览器搜索问题
2. 题目+每个选项都通过搜索引擎搜索，从网页代码中提取搜索结果计数
3. 只用题目进行搜索，统计结果页面代码中包含选项的词频
 
## 使用步骤 (谷歌 [Tesseract](https://github.com/madmaze/pytesseract)) 
### Android
#### 1. 安装 ADB

下载地址：https://adb.clockworkmod.com/
安装完后插入安卓设备且安卓已打开 USB 调试模式，终端输入 `adb devices` ，显示设备号则表示成功。我手上的机子是坚果 pro1，第一次不成功,查看设备管理器有叹号，使用 [handshaker](https://www.smartisan.com/apps/handshaker) 加载驱动后成功，也可以使用豌豆荚之类的试试。
#### 2. 安装 python 3
#### 3. 安装所需 python 包

命令行：
```
pip install pytesseract
pip install pillow  
pip install requests
```
#### 4. 安装 谷歌 Tesseract

Windows下链接：
*推荐使用安装版，在安装时选择增加中文简体语言包*
- 安装版：
https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-setup-3.05.01.exe
- 免安装版：
https://github.com/parrot-office/tesseract/releases/download/3.5.1/tesseract-Win64.zip
*免安装版需要下载[中文语言包](https://github.com/tesseract-ocr/tesseract/wiki/Data-Files)*


#### 5. 修改 `GetTitleTessAndroid` 代码相应目录信息（默认安装则无需修改）
```
# tesseract 路径
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract'
# 语言包目录和参数
tessdata_dir_config = '--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata" --psm 6'
```
#### 6. 运行脚本
`python GetQuestionTessAndroid.py`
会自动识别文字并打开浏览器

**注： 可以用 `GetImgTool.py` 调整题目截取位置**

若屏幕分辨率不同，请在 ocr.py 中自行修改代码即可
```
# 切割题目和选项位置，左上角坐标和右下角坐标,自行测试分辨率
question_im = image.crop((50, 350, 1000, 560))
choices_im = image.crop((75, 535, 990, 1150))
# question = img.crop((75, 315, 1167, 789))
```
### IOS

**未测试**

- 需要安装 WDA 进行截图，参考 https://testerhome.com/topics/7220 
- 安装 [python-wda](https://github.com/openatx/facebook-wda)
- 其他步骤相同。

- `python GetQuestionTessIos.py`

## 使用步骤 (百度 OCR)

请移步，[链接](/baiduApiVersion)

## 其它
- Tesseract 参数，若识别有问题可以更改参数解决
https://github.com/tesseract-ocr/tesseract/blob/master/doc/tesseract.1.asc
- 三种方法可以选择，可以加#注释掉只保留一个方法
## 总结

有了 ADB 截图，怕是各种小辅助都可以玩了。python 写小脚本真的很方便。

## Next

- 文字识别后 nlp 处理一下关系，然后搜索不同选择结果