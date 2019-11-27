#! /usr/bin/env python
#coding=utf-8

#办理就诊卡元素定位（test_get_hospital_card）
input = [

    {
        'key' : '/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div/div[2]/div[1]/div[1]/table/tbody/tr[1]/td/div/div[2]/div[1]/div/div[2]/div[1]/form/div/div/div[1]/div/div[1]/div/input',
        'notes' : 'F2刷卡',
        'index' : 0
    },

    {
        'key' : "/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div/div[2]/div[1]/div[1]/table/tbody/tr[1]/td/div/div[2]/div[1]/div/div[2]/div[1]/form/fieldset/div/div[1]/div/div[1]/div[1]/div[1]/div/input",
        'notes' :'姓名',
        'index' : 1
    },

    {
        'key': "/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div/div[2]/div[1]/div[1]/table/tbody/tr[1]/td/div/div[2]/div[1]/div/div[2]/div[1]/form/fieldset/div/div[1]/div/div[3]/div[1]/div[1]/div/input",
        'notes': '性别',
        'index': 2
    },

    {
        'key': "/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div/div[2]/div[1]/div[1]/table/tbody/tr[1]/td/div/div[2]/div[1]/div/div[2]/div[1]/form/fieldset/div/div[1]/div/div[4]/div[1]/div/div[1]/div/div[1]/div/input",
        'notes': '选择出生年月',
        'index': 3
    },

    {
        'key' : '/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div/div[2]/div[1]/div[1]/table/tbody/tr[1]/td/div/div[2]/div[1]/div/div[2]/div[1]/form/fieldset/div/div[1]/div/div[1]/div[2]/div[1]/div/input',
        'notes' : '电话1',
        'index' : 4
    },

    {
        'key' : '/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div/div[2]/div[1]/div[1]/table/tbody/tr[1]/td/div/div[2]/div[1]/div/div[2]/div[1]/form/fieldset/div/div[1]/div/div[2]/div[2]/div[1]/div/input',
        'notes' : '确认电话1',
        'index' : 5
    },

    {
        'key' : '/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div/div[2]/div[1]/div[1]/table/tbody/tr[2]/td/div/div[2]/div[1]/div/div[2]/div[1]/form/fieldset[2]/div/div/div/div[1]/div/div[1]/div/input',
        'notes' : '费别',
        'index' : 6
    }


]

#就诊卡充值定位元素（test_prepayment）
input2 = [

    {
        'key' : '/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div/div[2]/div[1]/div[1]/table/tbody/tr[1]/td/div/div[2]/div[1]/div/div[2]/div[1]/form/fieldset/div/div[1]/div/div[2]/div[2]/div[1]/div/input',
        'notes' : '刷卡',
        'index' : 0
    },


]