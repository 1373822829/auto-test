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
from UI.com_th_supcom_api.common.Common import focus
from UI.com_th_supcom_api.common.Utility import microsoft_xps_document_writer
from UI.com_th_supcom_api.common.Wait import on_click, send_value, element_wait, get_prompt, is_text, get_text
from UI.com_th_supcom_portal_dao.outp_bill_portal_dao.RegistVerify import find_min_ticket, find_rek_no
from UI.com_th_supcom_portal_element.outp_bill_portal_element.local import head
from UI.com_th_supcom_portal_service.usercenter import login
from UI.com_th_supcom_portal_element.outp_bill_portal_element.out_bill_print.invoice_print import verify_bill_window,query_area\
    ,consume_list,application_detail_list

log = Log.Logger(__name__)
def test_invoice_print(browser,cache):
    log.info('开始运行发票打印脚本')
    login.select_workstation(browser, '门诊挂号收费工作台', cache)  # 工作站是否打开
    on_click(browser,(By.XPATH,'//div[contains(text(),"发票打印管理")]'))
    on_click(browser,(By.LINK_TEXT,'发票打印'))
    if element_wait(browser,(By.XPATH,'//span[contains(text(),"验证最小票据号窗口")]')):
        usename = get_text(browser,(By.XPATH,head.用户)).split('(')[0]
        bill_num = find_min_ticket(usename,'门诊收费发票')
        send_value(browser,(By.XPATH,verify_bill_window.票据号),bill_num)  #输入票据号
        on_click(browser,(By.XPATH,verify_bill_window.确定))
        send_value(browser,(By.XPATH,query_area.刷卡),cache.get('patient_card')+'\n')
        lists = ['处方单', '毒麻单', '检查单', '检验单', '治疗单', '皮试单', '输液单', '草药', '病理类']
        rek_no_list = []
        for list_type in lists:
            applys = cache.get(list_type)
            if applys == None:
                continue
            for apply_id in list(applys.keys()):
                result = find_rek_no(apply_id)
                if result != []:
                    rek_no_list.append(result.Rek.rek_no)
                else:
                    log.info('%s申请单未收费或已退费' % apply_id)
        end_time = time.time() + 1
        while True:
            consume_collection = get_text(browser, (By.XPATH, consume_list.消费记录))
            if consume_collection != '查询暂无结算消费记录':
                break
            if time.time() > end_time:
                log.info('加载消费单失败')
                break
        # print(rek_no_list)
        if rek_no_list == []:
            log.info('没有需要打印的单据')
            return
        status = False
        reks = []
        for rek_no in rek_no_list:
            if rek_no in consume_collection:
                focus(browser,(By.XPATH,'//div[contains(text(),"%s")]'%rek_no))
                reks.append(rek_no)
                status = True
            else:
                log.info('%s消费单不存在或已作废' % rek_no)
        cache.set('rek_no_list',reks)
        if status:
            for rek_no in rek_no_list:
                end_time = time.time() + 1
                while True:
                    if rek_no in get_text(browser, (By.XPATH, application_detail_list.费用明细)):
                        break
                    if time.time() > end_time:
                        log.info('加载消费明细失败')
                        break
            on_click(browser, (By.XPATH, '//button[contains(text(),"打印")]'))
            on_click(browser, (By.XPATH, '//button[contains(text(),"确 定")]'))
            on_click(browser, (By.XPATH, '//button[contains(text(),"是")]'))
            microsoft_xps_document_writer('发票单')
    else:
        log.info('验证最小票据号窗口弹出异常')
    log.info('发票打印脚本运行结束')


if __name__ == '__main__':
    cache = Cache({})
    browser = Common.browser()
    testcase = {'用户名': 'jfli', '密码': '123456'}
    login.test_login(browser, testcase, cache)
    cache.set('quit_sign', ['王易', '呼吸内科急诊', '普通', '刘馗', '2017-06-09'])
    # cache.set('处方单',{'02A201706-1300038':'门诊药房(光谷)','02A201706-1300039':'门诊药房(光谷)'})
    cache.set('检查单',{'02D2017061200055':'超声影像科','02D2017033000025':'放射科','02D2017040100012':'超声影像科'})
    cache.set('patient_card','%E?;2501218606=99015012538?+E?')
    test_invoice_print(browser, cache)









