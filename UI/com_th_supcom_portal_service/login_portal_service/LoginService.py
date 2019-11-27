#! /usr/bin/env python
#coding=utf-8
'''
登录
'''
import UI.com_th_supcom_portal_element.login_portal_element.LoginElement as LoginElement

#登录工作台
def Login(browser):
    browser.maximize_window()
    browser.implicitly_wait(30)
    usernameElement = browser.find_element_by_xpath(LoginElement.input[0]['key'])
    usernameElement.clear()
    usernameElement.send_keys('jfli')
    pswElement = browser.find_element_by_xpath(LoginElement.input[1]['key'])
    pswElement.clear()
    pswElement.send_keys('123456' + '\n')
    browser.implicitly_wait(30)







