'''
登录
'''
import UI.com_th_supcom_portal_element.usercenter.portal.portal as portal
import UI.com_th_supcom_api.common.Utility as utility
import UI.com_th_supcom_api.common.Common as common
import UI.common_th_supcom_config.test_case_config.TestCaseCodeTable as table
import UI.common_th_supcom_config.work_bench_config.WorkBenchUrl as uum
import re
import time
import UI.com_th_supcom_api.common.Log as Log

import UI.common_th_supcom_config.url_config as path

from selenium.webdriver.common.keys import Keys

#日志对象初始化
from UI.com_th_supcom_api.common.Cache import Cache

log = Log.Logger(__name__)

def test_login(browser,testcase,cache):

    log.info("开始运行登陆脚本")
    #判断该uum portal是否打开
    if common.switch_window(browser,'UUM Portal',cache):
        return

    #登录测试用例
    browser.get(path.localhost)
    browser.implicitly_wait(20)

    # 判读用户是否已经登录
    cookies = browser.get_cookies()
    for cookie in cookies:
        if 'CASTGC' in cookie.values():
            browser.delete_all_cookies()
            browser.refresh()
    # browser.maximize_window()
    browser.find_element_by_xpath(portal.用户名).clear()
    browser.find_element_by_xpath(portal.用户名).send_keys(testcase[table.user_login['username']])
    browser.find_element_by_xpath(portal.密码).clear()
    browser.find_element_by_xpath(portal.密码).send_keys(testcase[table.user_login['psw']])
    browser.find_element_by_xpath(portal.登陆).send_keys(Keys.ENTER)
    time.sleep(2)
    if browser.title == 'UUM Portal':
        utility.writeFile('登录  pass')
    else:
        utility.writeFile('登录  fail')
    # browser.find_element_by_xpath(portal.input[2]['key']).click()
    # cache[browser.title] = browser.current_window_handle
    cache.set(browser.title,browser.current_window_handle)
    log.info("登陆脚本运行结束")


def test_logout(browser,cache):
    # 判断该uum portal是否打开
    log.info("开始运行退出脚本")
    if common.switch_window(browser, 'UUM Portal', cache):
        print(cache)
        browser.switch_to_window(cache.get('UUM Portal'))
        browser.find_element_by_xpath("//button[contains(text(),'退出系统')]").click()
        browser.find_element_by_xpath("//button[contains(text(),'是')]").click()
    else:
        raise Exception('请先登录!')
    log.info("退出脚本运行结束")



def select_workstation(browser,workstation,cache):
    #判断工作站是否打开
    if common.switch_window(browser,uum.workstation_name_collation1[workstation],cache):
        browser.switch_to_window(cache.get(uum.workstation_name_collation1[workstation]))
    else:
        browser.switch_to_window(cache.get('UUM Portal'))
        browser.find_element_by_link_text(workstation).send_keys(Keys.ENTER)
        time.sleep(1)
        handles = browser.window_handles
        end_time = time.time()+100
        while True:
            time.sleep(0.5)
            for handle in handles :
                if handle in cache.values():
                    continue
                browser.switch_to_window(handle)
                if re.sub('[A-Za-z0-9.]', '', browser.title).strip() == uum.workstation_name_collation1[workstation]:
                    cache.set(re.sub('[A-Za-z0-9.]', '', browser.title).strip(),browser.current_window_handle)
                    return
            if time.time()>end_time:
                log.info('%s页面加载失败!'%workstation)
                break




if __name__ =="__main__":
    browser = common.browser()
    testcase = {'用户名': 'jfli', '密码': '123456'}
    # caches = {'resultType': '1', 'specialName': '急诊内科', 'userId': '%E?;2001065723=99015011437?+E?'}
    cache = Cache({})
    test_login(browser, testcase, cache)

