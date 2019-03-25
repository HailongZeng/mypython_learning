'''
以下代码是在Windows系统下进行背景修改，mac不支持，因为无法连接win32系列模块
在cmd终端可以用Regedit打开注册表
'''
import win32api
import win32con
import win32gui

def setWallPaper(path):
    #打开注册表
    reg_key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,
                                    'Control Panle\\Desktop', 0,
                                    win32con.KEY_SET_VALUE)

    #2-拉伸 0-居中 6-适应 10-填充
    win32api.RegSetValueEx(reg_key, 'WallpaperStyle', 0, win32con.REG_SZ, '2')
    #win32api.RegSetValueEx(reg_key, )
    #win32api.RegSetValueEx(reg_key, 'WallPaper')

    #SPIF_SENDWININICHANGE   立即生效
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, path, win32con.SPIF_SENDWININICHANGE)

path = ''   #所要使用背景的路径
setWallPaper(path)