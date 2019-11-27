# ! /usr/bin/env python
# coding=utf8
'''
浏览器等待
'''
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from UI.com_th_supcom_api.common import Log
import selenium.webdriver.support.ui as ui

'''
'''
#日志对象初始化
log = Log.Logger(__name__)
#元素是否出现
def element_wait(browser,locator):
    try:
      WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located(locator))
      return True
    except TimeoutException as e:
        log.info('%s元素不存在'%locator[1])
        return False

#等待元素被加载
def element_inexistence(browser,locator):
    try:
      WebDriverWait(browser, 3, 0.1).until_not(EC.presence_of_element_located(locator))
      return True
    except TimeoutException as e:
        log.info('%s元素异常'%locator[1])
        return False

#等待页面被加载
def is_title(browser,title):
    try:
      WebDriverWait(browser, 20, 0.5).until(EC.title_contains(title)(browser))
      return True
    except EC.NoSuchElementException as e:
        log.info('%s页面加载失败'%title)
        return False

#等待的元素是否可见
def is_visible(browser,locator):
    if element_wait(browser,locator):
        if EC.visibility_of_element_located(locator):
            return True
    else:
        log.info('%s元素不可见'%locator)
        return False

# 一直等待某个元素消失，默认超时10秒
def is_not_visible(browser,locator):
    try:
        ui.WebDriverWait(browser,65,0.5).until_not(EC.visibility_of_element_located(locator))
        return True
    except TimeoutException:
        return False

#判断某段文本是否存在元素中
def is_text(browser,locator,text):
    try:
      WebDriverWait(browser, 5, 0.5).until(EC.text_to_be_present_in_element(locator,text))
      return True
    except EC.WebDriverException as e:
        log.info('%s不存在文本%s'%(locator[1],text))
        return False

#判断某段value是否存在元素中
def is_value(browser,locator,value):
    try:
        WebDriverWait(browser, 2, 0.5).until(EC.text_to_be_present_in_element_value(locator, value))
        return True
    except EC.WebDriverException as e:
        log.info('%s不存在文本%s'%(locator[1],value))
        return False

#判断元素是否可点击,并点击
def on_click(browser,locator):
    try:
        element_wait(browser,locator)
        WebDriverWait(browser, 50, 0.5).until(EC.element_to_be_clickable(locator))
        browser.find_element(locator[0],locator[1]).click()
        return True
    except EC.WebDriverException as e:
        # print(e)
        log.info('%s元素不能点击'%locator[1])
        return False


#判断元素是否被选择
def is_selected(browser,locator):
    try:
        WebDriverWait(browser, 2, 0.5).until(EC.element_located_to_be_selected(locator))
        return True
    except EC.WebDriverException as e:
        log.info('%s元素没有被选择'%locator[1])
        return False

#判断元素是否输入
def send_value(browser,locator,value):
    try:
        element_wait(browser, locator)
        WebDriverWait(browser, 10, 0.5).until(EC.presence_of_element_located(locator))
        browser.find_element(locator[0],locator[1]).clear()
        browser.find_element(locator[0],locator[1]).send_keys(value)
        if '%' not in value:
            if value == get_value(browser,locator):
                pass
    except EC.WebDriverException as e:
        log.info('%s元素输入失败'%locator[1])




#判断页面是否刷新
def is_refresh(browser,webElement):
    try:
        WebDriverWait(browser, 10, 0.5).until(EC.staleness_of(webElement))
        return True
    except EC.WebDriverException as e:
        log.info('页面刷新失败')
        return False

#获取是否弹出提示框，并获取其中的内容
def get_prompt(browser):
    if element_wait(browser, (By.XPATH, '//span[contains(text(),"提示")]')):
        time.sleep(1)
        index = len(browser.find_elements(By.XPATH, 'html/body/div'))
        # print('index: '+str(index))
        texts = browser.find_element(By.XPATH, 'html/body/div' + str([index - 1])).text
        # print(texts.split())
        text = texts.split()[1]
        # log.info(text)
        return text
    else:
        log.info('获取提示框内容失败')
        return False

#获取弹出窗口
def window(browser,value):
    if element_wait(browser, (By.XPATH, '//span[contains(text(),"'+value+'")]')):
        time.sleep(0.5)
        index = len(browser.find_elements(By.XPATH, 'html/body/div'))
        # print('index: '+str(index))
        texts = browser.find_element(By.XPATH, 'html/body/div' + str([index - 1])).text
        # print(texts.split())
        text = texts.split()[1]
        # log.info(text)
        return text
    else:
        log.info('获取弹出窗口失败')
        return False


#获取元素文本
def get_text(browser,locator):
    element_wait(browser,locator)
    webElement = browser.find_element(locator[0],locator[1])
    if hasattr(webElement,'text'):
        text = webElement.text
        return text
    else:
        log.info('%s没有text属性'%locator[1])

#获取元素value
def get_value(browser,locator):
    element_wait(browser, locator)
    webElement = browser.find_element(locator[0], locator[1])
    if hasattr(webElement, 'get_attribute'):
        value = webElement.get_attribute('value')
        return value
    else:
        log.info('%s没有text属性' % locator[1])




