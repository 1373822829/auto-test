#! /usr/bin/env python
#coding=utf-8
'''
#欠费结账
'''

#日志初始化
import re

import time

from UI.com_th_supcom_api.common import Common

from UI.com_th_supcom_api.common.Cache import Cache

from UI.com_th_supcom_portal_dao.outp_bill_portal_dao.RegistVerify import find_rek_no
from selenium.webdriver.common.by import By
from UI.com_th_supcom_api.common import Log
from UI.com_th_supcom_api.common.Utility import microsoft_xps_document_writer
from UI.com_th_supcom_api.common.Wait import on_click, send_value, element_wait, get_prompt, is_text, get_text, \
    is_selected
from UI.com_th_supcom_portal_element.outp_bill_portal_element.arrearage_settle.arrearage_settle_accounts import patient_message,recharge_window,\
    arrearage_list,arrearage_return_premium
from UI.com_th_supcom_portal_service.usercenter import login


log = Log.Logger(__name__)


def test_arrearage_settle_accounts(browser,cache):
    log.info('开始运行欠费结账脚本')
    login.select_workstation(browser, '门诊挂号收费工作台', cache)  # 工作站是否打开
    on_click(browser,(By.XPATH,'//div[contains(text(),"欠费管理")]'))
    on_click(browser,(By.LINK_TEXT,'欠费结账/退费'))
    boolen = get_prompt(browser)
    if  boolen:
        if re.sub('\D', '', boolen) == '0':
           log.info(boolen)
           return
        else:
           on_click(browser, (By.XPATH, "//button[contains(text(),'确定')]"))
    #刷卡
    send_value(browser,(By.XPATH,patient_message.刷卡),cache.get('patient_card')+'\n')
    on_click(browser,(By.XPATH,'//button[contains(text(),"收 费")]'))
    on_click(browser,(By.XPATH,'//button[contains(text(),"是")]'))
    text = get_text(browser,(By.XPATH,"//label"))
    if "交款方式" not in text:
        microsoft_xps_document_writer('欠费结账单')
    else:
        send_value(browser, (By.XPATH, recharge_window.支付类型), '1')
        on_click(browser, (By.XPATH, '//button[contains(text(),"确认")]'))
        on_click(browser, (By.XPATH, '//button[contains(text(),"是")]'))
        microsoft_xps_document_writer('欠费结账充值单')

#欠费退费
def test_arrearage_return_premium(browser,cache):
    log.info('开始运行欠费退费脚本')
    login.select_workstation(browser, '门诊挂号收费工作台', cache)  # 工作站是否打开
    on_click(browser,(By.XPATH,'//div[contains(text(),"欠费管理")]'))
    on_click(browser,(By.LINK_TEXT,'欠费结账/退费'))
    boolen = get_prompt(browser)
    if  boolen:
        if re.sub('\D', '', boolen) == '0':
           log.info(boolen)
           return
        else:
           on_click(browser, (By.XPATH, "//button[contains(text(),'确定')]"))
    #刷卡
    send_value(browser,(By.XPATH,patient_message.刷卡),cache.get('patient_card')+'\n')
    end_time = time.time()+1
    # arrearage_list_text = ''    #欠费记账列表信息
    while True:
        arrearage_list_text = get_text(browser,(By.XPATH,arrearage_list.欠费记账患者列表))
        if '暂无可显示的欠费病人信息' not in arrearage_list_text:
            break
        if time.time()>end_time:
            log.info('欠费记账患者列表加载超时')
            return
    lists = ['处方单', '毒麻单', '检查单', '检验单', '治疗单', '皮试单', '输液单', '草药', '病理类']
    applys = []     #所有申请单号
    for appply_type in lists:
        applycation = cache.get(appply_type)
        if applycation:
            applys = applys+list(applycation)
    for apply_id in applys:
        if is_selected(browser,((By.XPATH, arrearage_list.全选))):
             on_click(browser, (By.XPATH, arrearage_list.全选))
        rek_no = find_rek_no(apply_id)
        if rek_no == []:
            log.info('%s申请单未计费或已退费'%rek_no)
            continue
        elif rek_no in arrearage_list_text:
            on_click(browser,(By.XPATH,'//div[contains(text(),"%s")]'%rek_no))
            on_click(browser,(By.XPATH,'//div[contains(text(),"退 费")]'))
            element_wait(browser,(By.XPATH,'//span[contains(text(),"欠费记账退费窗口")]'))
            if '正常' in get_text(browser,(By.XPATH,arrearage_return_premium.退费列表)):
                webElement = browser.find_elements_by_xpath(arrearage_return_premium.退费列表+'//label[contains(text(),"正常")]')
                for element in webElement:
                    element.click()
            on_click(browser,(By.XPATH,'//button[contains(text(),"确定退费")]'))
            on_click(browser, (By.XPATH, '//button[contains(text(),"是")]'))
            microsoft_xps_document_writer('欠费退费单')



if __name__ == '__main__':
    cache = Cache({})
    browser = Common.browser()
    testcase = {'用户名': 'jfli', '密码': '123456'}
    login.test_login(browser, testcase, cache)
    cache.set('quit_sign', ['王易', '呼吸内科急诊', '普通', '刘馗', '2017-06-09'])
    cache.set('处方单', {'02A201706-1300038': '门诊药房(光谷)', '02C201706-1900005': '门诊药房(光谷)'})
    cache.set('检查单', {'02D2017062100011': '放射科', '02D2017062100065': '超声影像科'})
    cache.set('patient_card', '%E?;2501218606=99015012538?+E?')
    test_arrearage_return_premium(browser, cache)

























