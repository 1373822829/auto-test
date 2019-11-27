#! /usr/bin/env python
#coding=utf-8
'''
退号信息列表
'''
import time
from selenium.webdriver.common.by import By
from UI.com_th_supcom_api.common import Common
from UI.com_th_supcom_api.common import Log
from UI.com_th_supcom_api.common.Cache import Cache
from UI.com_th_supcom_api.common.Common import select_lists, calendar
from UI.com_th_supcom_api.common.Wait import on_click
from UI.com_th_supcom_portal_element.outp_bill_portal_element.reg_manager.outp_patient_quit_sign_list import head_button,body
from UI.com_th_supcom_portal_service.usercenter import login

#日志对象初始化



log = Log.Logger(__name__)
def test_quit_sign_list(browser,cache):
    log.info('开始运行退号信息列表脚本')
    login.select_workstation(browser, '门诊挂号收费工作台', cache)  # 工作站是否打开
    on_click(browser, (By.XPATH, '//div[contains(text(),"门诊挂号")]'))
    on_click(browser, (By.LINK_TEXT, '退号信息列表'))
    remove_js = 'document.getElementsByTagName("input")[26].removeAttribute("readonly")'
    focus_js = "document.getElementsByTagName('input')[26].blur()"
    input_locator = (By.XPATH,head_button.退号开始日期)
    img_locator = (By.XPATH,head_button.退号开始日历)
    date = time.strftime("%Y-%m-%d", time.localtime())
    calendar(browser, remove_js, focus_js, input_locator, img_locator, date)
    on_click(browser,(By.XPATH,'//button[contains(text(),"查询")]'))
    if select_lists(browser, (By.XPATH,body.号源列表), cache.get('quit_sign')):
        log.info('退号列表显示pass')
    else:
        log.info('退号列表显示pass')
    log.info('退号信息列表脚本运行结束')
if __name__ == '__main__':
    cache = Cache({})
    browser = Common.browser()
    testcase = {'用户名': 'jfli', '密码': '123456'}
    login.test_login(browser, testcase, cache)
    cache.set('quit_sign',['王易','呼吸内科急诊','普通','刘馗','2017-06-09'])
    test_quit_sign_list(browser, cache)

