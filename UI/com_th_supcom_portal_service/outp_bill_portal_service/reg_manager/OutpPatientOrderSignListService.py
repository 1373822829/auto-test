#! /usr/bin/env python
#coding=utf-8
'''
内部挂号列表
'''
import time
from selenium.webdriver.common.by import By

from UI.com_th_supcom_api.common import Common
from UI.com_th_supcom_api.common import Log
from UI.com_th_supcom_api.common.Cache import Cache
from UI.com_th_supcom_api.common.Common import select_lists
from UI.com_th_supcom_api.common.Wait import on_click, send_value
from UI.com_th_supcom_portal_element.outp_bill_portal_element.reg_manager.outp_patient_order_sign_list import head_button,body

from UI.com_th_supcom_portal_service.usercenter import login

#日志对象初始化


log = Log.Logger(__name__)
def test_order_sign_list(browser,cache):
    log.info('开始运行内部挂号列表脚本')
    login.select_workstation(browser, '门诊挂号收费工作台', cache)  # 工作站是否打开
    on_click(browser, (By.XPATH, '//div[contains(text(),"门诊挂号")]'))
    on_click(browser, (By.LINK_TEXT, '内部挂号列表'))
    # send_value(browser,(By.XPATH,head_button.查询条件),cache['name'])
    special_element = browser.find_element(By.XPATH,body.号源列表)
    if '没有可显示的数据....' in special_element.text:
        log.info('内部挂号没有号源信息')
        return
    locator = (By.XPATH,body.号源列表+'/div')
    list_messages = cache['business_type']
    if not list_messages:
        log.info('内部挂号没有号源信息')
        return
    for list_message in list_messages:
        boolen = select_lists(browser,locator,list_message)
        if boolen:
            if boolen[0] == '留号':
                index = 12
            if boolen[0] == '加号':
                index = 13
            if boolen and boolen[index] == '未取号':
                on_click(browser,(By.XPATH,'//button[contains(text(),"取消预约")]'))
                on_click(browser, (By.XPATH, '//button[contains(text(),"是")]'))
        else:
            log.info('内部挂号列表验证fail')
            return
if __name__ == '__main__':
    cache = Cache({})
    browser = Common.browser()
    testcase = {'用户名': 'jfli', '密码': '123456'}
    login.test_login(browser, testcase, cache)
    cache.set('business_type',[['王易','加号','肝脏内科','下午','周毅'],['杨竣熙','加号','肝脏内科','上午','周毅']])
    # testcase = {'门诊时间': '下午', '患者姓名': '杨俊熙', '医生': '李德民', '门诊科室': '消化内科门诊', '就诊时间': '2017-06-05',
    #             '患者卡号': '%E?;1004627675=99015017425?+E?', '专科名称': '消化内科','号源类别':'专家'}
    test_order_sign_list(browser, cache)

