import sys
import importlib
importlib.reload(sys)

from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal, LAParams
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed

def readPDF(path, toPath):
    f = open(path, 'rb')          #以二进制可读形式打开pdf文件，'rb'
    parser = PDFParser(f)         #创建一个pdf文档分析器
    pdfFile = PDFDocument()       #创建pdf文档
    parser.set_document(pdfFile)  #链接文档对象与分析器
    pdfFile.set_parser(parser)    #链接分析器与文档对象
    pdfFile.initialize('')        #提供初始化密码
    #检测文档是否提供txt转换
    if not pdfFile.is_extractable:  #
        raise PDFTextExtractionNotAllowed
    else:
        #解析数据
        # #数据管理器
        manager = PDFResourceManager()
        #创建一个PDF设备对象
        laparams = LAParams()
        device = PDFPageAggregator(manager, laparams=laparams)
        # 创建解释器对象
        interpreter = PDFPageInterpreter(manager, device)

        #开始循环处理，每次处理一页，只能把文本读出来，图片读不出
        for page in pdfFile.get_pages():
            interpreter.process_page(page)
            layout = device.get_result()
            for x in layout: #循环处理图层
                if isinstance(x, LTTextBoxHorizontal):  #判断图层类型为LTTextBoxHorizontal才可以进行读取
                    with open(toPath, 'a') as f:   #以追加的方式往txt里面写
                        str = x.get_text()
                        print(str)
                        f.write(str + '\n')



path = '/Users/zenghailong/PycharmProjects/mypro001/17、实际操作/作业/读取pdf文件/GreedIsGood.pdf'
toPath = '/Users/zenghailong/PycharmProjects/mypro001/17、实际操作/作业/读取pdf文件/GreedIsGood.txt'
readPDF(path, toPath)