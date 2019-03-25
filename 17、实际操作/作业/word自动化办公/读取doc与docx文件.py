#也可使用关于word的第三方库
import win32com
import win32com.client

def readWordFile(path):
    #调用系统word功能，可以处理doc和docx两种文件
    mw = win32com.client.Dispatch('Word.Application')
    #打开文件
    doc = mw.Documents.Open(path)
    for paragraph in doc.Paragraphs:
        line = paragraph.Range.Text
        print(line)
    #关闭文件
    doc.Close()
    #退出word
    mw.Quit()

path = '/Users/zenghailong/PycharmProjects/mypro001/17、实际操作/作业/word自动化办公/homework2.docx'
readWordFile(path)

