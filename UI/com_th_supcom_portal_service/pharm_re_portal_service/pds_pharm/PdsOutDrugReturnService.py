'''
处方退药
'''
from selenium.webdriver.common.by import By

from UI.com_th_supcom_api.common.Cache import Cache

import UI.com_th_supcom_portal_service.usercenter.login as login
import UI.com_th_supcom_portal_element.pharm_re_portal_element.pds_pharm.PdsOutDrugReturnElement as pharm_return

import time
from selenium.webdriver.common.keys import Keys
import random

import UI.com_th_supcom_api.common.Common as Common


import time
from selenium.webdriver.common.keys import Keys
import random
# import PdsApplyPharmService
import re

from UI.com_th_supcom_api.common.Utility import microsoft_xps_document_writer
from UI.com_th_supcom_api.common.Wait import on_click
# from UI.com_th_supcom_portal_service.pharm_re_portal_service.pds_pharm.PdsApplyPharmService import test_apply_pharm


def test_pharm_return(browser,cache):

    applications = list(cache['处方单'].keys())

    # 判断门诊挂号收费工作站是否打开
    login.select_workstation(browser, '药房工作站', cache)
    on_click(browser, (By.XPATH, '//div[contains(text(),"收方管理")]'))
    on_click(browser, (By.LINK_TEXT, "处方供药"))
    on_click(browser, (By.XPATH, '//div[contains(text(),"收方管理")]'))
    on_click(browser, (By.LINK_TEXT, "核对发药"))

    #进入处方退药界面
    browser.find_element_by_xpath(pharm_return.div[0]['key']).click()
    browser.find_element_by_link_text('处方退药').click()

    #退药信息区域
    drug_return_message = pharm_return.div[1]['key']

    #患者信息区域
    patient_message = pharm_return.div[2]['key']

    #申请单列表区域
    application_list = pharm_return.div[3]['key']

    #退药明细区域
    drug_return_detail = pharm_return.div[4]['key']

    calendar_element = browser.find_element_by_xpath(drug_return_message).find_elements_by_tag_name('input')[3]
    js = "document.getElementsByTagName('fieldset')[4].getElementsByTagName('input')[3].removeAttribute('readonly')"
    browser.execute_script(js)
    calendar_element.clear()
    calendar_element.send_keys(time.strftime("%Y-%m-%d", time.localtime()))
    time.sleep(2)
    js = "document.getElementsByTagName('fieldset')[4].getElementsByTagName('input')[3].blur()"
    browser.execute_script(js)
    browser.find_element_by_xpath(drug_return_message).find_elements_by_tag_name('img')[1].click()
    browser.find_element_by_xpath("//button[contains(text(),'今天')]").send_keys(Keys.ENTER)
    swip_card_element = browser.find_element_by_xpath(drug_return_message).find_elements_by_tag_name('input')[0]
    swip_card_element.clear()
    swip_card_element.send_keys(str(cache['patient_card'])+'\n')
    patient_message_elements = browser.find_element_by_xpath(patient_message).find_elements_by_tag_name('input')
    label_elements = browser.find_element_by_xpath(patient_message).find_elements_by_tag_name('label')

    patient_dict = {}
    for i in range(0, len(patient_message_elements)):
        patient_dict[label_elements[i].text] = patient_message_elements[i].text
    '''
    数据验证
    '''
    application_list_elements = browser.find_element_by_xpath(application_list).find_elements_by_tag_name('tr')
    for i in range(0, len(application_list_elements)):
        applyElement = application_list_elements[i].find_elements_by_tag_name('div')
        for j in range(0, len(applyElement)):
            for appliction in applications:
                if applyElement[j].text == appliction:
                    applyElement[j].click()

    drug_return_detail_elements = browser.find_element_by_xpath(drug_return_detail).find_elements_by_tag_name('tr')
    for drug_detail in drug_return_detail_elements:
        # drug_return_num = drug_detail.find_elements_by_tag_name('span')[1].text
        # print(drug_return_num)
        # number = random.randint(1,drug_return_num)
        # drug_detail.find_elements_by_tag_name('div')[7].send_keys(number)

        drug_return_num = int(re.sub('[\u4e00-\u9fa5]','',(drug_detail.find_elements_by_tag_name('span')[1].text)))
        number = random.randint(1,drug_return_num)
        drug_detail.find_elements_by_tag_name('div')[6].click()
        time.sleep(1)
        browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div[4]/div/div[2]/div[1]/div[2]/div[2]/div[1]/div/div[1]/div[1]/div[2]/div[2]/div/input').send_keys(number)
        # js = 'document.getElementsByClassName(" x-form-field x-form-text xh-highlight  x-form-focus")[0].innerHTML=1'
        # browser.execute_script(js)
    browser.find_element_by_xpath("//button[contains(text(),'退药(O)')]").click()
    time.sleep(1)
    browser.find_elements_by_xpath("//button[contains(text(),'确认(O)')]")[1].click()
    microsoft_xps_document_writer('退药单')
    cache.set('apply_date', time.strftime("%Y-%m-%d", time.localtime()))
    cache.set('apply_card', applications)
    browser.refresh()




if __name__ == '__main__':
    cache = Cache({})
    cache.set('resultType','1')
    cache.set('specialName','急诊内科')
    cache.set('检查单',{'02D2017042000008': '放射科', '02D2017042000009': '放射科'})
    cache.set('patient_card', '%E?;1004627675=99015017425?+E?')
    cache.set('处方单', {'02A201707-0400024': '门诊药房（光谷）'})
    cache.set('pds_emr', [{'疗程': 1, '医嘱名称': '温胃舒胶囊', '每次用量': 1, '药品规格': '0.4g@合肥华润神鹿(24)', '频次': 1}])
    browser = Common.browser()
    testcase = {'用户名': 'jfli', '密码': '123456'}
    login.test_login(browser, testcase, cache)
    # test_apply_pharm(browser, cache)
    # PdsApplyPharmService.test_apply_pharm(browser, cache)

    test_pharm_return(browser, cache)

