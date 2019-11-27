'''
检查预约工作站选取科室
'''
import UI.com_th_supcom_portal_service.usercenter.login as login
import UI.com_th_supcom_api.common.Common as common
import UI.com_th_supcom_portal_element.sp_res_app_portal_element.sp_res_app_work_plat.WorkPlatElement as plat
from selenium.webdriver.common.keys import Keys
import time
import UI.com_th_supcom_portal_element.sp_res_app_portal_element.crs_reservation_register.ReservationRegistElement as reservation
def select_department(browser,cache):
    depart_list = list(cache['检查单'].values())
    buttons = browser.find_elements_by_tag_name('button')
    for button in buttons:
        if  '【'in button.text :
            button.click()
            browser.find_element_by_xpath(plat.input[0]['key']).clear()
            # browser.find_element_by_xpath(plat.input[0]['key']).send_keys('光谷院区: '+depart_list[1])
            browser.find_element_by_xpath(plat.input[0]['key']).send_keys('光谷院区: 预约小组' )
            time.sleep(1)
            browser.find_element_by_xpath(plat.input[0]['key']).send_keys(Keys.ENTER)
            browser.find_element_by_xpath(plat.button[0]['key']).click()


if __name__ == '__main__':
    browser = common.browser()
    login.test_login(browser,testcase={'用户名':'jfli','密码':'123456'},cache={})
    login.select_workstation(browser, '检查预约', cache={})
    select_department(browser,cache={'depart':'预约小组'})
    time.sleep(2)

    swip_card = reservation.div[2]['key']
    swip_card_element = browser.find_element_by_xpath(swip_card).find_elements_by_tag_name('input')
    swip_card_element[0].send_keys('%E?;1004627675=99015017425?+E?' + '\n')
    time.sleep(2)
    browser.find_element_by_xpath("//div[contains(text(),'02D2017041400002')]").click()

    element = browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div/div/div[2]/div[1]/div[2]/div/div[3]/div/div[2]/div[1]/div').find_elements_by_tag_name('input')[0]
    print(element.get_attribute('value'))
    js = "document.getElementsByTagName('input')[16].removeAttribute('readonly')"
    browser.execute_script(js)

    element.clear()
    element.send_keys('2017-04-19')
    time.sleep(2)
    js1 = "document.getElementsByTagName('input')[16].blur()"
    browser.execute_script(js1)

    element1 = browser.find_element_by_xpath(
        '/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div/div/div[2]/div[1]/div[2]/div/div[3]/div/div[2]/div[1]/div').find_elements_by_tag_name('img')[0]
    element1.click()
    browser.find_element_by_xpath("//button[contains(text(),'今天')]").send_keys(Keys.ENTER)
    time.sleep(2)




