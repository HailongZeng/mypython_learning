#http://www.3366.com/flash/97506.shtml

from win32com.client import constants
import os
import win32com.client
import pythoncom
import win32con
import win32api
import time

class SpeechRecognition:
    def __init__(self, wordsToAdd):
        self.speaker = win32com.client.Dispatch('SAPI.SpVoice')
        self.listener = win32com.client.Dispatch('SAPI.SpSharedRecognizer')
        self.context = self.listener.CreateRecoContext()
        self.grammar = self.context.CreateGrammer()
        self.grammar.DictationSetState(0)
        self.wordsRule = self.grammer.Rules.Add('wordsRule',
                                                constants.SRATopLevel + constants.SRADynamic,0)
        self.wordsRule.Clear()
        [self.wordsRule.InitialState.AddWordTransition(None, word) for word in wordsToAdd]
        self.grammar.Rules.Commit()
        self.grammar.CmdSetRuleState('wordsRule', 1)
        self.grammar.Rules.Commit()
        self.eventHander = ContextEvents(self.context)
        self.say('Started successfully')
    def say(self, phrase):
        self.speaker.Speak(phrase)

class ContextEvents(win32com.client.getevents('SAPI.SpSharedRecoContext')):
    def OnRecognition(self, StreamNumber, StreamPosition, RecognitionType, Result):
        newResult = win32com.client.Dispatch(Result)
        print('说：', newResult.PhraseInfo.GetText())
        s =newResult.PhraseInfo.GetText()
        if s == '上':
            win32api.keybd_event(38, 0, 0, 0)  #上键-39
            time.slepp(1)
            win32api.keybd_event(38, 0, win32con.KEYEVENTF_KEYUP, 0)
            print('shang')
        elif s == '下':
            win32api.keybd_event(40, 0, 0, 0)  #下键-40
            time.slepp(1)
            win32api.keybd_event(40, 0, win32con.KEYEVENTF_KEYUP, 0)
            print('xia')
        elif s == '左':
            win32api.keybd_event(37, 0, 0, 0)  #左键-37
            time.slepp(1)
            win32api.keybd_event(37, 0, win32con.KEYEVENTF_KEYUP, 0)
            print('zuo')
        elif s == '右':
            win32api.keybd_event(39, 0, 0, 0)  #右键-39
            time.slepp(1)
            win32api.keybd_event(39, 0, win32con.KEYEVENTF_KEYUP, 0)
            print('you')

if __name__ == '__main__':
    wordsToAdd = ['上','下','左','右']
    speechReco = SpeechRecognition(wordsToAdd)
    while True:
        pythoncom.PumpWaitingMessages()