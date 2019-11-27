#! /usr/bin/env python
#coding=utf-8
'''
号源调整
'''
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from UI.com_th_supcom_api.common import Common
from UI.com_th_supcom_api.common import Log
from UI.com_th_supcom_api.common.Cache import Cache
from UI.com_th_supcom_api.common.Wait import on_click, is_text, element_wait, send_value
from UI.com_th_supcom_portal_element.outp_affairs_portal_element.outp_manager.OutpRegMasterPoolReviseElement import \
    Input, Img, Div
from UI.com_th_supcom_portal_service.usercenter import login

#日志对象初始化
from UI.common_th_supcom_config.test_case_config.TestCaseCodeTable import plus_sign

log = Log.Logger(__name__)
def test_revise(browser,testcase,cache):
    log.info('开始运行号源调整脚本')
    # 判断门诊办公室工作站是否打开
    login.select_workstation(browser, '门诊办公室工作站', cache)
    locator = (By.XPATH,'//div[contains(text(),"号源管理")]')
    on_click(browser,locator)
    locator = (By.LINK_TEXT,'号源调整')
    on_click(browser,locator)
    #输入日期
    calendar_element = browser.find_element(By.XPATH,Input.date)
    js = "document.getElementsByTagName('input')[1].removeAttribute('readonly')"
    browser.execute_script(js)
    calendar_element.clear()
    calendar_element.send_keys(time.strftime("%Y-%m-%d", time.localtime()))
    js = "document.getElementsByTagName('input')[1].blur()"
    browser.execute_script(js)
    locator = (By.XPATH,Img.calendar_img)
    on_click(browser,locator)
    browser.find_element_by_xpath("//button[contains(text(),'今天')]").send_keys(Keys.ENTER)
    # 输入门诊科室
    browser.find_element(By.XPATH,Input.belong_clinic_code).clear()
    browser.find_element(By.XPATH, Input.belong_clinic_code).send_keys(testcase[plus_sign['clinic_code']])
    locator = (By.XPATH,'//div[contains(text(),"光谷院区")]')
    on_click(browser,locator)
    #输入医生
    browser.find_element(By.XPATH,Input.doctor).clear()
    browser.find_element(By.XPATH,Input.doctor).send_keys(testcase[plus_sign['doctor_code']])
    locator = (By.XPATH, '//div[contains(text(),"' + testcase[plus_sign['doctor_name']] + '")]')
    on_click(browser, locator)
    #选择专家号
    locator = (By.XPATH,'//label[contains(text(),"专家")]')
    on_click(browser,locator)
    outp_time_dict = {'上午':8,'下午':19,'晚上':30}
    #判断是否存在相同号源
    special_element = browser.find_element(By.XPATH,Div.special_list).find_elements(By.TAG_NAME,'tr')
    if len(special_element)>1:
        log.info('存在相同号源')
    # print(browser.find_element_by_xpath(Div.special_list+'//td[8]').text)
    num = outp_time_dict[testcase[plus_sign['outp_time']]]
    locator = (By.XPATH,Div.special_list+'//td['+str(num)+']')
    on_click(browser,locator)
    reg_num = browser.find_element(By.XPATH, Div.special_list).find_elements(By.TAG_NAME,'td')[num+1].text  #已挂数
    appoint_num = browser.find_element(By.XPATH, Div.special_list).find_elements(By.TAG_NAME,'td')[num+4].text  #预约数
    #判断号源详情弹出窗是否弹出
    locator = (By.XPATH,Div.special_detail)
    if is_text(browser,locator,'号源详情'):
        send_value(browser,(By.XPATH,Input.appoint_limit_no),str(int(appoint_num)+1))
        send_value(browser,(By.XPATH,Input.limit_no),str(int(reg_num)+1))
        locator = (By.XPATH,'//button[contains(text(),"保存")]')
        on_click(browser,locator)
        locator = (By.XPATH, '//button[contains(text(),"是")]')
        on_click(browser,locator)
    else:
        log.info('号源详情窗口未弹出')
    log.info('号源调整脚本运行结束')






if __name__ == '__main__':
    cache = Cache({})
    browser = Common.browser()
    testcase = {'用户名': 'jfli', '密码': '123456'}
    login.test_login(browser, testcase, cache)
    testcase = {'门诊科室编码':'wkmz','医生编码':'zs','门诊科室':'外科门诊','医生':'郑爽','门诊时间':'上午'}
    test_revise(browser, testcase, cache)
