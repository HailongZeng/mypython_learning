import csv
import sys
import importlib
importlib.reload(sys)
from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal, LAParams
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed
import win32com
import win32com.client
from collections import OrderedDict
from pyexcel_xls import get_data

class DealFile(object):
    #读取csv

    def readCsv(self, path):
        infoList = []
        with open(path, 'r') as f:
            allFileInfo = csv.reader(f)  # 将csv中的数据读出来存入allFileInfo中，allFileInfo是一个对象(object)
            for row in allFileInfo:  # 一行一行取数据
                infoList.append(row)  # 将数据存入列表
        return infoList

    #写csv [[1,2,3],[4,5,6],[7,8,9]]
    def writeCsv(self, path, data):
        with open(path, 'w') as f:
            writer = csv.writer(f)
            for rowData in data:
                print('rowData = ', rowData)
                writer.writerow(rowData)
    #读取pdf
    def readPDF(self, path, callback = None, toPath = ''):
        f = open(path, 'rb')  # 以二进制可读形式打开pdf文件，'rb'
        parser = PDFParser(f)  # 创建一个pdf文档分析器
        pdfFile = PDFDocument()  # 创建pdf文档
        parser.set_document(pdfFile)  # 链接文档对象与分析器
        pdfFile.set_parser(parser)  # 链接分析器与文档对象
        pdfFile.initialize('')  # 提供初始化密码
        # 检测文档是否提供txt转换
        if not pdfFile.is_extractable:  #
            raise PDFTextExtractionNotAllowed
        else:
            # 解析数据
            # #数据管理器
            manager = PDFResourceManager()
            # 创建一个PDF设备对象
            laparams = LAParams()
            device = PDFPageAggregator(manager, laparams=laparams)
            # 创建解释器对象
            interpreter = PDFPageInterpreter(manager, device)

            # 开始循环处理，每次处理一页，只能把文本读出来，图片读不出
            for page in pdfFile.get_pages():
                interpreter.process_page(page)
                layout = device.get_result()
                for x in layout:  # 循环处理图层
                    if isinstance(x, LTTextBoxHorizontal):  # 判断图层类型为LTTextBoxHorizontal才可以进行读取
                        if toPath == '':
                            #处理每行数据
                            str = x.get_text()
                            if callback != None:
                                callback(str)
                            else:
                                print(str)
                        else:
                            #写文件
                            print('将PDF数据写入文件')
    #读取word文件
    def readWordFileToOtherFile(path, toPath):
        # 调用系统word功能，可以处理doc和docx两种文件
        mw = win32com.client.Dispatch('Word.Application')
        # 打开文件
        doc = mw.Documents.Open(path)
        # 将word的数据保存到另一个文件
        doc.SaveAs(toPath, 2)  # 2表示文件格式为txt文件
        # 关闭文件
        doc.Close()
        # 退出word
        mw.Quit()
    #处理excel文件
    def readXlsAndXlsxFile(path):
        dic = OrderedDict()
        # 抓取数据
        xdata = get_data(path)  # 获取到整体数据
        for sheet in xdata:
            dic[sheet] = xdata[sheet]
        return dic
    #写ppt文件
    def makePPT(path):
        ppt = win32com.client.Dispatch('PowerPoint.Application')
        ppt.Visible = True

        # 增加一个文件
        pptFile = ppt.Presentations.Add()

        # 创建页
        page1 = pptFile.Slides.Add(1, 1)  # Add中参数1为页数，参数2为模板类型
        t1 = page1.Shapes[0].TextFrame.TextRange
        t1.Text = 'Hailong'
        t2 = page1.Shapes[1].TextFrame.TextRange
        t2.Text = 'Hailong is good'

        page2 = pptFile.Slides.Add(2, 1)  # Add中参数1为页数，参数2为类型
        t1 = page2.Shapes[0].TextFrame.TextRange
        t1.Text = 'Haifei'
        t2 = page2.Shapes[1].TextFrame.TextRange
        t2.Text = 'Haifei is good'
        # ......

        # 保存
        pptFile.SaveAs(path)
        pptFile.Close()
        ppt.Quit()


