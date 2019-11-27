#! /usr/bin/env python
#coding=utf-8
'''
脚本公共步骤，包括初始化，资源释放等
'''
from selenium import webdriver
from selenium.webdriver.common.by import By

import UI.com_th_supcom_api.common.Utility as utility
import UI.common_th_supcom_config.test_case_config.TestCaseUrl as file
from selenium.webdriver.common.keys import Keys
import time
from UI.com_th_supcom_api.common import Log
from UI.com_th_supcom_api.common.Wait import on_click, send_value, element_wait, window
import getpass

log = Log.Logger(__name__)
#浏览器对象初始化

import getpass
import threading

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys

from UI.common_th_supcom_config.url_config import localhost
# lists = ['http://192.168.6.44:5555/wd/hub']

def browser(ip):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
    options.add_argument("--user-data-dir=" + r"C:\Users\%s\AppData\Local\Google\Chrome\User Data" % getpass.getuser())
    caps = options.to_capabilities()
    host = 'http://%s:8080/wd/hub'%ip
    driver = webdriver.Remote(
        command_executor=host,
        desired_capabilities=caps
    )
    return driver

# def action_browser(lists):
#     thread = []
#     files = range(len(lists))
#     #创建线程
#     for host in lists:
#         t = threading.Thread(target=browser,args=(host,))
#         thread.append(t)
#     for i in files:
#         thread[i].start()
#     for i in files:
#         thread[i].join()



#工作站之间的转换
def switch_window(browser,windowname,cache):
    #判断该窗口是否打开
    if windowname in cache.keys():
        return True
    else:
        return False



#工作站之间的转换
def switchWindow(browser,windowname):
    all_handles = browser.window_handles
    for handle in all_handles:
        browser.switch_to.window(handle)
        if windowname in browser.title:
            #browser.switch_to_window(handle)
            break


#处理窗口工作站名称，去掉版本号
def workStation_name_modify(workStation_name):
    if ' V' in workStation_name:
        return workStation_name.split(' V')[0]
    else:
        return workStation_name

#读取测试用例
def read_test_case(testcase_name):
    list = utility.GetTestcase(file.getUrl[testcase_name])
    return list


'''
param_xpath:包含整个滚动条的元素路径
param_text:需要查找的元素的文本
message:抛出异常信息
'''
#处理滚动条
def scroll_bar(browser,xpath,text,message):
    num = 0
    j = 0
    time.sleep(2)
    while True:
        # span_elements = browser.find_element_by_xpath(xpath).find_elements_by_tag_name('span')#获取元素下所有的span
        div_elements = browser.find_elements_by_xpath(xpath)#获取元素下所有的div
        if j == len(div_elements): #当j == len(span_elements)时，滚动条已移动到最底部，未找到元素，抛出异常
            raise Exception(message)
        for element in div_elements:
            text_elements = element.find_elements_by_tag_name('div')
            for i in range(j, len(text_elements)):
                j += 1
                js = "arguments[0].scrollIntoView();"
                browser.execute_script(js, text_elements[5])
                if text_elements[i].text == text:  #找到元素时，点击该元素并将num赋值为1
                    text_elements[i].click()
                    num = 1
        if num == 1: break  #找到元素，则停止循环

#处理滚动条
'''
driver:浏览器对象
locator:元素
'''
def focus(driver, locator):
    """Sets focus to element identified by `locator`."""
    element_wait(driver,locator)
    target = driver.find_element(locator[0],locator[1])
    driver.execute_script("arguments[0].scrollIntoView();", target)  # 拖动到可见的元素去
    on_click(driver,locator)
    return

'''
入参：（class browser,str input_js,str img_js,tuple img_locator,tuple img_locator,time date）
browser  浏览器对象
remove_js  移除日历input中readonly属性
focus_js   日历input失去焦点
input_locator  日历输入框定位
img_locator  日历图标定位
date   日期
'''
#日历处理
def calendar(browser, remove_js,focus_js, input_locator,img_locator,date):

    browser.execute_script(remove_js)
    send_value(browser,input_locator,date)
    browser.execute_script(focus_js)
    time.sleep(2)
    on_click(browser, img_locator)
    browser.find_element_by_xpath("//button[contains(text(),'今天')]").send_keys(Keys.ENTER)


#过滤后从列表中选择所需要的数据
def filter_lists(browser,locator,list_message,num,tab):
    end_time = time.time() + 1
    while True:
        if len( browser.find_elements(locator[0],locator[1]))<num:
            break
        if time.time()>end_time:
            break
        time.sleep(0.5)
    special_elements = browser.find_elements(locator[0],locator[1])
    for i in range(0, len(special_elements)):
        special_message_elements = browser.find_elements(locator[0],locator[1])[i]
        texts = (special_message_elements.text).split()
        print(texts)
        boolen = fun(list_message,texts)
        if ('已达次数上限' in texts ) or texts[9] == '3':
            return texts
        if boolen:
            locator = (locator[0], locator[1] + str([i + 1]) + '//'+tab)
            on_click(browser, locator)
            return texts
        else:
            texts = []
    return False

#判断集合list1是否包含list2
def fun(list_message,texts):
    for text in list_message:
        if text not in texts:
            return False
    return True

#从列表中选择所需要都的数据
def select_lists(browser,locator,list_message):
    element_wait(browser,locator)
    elements =  browser.find_elements(locator[0],locator[1])
    for i in range(0, len(elements)):
        message_elements = browser.find_elements(locator[0],locator[1])[i]
        texts = (message_elements.text).split()

        boolen = fun(list_message,texts)
        if boolen:
            locator = (locator[0], locator[1] + str([i + 1]) + '//div')
            print(locator)
            on_click(browser, locator)
            return texts
    return False

#选择执行科室
'''
browser:浏览器对象
value:窗口名称
dept_name:执行科室
locator:元素
'''
def select_dept(browser,value,dept_name,locator):
    # print(locator)
    time.sleep(1)
    if window(browser,value):
        on_click(browser,locator)
        focus(browser,(By.XPATH,("//div[contains(text(),'%s')]"%dept_name)))
    else:
        log.info('%s窗口未打开'%value)



#浏览器对象释放
def tear_down(browser):
    browser.quit()


