import time
import pygame

filePath = ''  #音乐路径

#初始化
pygame.mixer.init()

#加载音乐
track = pygame.mixer.music.load(filePath)

#播放音乐
pygame.mixer.music.play()

time.sleep(60)

#暂停
#pygame.mixer.music.pause()

#停止
pygame.mixer.music.stop()
