'''
Mac和Linux:无需安装，自带
windows:勾选了pip和Add python.ext to Path
'''
#要安装三方模块，需要知道模块的名字
#Pillow   非常强大的处理图像的工具库
#pip install+所需安装的模块名   有时会需要permission,在mac中则用sudo pip3(安装在python 3.版本） install+所需要安装的模块名(给权限)
#windows如果报错，则输入pip install --upgrade pip，更新pip的版本，然后再pip install+所需要安装的模块名

#引入了第三方库
from PIL import Image
#打开图片
im=Image.open('WechatIMG1.jpeg')
#查看图片的信息
print(im.format,im.size,im.mode)
#设置图片的大小
im.thumbnail((400,300))
#保存成新图片
im.save('temp.jpg','JPEG')
