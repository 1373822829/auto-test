'''
检验医嘱开立
'''
import UI.com_th_supcom_portal_element.outp_doctor_portal_element.cpoe_manager.InsCpoeOutOrderElement as ins_cpoe_element
import UI.com_th_supcom_portal_element.outp_doctor_portal_element.cpoe_manager.CpoeOutOrderElement as CpoeOutOrderElement
import UI.common_th_supcom_config.test_case_config.TestCaseCodeTable as Code
import UI.com_th_supcom_portal_service.usercenter.login as login
import UI.com_th_supcom_api.common.Common as common
from selenium.webdriver.common.keys import Keys
import UI.com_th_supcom_portal_service.outp_doctor_portal_service.cpoe_manager.CpoeSubmit as CpoeSubmit
import time



def test_emr_ins(browser,ins_test_case,cache):

    # 判断门诊医生站是否打开
    login.select_workstation(browser, '门诊医生站', cache)
    # 进入医嘱开立界面

    browser.find_element_by_xpath(CpoeOutOrderElement.div[4]['key']).click()
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
    ins_cpoe_list = ins_test_case

    #将多部位分装为集合
    item_name = ins_cpoe_list[Code.ins_cpoe['item_name']]
    ins_detail = ins_cpoe_list[Code.ins_cpoe['ins_detail']]
    ins_specimen = ins_cpoe_list[Code.ins_cpoe['specimen']]

    item_name_list = str(item_name).split(',')
    print(item_name_list)
    ins_detail_list = str(ins_detail).split(',')
    ins_specimen_list = str(ins_specimen).split(',')


    #检验按钮
    ins_button = ins_cpoe_element.div[0]['key']

    #检验项目区域
    ins_item = ins_cpoe_element.div[1]['key']

    #检验项目名称区域
    ins_item_name = ins_cpoe_element.div[2]['key']

    #执行科室列表区域
    execute_depart = ins_cpoe_element.div[3]['key']

    #检验项目明细
    ins_item_detail = ins_cpoe_element.div[4]['key']

    #诊断录入区域
    dia_input = ins_cpoe_element.div[5]['key']

    #项目名称录入
    ins_item_input = ins_cpoe_element.table[0]['key']

    #保存区域
    ins_save = ins_cpoe_element.table[1]['key']

    #标本区域
    specimen = ins_cpoe_element.div[6]['key']

    #开立检验医嘱
    ins_button_element = browser.find_element_by_xpath(ins_button).find_elements_by_tag_name('button')[1]
    ins_button_element.click()
    time.sleep(1)
    ins_item_element = browser.find_element_by_xpath(ins_item).find_elements_by_tag_name('input')    #元素为找到
    ins_item_element[0].send_keys('s'+'\n')
    time.sleep(4)
    num = 0
    j = 0
    while True:
        ins_item_elements = browser.find_element_by_xpath(ins_item).find_elements_by_tag_name('span')
        elements = browser.find_element_by_xpath(ins_item).find_elements_by_tag_name('div')
        for i in range(j,len(ins_item_elements)):
            j += 1
            browser.execute_script("arguments[0].scrollIntoView();", elements[i])
            if ins_item_elements[i].text == ins_cpoe_list[Code.ins_cpoe['ins_item']]:
                ins_item_elements[i].click()
                num = 1
            if num == 1: break

        if num == 1: break
    if num == 0:raise Exception('没有该检验项目')
    time.sleep(2)
    ins_item_name_elements = browser.find_element_by_xpath(ins_item_name).find_elements_by_tag_name('div')
    print(len(ins_item_name_elements))
    for i in range(0,len(ins_item_name_elements)):
        for j in range(0,len(item_name_list)):
            if item_name_list[j] == ins_item_name_elements[i].text:
                ins_item_name_elements[i].click()

    execute_element = browser.find_element_by_xpath(ins_item_input).find_elements_by_tag_name('input')[1]
    execute_element.send_keys(ins_cpoe_list[Code.ins_cpoe['execute_depat']])
    time.sleep(2)
    execute_element.send_keys(Keys.ENTER)


   # browser.find_element_by_xpath(ins_item_input).find_elements_by_tag_name('bill')[1].click()
   #  execute_depart_elements = browser.find_element_by_xpath( execute_depart).find_elements_by_tag_name('div')
    # for execute_depart_element in execute_depart_elements:
    #     if  ins_cpoe_list[Code.ins_cpoe['execute_depat']] == execute_depart_element.text:
    #         execute_depart_element.click()


    k = 0
    count = 0
    while True:
        ins_detail_elements = browser.find_element_by_xpath(ins_item_detail).find_elements_by_tag_name('tr')

        for i in range(k,len(ins_detail_elements)):
            k +=1
            js = "var q=document.body.scrollTop=1"
            browser.execute_script("arguments[0].scrollIntoView();", ins_detail_elements[i])

            detail_elements = ins_detail_elements[i].find_elements_by_tag_name('div')
            specimen_elements = ins_detail_elements[i].find_elements_by_tag_name('img')
            for j in range(0,len(detail_elements)):
                for t in range(0,len(ins_detail_list)):
                    if ins_detail_list[t] == detail_elements[j].text:
                        count = count+1
                        detail_elements[0].click()
                        specimen_elements[1].click()
                        time.sleep(1)
                        specimen_name_elements = browser.find_element_by_xpath(specimen).find_elements_by_tag_name('div')
                        for specimen_name_element in specimen_name_elements:
                            if ins_specimen_list[t] == specimen_name_element.text:
                                specimen_name_element.click()
        if count == len(ins_detail_list):
            break
    button_element = browser.find_element_by_xpath(ins_save).find_elements_by_tag_name('button')[1]
    button_element.click()
    CpoeSubmit.test_cpoe_submit(browser,'检验单')







if __name__ == '__main__':
    ##执行前提条件：患者已挂号且患者已录入诊断信息

    browser = common.browser()
    testcase = {'用户名': 'jfli', '密码': '123456'}
    caches = {'resultType': '1', 'specialName': '急诊内科', 'userId': '%E?;2001065723=99015011437?+E?'}
    login.login(browser, testcase, caches)

    test_emr_ins(browser, ins_test_case={'检验目的': '查体', '检验项目': '分子诊断检测项目', '标本': '血,其他', '临床诊断': '神经痛', '检验明细': 'F042_他克莫司用药相关基因位点检测（CYP3A5）,F021_α-地中海贫血基因诊断', '患者卡号': '%E?;1004627675=99015017425?+E?', '执行科室': 'fnfmyjs', '患者姓名': '杨俊熙', '项目名称': '个体化用药基因检测,遗传性疾病核酸检测'},cache={'userId': '%E?;2001065723=99015011437?+E?'})
    CpoeSubmit.test_cpoe_submit(browser,caches)

