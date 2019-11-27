'''
预付费退费（窗口)
'''

import re
from selenium.webdriver.common.by import By
from UI.com_th_supcom_api.common import Common
from UI.com_th_supcom_api.common import Log
from UI.com_th_supcom_api.common.Cache import Cache
from UI.com_th_supcom_api.common.Utility import microsoft_xps_document_writer
from UI.com_th_supcom_api.common.Wait import on_click, send_value, get_prompt,get_text
from UI.com_th_supcom_portal_dao.outp_bill_portal_dao.RegistVerify import find_rek_no
from UI.com_th_supcom_portal_service.usercenter import login
from UI.com_th_supcom_portal_element.outp_bill_portal_element.out_bill_refund.prepaid_refund import list_area,query_area
#日志初始化
log = Log.Logger(__name__)
def test_pay_refund(browser, cache):
    log.info('开始运行预付费退费(窗口)脚本')
    login.select_workstation(browser, '门诊挂号收费工作台', cache)  # 工作站是否打开
    on_click(browser,(By.XPATH,'//div[contains(text(),"门诊退费管理")]'))
    on_click(browser,(By.LINK_TEXT,'预付费退费(窗口)'))
    boolen = get_prompt(browser)
    if  boolen:
        if re.sub('\D', '', boolen) == '0':
           log.info(boolen)
           return
        else:
           on_click(browser, (By.XPATH, "//button[contains(text(),'确定')]"))

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
                log.info('%s申请单未收费或已退费'%apply_id)
    for rek_no in rek_no_list:
        # print(rek_no)
        send_value(browser,(By.XPATH,query_area.缴费流水号),rek_no+'\n')
        apply_status = get_text(browser,(By.XPATH,list_area.退费明细列表+'//label'))
        if '正常' in apply_status:
            status_elements = browser.find_elements_by_xpath(list_area.退费明细列表 + '//label')
            for status_element in status_elements:
                status_element.click()
        if '取消' in get_text(browser,(By.XPATH,list_area.退费明细列表+'//label')):
            on_click(browser,(By.XPATH,query_area.退费))
            on_click(browser,(By.XPATH,'//button[contains(text(),"确定")]'))
            microsoft_xps_document_writer('退费单')
            on_click(browser, (By.XPATH, '//button[contains(text(),"确定")]'))
    log.info('运行预付费退费(窗口)脚本结束')


if __name__ == '__main__':
    cache = Cache({})

    browser = Common.browser()
    testcase = {'用户名': 'jfli', '密码': '123456'}
    login.test_login(browser, testcase, cache)
    cache.set('quit_sign', ['王易', '呼吸内科急诊', '普通', '刘馗', '2017-06-09'])
    cache.set('处方单',{'02A201706-1300038':'门诊药房(光谷)','02A201706-1300039':'门诊药房(光谷)'})
    cache.set('检查单',{'02D2017062000009':'超声影像科','02D2017062000008':'超声影像科'})
    cache.set('patient_card','%E?;2501218606=99015012538?+E?')
    cache.set('草药',{'02A201706-2000024':'中药饮片药房（光谷）'})
    test_pay_refund(browser, cache)









