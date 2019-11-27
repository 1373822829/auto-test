'''
预付费退费（执行科室退费)
'''
from selenium.webdriver.common.by import By

import UI.com_th_supcom_portal_element.outp_bill_portal_element.out_bill_refund.OutbillPrepayRefuseElement as OutbillPrepayRefuseElement

import UI.com_th_supcom_api.common.Utility as Utility
from selenium.webdriver.common.keys import Keys
import UI.com_th_supcom_portal_service.usercenter.login as login
import UI.com_th_supcom_api.common.Common as Common
import time

from UI.com_th_supcom_api.common.Cache import Cache
from UI.com_th_supcom_api.common.Wait import on_click


def test_outbill_prepay_refuse(browser,cache):
     #判断门诊挂号收费工作站是否打开
     login.select_workstation(browser, '门诊挂号收费工作台', cache)

     #获取退费管理菜单元素
     outbill_refund = OutbillPrepayRefuseElement.div[0]['key']

     #获取预付费缴费（执行科室退费）元素
     outbpre_refuse = OutbillPrepayRefuseElement.a[0]['key']

     #获取提示框
     alert = OutbillPrepayRefuseElement.button[0]['key']

     #获取申请单列表区域元素
     apply_list = OutbillPrepayRefuseElement.div[1]['key']

     #获取患者信息元素
     patient_message = OutbillPrepayRefuseElement.form[0]['key']

     #获取退费明细列表区域元素
     refund_detail = OutbillPrepayRefuseElement.div[2]['key']

     #获取卡号元素
     card = OutbillPrepayRefuseElement.div[3]['key']

     #获取按钮区域元素
     button = OutbillPrepayRefuseElement.div[4]['key']

     #患者信息列表
     patient_message_dict = {}

     #申请单号列表
     apply_card = []

     #是否退费
     sure_button = OutbillPrepayRefuseElement.button[1]['key']

     #退费金额合计
     refund_count = OutbillPrepayRefuseElement.b[0]['key']

     outbill_refund_element = browser.find_element_by_xpath(outbill_refund)
     outbill_refund_element.click()
     browser.implicitly_wait(30)
     outbpre_refuse_element = browser.find_element_by_xpath(outbpre_refuse)
     outbpre_refuse_element.click()
     browser.implicitly_wait(30)
     alert_element = browser.find_element_by_xpath(alert)
     alert_element.click()
     card_element = browser.find_element_by_xpath(card).find_elements_by_tag_name('input')
     card_element[0].clear()

     card_element[0].send_keys(str(cache.get('patient_card'))+'\n')

     patient_message_elements = browser.find_element_by_xpath(patient_message).find_elements_by_tag_name('input')
     # for i in range(0,len(patient_message_elements)):
     #     patient_message_list.append(patient_message_elements[i].text)
     patient_message_dict['patient_id'] = patient_message_elements[0].text
     patient_message_dict['balance'] = patient_message_elements[1].text
     # 数据校验
     '''
     '''

     apply_list_element = browser.find_element_by_xpath(apply_list).find_elements_by_tag_name('tr')
     for i in range(0,len(apply_list_element)):
         apply_element = apply_list_element[i].find_elements_by_tag_name('div')
         for j in range(0,len(apply_element)):
             if cache.get('apply_date') == apply_element[j].text:
                 apply_element[j].click()
                 browser.implicitly_wait(30)
                 time.sleep(2)
                 refund_detail_elements = browser.find_element_by_xpath(refund_detail).find_elements_by_tag_name('table')
                 # print(len(refund_detail_elements))
                 for i in range(0, len(refund_detail_elements)):
                     apply_text = refund_detail_elements[i].find_elements_by_tag_name('div')[7].text
                     apply_card.append(apply_text)

                 print(apply_card)
                 if set(apply_card).issubset(set(cache.get('apply_card'))):
                     patient_message_dict['refund_count'] = browser.find_element_by_xpath(refund_count)
                     '''
                  数据校验
                  '''

                     on_click(browser,(By.XPATH,'//button[contains(text(),"退费")]'))

                     on_click(browser, (By.XPATH, '//button[contains(text(),"确定")]'))
                     time.sleep(4)
                     listUrl = '退费发票单'
                     Utility.microsoft_xps_document_writer(listUrl)
                     browser.implicitly_wait(30)
                     on_click(browser, (By.XPATH, '//button[contains(text(),"确定")]'))
                     return
                 else:
                     apply_card = []
     browser.refresh()



if __name__ == '__main__':
    cache = Cache({})
    browser = Common.browser()
    testcase = {'用户名': 'jfli', '密码': '123456'}
    login.test_login(browser,testcase,cache)
    cache.set('apply_date','2017-07-04')
    cache.set('apply_card',['02A201707-0400024'])
    cache.set('patient_card', '%E?;1004627675=99015017425?+E?')
    test_outbill_prepay_refuse(browser, cache)






