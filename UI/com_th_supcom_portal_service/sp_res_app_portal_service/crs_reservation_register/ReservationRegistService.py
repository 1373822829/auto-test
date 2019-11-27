#coding=utf-8
'''
预约登记管理
'''
from selenium.webdriver.common.by import By

import UI.com_th_supcom_portal_service.usercenter.login as login
import UI.com_th_supcom_portal_element.sp_res_app_portal_element.crs_reservation_register.ReservationRegistElement as reservation
import time
import UI.com_th_supcom_api.common.Common as common
import UI.com_th_supcom_portal_service.sp_res_app_portal_service.work.WorkPlatService as work_select
import UI.com_th_supcom_api.common.Utility as utility
from UI.com_th_supcom_api.common.Cache import Cache
from UI.com_th_supcom_api.common.Wait import on_click


def test_reservation_regist(browser,cache):
    #判断检查预约工作站是否打开
    login.select_workstation(browser, '检查预约', cache)
    work_select.select_department(browser,cache)
    browser.find_element_by_xpath(reservation.div[0]['key']).click()
    browser.find_element_by_link_text('预约登记管理').click()
    time.sleep(2)

    apply_list = list(cache['检查单'].keys())

    #选取预约类型（门诊o  住院i）
    reservation_type = reservation.div[1]['key']

    #刷卡
    swip_card = reservation.div[2]['key']

    #是否预约按钮区域
    res_button = reservation.div[3]['key']

    #申请单列表区域
    application_list = reservation.div[4]['key']

    #患者列表区域
    pai_detail = reservation.div[5]['key']

    #申请单明细区域
    application_detail = reservation.div[6]['key']

    # 预约日期区域
    calendar_xpath = reservation.div[7]['key']

    #预约资源明细区域
    res_resource_detail = reservation.div[8]['key']

    #提示框
    prompt = reservation.div[9]['key']

    #确认预约框
    sure_res = reservation.div[10]['key']


    # reservation_type_elements = browser.find_element_by_xpath(reservation_type).find_elements_by_tag_name('button')
    if cache['pai_type'] == 'o':
        browser.find_element_by_link_text('门诊预约').click()
    elif cache['pai_type'] == 'i':
        browser.find_element_by_link_text('住院预约').click()
    swip_card_element = browser.find_element_by_xpath(swip_card).find_elements_by_tag_name('input')
    swip_card_element[0].send_keys(str(cache['userId'])+'\n')
    time.sleep(2)

    #选取申请单
    for apply in apply_list:
        browser.find_element_by_xpath("//div[contains(text(),'"+apply+"')]").click()

        application_list_elements = browser.find_element_by_xpath(application_list).find_elements_by_tag_name('div')

        #预约当前时间最近的且预约人数<可预约人数

        #当前时间
        date = time.strftime("%Y-%m-%d", time.localtime())
        remove_js = "document.getElementsByTagName('input')[16].removeAttribute('readonly')"
        focus_js = "document.getElementsByTagName('input')[16].blur()"
        input_locator = (By.XPATH,calendar_xpath+'//input[1]')
        img_locator = (By.XPATH,calendar_xpath+'//img[1]')
        common.calendar(browser,remove_js,focus_js,input_locator,img_locator,date)
        time.sleep(2)
        now = time.strftime("%Y-%m-%d %H:%M", time.localtime())
        table_elements = browser.find_element_by_xpath(res_resource_detail).find_elements_by_tag_name('table')
        for table_element in table_elements:
           div_elements = table_element.find_elements_by_tag_name('div')
           if div_elements[3].text>now:
               print(div_elements[5].text)
               if div_elements[4].text>div_elements[5].text:
                   div_elements[4].click()
                   break

        browser.find_element_by_xpath("//button[contains(text(),'预约并确认')]").click()
        browser.find_element_by_xpath("//button[contains(text(),'是')]").click()
        # browser.find_element_by_xpath("//button[text()='确认')]").click()
        locator = (By.XPATH,"//button[text()='确认']")
        on_click(browser,locator)
        time.sleep(4)
        url = "检查预约单"
        utility.microsoft_xps_document_writer(url)


if __name__ == "__main__":
    browser = common.browser()
    cache = Cache({})
    cache.set('检查单',{'02D2017060500055':'预约小组'})
    cache.set('pai_type','o')
    cache.set('userId','%E?;1004627675=99015017425?+E?')
    testcase = {'用户名': 'jfli', '密码': '123456'}
    login.test_login(browser,testcase,cache)
    test_reservation_regist(browser, cache)



