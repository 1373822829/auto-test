'''
患者挂号
'''
import UI.com_th_supcom_portal_element.outp_bill_portal_element.reg_manager.PatientVisitCardElement as PatientVisitCardElement
import UI.common_th_supcom_config.test_case_config.TestCaseCodeTable as TestCaseCodeTable
import UI.com_th_supcom_portal_service.usercenter.login as login
import UI.com_th_supcom_api.common.Utility as Utility
import time
import UI.com_th_supcom_api.common.Common as Common
import UI.com_th_supcom_portal_dao.outp_bill_portal_dao.RegistVerify as dao
import UI.com_th_supcom_portal_template.outp_bill_portal_template.RegistTemplate as temp
from UI.com_th_supcom_api.common import Log
from UI.com_th_supcom_api.common.Cache import Cache
#日志对象初始化
log = Log.Logger(__name__)
def test_regist(browser,userList,cache):

    log.info('开始运行挂号脚本')
    login.select_workstation(browser,'门诊挂号收费工作台',cache)
    #点击挂号菜单进入挂号界面
    browser.find_element_by_xpath(PatientVisitCardElement.div[0]['key']).click()
    time.sleep(1)
    element = browser.find_element_by_link_text('门诊挂号(就诊卡)')
    element.click()

    #调取挂号验证模板
    Fee = dao.outp_balance(userList)
    temp.outp_fee_temp(Fee)
    RegSource = dao.outp_regist_master(userList)
    print(RegSource)
    temp.outp_reg_source_temp(RegSource)
    OfficeRegSource = dao.outp_patient_visit(userList)
    temp.outp_office_reg_source_temp(OfficeRegSource)
    balance = Fee.PcaPrepayAccountMaster.balance
    current_no = RegSource.OutpRegMaster.current_no
    current_limits = RegSource.OutpRegMaster.current_limits


    #开始挂号
    dict = TestCaseCodeTable.patient_visit_card
    cardElement = browser.find_element_by_xpath(PatientVisitCardElement.form[0]['key']).find_elements_by_tag_name('input')[3]
    cardElement.clear()
    cardElement.send_keys(userList[dict['patient_card']] + '\n')
    browser.implicitly_wait(30)
    span=browser.find_element_by_xpath(PatientVisitCardElement.span[7]['key']).text
    if span!='是否通过市医保进行结算?':
        raise Exception(span)
    iselfElement = browser.find_element_by_xpath(PatientVisitCardElement.table[0]['key']).find_elements_by_tag_name('button')[1].click()
    # iselfElement.send_keys(Keys.ENTER)
    if userList[dict['special_type']] in '普通和急诊':

        radioElement = browser.find_element_by_xpath(PatientVisitCardElement.radiobutton[4]['key'])
        radioElement.click()
        # browser.find_element_by_xpath("//input[contains(text(),'普通和急诊')]").send_keys(Keys.ENTER)
    if userList[dict['special_type']] in "专家":
        browser.find_element_by_xpath("//label[contains(text(),'专家')]").click()

    specialElement = browser.find_element_by_xpath(PatientVisitCardElement.form[0]['key']).find_elements_by_tag_name('input')[4]
    specialElement.clear()
    time.sleep(2)
    specialElement.send_keys(str(userList[dict['special_num']]))
    time.sleep(2)
    spElement=browser.find_element_by_xpath(PatientVisitCardElement.div[2]['key']).find_elements_by_tag_name('tr')[0]
    # special_messages = spElement.find_elements_by_tag_name('div')

    # verify_data = []
    # for i in range(0,len(special_messages)):
    #     verify_data.append(special_messages[i].text)
    # cache['verify'] = verify_data
    spElement.click()
    time.sleep(1)
    specialElement.send_keys('\n' + '\n')
    time.sleep(1.5)
    browser.find_element_by_xpath('//button[contains(text(),"是")]').click()
    # end_time = time.time()+3
    # status = False
    # while True:
    #     text = browser.find_element_by_xpath("html/body/div").text
    #     print('.'*15)
    #     print(text)
    #     if '挂号成功' in text:
    #         status = True
    #         break
    #     if end_time<time.time():
    #         break
    # if not status:
    #     log.info("挂号失败!")
    #     #抛出异常
    #     Utility.throw_error("挂号失败!")

    # sureElement.send_keys(Keys.ENTER)
    time.sleep(2)
    listUrl='挂号单'
    Utility.microsoft_xps_document_writer(listUrl)
    # cache['resultType']=1
    # cache['userId']=userList[dict['patient_card']]
    # cache['specialName']=userList[dict['special_name']]
    cache.set('resultType',1)
    cache.set('patient_card',userList[dict['patient_card']])
    cache.set('specialName',userList[dict['reside_dept']])
    # 调取挂号验证模板
    FeeAfter = dao.outp_balance(userList)
    temp.outp_fee_temp(FeeAfter)
    RegSourceAfter = dao.outp_regist_master(userList)
    temp.outp_reg_source_temp(RegSourceAfter)
    OfficeRegSourceAfter = dao.outp_patient_visit(userList)
    temp.outp_office_reg_source_temp(OfficeRegSourceAfter)
    bool = True
    #数据验证
    if (balance - FeeAfter.PcaPrepayAccountMaster.balance) == userList[dict['regist_fee']]:
        Utility.writeFile('患者挂号扣费  pass')
    else:
        bool = False
        Utility.writeFile('患者挂号扣费  fail')

    if RegSourceAfter.OutpRegMaster.current_no - current_no == 1  and current_limits - RegSourceAfter.OutpRegMaster.current_limits == 1:
        Utility.writeFile('当前号和已挂数  pass')
    else:
        bool = False
        Utility.writeFile('当前号和已挂数  fail')
    if OfficeRegSourceAfter[0]-OfficeRegSource[0] == 1:
        Utility.writeFile('门办已挂数  pass')
    else:
        bool = False
        Utility.writeFile('门办已挂数  fail')
    log.info('挂号脚本运行结束')










#进入挂号界面
def enter_regist(browser,cache):
    login.select_workstation(browser, '门诊挂号收费工作台', cache)
    # 点击挂号菜单进入挂号界面
    browser.find_element_by_xpath(PatientVisitCardElement.div[0]['key']).click()
    time.sleep(1)
    browser.find_element_by_xpath(PatientVisitCardElement.a[0]['key']).click()

#刷卡
def swip_card(browser,userList):

    dict = TestCaseCodeTable.patient_visit_card
    inputs=browser.find_element_by_xpath(PatientVisitCardElement.form[0]['key']).find_elements_by_tag_name('input')
    cardElement = inputs[3]
    cardElement.clear()
    cardElement.send_keys(userList[dict['patient_card']] + '\n')
    browser.implicitly_wait(30)



#是否自费
def iself_pay(browser):
    iselfElement=browser.find_element_by_xpath(PatientVisitCardElement.table[0]['key']).find_elements_by_tag_name('button')
    inputs = browser.find_element_by_xpath(PatientVisitCardElement.form[0]['key']).find_elements_by_tag_name('input')
    bollen=True
    if bollen:
        sureElement =iselfElement[0]
        iselfElement.click()
        patientName = inputs[0].is_enabled()
    else:
        noElement=iselfElement[1]
        noElement.click()

#选择号源类别
def card_type(browser,number):
    radioElements=browser.find_element_by_xpath(PatientVisitCardElement.form[1]['key']).find_elements_by_tag_name('input')
    radioElement=radioElements[number]
    radioElement.click()

#选择号源
def chooice_card(browser,userList):

    dict = TestCaseCodeTable.patient_visit_card
    specialElement = browser.find_element_by_xpath(PatientVisitCardElement.form[0]['key']).find_elements_by_tag_name('input')[4]
    specialElement.clear()
    specialElement.send_keys(str(userList[dict['special_type']]))
    time.sleep(1)
    spElement = browser.find_element_by_xpath(PatientVisitCardElement.div[2]['key']).find_elements_by_tag_name('tr')[0]
    print(spElement.find_elements_by_tag_name('td')[0].text)
    spElement.click()
    specialElement.send_keys('\n' + '\n')

#是否确认挂号
def sure(browser):
    sureElement = browser.find_element_by_xpath(PatientVisitCardElement.button[11]['key'])
    sureElement.click()

#单据是否打印
def print_bill():
    listUrl = 'D:\\centaurus-a\\UI\\img\\挂号单'
    Utility.microsoft_xps_document_writer(listUrl)



if __name__ == '__main__':
    cache = Cache({})
    browser = Common.browser()
    testcase = {'用户名': 'jfli', '密码': '123456'}
    login.test_login(browser, testcase, cache)
    test_case = {'门诊时间': '全天', '患者姓名': '杨俊熙', '医生': '', '门诊科室': '眼科门诊', '就诊时间': '2017-06-30',
                 '患者卡号': '%E?;1004627675=99015017425?+E?', '专科名称': '急诊眼科', '号源类别': '急诊','专科编码':560}
    test_regist(browser, test_case, cache)


