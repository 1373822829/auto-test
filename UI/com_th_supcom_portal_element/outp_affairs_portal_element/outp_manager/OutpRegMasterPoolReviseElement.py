#! /usr/bin/env python
#coding=utf-8
'''
号源调整
'''
class Input:

    date = '/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div/div/div[2]/div[1]/div[2]/div[2]/div[1]/div/div[2]/div[1]' \
            '/div/table/tbody/tr/td[2]/table/tbody/tr/td[1]/table/tbody/tr/td[5]/div/input'  #日期

    belong_clinic_code = '/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div/div/div[2]/div[1]/div[2]/div[2]/div[1]/div/' \
                         'div[2]/div[1]/div/table/tbody/tr/td[2]/table/tbody/tr/td[1]/table/tbody/tr/td[8]/div/input'  #门诊科室

    doctor = '/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div/div/div[2]/div[1]/div[2]/div[2]/div[1]/div/div[2]/div[1]/' \
             'div/table/tbody/tr/td[2]/table/tbody/tr/td[1]/table/tbody/tr/td[11]/div/input'   #医生

    limit_no = '/html/body/div[8]/div[2]/div[1]/div/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div[5]/div[1]/div/input'  #限号数

    appoint_limit_no = '/html/body/div[8]/div[2]/div[1]/div/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div[5]/div[1]/div/input'  #预约限号数

class Div:

    special_list = '/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div/div/div[2]/div[1]/div[2]/div[2]/div[1]/div/div[2]/div[2]/div/div/div[1]/div[1]/div[2]' #号源列表

    special_detail = '/html/body/div[8]/div[1]/div/div/div'  #号源详情弹出窗口

class Img:
    calendar_img = '/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div/div/div[2]/div[1]/div[2]/div[2]/div[1]/div/div[2]/div[1]/div/' \
                   'table/tbody/tr/td[2]/table/tbody/tr/td[1]/table/tbody/tr/td[5]/div/img'   #日历