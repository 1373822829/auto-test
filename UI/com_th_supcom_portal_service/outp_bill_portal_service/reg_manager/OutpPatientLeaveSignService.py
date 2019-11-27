#! /usr/bin/env python
#coding=utf-8
'''
留号脚本
'''

#日志对象初始化
from selenium.webdriver.common.by import By
from UI.com_th_supcom_api.common import Common
from UI.com_th_supcom_api.common import Log
from UI.com_th_supcom_api.common.Cache import Cache
from UI.com_th_supcom_api.common.Common import calendar, filter_lists
from UI.com_th_supcom_api.common.Wait import send_value, on_click
from UI.com_th_supcom_portal_element.outp_bill_portal_element.reg_manager.outp_patient_leave_sign import body
from UI.com_th_supcom_portal_element.outp_bill_portal_element.reg_manager.outp_patient_leave_sign import head_button
from UI.com_th_supcom_portal_service.usercenter import login
from UI.common_th_supcom_config.test_case_config.TestCaseCodeTable import leave_sign
import UI.com_th_supcom_portal_dao.outp_bill_portal_dao.RegistVerify as dao
import UI.com_th_supcom_portal_template.outp_bill_portal_template.RegistTemplate as temp
import UI.com_th_supcom_api.common.Utility as Utility

log = Log.Logger(__name__)

def test_leave_sign(browser,testcase,cache):
    log.info('开始运行留号脚本')
    login.select_workstation(browser, '门诊挂号收费工作台', cache)  # 工作站是否打开
    on_click(browser, (By.XPATH, '//div[contains(text(),"门诊挂号")]'))
    on_click(browser, (By.LINK_TEXT, '留号'))

    # 调取挂号验证模板
    RegSource = dao.outp_regist_master(testcase)
    if RegSource != None:
        temp.outp_reg_source_temp(RegSource)
        current_no = RegSource.OutpRegMaster.current_no
        current_limits = RegSource.OutpRegMaster.current_limits
    
    #刷卡
    locator = (By.XPATH,body.卡号)
    send_value(browser,locator,testcase[leave_sign['patient_card']]+'\n')
    #输入日期
    remove_js = "document.getElementsByClassName('x-triggerfield-noedit')[0].removeAttribute('readonly')"
    focus_js = "document.getElementsByClassName('x-triggerfield-noedit')[0].blur()"
    input_locator = (By.XPATH,head_button.就诊时间)
    img_locator = (By.XPATH,head_button.日期图标)
    date = testcase[leave_sign['visit_time']]
    calendar(browser,remove_js,focus_js,input_locator,img_locator,date)
    locator = (By.XPATH, body.号源列表 + '//tr')
    num = len(browser.find_elements(locator[0],locator[1]))
    #输入医生名
    select_locator = (By.XPATH,head_button.查询条件)
    send_value(browser,select_locator,testcase[leave_sign['doctor_name']])
    list_message = [testcase[leave_sign['outp_time']],testcase[leave_sign['special_name']]]
    if not filter_lists(browser,locator,list_message,num,'button'):
        log.info('没有号源信息')
        return
    on_click(browser, (By.XPATH, '//button[contains(text(),"是")]'))
    # 调取挂号验证模板
    RegSource = dao.outp_regist_master(testcase)
    if RegSource != None:
        RegSourceAfter = dao.outp_regist_master(testcase)
        temp.outp_reg_source_temp(RegSourceAfter)
    # 数据验证
    if RegSourceAfter.OutpRegMaster.current_no - current_no == 1 and current_limits - RegSourceAfter.OutpRegMaster.current_limits == 1:
        Utility.writeFile('当前号和已挂数  pass')
    else:
        Utility.writeFile('当前号和已挂数  fail')
    business_type = cache.get('business_type')
    if not business_type:
       cache.set('business_type',[['留号',testcase[leave_sign['name']],testcase[leave_sign['special_name']],testcase[leave_sign['outp_time']],testcase[leave_sign['doctor_name']],testcase[leave_sign['visit_time']]]])
    else:
        business_type.append(['留号',testcase[leave_sign['name']],testcase[leave_sign['special_name']],testcase[leave_sign['outp_time']],testcase[leave_sign['doctor_name']],testcase[leave_sign['visit_time']]])
    log.info('挂号留号运行结束')

if __name__ == '__main__':
    cache = Cache({})
    browser = Common.browser()
    testcase = {'用户名': 'jfli', '密码': '123456'}
    login.test_login(browser, testcase, cache)
    testcase = {'门诊时间': '下午', '患者姓名': '杨俊熙', '医生': '李德民', '门诊科室': '消化内科门诊', '就诊时间': '2017-06-10',
                '患者卡号': '%E?;1004627675=99015017425?+E?', '专科名称': '消化内科','号源类别':'专家'}
    test_leave_sign(browser, testcase, cache)

