#! /usr/bin/env python
#coding=utf-8
'''
就诊卡挂失
'''
#日志对象初始化
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from UI.com_th_supcom_api.common import Common
from UI.com_th_supcom_api.common import Log
from UI.com_th_supcom_api.common.Cache import Cache
from UI.com_th_supcom_api.common.Wait import is_text, element_wait
from UI.com_th_supcom_portal_element.outp_bill_portal_element.reg_manager.LossAttendanceCardElement import InputLocator, \
    DivLocator, ButtonLocator
from UI.com_th_supcom_portal_service.usercenter import login
from UI.common_th_supcom_config.test_case_config.TestCaseCodeTable import loss

log = Log.Logger(__name__)

def choice_loss(browser,test_case,cache):
    login.select_workstation(browser, '门诊挂号收费工作台', cache)  #工作站是否打开
    browser.find_element(By.XPATH,'//div[contains(text(),"门诊挂号")]').click()
    browser.find_element(By.LINK_TEXT,'就诊卡挂失').click()
    browser.find_element(By.XPATH,InputLocator.name).clear()
    browser.find_element(By.XPATH,InputLocator.name).send_keys(test_case[loss['name']])
    browser.find_element(By.XPATH, InputLocator.id_type).clear()
    browser.find_element(By.XPATH,InputLocator.id_type).send_keys('居民身份证')
    browser.find_element(By.XPATH, InputLocator.id_card).clear()
    browser.find_element(By.XPATH,InputLocator.id_card).send_keys(test_case[loss['id_card']])
    browser.find_element(By.XPATH, InputLocator.phone_num).clear()
    browser.find_element(By.XPATH,InputLocator.phone_num).send_keys(test_case[loss['phone_num']])
    browser.implicitly_wait(30)
    if element_wait(browser,(By.XPATH,'//button[contains(text(),"查询")]')):
        browser.find_element(By.XPATH, '//button[contains(text(),"查询")]').click()
    locator = (By.XPATH,DivLocator.checkbox)
    if element_wait(browser,locator):
        browser.find_element(By.XPATH,DivLocator.checkbox).click()   #选择患者
    else:
        log.info('没查询到该患者信息!')

#就诊卡挂失
def test_loss_card(browser,test_case,cache):
    log.info('开始运行就诊卡挂失脚本')
    choice_loss(browser, test_case, cache)
    browser.find_element(By.XPATH, '//button[contains(text(),"挂失")]').click()
    #判断患者卡列表窗口是否打开
    locators = (By.XPATH,DivLocator.pai_list)
    if is_text(browser,locators,'患者卡列表'):
        if element_wait(browser,(By.XPATH,DivLocator.checkbox_pai)):
            browser.find_element(By.XPATH,DivLocator.checkbox_pai).click()
            browser.find_element(By.XPATH,'//button[contains(text(),"挂  失")]').click()
            browser.find_element(By.XPATH,'//button[contains(text(),"是")]').click()
        else:
            log.info('就诊卡已挂失,不能进行挂失')
    else:
        log.info('挂失窗口无法正常打开!')

    log.info('就诊卡挂失脚本运行结束')
    # browser.refresh()

##取消挂失
def test_cancel_loss_card(browser, test_case, cache):
    log.info('开始运行就诊卡取消挂失脚本')
    choice_loss(browser, test_case, cache)
    browser.find_element(By.XPATH,'//button[contains(text(),"取消挂失")]').click()
    # 判断患者卡列表窗口是否打开
    locators = (By.XPATH, DivLocator.pai_list)
    if is_text(browser,locators,'患者卡列表'):
        if element_wait(browser,(By.XPATH,DivLocator.checkbox_pai)):
            browser.find_element(By.XPATH,DivLocator.checkbox_pai).click()
            browser.find_element(By.XPATH,ButtonLocator.cancel_loss).click()
            browser.find_element(By.XPATH,'//button[contains(text(),"是")]').click()
        else:
            log.info('就诊未挂失,不能取消挂失')
    else:
        log.info('取消挂失窗口无法正常打开!')

    log.info('就诊卡取消挂失脚本运行结束')
    # browser.refresh()


if __name__ == '__main__':
    cache = Cache({})
    browser = Common.browser()
    testcase = {'用户名': 'jfli', '密码': '123456'}
    login.test_login(browser, testcase, cache)
    test_case = {'患者姓名':'明诚','患者身份证号':'11111111111','电话号':'13600000000'}
    test_loss_card(browser, test_case, cache)
    test_cancel_loss_card(browser, test_case, cache)



