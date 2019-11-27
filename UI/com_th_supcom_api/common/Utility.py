#! /usr/bin/env python
#coding=utf-8
'''
包含各种文件读入、解析等工具类
'''
import xlrd
import time  # 调入time函数
import zipfile
import os
from PIL import ImageGrab
# import win32gui
# import win32con
import UI.common_th_supcom_config.url_config as path
from sqlalchemy import create_engine

from sqlalchemy.orm import  sessionmaker

import datetime
import os
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'





'''
名称：SaveLog
入参：(list[col1,col2,col3....],boolean TestResult)
出参：写日志成功1，不成功0
示例：
请求：SaveLog((list,TestResult))
返回：1或0，将list和TestResult内容写日志
'''
def SaveLog(value, TestResult):
    if TestResult == 1:
        try:


            fileUrl = path.dir+'\\temp\\log\\log.txt'

            fileHandle = open(fileUrl, 'a')  # w覆盖写 a追加写
            fileHandle.write(str(time.strftime('%Y-%m-%d %X',time.localtime())+'\r\n')+str(value))
            return 1

            fileUrl = path.dir+'\\temp\\log\\log.txt'
            fileHandle = open(fileUrl, 'a',encoding='utf8')  # w覆盖写 a追加写
            fileHandle.write(str(time.strftime('%Y-%m-%d %X',time.localtime()))+'\t'+str(value)+'\r\n')
            logstatus = 1
        except Exception as enumerate:
            print(enumerate)
            # TestResult = False
            return 0

"""
GetTestcase
入参：(string filepath)
出参：(list[col1,col2,col3.....])
一行为一个列表，行中的列为一个元素
示例：
请求:GetTestcase(filepath)
返回:[[col1,col2,col3....],[col1,col2,col3....]]
要增加注释功能
"""
def GetTestcase(filepath,sheet_name):
    if not os.path.exists(filepath):
        raise  Exception("文件不存在!")
        return
    workbook = xlrd.open_workbook(filepath)  # 打开文件
    shxrange = range(workbook.nsheets)
    print(sheet_name)
    # sh = workbook.sheet_by_index(0)  # # 根据sheet索引或者名称获取sheet内容
    # print (workbook.sheet_names()) # [u'sheet1', u'sheet2'
    sh = workbook.sheet_by_name(sheet_name)
    lists = []
    list1=[]
    list2 = []
    list3 = []
    nrow = sh.nrows  # 行数
    ncol = sh.ncols  # 列数
    i = 0
    # 遍历sheet1中所有单元格cell
    for rown in range(1, nrow):  # 跳过第一行
        for coln in range(ncol):
            if sh.cell(rown, coln).ctype == 3:  # 判断单元格内容格式如果为日期类型
                cell = (sh.cell_value(rown, coln))
                cell = (xlrd.xldate.xldate_as_datetime(cell, 0).strftime('%Y-%m-%d'))  # 把日期 格式化
            elif sh.cell(rown, coln).ctype == 2:  # 判断单元格内容为数值型
                if int(sh.cell_value(rown, coln)) == (sh.cell_value(rown, coln)):
                    cell = int(sh.cell_value(rown, coln))  # 转换成整型
                else:
                    cell = sh.cell_value(rown, coln)
            elif sh.cell(rown, coln).ctype == 1:  # 判断为字符型 不转换
                cell = sh.cell_value(rown, coln)  # 获取单元格内容
            elif sh.cell(rown, coln).ctype == 0:
                cell = ''
            list1.insert((nrow - 1) * ncol-1 , cell)  # 把内容放入一个列表中

    coln = ncol  # 获取列数
    while coln <= (nrow-1) * ncol:  # 控制最大列表索引
        value = list1[coln - ncol:coln]  # 每行放入一个列表中
        coln = coln + ncol
        if list(set(value)) == ['']:
            break
        list2.insert(i, value)
        i = i + 1
    for coln in range(ncol):
        cell = sh.cell_value(0, coln)
        list3.append(cell)
    for i in range(0,len(list2)):
         nvs = zip(list3,list2[i])
         dictionary = dict( (name,value) for name,value in nvs)
         lists.append(dictionary)
    return lists


'''
名称：CapturePicture
入参：(boolean TestResult)
出参：(string boolean,fullsavepath)
示例：
请求：CapturePicture(TestResult)
返回，(1,fullsavepath)
'''
# def CapturePicture(TestResult,browser):
#     if TestResult == True:
#         browser.set_window_size(1200 , 900)
#         browser.implicitly_wait(30)
#         pjname = time.strftime("%Y%m%d%H%M%S", time.localtime()+ ".png")
#         print(pjname)
#         # str =datetime.now().strftime("%Y%m%d%H%M%S")
#         # adress=os.mkdir("D:\Python34\img\pjname")#创建文件夹
#         adress = "D:\\log\\img\\"
#         b = browser.save_screenshot(adress+pjname)
#         if b == True:
#             print("截图成功", b, "截图保存的地址为：", adress)
#             return (b, adress)
#             browser.close()
#         else:
#             return (b, adress)
#     else:
#         pass

'''
名称：getElements
入参：(listPath,browser)
出参：(list:elements)
'''
def getElements(browser,listPath):
    elements=[]
    for i in range(0,len(listPath)):
        elements.append(browser.find_element_by_xpath(listPath[i]))
    return elements

'''
名称：zipDirectory
入参：(boolean TestResult)
出参：(string boolean,fullsavepath)
示例：
请求：CapturePicture(TestResult)
返回，(1,fullsavepath)
'''
def zipFile(directoryUrl):
    f=zipfile.ZipFile('file.zip','w',zipfile.ZIP_DEFLATED)
    for dirpath,dirnames,filenames in os.walk(directoryUrl):
        for filename in filenames:
            f.write(os.path.join(dirpath,filename))
    f.close()

#截图
def capture(browser,imagename):


    imageUrl = path.dir+'\\temp\\img\\'+imagename+time.strftime("%Y%m%d%H%M%S", time.localtime())+'.jpg'
    imageUrl = path.dir+'\\temp\\img\\'+imagename+time.strftime("%Y%m%d%H%M%S", time.localtime())+'.jpg'
    im = ImageGrab.grab(bbox=(2,105,1278,942))
    im.save(imageUrl, 'png')
    return imageUrl


'''
名称:wirteFile
入参：(list string)
出参：(string)
'''
#将数据写入text文件中
def writeFile(data):
    try:
        fileUrl = path.dir + '\\temp\\vertify\\vertify.txt'
        fileHandle = open(fileUrl, 'a',encoding='utf8') # w覆盖写 a追加写
        fileHandle.write(str(time.strftime('%Y-%m-%d %X', time.localtime()))+'  '+ str(data) +  '\n')
        return 1
    except:
        return 0

'''
名称:readFile
入参：(string)
出参：(list)
'''
#读取文件中的数据

def readFile():
    fileUrl = path.dir+'\\temp\\vertify\\vertify.txt'
    f = open(fileUrl,"r",encoding='UTF-8')
    lines = f.readlines()  # 调用文件的 readline()方法
    return lines

#清空文件中的内容
def empty_file():
    fileUrl = path.dir + '\\temp\\vertify\\vertify.txt'
    f = open(fileUrl, "w", encoding='UTF-8')
    f.truncate()
    f.close()


#打印机
#listUrl  单据保存路径
# def microsoft_xps_document_writer(file_name):
#
#      url = path.dir+'\\temp\\bill\\'+file_name
#      print(url)
#      while True:
#          time.sleep(3)
#          for title in path.print_title:
#              dialog = win32gui.FindWindow('#32770', title)  # 对话框
#              if dialog != 0:
#                  break
#          if dialog == 0:
#              break
#          else:
#
#             pjname = time.strftime("%Y%m%d%H%M%S", time.localtime())
#
#             DUIViewWndClassName = win32gui.FindWindowEx(dialog, 0, 'DUIViewWndClassName', None)
#
#             DirectUIHWND = win32gui.FindWindowEx(DUIViewWndClassName, 0, 'DirectUIHWND', None)
#
#             FloatNotifySink = win32gui.FindWindowEx(DirectUIHWND, 0, 'FloatNotifySink', None)
#
#             ComboBox = win32gui.FindWindowEx(FloatNotifySink, 0, 'ComboBox', None)
#
#             Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)  # 上面三句依次寻找对象，直到找到输入框Edit对象的句柄
#
#             button = win32gui.FindWindowEx(dialog, 0, 'Button', None)  # 确定按钮Button
#
#             win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, url+str(pjname))  # 往输入框输入绝对地址
#
#             win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 按button

#连接数据库
def db_session(DB_HOST):
    engine = create_engine(DB_HOST, encoding='utf-8')
    Session_class = sessionmaker(bind=engine)
    Session = Session_class()  # 生成session实例
    return Session


#自定义异常
def throw_error(message):
    raise Exception(message)  # 异常被抛出，print函数无法执行




