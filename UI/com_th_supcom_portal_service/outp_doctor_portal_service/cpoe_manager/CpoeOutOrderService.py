'''
开立医嘱
'''
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import UI.com_th_supcom_api.common.Common as common
import UI.com_th_supcom_api.common.Utility as Utility
import UI.com_th_supcom_portal_element.outp_doctor_portal_element.cpoe_manager.CpoeOutOrderElement as CpoeOutOrderElement
import UI.com_th_supcom_portal_service.outp_doctor_portal_service.cpoe_manager.CpoeSubmit as submit
import UI.com_th_supcom_portal_service.usercenter.login as login
import UI.common_th_supcom_config.test_case_config.TestCaseCodeTable as TestCaseCodeTable
from UI.com_th_supcom_api.common.Cache import Cache
from UI.com_th_supcom_api.common.Wait import on_click, send_value
# from UI.com_th_supcom_portal_service.outp_doctor_portal_service.adt_patient_manager.PatientListOutOrderService import \
#     test_workstation, test_diagnose


def test_emr_pds(browser,pdsList,cache):


    # 判断门诊医生站是否打开
    login.select_workstation(browser, '门诊医生站', cache)
    #进入医嘱开立界面

    browser.find_element_by_xpath(CpoeOutOrderElement.div[4]['key']).click()
    time.sleep(2)
    element = browser.find_element_by_link_text('门诊医嘱开立')
    element.click()

    browser.find_element_by_xpath(CpoeOutOrderElement.input[12]['key']).send_keys(str(cache.get('patient_card'))+'\n')
    time.sleep(2)
    browser.find_element_by_xpath(CpoeOutOrderElement.input[12]['key']).click()

    dict = TestCaseCodeTable.cpoe_out_order
    type = pdsList[dict['cpoe_type']]
    pdsName = pdsList[dict['cpoe_name']]
    takeMedicine = pdsList[dict['is_outpresc']]
    useLevel = pdsList[dict['dosage']]
    tuJin = pdsList[dict['way']]
    pinCi = pdsList[dict['frequency']]
    liaoChen = pdsList[dict['course_treat']]
    aim = pdsList[dict['treat_pur']]
    list=[type,pdsName,takeMedicine,useLevel,tuJin,pinCi,liaoChen,aim]
    pdsEmrs = []
    pdsEmrs.append(pdsList)
    #判断药疗医嘱是否开立
    if cache.get('pds_emr'):
        cache.set('pds_emr',cache.get('pds_emr')+pdsEmrs)
    else:
        cache.set('pds_emr',pdsEmrs)
    #医嘱区域
    # try:
    doctorAdviceElement=browser.find_element_by_xpath(CpoeOutOrderElement.div[0]['key'])

    if '没有可显示的数据' in doctorAdviceElement.text:
        pds_emr_login(browser,list,pdsList,cache)
        submit.test_cpoe_submit(browser,'处方笺')
    else:
        pds_emr(browser, list, pdsList, cache)
        submit.test_cpoe_submit(browser, '处方笺')

    # except :
    #        pds_emr(browser,list,pdsList,cache)



def pds_emr(browser,list,pdsList,cache):
    on_click(browser, (By.XPATH, CpoeOutOrderElement.input[9]['key']))
    js = "document.getElementsByTagName('img')[54].click()"
    browser.execute_script(js)

    # tyElement = browser.find_element_by_xpath(
    #     str(CpoeOutOrderElement.select[3]['key']) + 'div[' + str(list[0]) + ']')
    # tyElement.click()
    on_click(browser, (By.XPATH, '//div[contains(text(),"药疗")]'))
    pdsNameElement1 = browser.find_element_by_xpath(CpoeOutOrderElement.input[9]['key'])
    pdsNameElement1.send_keys(list[1])
    time.sleep(1.5)
    pdsNameElement1.send_keys(Keys.ENTER)
    if list[2] == 1:
        takeMedicineElement = browser.find_element_by_xpath(CpoeOutOrderElement.input[3]['key'])
        takeMedicineElement.click()
    time.sleep(1.5)
    useLevelElement = browser.find_element_by_xpath(CpoeOutOrderElement.input[10]['key'])
    useLevelElement.send_keys(list[3])
    #途径
    send_value(browser,(By.XPATH,'/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div/div/div/div[2]/div[2]/div[1]/div[8]/div[3]/div/div[1]/div/input'),'口服')
    time.sleep(1.5)
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div/div/div/div[2]/div[2]/div[1]/div[8]/div[3]/div/div[1]/div/input').send_keys(Keys.ENTER)
    #频次
    js = "document.getElementsByTagName('img')[58].click()"
    browser.execute_script(js)
    time.sleep(1.5)
    browser.find_element_by_xpath(
        '/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div/div/div/div[2]/div[2]/div[1]/div[8]/div[4]/div/div[1]/div/input').send_keys(
        Keys.ENTER)
    #疗程
    send_value(browser, (By.XPATH,
                         '/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div/div/div/div[2]/div[2]/div[1]/div[8]/div[6]/div/div[1]/div/input'),
               '1')
    browser.find_element_by_xpath(
        '/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[2]/div[1]/div/div[5]/div/div[1]/div/input').send_keys(
        Keys.ENTER)
    time.sleep(1.5)
    js = "document.getElementsByTagName('button')[13].click()"
    browser.execute_script(js)
    cache.set('actionDepartment', '门诊药房')
    listUrl = '医嘱'
    Utility.microsoft_xps_document_writer(listUrl)


def pds_emr_login(browser,list,pdsList,cache):
    # typeElement1 = browser.find_element_by_xpath(CpoeOutOrderElement.img[5]['key'])
    # typeElement1.click()
    # time.sleep(2)
    on_click(browser,(By.XPATH,CpoeOutOrderElement.input[9]['key']))
    js = "document.getElementsByTagName('img')[54].click()"
    browser.execute_script(js)

    # tyElement = browser.find_element_by_xpath(
    #     str(CpoeOutOrderElement.select[3]['key']) + 'div[' + str(list[0]) + ']')
    # tyElement.click()
    on_click(browser,(By.XPATH,'//div[contains(text(),"药疗")]'))
    pdsNameElement1 = browser.find_element_by_xpath(CpoeOutOrderElement.input[9]['key'])
    pdsNameElement1.send_keys(list[1])
    time.sleep(1.5)
    pdsNameElement1.send_keys(Keys.ENTER)
    if list[2] == 1:
        takeMedicineElement = browser.find_element_by_xpath(CpoeOutOrderElement.input[3]['key'])
        takeMedicineElement.click()
    time.sleep(1.5)
    useLevelElement = browser.find_element_by_xpath(CpoeOutOrderElement.input[10]['key'])
    useLevelElement.send_keys(list[3])
    # tuJinElement = browser.find_element_by_xpath(CpoeOutOrderElement.img[6]['key'])
    # tuJinElement.click()
    # js = "document.getElementsByTagName('img')[57].click()"
    # browser.execute_script(js)
    # time.sleep(2)
    # browser.find_element_by_xpath('//div[contains(text(),"口服")]').send_keys(Keys.ENTER)

    send_value(browser,(By.XPATH,'/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div/div/div/div[2]/div[2]/div[1]/div[6]/div[3]/div/div[1]/div/input'),'口服')
    time.sleep(1.5)
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div/div/div/div[2]/div[2]/div[1]/div[6]/div[3]/div/div[1]/div/input').send_keys(Keys.ENTER)



    js = "document.getElementsByTagName('img')[58].click()"
    browser.execute_script(js)
    time.sleep(1.5)
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div/div/div/div[2]/div[2]/div[1]/div[6]/div[4]/div/div[1]/div/input').send_keys(Keys.ENTER)
    # liaoChenElement = browser.find_element_by_xpath(CpoeOutOrderElement.input[11]['key'])
    # liaoChenElement.send_keys(list[6])
    # liaoChenElement.send_keys(Keys.ENTER)
    send_value(browser,(By.XPATH,'/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div/div/div/div[2]/div[2]/div[1]/div[6]/div[6]/div/div[1]/div/input'),'1')
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div/div/div/div[2]/div[2]/div[1]/div[6]/div[6]/div/div[1]/div/input').send_keys(Keys.ENTER)
    time.sleep(1.5)
    js = "document.getElementsByTagName('button')[13].click()"
    browser.execute_script(js)
    cache.set('actionDepartment','门诊药房')
    listUrl = '医嘱'
    Utility.microsoft_xps_document_writer(listUrl)


# if __name__ == '__main__':
#     browser = common.browser()
#     testcase = {'用户名': 'jfli', '密码': '123456'}
#     cache = Cache({})
#     cache.set('resultType',1)
#     cache.set('specialName', '眼科门诊')
#     cache.set('patient_card','%E?;1004627675=99015017425?+E?')
#     login.test_login(browser, testcase, cache)
#     emrList = {'诊断类别': '2', '诊断名称': '神经痛'}
#     # test_workstation(browser, cache)
#     # test_diagnose(browser, emrList, cache)
#     pdsList = {'途径': 1, '患者姓名': 'ray', '用药目的': '', '诊断类别': 1, '患者卡号': '%E?;1004627675=99015017425?+E?', '诊断名称': '神经痛', '频次': 1, '每次用量': 1, '医嘱类型': 3, '是否带药': 0, '医嘱名称拼音码': 'wwsjn', '执行科室': '', '疗程': 1}
#     test_emr_pds(browser, pdsList, cache)