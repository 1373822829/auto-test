#! /usr/bin/env python
#coding=utf-8


import time, os

from selenium.webdriver.common.by import By

from UI.com_th_supcom_api.common import Log
from UI.com_th_supcom_api.common import Utility
from UI.com_th_supcom_api.common.Wait import on_click, send_value, is_not_visible, get_text

from UI.com_th_supcom_api.common.Cache import Cache
from selenium import webdriver
import zipfile


import UI.com_th_supcom_api.common.Common as common
import UI.common_th_supcom_config.url_config as path
import UI.com_th_supcom_portal_service.usercenter.login as login
log = Log.Logger(__name__)
def card(path=r"C:\Users\tjh\Downloads\PC_20170510093337DG.zip"):
    dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    zip = zipfile.ZipFile(path)
    zipname = zip.namelist()
    zip.extractall()
    zip.close()

    filedir = os.path.join(dir, str(zipname[0])) #当前文件路径
    f = open(zipname[0])
    lines = f.readline()
    # print(lines)
    f.close()

    # 拼写制卡卡号
    card = '%E?;' + lines.rstrip('\n').split("|")[1] + '%E+?'
    # print(card)

    #删除解压文件
    if os.path.exists(zipname[0]):
        os.remove(zipname[0])


    print(card)

def switchWindow(browser,windowname):
    all_handles = browser.window_handles
    for handle in all_handles:
        browser.switch_to.window(handle)
        if windowname in browser.title:
            #browser.switch_to_window(handle)
            break

def browser():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
    options.add_argument("--user-data-dir="+r"C:\Users\Administrator\AppData\Local\Google\Chrome\User Data")
    browser = webdriver.Chrome(chrome_options=options) #载入webdriver驱动并加载参数
    return browser



def test_businessCard(browser,cache):


    #start login
    login.select_workstation(browser, '基础费用管理', cache)

    # 点击左边菜单
    on_click(browser,(By.XPATH,"//span[contains(text(), '患者信息查询')]"))
    # 点击二级菜单
    on_click(browser,(By.XPATH,"//span[contains(text(), '批量制卡')]"))


    # #清除垃圾数据
    # elements  = browser.find_elements_by_xpath("//button[contains(text(), '生成卡磁道')]")
    # print(len(elements))
    #
    # for i in range(len(elements)):
    #     if len(elements) >= 1:
    #         browser.find_element_by_xpath("//button[contains(text(), '生成卡磁道')]").click()
    #         browser.find_element_by_xpath("//button[contains(text(), '是')]").click()
    #         time.sleep(1)
    #
    #     else:
    #         break
    #
    # time.sleep(2)
    #
    # elements2 = browser.find_elements_by_xpath("//button[contains(text(), '确认')]")
    # print(len(elements2))
    #
    # for i in range(len(elements2)):
    #     if len(elements2) >= 1:
    #         browser.find_element_by_xpath("//button[contains(text(), '确认')]").click()
    #         browser.find_element_by_xpath("//button[contains(text(), '是')]").click()
    #         time.sleep(1)
    #
    #     else:
    #         break

    # 输入预计制卡数量，点击批量生成
    send_value(browser,(By.XPATH,"//input"),'1')
    on_click(browser,(By.XPATH,"//button[contains(text(), '生成批次')]"))

    #获取压缩文件时间，用于匹配压缩文件
    # now = time.strftime("%Y%m%d%H", time.localtime())
    # time.sleep(1)

    # 点击生成磁道
    time.sleep(1)
    browser.find_elements(By.XPATH,"//button[contains(text(), '生成卡磁道')]")[0].click()
    on_click(browser,(By.XPATH,"//button[contains(text(), '是')]"))

    # 点击下载
    time.sleep(2)
    browser.find_elements(By.XPATH, "//button[contains(text(), '下载')]")[0].click()
    on_click(browser, (By.XPATH, "//button[contains(text(), '是')]"))

    # 点击确认
    end_time = time.time()+500
    time.sleep(2)
    while True:
        time.sleep(1)
        text = get_text(browser,(By.XPATH,'//span'))
        if '提示' not in text:
            print('提示不存在')
            break
        if time.time()>end_time:
            log.info('页面加载超时')
            return

    on_click(browser,(By.XPATH,"//button[contains(text(), '确认')]"))
    on_click(browser, (By.XPATH, "//button[contains(text(), '是')]"))


    # 匹配下载文件
    f = browser.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div[2]/div/div[1]/div[1]/div[2]/div/div[1]/table/tbody/tr/td[1]/div")
    fname = f.text #使用获取页面的批次号来匹配压缩文件

    for i in os.listdir(path.download_dir):           #获取指定下载文件夹所有文件
        if (i.split(".")[0].find(fname)) > 0:         #使用字符串对比匹配到下载文件
            fpath = os.path.join(path.download_dir, i) #生成解压文件路径
            zip = zipfile.ZipFile(fpath)
            zipname = zip.namelist()                   #返回压缩包中所有文件的文件名
            zip.extractall()                           #解压所有文件
            zip.close()
            f = open(zipname[0])
            lines = f.readline()
            # print(lines)
            f.close()

            # 拼写制卡卡号
            card = '%E?;' + lines.rstrip('\n').split("|")[1] + '?+E?'
            cache.set('patient_card',card)
            log.info(card)
            Utility.writeFile(card)

            # 删除解压文件
            if os.path.exists(zipname[0]):
                os.remove(zipname[0])









if __name__ == "__main__":
    browser = common.browser()
    cache = Cache({})
    testcase = {'用户名': 'jfli', '密码': '123456'}
    cache.set('resultType', '1')
    cache.set('specialName', '急诊内科')
    cache.set('userId', '%E?;2001065723=99015011437?+E?')
    login.test_login(browser, testcase, cache)
    test_businessCard(browser, cache)
    browser.find_elements_tag_name('img')[21].click()
    browser.find_elements_by_xpath('//img')[21].click()

