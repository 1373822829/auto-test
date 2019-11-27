#! /usr/bin/env python
#coding=utf-8
'''
预付费缴费
'''

#日志初始化
import re

import time
from selenium.webdriver.common.by import By
from UI.com_th_supcom_api.common import Common
from UI.com_th_supcom_api.common import Log
from UI.com_th_supcom_api.common.Cache import Cache
from UI.com_th_supcom_api.common.Common import focus
from UI.com_th_supcom_api.common.Utility import microsoft_xps_document_writer
from UI.com_th_supcom_api.common.Wait import on_click, send_value, element_wait, get_prompt, is_text, get_text
from UI.com_th_supcom_portal_service.usercenter import login
from UI.com_th_supcom_portal_element.outp_bill_portal_element.out_bill_manager.out_bill_prepay import head_button,application_list_window,body

log = Log.Logger(__name__)
def test_prepay(browser,cache):
    log.info('开始运行预付费缴费脚本')
    login.select_workstation(browser, '门诊挂号收费工作台', cache)  # 工作站是否打开
    on_click(browser,(By.XPATH,'//div[contains(text(),"门诊缴费管理")]'))
    on_click(browser,(By.LINK_TEXT,'预付费缴费'))
    boolen = get_prompt(browser)
    if  boolen:
        if re.sub('\D', '', boolen) == '0':
           log.info(boolen)
           return
        else:
           on_click(browser, (By.XPATH, "//button[contains(text(),'确定')]"))

    lists = ['处方单', '毒麻单', '检查单', '检验单', '治疗单', '皮试单', '输液单', '草药', '病理类']
    click_application(browser,lists,cache)
    # 收费状态
    cache.set('prepay_status',1)





def click_application(browser,application_type_list,cache):
    for application_type in application_type_list:
        diction = cache.get(application_type)
        if diction:
            application_list = list(diction.keys())
            executive_department_list = list(diction.values())

            for t in list(set(executive_department_list)):
                # 刷卡
                send_value(browser, (By.XPATH, head_button.刷卡), cache.get('patient_card')+'\n')
                # 判断弹出窗口是否正确弹出
                if not is_text(browser, (By.XPATH, application_list_window.申请单列表), '申请单列表'):
                    log.info('没有找到申请单列表窗口')
                    return
                apply_messages = get_text(browser,(By.XPATH,application_list_window.申请单信息))
                if application_type in ['处方单', '毒麻单','草药']:
                   on_click(browser, (By.XPATH, "//span[contains(text(),'全部药品')]"))
                date = time.strftime("%Y-%m-%d", time.localtime())
                send_value(browser, (By.XPATH, application_list_window.开始时间), date)
                on_click(browser, (By.XPATH, "//button[contains(text(),'查询(Q)')]"))
                first_pos = 0
                status = False   #执行状态
                for i in range(executive_department_list.count(t)):
                    new_list = executive_department_list[first_pos:]
                    next_pos = new_list.index(t) + 1
                    index = first_pos + new_list.index(t)
                    print(application_list[index])
                    first_pos += next_pos
                    locator = (By.XPATH,'//div[contains(text(),"'+application_list[index]+'")]')
                    if application_list[index] in apply_messages:
                        status = True
                        focus(browser, locator)
                    else:
                        log.info('不存在%s申请单' % application_list[index])
                if not status :
                    on_click(browser,(By.XPATH,'//button[contains(text(),"取消(C)")]'))
                    continue
                on_click(browser, (By.XPATH, "//button[contains(text(),'确定(S)')]"))
                time.sleep(0.5)
                send_value(browser,(By.XPATH, body.缴费方式),'\n')
                if get_prompt(browser):
                   on_click(browser, (By.XPATH, "//button[contains(text(),'是')]"))
                   microsoft_xps_document_writer(application_type)
    log.info('预付费缴费脚本运行结束')



if __name__ == '__main__':
    cache = Cache({})
    browser = Common.browser()
    testcase = {'用户名': 'jfli', '密码': '123456'}
    login.test_login(browser, testcase, cache)
    cache.set('quit_sign', ['王易', '呼吸内科急诊', '普通', '刘馗', '2017-06-09'])
    cache.set('处方单',{'02A201706-1300038':'门诊药房(光谷)','02A201706-1300039':'门诊药房(光谷)'})
    cache.set('检查单',{'02D2017061300046':'放射科','02D2017061200055':'超声影像科'})
    cache.set('patient_card','%E?;2501218606=99015012538?+E?')
    test_prepay(browser, cache)


