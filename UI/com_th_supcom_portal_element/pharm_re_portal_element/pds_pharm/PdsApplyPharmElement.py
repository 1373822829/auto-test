#! /usr/bin/env python
#coding=utf-8
'''
获取药房工作站元素地址
'''

button = [
    {
        'key':'/html/body/div[1]/div/div[1]/div/div/div[1]/div/table/tbody/tr/td[2]/table/tbody/tr/td[1]/table/tbody/tr/td[4]/table/tbody/tr[2]/td[2]/em/button',
        'notes':'药房工作站按钮',
        'index':'0'
    },
    {
        'key':'/html/body/div[7]/div[2]/div[2]/div/div/div/div/div[1]/table/tbody/tr/td[2]/table/tbody/tr/td[1]/table/tbody/tr/td[2]/table/tbody/tr[2]/td[2]/em/button',
        'notes':'药房工作站确定',
        'index':'1'
    },
    {
        'key':'/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/div/div[1]/table/tbody/tr/td[1]/table/tbody/tr/td[2]/table/tbody/tr[2]/td[2]/em/button',
        'notes':'处方确定按钮',
        'index':'2'
    },
    {
        'key':'/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div[3]/div/div[2]/div[1]/div[2]/fieldset[1]/div/div/div/div[7]/table/tbody/tr[2]/td[2]/em/button',
        'notes':'发药(0)',
        'index':'3'
    },
    {
        'key':'/html/body/div[7]/div[2]/div[2]/div/div/div/div/div[1]/table/tbody/tr/td[1]/table/tbody/tr/td[1]/table/tbody/tr[2]/td[2]/em/button',
        'notes':'发药-是',
        'index':'4'
    },
    {
        'key':'',
        'notes':'',
        'index':'5'
    }


  ]

input = [

    {
        'key': '/html/body/div[7]/div[2]/div[1]/div/div/div/div/div[1]/input',
        'notes': '药房工作站',
        'index': '0'
    },
    {
        'key':'/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div/div/div/fieldset[1]/div/div/div/div[1]/div/div[1]/div/input',
        'notes':'供药刷卡',
        'index':'1'
    },
    {
        'key':'/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div[3]/div/div[2]/div[1]/div[2]/fieldset[1]/div/div/div/div[2]/div/div[1]/div/input',
        'notes':'发药刷卡',
        'index':'2'
    },
    {
        'key':'',
        'notes':'',
        'index':''
    },
    {
        'key':'',
        'notes':'',
        'index':''
    },
    {
        'key':'',
        'notes':'',
        'index':''
    },
    {
        'key':'',
        'notes':'',
        'index':''
    },
]


a=[
    {
        'key': '/html/body/div[7]/div/div[1]/a',
        'notes': '处方退药查询及补打',
        'index': '0'
    },
    {
        'key':'/html/body/div[7]/div/div[2]/a',
        'notes':'附加费用收退',
        'index':'1'
    },
    {
        'key': '/html/body/div[7]/div/div[3]/a',
        'notes': '处方供药(科室)',
        'index': '2'
    },
    {
        'key': '/html/body/div[7]/div/div[4]/a',
        'notes': '处方供药',
        'index': '3'
    },
    {
        'key': '/html/body/div[7]/div/div[5]/a',
        'notes': '处方审核',
        'index': '4'
    },
    {
        'key': '/html/body/div[7]/div/div[6]/a',
        'notes': '处方状态查询',
        'index': '5'
    },
    {
        'key': '/html/body/div[8]/div/div[7]/a',
        'notes': '核对发药',
        'index': '6'
    },
    {
        'key': '/html/body/div[7]/div/div[8]/a',
        'notes': '处方退药',
        'index': '7'
    },

]
div=[
    {
        'key':'/html/body/div[1]/div/div[2]/div[2]/div/div[5]',
        'notes':'收方管理',
        'index':'0'
    },
    {
        'key': '/html/html/div[2]/div[2]/div[1]/div/div[2]/div[1]/div/div[1]/div[1]/div[2]/div/div/table/tbody/tr/td[2]/div',
        'notes': '处方信息',
        'index': '1'
    },
    {
        'key': '/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div[3]/div/div[2]/div[1]/div[4]/div[2]/div[1]/div/div[2]/div[1]/div/div[1]/div[1]/div[2]/div/div[1]/table/tbody/tr/td[2]/div',
        'notes': '核对发药处方',
        'index': '2'
    },
    {
        'key': '/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[3]/div[2]/div[1]/div/div[2]/div[1]/div/div[1]/div[1]/div[2]/div',
        'notes': '处方单列表',
        'index': '3'
    },
    {
        'key': '/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div/div[1]/div[1]/div[2]',
        'notes': '处方单详情列表区域',
        'index': '4'
    },
    {
        'key' : '/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div[3]/div/div[2]/div[1]/div[2]/div[2]/div[1]/div/div[2]/div[1]/div/div[2]/div[1]/div/div[1]/div[1]/div[2]',
        'notes': '处方明细',
        'index':'5'
    }
]
fieldset=[
#/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div/div/div/fieldset[1]/div/div/div/div[1]/div/div[1]/div/input
    {
        'key':'/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div[3]/div/div[2]/div[1]/div[1]/fieldset[1]',
        'notes':'供药查询区域',
        'index':'0'
    },
   {
        'key':'/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div[3]/div/div[2]/div[1]/div[1]/fieldset[2]',
        'notes':'患者基本信息区域',
        'index':'1'
    },
    {
        'key' : '/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div/div/div/fieldset[1]',
        'notes':'收方区域',
        'index' :'2'
    }
]
