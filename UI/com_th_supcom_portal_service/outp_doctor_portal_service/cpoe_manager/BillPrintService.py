'''
单据打印
'''

import UI.com_th_supcom_portal_element.outp_doctor_portal_element.cpoe_manager.BillPrintElement as BillPrintElement
import UI.com_th_supcom_portal_service.usercenter.login as login
import time
import UI.com_th_supcom_api.common.Common as common
import sys
sys.path.append(r'..\adt_patient_manager\patient_list_out')
# import PatientListOutOrderService as pai_list

def test_bill_print(browser,cache):
    #判断门诊医生站是否打开
    login.select_workstation(browser, '门诊医生站', cache)

    cpoeManager=BillPrintElement.div[1]['key']
    functionTable=BillPrintElement.table[0]['key']
    billType=BillPrintElement.ul[0]['key']
    billList=BillPrintElement.div[0]['key']
    cpoeManagerElement=browser.find_element_by_xpath(cpoeManager)
    cpoeManagerElement.click()
    time.sleep(2)
    elements = browser.find_elements_by_tag_name('a')
    for element in elements:
        if element.text == '单据打印':
            element.click()
            break
    time.sleep(2)
    # printElement=browser.find_element_by_xpath(functionTable).find_elements_by_tag_name('button')[0]
    # billTypeElemnts=browser.find_element_by_xpath(billType).find_elements_by_tag_name('span')

    # for i in range(0,len(billTypeElemnts)):
    #     if "处方单" in billTypeElemnts[i].text:
    #         billTypeElemnts[i].click()

    billListElements=browser.find_element_by_xpath(billList).find_elements_by_tag_name('tr')

    application_dict = {}
    bill_name = ''
    num = -1

    for i in range(0,len(billListElements)):
        bill_detail_elements = billListElements[i].find_elements_by_tag_name('td')
       
        if len(bill_detail_elements)<2:
            span_elements = billListElements[i].find_elements_by_tag_name('span')
            if len(span_elements) == 2 and '张' in span_elements[1].text:
                application_dict = {}
                if num != -1:
                    billListElements[num].find_element_by_tag_name('input').click()
                bill_name = str(span_elements[1].text).split('(')[0]
                billListElements[i].find_element_by_tag_name('input').click()
                num = i
                continue
            else:
                if billListElements[i].find_element_by_tag_name('input').is_selected():
                    bill_elements = billListElements[i+1].find_elements_by_tag_name('td')
                    application_dict[str(bill_elements[0].text).strip()] = bill_elements[3].text
                    cache.set(bill_name,application_dict)
                    continue


