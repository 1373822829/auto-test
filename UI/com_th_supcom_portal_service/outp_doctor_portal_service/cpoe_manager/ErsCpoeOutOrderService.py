#! /usr/bin/env python
# coding=utf-8
'''
检查，检验医嘱开立
'''
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import UI.com_th_supcom_api.common.Common as common
import UI.com_th_supcom_portal_element.outp_doctor_portal_element.cpoe_manager.CpoeOutOrderElement as CpoeOutOrderElement
import UI.com_th_supcom_portal_element.outp_doctor_portal_element.cpoe_manager.ErsCpoeOutOrderElement as ErsCpoeElement
import UI.com_th_supcom_portal_service.outp_doctor_portal_service.adt_patient_manager.PatientListOutOrderService as pai
import UI.com_th_supcom_portal_service.outp_doctor_portal_service.cpoe_manager.CpoeSubmit as CpoeSubmit
import UI.com_th_supcom_portal_service.usercenter.login as login
import UI.common_th_supcom_config.test_case_config.TestCaseCodeTable as Code
from UI.com_th_supcom_api.common.Cache import Cache
from UI.com_th_supcom_api.common.Wait import on_click


def test_emr_ers(browser,test_case,cache):

    # 判断门诊医生站是否打开
    login.select_workstation(browser, '门诊医生站', cache)
    # 进入医嘱开立界面

    browser.find_element_by_xpath(CpoeOutOrderElement.div[4]['key']).click()
    time.sleep(2)
    elements = browser.find_elements_by_tag_name('a')
    for element in elements:
        if element.text == '门诊医嘱开立':
            element.click()
            break
    # browser.find_element_by_xpath(CpoeOutOrderElement.a[1]['key'])
    browser.find_element_by_xpath(CpoeOutOrderElement.input[12]['key']).send_keys(str(cache.get('patient_card')) + '\n')
    time.sleep(2)
    browser.find_element_by_xpath(CpoeOutOrderElement.input[12]['key']).click()
    #获取测试用例
    ers_cpoe_list = test_case

    #将多部位分装为集合
    ers_combin_part_list = ers_cpoe_list[Code.ers_cpoe_table['ers_combin_part']]

    ers_part = ers_cpoe_list[Code.ers_cpoe_table['ers_part']]
    ers_part_list = str(ers_part).split(',')

    #获取检查医嘱按钮区域
    ers_cpoe_area = ErsCpoeElement.div[0]['key']

    #检查项目录入区域
    ers_item_area = ErsCpoeElement.div[1]['key']

    #检查执行科室区域
    ers_execute_area = ErsCpoeElement.div[2]['key']

    #检查项目基本信息
    ers_base_message_area = ErsCpoeElement.fieldset[0]['key']

    #部位或方法组
    ers_combin_part_area = ErsCpoeElement.fieldset[1]['key']

    #部位或方法
    ers_part_area = ErsCpoeElement.fieldset[2]['key']

    #附加项目
    ers_add_item_area = ErsCpoeElement.fieldset[3]['key']

    #保存
    ers_save = ErsCpoeElement.table[0]['key']

    #执行科室列表
    ers_execute_list = ErsCpoeElement.div[3]['key']

    # ers_cpoe_button_element = browser.find_element_by_xpath(ers_cpoe_area).find_elements_by_tag_name('button')
    # ers_cpoe_button_element[3].click()
    # time.sleep(2)
    #点击检查按钮
    js = 'document.getElementsByTagName("button")[10].click()'
    browser.execute_script(js)
    ers_cpoe_area_element = browser.find_element_by_xpath(ers_item_area)
    ers_cpoe_input_element = ers_cpoe_area_element.find_elements_by_tag_name('input')
    ers_cpoe_input_element[0].send_keys(ers_cpoe_list[Code.ers_cpoe_table['cpoe_name']]+'\n')
    time.sleep(1)
    ers_cpoe_name_elements = ers_cpoe_area_element.find_elements_by_tag_name('span')
    num = -1
    for i in range(0,len(ers_cpoe_name_elements)):
        if ers_cpoe_list[Code.ers_cpoe_table['cpoe_name']] == ers_cpoe_name_elements[i].text:
            num = i
    if num == -1:
        raise Exception('该项目不存在')
    else:
        on_click(browser,(By.XPATH,'//span[contains(text(),"%s")]'%ers_cpoe_list[Code.ers_cpoe_table['cpoe_name']]))
    time.sleep(1)
    ers_execute_element = browser.find_element_by_xpath(ers_execute_area).find_elements_by_tag_name('input')
    print(ers_execute_element[1].text)
    ers_execute_element[1].clear()
    ers_execute_element[1].send_keys(ers_cpoe_list[Code.ers_cpoe_table['execute_depat']])
    time.sleep(1)
    ers_execute_element[1].send_keys(Keys.ENTER)
    # time.sleep(2)
    # execute_list_elements = browser.find_element_by_xpath(ers_execute_list).find_elements_by_tag_name('div')
    # bollen = True
    # for i in range(0,len(execute_list_elements)):
    #     if ers_cpoe_list[Code.ers_cpoe_table['execute_depat']] == execute_list_elements[i].text:
    #         execute_list_elements[i].click()
    #         bollen = False
    #     if i == len(execute_list_elements)-1:
    #         if bollen:raise Exception('没有该执行科室，请配置流向!')

    count = 1
    ers_combin_part_element = browser.find_element_by_xpath(ers_combin_part_area).find_elements_by_tag_name('div')
    time.sleep(2)
    for i in range(0,len(ers_combin_part_element)):
        if '无数据' == ers_combin_part_element[i].text:
            print('********')
            count = 0
            browser.find_element_by_xpath("//button[contains(text(),'保存并关闭')]").click()
            cache.set('pai_type','o')
            CpoeSubmit.test_cpoe_submit(browser, '检查单')
            return
    if count == 1:
        ers_combin_elements = browser.find_element_by_xpath(ers_combin_part_area).find_elements_by_tag_name('label')
        print(len(ers_combin_elements))
        for i in range(0,len(ers_combin_elements)):
            if ers_combin_part_list == ers_combin_elements[i].text:
                ers_combin_elements[i].click()
        time.sleep(1)
        ers_part_elements = browser.find_element_by_xpath(ers_part_area).find_elements_by_tag_name('label')
        print(ers_part_list)
        for i in range(0,len(ers_part_elements)):
            for j in range(0,len(ers_part_list)):
                if ers_part_list[j] == ers_part_elements[i].text:
                    ers_part_elements[i].click()
        cache.set('pai_type', 'o')
        button_element = browser.find_element_by_xpath(ers_save).find_elements_by_tag_name('button')[1]
        button_element.click()
        CpoeSubmit.test_cpoe_submit(browser,'检查单')



if __name__ == '__main__':
    browser = common.browser()
    testcase = {'用户名': 'jfli', '密码': '123456','诊断类别': 1, '诊断名称': '神经痛'}
    cache = Cache({})
    cache.set('resultType', 1)
    cache.set('specialName', '眼科门诊')
    cache.set('patient_card', '%E?;1004627675=99015017425?+E?')
    login.test_login(browser, testcase, cache)
    pai.test_workstation(browser,cache)
    pai.test_diagnose(browser,testcase,cache)
    test_case = {'附加项目': '', '患者姓名': '杨俊熙', '患者卡号': '%E?;1004627675=99015017425?+E?', '执行科室': '生殖医学中心',
                 '检查部位/方法分组': '部位', '部位/方法': '纵膈', '医嘱名称': '彩超常规检查'}
    test_emr_ers(browser,test_case, cache)


