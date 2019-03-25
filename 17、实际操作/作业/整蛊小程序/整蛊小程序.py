import time
import pygame

import win32api
import win32con
import win32gui

#线程模块
import threading

def go():
    pygame.mixer.init()
    while True:
        for i in range(5):  #循环播放五首音乐
            filePath = '' + str(i) + '.mp3'
            track = pygame.mixer.musix.load(filePath)
            pygame.mixer.music.play(track)
            time.sleep(10)
            pygame.mixer.music.stop()

def setWallPaper(path):
    reg_key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,
                                    'Control Panle\\Desktop', 0,
                                    win32con.KEY_SET_VALUE)
    win32api.RegSetValueEx(reg_key, 'WallpaperStyle', 0, win32con.REG_SZ, '2')
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, path, win32con.SPIF_SENDWININICHANGE)

#加上线程才能使得音乐播放和修改背景图片同时执行
th = threading.Thread(target=go, name='LoopThread')
th.start()
while True:
    go()
    for i in range(9):  #循环修改背景图片
            filePath = '' + str(i) + '.jpg'
            setWallPaper(filePath)
            time.sleep(5)