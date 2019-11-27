#! /usr/bin/env python
#coding=utf-8
'''
挂号页面按钮功能验证
'''

from selenium.webdriver.common.by import By
from UI.com_th_supcom_api.common import Common
from UI.com_th_supcom_api.common import Log
from UI.com_th_supcom_api.common.Cache import Cache
from UI.com_th_supcom_api.common.Wait import element_wait, is_text, is_selected
from UI.com_th_supcom_portal_service.usercenter import login
from UI.com_th_supcom_portal_element.outp_bill_portal_element.reg_manager.PatientVisitCardElement import div, form
from UI.common_th_supcom_config.test_case_config import TestCaseCodeTable
#日志对象初始化
log = Log.Logger(__name__)
def test_regist_button(browser,test_case,cache):
    login.select_workstation(browser, '门诊挂号收费工作台', cache)
    #验证取号按钮功能
    browser.find_element_by_xpath('//button[contains(text(),"取        号(U)")]').click()
    locator = (By.XPATH,'//button[contains(text(),"取        号")]')
    if element_wait(browser,locator):
        log.info('取号按钮功能pass')
    else:
        log.info('取号按钮功能fail')
    browser.refresh()
    #验证退号按钮功能
    browser.find_element_by_xpath('//button[contains(text(),"退        号(X)")]').click()
    locator = (By.XPATH,div[4]['key'])
    if is_text(browser,locator,'门诊退号'):
        log.info("退号按钮功能pass")
        browser.find_element_by_xpath('//button[contains(text(),"关闭")]').click()
    else:
        log.info("退号按钮功能fail")
    #验证重置按钮功能
    dict = TestCaseCodeTable.patient_visit_card
    cardElement = \
    browser.find_element_by_xpath(form[0]['key']).find_elements_by_tag_name('input')[3]
    cardElement.clear()
    cardElement.send_keys(test_case[dict['patient_card']] + '\n')
    browser.find_element_by_xpath('//button[contains(text(),"否")]').click()
    browser.find_element_by_xpath('//button[contains(text(),"重置")]').click()
    text = browser.find_element_by_xpath(form[0]['key']).find_elements_by_tag_name('input')[0].get_attribute('value')
    if text == '':
        log.info('重置按钮功能pass')
    else:
        log.info('重置按钮功能fail')

    #验证号别过滤及门诊时间过滤
    result = 1
    #全部
    all_boxs = browser.find_elements_by_xpath('//label[contains(text(),"全部")]')
    for box in all_boxs:
        box.click()
    lists = outp_message(browser)
    if len(list(set(lists[0])))>1 and len(list(set(lists[1])))>1:
        # log.info('全部按钮验证pass')
        pass
    elif len(list(set(lists[0]))) == 1 and ('急诊' in lists[0]):
        # log.info('全部按钮验证pass')
        pass
    else:
        # log.info('全部按钮验证fail')
        result = 0
    #全天，普通和急诊
    browser.find_element_by_xpath('//label[contains(text(),"全天")]').click()
    browser.find_element_by_xpath('//label[contains(text(),"普通和急诊")]').click()
    lists = outp_message(browser)
    for outp_type in lists[0]:
        if outp_type in ('普通','急诊'):
            # log.info('普通急诊按钮验证pass')
            pass
        else:
            # log.info('普通急诊按钮验证fail')
            result = 0
    if list(set(lists[1])) in (['全天'],[]):
        # log.info('全天按钮验证pass')
        pass
    else:
        # log.info('全天按钮验证fail')
        result = 0
    #上午，专家
    type_locator = '//label[contains(text(),"上午")]'
    date_locator = '//label[contains(text(),"专家")]'
    verify(browser, type_locator, date_locator, '上午', '专家',result)
    #下午，业余
    type_locator = '//label[contains(text(),"下午")]'
    date_locator = '//label[contains(text(),"业余")]'
    verify(browser, type_locator, date_locator, '下午', '业余',result)
    #晚上，保健
    type_locator = '//label[contains(text(),"晚上")]'
    date_locator = '//label[contains(text(),"保健")]'
    verify(browser, type_locator, date_locator, '晚上', '保健',result)

    if result:
        log.info('号源过滤按钮验证pass')
    else:
        log.info('号源过滤按钮验证fail')


def verify(browser,type_locator,date_locator,outp_type,outp_date,result):
    browser.find_element(By.XPATH,type_locator).click()
    browser.find_element(By.XPATH,date_locator).click()
    lists = outp_message(browser)
    if (list(set(lists[0])) in ([outp_type], [])) and (list(set(lists[1])) in ([outp_date], [])):
        # log.info('按钮验证pass')
        pass
    else:
        # log.info('按钮验证fail')
        result = 0

def outp_message(browser):
    special_elements = browser.find_elements_by_xpath(div[3]['key'])
    outp_type_code = []
    outp_date = []
    if len(special_elements)>1:
        for special_element in special_elements:
             outp_type_code.append(special_element.find_elements_by_tag_name('div')[1].text)
             outp_date.append(special_element.find_elements_by_tag_name('div')[4].text)
    return [outp_type_code,outp_date]


if __name__ == '__main__':
    cache = Cache({})
    browser = Common.browser()
    testcase = {'用户名': 'jfli', '密码': '123456'}
    login.test_login(browser, testcase, cache)
    test_case = {
                 '患者卡号':'%E?;1004627675=99015017425?+E?','患者姓名':'','号源类别':'专家',
                 '专科编码':'083','专科名称':'','医生':''
               }
    test_regist_button(browser, test_case, cache)

