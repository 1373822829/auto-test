#! /usr/bin/env python
#coding=utf-8

import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import UI.common_th_supcom_config.url_config as path
import UI.com_th_supcom_portal_service.usercenter.login as login
import UI.com_th_supcom_api.common.Common as common
import UI.com_th_supcom_portal_element.outp_bill_portal_element.get_hospital_card.GetHospitalCardElement as hospital_card
import UI.common_th_supcom_config.test_case_config.TestCaseCodeTable as TestCaseCodeTable


def switchWindow(browser,windowname):
    all_handles = browser.window_handles
    for handle in all_handles:
        browser.switch_to.window(handle)
        if windowname in browser.title:
            #browser.switch_to_window(handle)
            break

def test_get_hospital_card(browser, userList, cache):



    #参数化数据
    dict = TestCaseCodeTable.get_hospital_card

    #切换到工作站
    login.select_workstation(browser, '门诊挂号收费工作台', cache)
    # switchWindow(browser, '门诊挂号收费工作台')

    #点击菜单进入就诊卡办理页面
    e = browser.find_element_by_xpath("//div[contains(text(), '门诊挂号')]")
    e.click()
    time.sleep(2)
    browser.find_element_by_xpath("//a[contains(text(), '就诊卡办理')]").click()

    #就诊卡办理页面，填写信息

    #F2刷卡
    # e = browser.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div/div[2]/div[1]/div[1]/table/tbody/tr[1]/td/div/div[2]/div[1]/div/div[2]/div[1]/form/div/div/div[1]/div/div[1]/div/input")
    e = browser.find_element_by_xpath(hospital_card.input[0]["key"])
    # e.send_keys("%E?;2501218839=99015016158?+E?" + "\n")
    print(cache.get('patient_card'))
    e.send_keys(str(cache.get('patient_card')) + "\n")
    time.sleep(2)


    try:
        if browser.find_element_by_xpath("//font[contains(text(), '新卡')]"):


            #填写姓名
            # e1 = browser.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div/div[2]/div[1]/div[1]/table/tbody/tr[1]/td/div/div[2]/div[1]/div/div[2]/div[1]/form/fieldset/div/div[1]/div/div[1]/div[1]/div[1]/div/input")
            e1 = browser.find_element_by_xpath(hospital_card.input[1]["key"])
            # e1.send_keys(r"田伟511")
            e1.send_keys(userList[dict[ 'patient_name']])

            #选择性别
            # browser.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div/div[2]/div[1]/div[1]/table/tbody/tr[1]/td/div/div[2]/div[1]/div/div[2]/div[1]/form/fieldset/div/div[1]/div/div[3]/div[1]/div[1]/div/input").click()
            browser.find_element_by_xpath(hospital_card.input[2]["key"]).click()
            browser.find_element_by_xpath("//div[contains(text(), '男')]").click()

            #选择出生年月
            # e2 = browser.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div/div[2]/div[1]/div[1]/table/tbody/tr[1]/td/div/div[2]/div[1]/div/div[2]/div[1]/form/fieldset/div/div[1]/div/div[4]/div[1]/div/div[1]/div/div[1]/div/input")
            e2 = browser.find_element_by_xpath(hospital_card.input[3]["key"])
            # e2.send_keys("19840203")
            e2.send_keys(userList[dict[ 'birthday']])

            #输入电话1和确认电话1
            # e3 = browser.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div/div[2]/div[1]/div[1]/table/tbody/tr[1]/td/div/div[2]/div[1]/div/div[2]/div[1]/form/fieldset/div/div[1]/div/div[1]/div[2]/div[1]/div/input")
            e3 = browser.find_element_by_xpath(hospital_card.input[4]["key"])
            # e3.send_keys("15207145415")
            e3.send_keys(userList[dict[ 'phone']])

            # e4 = browser.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div/div[2]/div[1]/div[1]/table/tbody/tr[1]/td/div/div[2]/div[1]/div/div[2]/div[1]/form/fieldset/div/div[1]/div/div[2]/div[2]/div[1]/div/input")
            e4 = browser.find_element_by_xpath(hospital_card.input[5]["key"])
            # e4.send_keys("15207145415")
            e4.send_keys(userList[dict[ 'phone1']])
            print("电话ok")

            #费别
            # e5 = browser.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div/div[2]/div[1]/div[1]/table/tbody/tr[2]/td/div/div[2]/div[1]/div/div[2]/div[1]/form/fieldset[2]/div/div/div/div[1]/div/div[1]/div/input")
            e5 = browser.find_element_by_xpath(hospital_card.input[6]["key"])
            e5.click()


            # browser.find_element_by_xpath("//div[contains(text(), '自费')]").click()
            t = userList[dict[ 'charge_type']]
            browser.find_element_by_xpath("//div[contains(text(), t)]").click()
            print(userList[dict[ 'charge_type']])
            print("费别ok")

            #保存
            time.sleep(2)
            browser.find_element_by_xpath("//button[contains(text(), '保存')]").click()
            time.sleep(2)
            print("新卡办理ok")

    except:
        if browser.find_element_by_xpath("//font[contains(text(), '正常')]"):
            browser.find_element_by_xpath("//button[contains(text(), '修改')]").click()
        else:
            browser.find_element_by_xpath("//font[contains(text(), '新卡')]")
            browser.find_element_by_xpath("//button[contains(text(), '保存')]").click()

        print("修改点击ok")

    # browser.find_element_by_xpath("//span[contains(text(), '就诊卡办理')]//parent::span//parent::em//parent::a//parent::li//child::a").click()
    browser.refresh()
    time.sleep(2)
    print("退出ok")



def test_prepayment(browser, userList, cache):


    # 参数化数据
    d = TestCaseCodeTable.prepayment
    print(userList)
    # 切换到工作站
    login.select_workstation(browser, '门诊挂号收费工作台', cache)

    # 点击菜单进入就诊卡办理页面
    e = browser.find_element_by_xpath("//div[contains(text(), '门诊缴费管理')]")
    e.click()
    time.sleep(3)
    browser.find_element_by_xpath("//a[contains(text(), '预付费充值')]").click()

    #点击确定
    browser.find_element_by_xpath("//button[contains(text(), '确定')]").click()

    #刷卡
    e = browser.find_element_by_xpath("//label[contains(text(), '卡信息')]/parent::div/div/div/child::input")
    # e.send_keys("%E?;2501218839=99015016158?+E?" + "\n")
    e.send_keys(str(cache.get('patient_card')) + "\n")

    #汉字输入验证
    browser.find_element_by_xpath("//label[contains(text(), '汉字')]").click()
    time.sleep(2)
    e2 = browser.find_element_by_xpath("/html/body/div[8]/div[2]/div[1]/div/div/div/fieldset/div/div/div[5]/div/div[1]/div/div[1]/div/input")
    j = userList[d['patient_name']][1:2]
    print(j)
    time.sleep(2)
    e2.send_keys(j)  #截取名字第二个字

    #点击确定
    time.sleep(1)
    browser.find_element_by_xpath("//button[contains(text(), '确定')]").click()

    #选择支付方式
    time.sleep(1)
    e3 = browser.find_element_by_xpath("//label[contains(text(), '支付方式')]/parent::div/div/div/child::input")
    e3.send_keys(userList[d['payment_code']])

    #应收费用输入
    time.sleep(1)
    e4 = browser.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div/div[2]/div[1]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/div/input")
    f = userList[d['recharge_number']]
    print(f)
    e4.send_keys(f)
    #实收费用输入
    time.sleep(1)
    e5 = browser.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div/div[2]/div[1]/div[1]/div/div/div[2]/div/div[2]/div/div[1]/div/input")
    f2 = userList[d['recharge_number']]
    e5.send_keys(f2)


    #点击确认
    e5.send_keys("\n" + "\n" + "\n")
    browser.find_element_by_xpath("//button[contains(text(), '是')]").click()

    #工作站页面刷新
    browser.refresh()
    time.sleep(2)
    print("充值成功")

    #打印信息
    time.sleep(2)
    e7 = browser.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div/div[1]/div[2]/div[1]/div[3]/div/div[1]/div[1]/div[2]")

    y1 = ["患者ID：", "姓名：", "金额：", "支付方式：", "预交金流水号："]

    x1 = []
    for i in list(e7.text.split("\n")):
        x1.append(i)


    d = dict((x, y) for x, y in zip(y1, x1))
    print(d)

if __name__ == "__main__":
    browser = common.browser()
    testcase = {'用户名': 'jfli', '密码': '123456'}
    caches = {'resultType': '1', 'specialName': '急诊内科', 'userId': '%E?;2001065723=99015011437?+E?'}

    login.test_login(browser, testcase, caches)
    # userList = {'患者卡号': '%E?;2501218841=99015014023?+E?',  '患者姓名': '田伟515', '支付方式': '1', '充值数': 1000}
    userList = {'确认电话': 15207145415, '电话': 15207145415, '性别': '男', '生日': 19840203, '患者卡号': '%E?;2501218842=99015019990?+E?','费别': '自费', '患者姓名': '田伟515'}
    test_get_hospital_card(browser, userList, caches)
    # test_prepayment(browser, userList, caches)