#! /usr/bin/env python
#coding=utf-8
'''
取留号
'''

from selenium.webdriver.common.by import By
from UI.com_th_supcom_api.common import Common
from UI.com_th_supcom_api.common import Log
from UI.com_th_supcom_api.common.Cache import Cache
from UI.com_th_supcom_api.common.Wait import is_text, element_wait, on_click
from UI.com_th_supcom_portal_service.outp_bill_portal_service.reg_manager.OutpPatientGetPlusAndOrderSignService import get_sign
from UI.com_th_supcom_portal_service.usercenter import login
from UI.common_th_supcom_config.test_case_config.TestCaseCodeTable import loss, leave_sign
import UI.com_th_supcom_portal_dao.outp_bill_portal_dao.RegistVerify as dao
import UI.com_th_supcom_portal_template.outp_bill_portal_template.RegistTemplate as temp
import UI.com_th_supcom_api.common.Utility as Utility
#日志对象初始化
log = Log.Logger(__name__)

def test_get_leave_sign(browser,testcase,cache):
    log.info('开始运行取留号脚本')
    login.select_workstation(browser, '门诊挂号收费工作台', cache)  # 工作站是否打开
    on_click(browser, (By.XPATH, '//div[contains(text(),"门诊挂号")]'))
    on_click(browser, (By.LINK_TEXT, '取留号'))
    # 调取挂号验证模板
    Fee = dao.outp_balance(testcase)
    temp.outp_fee_temp(Fee)
    RegSource = dao.outp_regist_master(testcase)
    temp.outp_reg_source_temp(RegSource)
    OfficeRegSource = dao.outp_patient_visit(testcase)
    temp.outp_office_reg_source_temp(OfficeRegSource)
    balance = Fee.PcaPrepayAccountMaster.balance
    current_no = RegSource.OutpRegMaster.current_no
    current_limits = RegSource.OutpRegMaster.current_limits
    get_sign(browser,testcase)
    # 调取挂号验证模板
    FeeAfter = dao.outp_balance(testcase)
    temp.outp_fee_temp(FeeAfter)
    RegSourceAfter = dao.outp_regist_master(testcase)
    temp.outp_reg_source_temp(RegSourceAfter)
    OfficeRegSourceAfter = dao.outp_patient_visit(testcase)
    temp.outp_office_reg_source_temp(OfficeRegSourceAfter)

    # 数据验证
    if (balance - FeeAfter.PcaPrepayAccountMaster.balance) == testcase[leave_sign['regist_fee']]:
        Utility.writeFile('患者挂号扣费  pass')
    else:
        Utility.writeFile('患者挂号扣费  fail')
    if RegSourceAfter.OutpRegMaster.current_no - current_no == 0 and current_limits - RegSourceAfter.OutpRegMaster.current_limits == 0:
        Utility.writeFile('当前号和已挂数  pass')
    else:
        Utility.writeFile('当前号和已挂数  fail')
    if OfficeRegSourceAfter[0] - OfficeRegSource[0] == 1:
        Utility.writeFile('门办已挂数  pass')
    else:
        Utility.writeFile('门办已挂数  fail')
    log.info('取留号脚本运行结束')

if __name__ == '__main__':
    cache = Cache({})
    browser = Common.browser()
    testcase = {'用户名': 'jfli', '密码': '123456'}
    login.test_login(browser, testcase, cache)
    testcase = {'门诊科室编码': 'xhnkmz', '医生编码': 'hh', '门诊科室': '呼吸内科门诊', '医生': '黄宏', '门诊时间': '上午',
                '专科名称': '呼吸内科', '患者卡号': '%E?;2001065723=99015011437?+E?', '号源类别': '专家','挂号费':'21'}
    get_leave_sign(browser, testcase, cache)
