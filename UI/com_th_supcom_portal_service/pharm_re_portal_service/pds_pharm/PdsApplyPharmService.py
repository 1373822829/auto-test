'''
选取就诊科室
'''
import math

from selenium.webdriver.common.by import By

from UI.com_th_supcom_api.common.Wait import on_click, get_text

from UI.com_th_supcom_api.common.Cache import Cache

from UI.com_th_supcom_api.common import Log
from UI.com_th_supcom_portal_template.pharm_re_portal_template.Pharm import appy_pham_temp
from UI.common_th_supcom_config.test_case_config.TestCaseCodeTable import cpoe_out_order

import UI.com_th_supcom_portal_element.pharm_re_portal_element.pds_pharm.PdsApplyPharmElement as PdsApplyPharmElement
import UI.com_th_supcom_api.common.Utility as Utility
import time
import UI.com_th_supcom_portal_service.usercenter.login as login
from selenium.webdriver.common.keys import Keys
import UI.com_th_supcom_api.common.Common as Common
import UI.com_th_supcom_portal_dao.pharm_re_portal_dao.ApplyPharmVerify as dao

log = Log.Logger(__name__)
def test_apply_pharm(browser,cache):
    log.info('开始运行供药脚本')
    # 判断门诊挂号收费工作站是否打开
    login.select_workstation(browser, '药房工作站', cache)

    if int(cache.get('resultType')) != 1:
        return

    # 获取申请单号及执行科室
    application_list = list(cache.get('处方单').keys())
    execute_list = list(set(list(cache.get('处方单').values())))

    # 选取工作站
    workstationElement = browser.find_element_by_xpath(PdsApplyPharmElement.button[0]['key'])
    workstationElement.click()
    time.sleep(1)
    workstationInputElement = browser.find_element_by_xpath(PdsApplyPharmElement.input[0]['key'])
    workstationInputElement.clear()
    time.sleep(1)
    if workstationInputElement.text == "":
        workstationInputElement.send_keys("光谷院区: " + execute_list[0])
    else:
        workstationInputElement.clear()
        time.sleep(1)
        workstationInputElement.send_keys("光谷院区: " + execute_list[0])


    time.sleep(1)
    workstationInputElement.send_keys(Keys.ENTER)
    on_click(browser,(By.XPATH,'//button[contains(text(),"确定")]'))
    browser.implicitly_wait(30)
    time.sleep(2)
    # 处方供药
    reManageElement = browser.find_element_by_xpath(PdsApplyPharmElement.div[0]['key'])
    reManageElement.click()
    browser.find_element_by_link_text('处方供药').click()
    time.sleep(2)

    calendar_element = \
    browser.find_element_by_xpath(PdsApplyPharmElement.fieldset[2]['key']).find_elements_by_tag_name('input')[3]
    js = "document.getElementsByTagName('fieldset')[0].getElementsByTagName('input')[3].removeAttribute('readonly')"
    browser.execute_script(js)
    calendar_element.clear()
    calendar_element.send_keys(time.strftime("%Y-%m-%d", time.localtime()))
    time.sleep(2)
    js = "document.getElementsByTagName('fieldset')[0].getElementsByTagName('input')[3].blur()"
    browser.execute_script(js)
    browser.find_element_by_xpath(PdsApplyPharmElement.fieldset[2]['key']).find_elements_by_tag_name('img')[1].click()
    browser.find_element_by_xpath("//button[contains(text(),'今天')]").send_keys(Keys.ENTER)

    cardElement = browser.find_element_by_xpath(PdsApplyPharmElement.input[1]['key'])
    cardElement.send_keys(cache.get('patient_card') + '\n')
    browser.implicitly_wait(30)
    receiveListElement = browser.find_element_by_xpath(PdsApplyPharmElement.div[3]['key']).find_elements_by_tag_name(
        'tr')
    for i in range(0, len(receiveListElement)):
        applyElement = receiveListElement[i].find_elements_by_tag_name('div')
        for j in range(0, len(applyElement)):
            for appliction in application_list:
                if applyElement[j].text == appliction:
                    applyElement[j].click()



    #获取处方药品信息
    drug_detail = PdsApplyPharmElement.div[4]['key']
    drug_detail_elements = browser.find_element_by_xpath(drug_detail).find_elements_by_tag_name('tr')
    verifys = []
    pds_emr = cache.get('pds_emr')
    for i in range(0,len(drug_detail_elements)):
        pham = []
        drug_elements = drug_detail_elements[i].find_elements_by_tag_name('div')
        for drug in drug_elements:
            pham.append(drug.text)
        verifys.append(pham)
    #验证药品库存数量
    totals = []     #处方供药的药品总量的集合
    pham_stocks = []  #药品库存集合

    for verify in verifys:
        for i in range(0,len(pds_emr)):
            if pds_emr[i][cpoe_out_order['pham_name']] == verify[2]:
                pham_num = dao.find_pham_num(verify[2],verify[3],execute_list[0])  #药品库存数量
                pham_basic_info = dao.find_pham_basic_info(verify[2],verify[3])    #药品基本信息
                appy_pham_temp(pham_num,pham_basic_info,pds_emr[i])                #调用供药模板
                total = math.ceil(pds_emr[i][cpoe_out_order['dosage']]/pham_basic_info.dose_per_unit*pham_basic_info.package_factor)#药品总量
                totals.append(total)
                pham_stocks.append(pham_num[0])
            else:
                log.info('未找到%s医嘱'%verify[2])
    time.sleep(1)
    recSureElement = browser.find_element_by_xpath(PdsApplyPharmElement.button[2]['key'])
    recSureElement.click()
    on_click(browser,(By.XPATH,'//button[contains(text(),"是")]'))
    browser.implicitly_wait(30)
    time.sleep(2)
    listUrl = '处方单'
    Utility.microsoft_xps_document_writer(listUrl)

    browser.implicitly_wait(30)
    log.info('获取药品信息....')
    time.sleep(4)



    #验证
    pham_stocks_after = []   #供药后，药品库存
    for verify in verifys:
        for i in range(0,len(pds_emr)):
            if pds_emr[i][cpoe_out_order['pham_name']] == verify[2]:
                pham_num = dao.find_pham_num(verify[2],verify[3],execute_list[0])
                pham_basic_info = dao.find_pham_basic_info(verify[2],verify[3])
                appy_pham_temp(pham_num,pham_basic_info,pds_emr[i])
                pham_stocks_after.append(pham_num[0])
            else:
                log.info('未找到%s医嘱'%verify[2])
    status = True
    for i in range(0,len(totals)):
        print(pham_stocks[i] - pham_stocks_after[i] == totals[i])
        if not (pham_stocks[i] - pham_stocks_after[i] == totals[i]):
            status = False
            log.info('处方供药，药品库存数量验证fial')
    if status:
        log.info('处方供药，药品库存数量验证pass')




    #核对发药
    receiveManagerElement = browser.find_element_by_xpath(PdsApplyPharmElement.div[0]['key'])
    receiveManagerElement.click()
    # sendMedElement=browser.find_element_by_xpath(PdsApplyPharmElement.a[6]['key'])
    # sendMedElement.click()
    browser.find_element_by_link_text('核对发药').click()
    sendCardElement=browser.find_element_by_xpath(PdsApplyPharmElement.fieldset[0]['key']).find_elements_by_tag_name('input')[1]

    sendCardElement.send_keys(str(cache.get('patient_card'))+'\n')
    end_time = time.time()+3
    while True:
        if '暂时没有您需要的数据...' not in get_text(browser,(By.XPATH,PdsApplyPharmElement.div[5]['key'])):
            break
        if time.time()>end_time:
            log.info('核对发药页面加载超时或没有找到发药单')
            return
    # browser.find_element_by_xpath(PdsApplyPharmElement.fieldset[0]['key']).find_elements_by_tag_name('button')[0].click()
    browser.find_element_by_xpath("//button[contains(text(),'发药(O)')]").click()
    browser.find_element_by_xpath("//button[contains(text(),'是')]").click()
    log.info('供药脚本运行结束')

if __name__ == "__main__":
    cache = Cache({})
    cache.set('resultType', '1')
    cache.set('specialName', '急诊内科'),
    cache.set('处方单',{'02A201707-0400024': '门诊药房（光谷）'})
    cache.set('patient_card','%E?;1004627675=99015017425?+E?')
    cache.set('pds_emr',[{'疗程': 1, '医嘱名称': '温胃舒胶囊', '每次用量': 1, '药品规格': '0.4g@合肥华润神鹿(24)', '频次': 1}])
    browser = Common.browser()
    testcase = {'用户名': 'jfli', '密码': '123456'}
    login.test_login(browser, testcase, cache)
    test_apply_pharm(browser, cache)

