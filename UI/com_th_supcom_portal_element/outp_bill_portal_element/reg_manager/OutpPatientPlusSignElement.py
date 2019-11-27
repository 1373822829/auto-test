#! /usr/bin/env python
#coding=utf-8
'''
加号脚本
'''
class PlusSignInput:
    swipe_card = '/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div/div[2]/div[1]/div/div[2]/div[1]/' \
                 'form/div[2]/div[2]/div[1]/div/div/div/div[2]/div[1]/div/input'  #刷卡
    doctor_name = '/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div/div[2]/div[1]/div/div[2]/div[1]/form/div[1]/' \
                   'div[2]/div[1]/div/table/tbody/tr/td[2]/table/tbody/tr/td[1]/table/tbody/tr/td[3]/div/input'  #根据医生检索号源

class PlusSignDiv:
    special_list = '/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div/div[2]/div[1]/div/div[2]/' \
                   'div[1]/form/div[1]/div[2]/div[2]/div/div[1]/div[1]/div[2]/div'  #号源列表