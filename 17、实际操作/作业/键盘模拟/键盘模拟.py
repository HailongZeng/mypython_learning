import win32con
import win32api
import time

'''
win32api.keybd_event(91,0,0,0)  #windows键--91，按下
time.slepp(1)
win32api.keybd_event(91,0,win32con.KEYEVENTF_KEYUP,0)  #抬起
'''

while True:
    win32api.keybd_event(91, 0, 0, 0)
    time.slepp(1)
    win32api.keybd_event(77, 0, 0, 0)
    time.slepp(1)
    win32api.keybd_event(77, 0, win32con.KEYEVENTF_KEYUP, 0)
    win32api.keybd_event(91, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(3)
