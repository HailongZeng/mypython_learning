import win32com
import win32com.client

def makePPT(path):
    ppt = win32com.client.Dispatch('PowerPoint.Application')
    ppt.Visible = True

    #增加一个文件
    pptFile = ppt.Presentations.Add()

    #创建页
    page1 = pptFile.Slides.Add(1,1)  #Add中参数1为页数，参数2为模板类型
    t1 = page1.Shapes[0].TextFrame.TextRange
    t1.Text = 'Hailong'
    t2 = page1.Shapes[1].TextFrame.TextRange
    t2.Text = 'Hailong is good'

    page2 = pptFile.Slides.Add(2,1)  # Add中参数1为页数，参数2为类型
    t1 = page2.Shapes[0].TextFrame.TextRange
    t1.Text = 'Haifei'
    t2 = page2.Shapes[1].TextFrame.TextRange
    t2.Text = 'Haifei is good'
    #......

    #保存
    pptFile.SaveAs(path)
    pptFile.Close()
    ppt.Quit()


path = ''
makePPT(path)