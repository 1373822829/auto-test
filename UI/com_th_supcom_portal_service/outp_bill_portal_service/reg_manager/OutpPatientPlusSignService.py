#! /usr/bin/env python
#coding=utf-8
'''
加号脚本
'''
import time
from selenium.webdriver.common.by import By
from UI.com_th_supcom_api.common import Common
from UI.com_th_supcom_api.common import Log
from UI.com_th_supcom_api.common import Utility
from UI.com_th_supcom_api.common.Cache import Cache
from UI.com_th_supcom_api.common.Common import filter_lists
from UI.com_th_supcom_api.common.Wait import on_click, send_value, element_wait, get_prompt
from UI.com_th_supcom_portal_element.outp_bill_portal_element.reg_manager.OutpPatientPlusSignElement import PlusSignInput, \
    PlusSignDiv
from UI.com_th_supcom_portal_service.usercenter import login
from UI.common_th_supcom_config.test_case_config.TestCaseCodeTable import plus_sign
import UI.com_th_supcom_portal_dao.outp_bill_portal_dao.RegistVerify as dao
import UI.com_th_supcom_portal_template.outp_bill_portal_template.RegistTemplate as temp
#日志对象初始化
log = Log.Logger(__name__)
def test_plus_sign(browser,testcase,cache):
    log.info('开始运行加号脚本')
    login.select_workstation(browser, '门诊挂号收费工作台', cache)  # 工作站是否打开
    on_click(browser,(By.XPATH,'//div[contains(text(),"门诊挂号")]'))
    on_click(browser,(By.LINK_TEXT,'加号'))
    # 调取挂号验证模板
    RegSource = dao.outp_regist_master(testcase)
    temp.outp_reg_source_temp(RegSource)
    current_no = RegSource.OutpRegMaster.current_no
    current_limits = RegSource.OutpRegMaster.current_limits
    #刷卡
    send_value(browser,(By.XPATH,PlusSignInput.swipe_card),(testcase[plus_sign['patient_card']]+'\n'))
    #输入科室名称进行过滤
    num = len( browser.find_elements(By.XPATH,PlusSignDiv.special_list+'//tr'))
    send_value(browser,(By.XPATH,PlusSignInput.doctor_name),testcase[plus_sign['doctor_name']])
    locator = (By.XPATH,PlusSignDiv.special_list+'//tr')
    list_message = [testcase[plus_sign['special_name']]]
    if not filter_lists(browser,locator,list_message,num,'button'):
        log.info('没有号源信息')
        return
    on_click(browser, (By.XPATH, '//button[contains(text(),"是")]'))
    #判断提示框中的内容是否正确
    if get_prompt(browser):
        prompt_text = get_prompt(browser)
        on_click(browser,(By.XPATH,'//button[contains(text(),"确定"   )]'))
    else:
        browser.refresh()
    # 调取挂号验证模板
    RegSourceAfter = dao.outp_regist_master(testcase)
    temp.outp_reg_source_temp(RegSourceAfter)
    # 数据验证
    if RegSourceAfter.OutpRegMaster.current_no - current_no == 0 and current_limits - RegSourceAfter.OutpRegMaster.current_limits == 0:
        Utility.writeFile('当前号和已挂数  pass')
    else:
        Utility.writeFile('当前号和已挂数  fail')
    business_type = cache.get('business_type')
    if not business_type:
       cache.set('business_type',[['加号',testcase[plus_sign['name']],testcase[plus_sign['special_name']],testcase[plus_sign['outp_time']],testcase[plus_sign['doctor_name']]]])
    else:
        business_type.append(['加号',testcase[plus_sign['name']],testcase[plus_sign['special_name']],testcase[plus_sign['outp_time']],testcase[plus_sign['doctor_name']]])
    log.info('挂号留号运行结束')

if __name__ == '__main__':
    cache = Cache({})
    browser = Common.browser()
    testcase = {'用户名': 'jfli', '密码': '123456'}
    login.test_login(browser, testcase, cache)
    testcase = {'门诊科室编码': 'xhnkmz', '医生编码': 'ldm', '门诊科室': '消化内科门诊', '医生': '李德民', '门诊时间': '下午',
                '专科名称':'消化内科','患者卡号':'%E?;1004627675=99015017425?+E?','号源类别':'专家'}
    test_plus_sign(browser, testcase, cache)

