#! /usr/bin/env python
#coding=utf-8
'''
发票打印
'''

#日志初始化
import re

import time
from selenium.webdriver.common.by import By
from UI.com_th_supcom_api.common import Common
from UI.com_th_supcom_api.common import Log
from UI.com_th_supcom_api.common.Cache import Cache
from UI.com_th_supcom_api.common.Utility import microsoft_xps_document_writer
from UI.com_th_supcom_api.common.Wait import on_click, send_value, element_wait,get_text, get_prompt
from UI.com_th_supcom_portal_dao.outp_bill_portal_dao.RegistVerify import find_min_ticket, find_rek_no, \
    find_mechanism_numbe
from UI.com_th_supcom_portal_element.outp_bill_portal_element.local import head
# from UI.com_th_supcom_portal_service.outp_bill_portal_service.out_bill_print.InvoicePrint import test_invoice_print
from UI.com_th_supcom_portal_service.usercenter import login
from UI.com_th_supcom_portal_element.outp_bill_portal_element.out_bill_print.invoice_record_query import invoice_history_list,query_area
from UI.com_th_supcom_portal_element.outp_bill_portal_element.out_bill_print.invoice_print import verify_bill_window

#日志初始化
log = Log.Logger(__name__)
#发票重打
def test_invoice_print_again(browser,cache):
    log.info('开始运行发票重打脚本')
    if not invoice_record_query(browser,cache):
        return
    consume_collection = get_text(browser, (By.XPATH, invoice_history_list.发票记录))
    mechanism_numbe = find_mechanism_numbe(cache.get('rek_no_list'))
    print(mechanism_numbe)
    if mechanism_numbe and (mechanism_numbe[0] in consume_collection):
            on_click(browser,(By.XPATH,'//div[contains(text(),"%s")]'%mechanism_numbe))
            on_click(browser, (By.XPATH, "//button[contains(text(),'重打')]"))
            microsoft_xps_document_writer('票据重打单')
    else:
        log.info('没有找到机制号')
    log.info('发票重打脚本运行结束')

#发票作废
def test_invoice_obsolete(browser,cache):
    log.info('开始运行发票作废脚本')
    if not invoice_record_query(browser, cache):
        return
    consume_collection = get_text(browser, (By.XPATH, invoice_history_list.发票记录))
    mechanism_numbe = find_mechanism_numbe(cache.get('rek_no_list'))
    if mechanism_numbe and (mechanism_numbe[0] in consume_collection):
        on_click(browser, (By.XPATH, '//div[contains(text(),"%s")]' % mechanism_numbe))
        on_click(browser, (By.XPATH, "//button[contains(text(),'作废')]"))
        on_click(browser, (By.XPATH, "//button[contains(text(),'是')]"))
        microsoft_xps_document_writer('票据作废单')
    else:
        log.info('没有找到机制号')
    log.info('发票作废脚本运行结束')

def invoice_record_query(browser,cache):
    login.select_workstation(browser, '门诊挂号收费工作台', cache)  # 工作站是否打开
    on_click(browser,(By.XPATH,'//div[contains(text(),"发票打印管理")]'))
    on_click(browser,(By.LINK_TEXT,'发票记录查询'))
    if element_wait(browser,(By.XPATH,'//span[contains(text(),"验证最小票据号窗口")]')):
        usename = get_text(browser,(By.XPATH,head.用户)).split('(')[0]
        bill_num = find_min_ticket(usename,'门诊收费发票')
        send_value(browser,(By.XPATH,verify_bill_window.票据号),bill_num)  #输入票据号
        on_click(browser,(By.XPATH,verify_bill_window.确定))
        send_value(browser,(By.XPATH,query_area.刷卡),cache.get('patient_card')+'\n')
        end_time = time.time() + 1
        while True:
            consume_collection = get_text(browser, (By.XPATH,invoice_history_list.发票记录))
            if consume_collection != '暂无可显示票据记录...':
                break
            if time.time() > end_time:
                log.info('加载消费单失败')
                break
        return True
    else:
        log.info('验证最小票据号窗口弹出异常')
        return False




# if __name__ == '__main__':
#     cache = Cache({})
#     browser = Common.browser()
#     testcase = {'用户名': 'jfli', '密码': '123456'}
#     login.test_login(browser, testcase, cache)
#     cache.set('处方单', {'02A201703-3000056': '门诊药房(光谷)', '02A201703-3000057': '门诊药房(光谷)'})
#     cache.set('检查单', {'02C201703-3000014': '超声影像科'})
#     cache.set('patient_card','%E?;2501218606=99015012538?+E?')
#     test_invoice_print(browser, cache)
#     browser.refresh()
#     test_invoice_print_again(browser, cache)
#     browser.refresh()
#     test_invoice_obsolete(browser, cache)










