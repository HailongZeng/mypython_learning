import win32com
import win32com.client
import os

def makeWordFile(path, name):
    # 调用系统word功能
    word = win32com.client.Dispatch('Word.Application')
    #让文档可见
    word.Visible = True
    #创建文件
    doc = word.Documents.Add()

    #写入内容，从头开始写
    r = doc.Range(0, 0)
    r.InsertAfter('亲爱的'+name+'\n')
    r.InsertAfter('   最近可好...我很想你\n')
    #存储文件
    doc.SaveAs(path)
    #关闭文件
    doc.Close()
    #退出word
    word.Quit()


names = ['曾海龙', '曾海飞', '曾艳琴']
for name in names:
    path = os.path.join(os.getcwd(), name)
    makeWordFile(path, name)