#! /usr/bin/env python
#coding=utf-8
'''
医技执行科室收费
'''

#日志对象初始化
import time
from selenium.webdriver.common.by import By
from UI.com_th_supcom_api.common import Common
from UI.com_th_supcom_api.common import Log
from UI.com_th_supcom_api.common.Cache import Cache
from UI.com_th_supcom_api.common.Common import select_dept, focus
from UI.com_th_supcom_api.common.Wait import on_click, send_value, is_refresh, element_wait, element_inexistence
from UI.com_th_supcom_portal_service.usercenter import login
from UI.com_th_supcom_portal_element.med_lab_bill_portal_element.outbill_pay_execute.pay_org import patient_message,select_window,application_detail,application_list
from UI.common_th_supcom_config.url_config import HOSPITA_AREA

log = Log.Logger(__name__)
def test_pay_org(browser,cache):
    log.info('开始运行医技执行科室收费脚本')
    login.select_workstation(browser, '医技工作站', cache)  # 工作站是否打开
    #获取申请单及执行科室
    application_type_list = ['检验单', '治疗单', '病理类','检查单']
    #对所有申请单进行归类整理，把执行科室相同的申请单归为一类
    for application_type in application_type_list:
        diction = cache.get(application_type)
        if diction:
            application = list(diction.keys())
            executive_department_list = list(diction.values())
            for t in list(set(executive_department_list)):
                on_click(browser,(By.XPATH,'//button[contains(text(),"【")]'))
                #选择工作站
                executive_department_name = HOSPITA_AREA+': '+t
                select_dept(browser, '选择工作台',executive_department_name,(By.XPATH,select_window.选择工作站))
                on_click(browser,(By.XPATH,"//button[contains(text(),'确定')]"))
                # is_refresh(browser,browser.find_element_by_xpath('//div[contains(text(),"门诊执行收退费")]'))
                element_wait(browser,(By.XPATH, '//div[contains(text(),"门诊执行收退费")]'))
                on_click(browser, (By.XPATH, '//div[contains(text(),"门诊执行收退费")]'))
                on_click(browser, (By.LINK_TEXT, '门诊执行科室收费'))
                # 刷卡
                date = time.strftime("%Y-%m-%d", time.localtime())
                send_value(browser, (By.XPATH, application_list.开单时间), '2017-06-15')
                send_value(browser, (By.XPATH, patient_message.卡号), cache.get('patient_card')+'\n')
                # 勾选是否打印
                on_click(browser, (By.XPATH, '//label[contains(text(),"是否打印收费凭证")]'))
                first_pos = 0
                for i in range(executive_department_list.count(t)):
                    element_inexistence(browser, (By.XPATH, "//div[contains(text(),'正在加载')]"))
                    new_list = executive_department_list[first_pos:]
                    next_pos = new_list.index(t) + 1
                    index = first_pos + new_list.index(t)
                    first_pos += next_pos
                    locator = (By.XPATH, '//div[contains(text(),"%s")]'%application[index])
                    on_click(browser,locator)
                    # time.sleep(2)
                    element_inexistence(browser,(By.XPATH,"//div[contains(text(),'正在加载')]"))
                    application_detail_text = browser.find_element_by_xpath(application_detail.申请单计费明细列表).text
                    if application_detail_text.strip()!='':
                        on_click(browser,(By.XPATH,'//button[contains(text(),"收费(Enter)")]'))
                        on_click(browser, (By.XPATH, '//button[contains(text(),"是")]'))
                    else:
                        log.info('%s申请单已计费'%application[index])
                element_wait(browser, (By.XPATH, application_detail.申请单计费明细列表))
                browser.refresh()





if __name__ == '__main__':
    cache = Cache({})
    browser = Common.browser()
    testcase = {'用户名': 'jfli', '密码': '123456'}
    login.test_login(browser, testcase, cache)
    # cache.set('检验单',{'02C201706-1900002':'妇产前诊断实验室','02C201706-1900004':'妇产前诊断实验室','02C201706-1900003':'检验科'})
    cache.set('检查单',{'02D2017061900012':'超声影像科','02D2017061900005':'放射科','02D2017061900008':'放射科'})
    # cache.set('病理类',{'02O201706-1600053':'病理科','02O201706-1600052':'病理科'})
    cache.set('patient_card','%E?;1004627675=99015017425?+E?')
    test_pay_org(browser,cache)









