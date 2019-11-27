#! /usr/bin/env python
#coding=utf-8
'''
补打挂号单
'''
from selenium.webdriver.common.by import By

from UI.com_th_supcom_api.common import Common
from UI.com_th_supcom_api.common import Log
#日志对象初始化
from UI.com_th_supcom_api.common import Utility
from UI.com_th_supcom_api.common.Cache import Cache
from UI.com_th_supcom_api.common.Common import filter_lists
from UI.com_th_supcom_api.common.Wait import on_click, send_value
from UI.com_th_supcom_portal_element.outp_bill_portal_element.reg_manager.outp_patient_repair_reg import head_button,repair_reg_body
from UI.com_th_supcom_portal_service.usercenter import login
from UI.common_th_supcom_config.test_case_config.TestCaseCodeTable import repair_reg

log = Log.Logger(__name__)
def test_repair_reg(browser,testcase,cache):
    log.info('开始运行补打挂号单脚本')
    login.select_workstation(browser, '门诊挂号收费工作台', cache)  # 工作站是否打开
    on_click(browser, (By.XPATH, '//div[contains(text(),"门诊挂号")]'))
    on_click(browser, (By.LINK_TEXT, '补打挂号单'))

    #刷卡
    for i in range(0,3):
        send_value(browser,(By.XPATH,head_button.就诊卡号),testcase[repair_reg['patient_card']]+'\n')
        locator = (By.XPATH, repair_reg_body.号源列表 + '//tr')
        num = len(browser.find_elements(locator[0], locator[1]))  # 号源列表的数量
        send_value(browser,(By.XPATH,head_button.查询条件),testcase[repair_reg['doctor_name']])
        list_message = [testcase[repair_reg['special_name']],testcase[repair_reg['special_type']],testcase[repair_reg['outp_time']]]
        boolen = filter_lists(browser,locator,list_message,num,'button')
        if not boolen:
            log.info('没有号源信息')
            return
        if boolen[9] == '3' or ('已达次数上限' in boolen):
            if boolen[9] == '3' and ('已达次数上限' in boolen):
                log.info('补打挂号单验证pass')
                break
            else:
                log.info('补打挂号单验证fail')
                break
        on_click(browser,(By.XPATH,'//button[contains(text(),"是")]'))
        Utility.microsoft_xps_document_writer('补打挂号单')
    log.info('补打挂号单脚本运行结束')

if __name__ == '__main__':
    cache = Cache({})
    browser = Common.browser()
    testcase = {'用户名': 'jfli', '密码': '123456'}
    login.test_login(browser, testcase, cache)
    testcase = {'门诊科室编码': 'xhnkmz', '医生编码': 'ldm', '门诊科室': '消化内科门诊', '医生': '李德民', '门诊时间': '下午',
                '专科名称': '消化内科', '患者卡号': '%E?;2001102623=99015015172?+E?', '号源类别': '专家'}
    test_repair_reg(browser, testcase, cache)