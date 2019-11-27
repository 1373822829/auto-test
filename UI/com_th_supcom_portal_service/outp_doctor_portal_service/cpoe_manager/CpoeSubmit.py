'''
提交医嘱
'''
import UI.com_th_supcom_api.common.Utility as Utility
import UI.com_th_supcom_portal_element.outp_doctor_portal_element.cpoe_manager.CpoeOutOrderElement as CpoeOutOrderElement
import time


def test_cpoe_submit(browser,bill_name):
    time.sleep(1)
    submitElement = browser.find_element_by_xpath(CpoeOutOrderElement.button[4]['key'])
    submitElement.click()
    time.sleep(3)
    Utility.microsoft_xps_document_writer(bill_name)
    listUrl = '医嘱'
    Utility.microsoft_xps_document_writer(listUrl)



