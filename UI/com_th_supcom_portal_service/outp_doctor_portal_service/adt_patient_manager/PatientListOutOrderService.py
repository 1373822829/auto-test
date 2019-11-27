from UI.com_th_supcom_api.common import Log
import time

import UI.com_th_supcom_portal_element.outp_doctor_portal_element.cpoe_manager.CpoeOutOrderElement as CpoeOutOrderElement
import UI.com_th_supcom_api.common.Common as common
import UI.common_th_supcom_config.test_case_config.TestCaseCodeTable as TestCaseCodeTable
import UI.com_th_supcom_portal_service.usercenter.login as login
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from UI.com_th_supcom_api.common.Cache import Cache

log = Log.Logger(__name__)

def test_workstation(browser,cache):
    log.info('开始运行工作站选择脚本')
    #判断该工作站是否打开
    login.select_workstation(browser,'门诊医生站',cache)

    if int(cache['resultType']) != 1:
        return

    # 选取工作站
    time.sleep(1)
    workstationElement = browser.find_element_by_xpath(CpoeOutOrderElement.button[0]['key'])
    workstationElement.click()
    browser.implicitly_wait(30)
    workstationInputElement = browser.find_element_by_xpath(CpoeOutOrderElement.input[0]['key'])
    time.sleep(2)
    workstationInputElement.clear()
    time.sleep(2)
    workstationInputElement.send_keys("光谷院区: " + cache.get('specialName'))
    time.sleep(1)
    sureElement = browser.find_element_by_xpath(CpoeOutOrderElement.button[1]['key'])
    sureElement.click()
    browser.implicitly_wait(30)

def test_diagnose(browser,diagnoseList,registCache):
    log.info('开始运行诊断脚本')
    #判断该工作站是否打开
    login.select_workstation(browser, '门诊医生站', registCache)
    time.sleep(2)
    #进入患者列表界面
    browser.find_element_by_xpath(CpoeOutOrderElement.div[3]['key']).click()
    # browser.find_element_by_xpath("//button[contains(text(),'确定')]")
    # browser.find_element_by_xpath(CpoeOutOrderElement.a[0]['key']).click()
    browser.find_element_by_link_text('门诊患者列表').click()

    dict = TestCaseCodeTable.diagnose
    #刷卡
    cardElement= browser.find_element_by_xpath(CpoeOutOrderElement.input[1]['key'])
    cardElement.send_keys( registCache.get('patient_card')+ '\n' + '\n')
    browser.implicitly_wait(30)
    time.sleep(2)
    #就诊
    #患者列表区域
    usersElement = browser.find_element_by_xpath(CpoeOutOrderElement.div[1]['key']).find_elements_by_tag_name('tr')
    userElement=usersElement[0].find_elements_by_tag_name('div')[0]
    userText=userElement.text
    ActionChains(browser).double_click(userElement).perform()
    browser.implicitly_wait(30)
    time.sleep(2)
    #诊断
    if userText=="已就诊":
        return
    diagnoseElement = browser.find_element_by_xpath(CpoeOutOrderElement.button[2]['key'])
    diagnoseElement.click()
    browser.implicitly_wait(30)
    diagnoseTypeElement = browser.find_element_by_xpath(CpoeOutOrderElement.img[4]['key'])
    diagnoseTypeElement.click()
    diagElement = browser.find_element_by_xpath(CpoeOutOrderElement.select[int(diagnoseList[dict['dia_type']]) - 1]['key'])
    diagElement.click()
    time.sleep(2)
    diaChooseElement = browser.find_element_by_xpath(CpoeOutOrderElement.input[7]['key'])
    diaChooseElement.send_keys(diagnoseList[dict['dia_name']])
    time.sleep(2)
    diaChooseElement.send_keys(Keys.ENTER)
    saveElement = browser.find_element_by_xpath(CpoeOutOrderElement.button[3]['key'])
    saveElement.click()
    browser.implicitly_wait(30)
    time.sleep(1)
    log.info('诊断脚本运行结束')


##验证挂号脚本是否通过
if __name__=='__main__':
    browser = common.browser()
    cache = Cache({})
    testcase = {'用户名':'jfli','密码':'123456'}
    cache.set('resultType','1')
    cache.set('specialName','急诊内科')
    cache.set('patient_card','%E?;1004627675=99015017425?+E?')
    login.test_login(browser,testcase,cache)
    test_workstation(browser,cache)
    emrList = {'诊断类别': '2', '诊断名称': '神经痛'}
    # test_diagnose(browser,cache,emrList)

