#! /usr/bin/env python
#coding=utf-8
'''
获取元素地址
'''

label = [
      {
          'key':'',
          'notes':"",
          'index':'0'
      },
      {
          'key': '',
         'notes': "",
          'index': '1'
      },
      {
         'key': '',
        'notes': "：",
        'index': '2'
       },
      {
          'key': '',
          'notes': "",
          'index': '3'
      },
      {
          'key': '',
          'notes': "",
          'index': '4'
      },
      {
          'key': '',
          'notes': "",
          'index': '5'
      },
      {
          'key': '',
          'notes': "",
          'index': '6'
      },
      {
          'key': '',
          'notes': "",
          'index': '7'
      },
      {
          'key': '',
          'notes': "",
          'index': '8'
      },
      {
          'key': '',
          'notes': "",
          'index': '9'
      },
      {
          'key': '',
          'notes': "",
          'index': '10'
      },
]

button = [

    {
        'key': '/html/body/div[1]/div/div[1]/div/div/div[1]/div/table/tbody/tr/td[2]/table/tbody/tr/td[1]/table/tbody/tr/td[4]/table/tbody/tr[2]/td[2]/em/button',
        'notes':'工作台按钮',
        'index': '0'
    },
    {
        'key':'/html/body/div[8]/div[2]/div[2]/div/div/div/div/div[1]/table/tbody/tr/td[2]/table/tbody/tr/td[1]/table/tbody/tr/td[2]/table/tbody/tr[2]/td[2]/em/button',
        'notes':'确定',
        'index': '1'
    },
    {
        'key':'/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div/div[2]/div[1]/div[2]/div[1]/div/table/tbody/tr/td[1]/table/tbody/tr/td[14]/table/tbody/tr[2]/td[2]/em/button',
        'notes':'诊断',
        'index':'2'
    },
    {    #/html/body/div[11]/div[2]/div[2]/div/div/div/div/div[1]/table/tbody/tr/td[2]/table/tbody/tr/td[1]/table/tbody/tr/td[1]/table/tbody/tr[2]/td[2]/em/butto
        'key':'/html/body/div[8]/div[2]/div[2]/div/div/div/div/div[1]/table/tbody/tr/td[2]/table/tbody/tr/td[1]/table/tbody/tr/td[1]/table/tbody/tr[2]/td[2]/em/button',
        'notes':'保存',
        'index':'3'
    },
    {           #'/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div/div[2]/div[1]/div[2]/div[1]/div/table/tbody/tr/td[1]/table/tbody/tr/td[1]/table/tbody/tr[2]/td[2]/em/button'
        'key':'/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div/div[2]/div[1]/div[2]/div[1]/div/table/tbody/tr/td[1]/table/tbody/tr/td[1]/table/tbody/tr[2]/td[2]/em/button',
        'notes':'提交',
        'index':'4'
    }
  ]

input = [
    {
        'key': '/html/body/div[8]/div[2]/div[1]/div/div/div/div/div[1]/input',
        'notes': "工作台",
        'index': '0'
    },
    {
        'key':'/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div/div/div[2]/div[1]/div[1]/div[2]/div[1]/div/table/tbody/tr/td[2]/table/tbody/tr/td[1]/table/tbody/tr/td[2]/div/input',
        'notes':'刷卡',
        'index': '1'
    },
    {
        'key': '/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div/div/div[2]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[2]/div[1]/div/div[3]/div/div[1]/div/input',
        'notes': "医嘱名称",
        'index': '2'
    },

    {
        'key': '/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[2]/div[1]/div/div[6]/div/div[1]/div/input',
        'notes': "带药",
        'index': '3'
    },
    {
        'key':'/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div/div/div/div[2]/div[2]/div[1]/div[8]/div[1]/div/div[1]/div/input',
        'notes':"每次用量",
        'index':'4'
    },
    {
        'key': '/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div/div/div/div[2]/div[2]/div[1]/div[8]/div[6]/div/div[1]/div/input',
        'notes': '疗程',
        'index': '5'
    },
    {
        'key': '/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div/div/div/div[2]/div[2]/div[1]/div[8]/div[8]/div/div[1]/div/div[1]/div/input',
        'notes': '总量',
        'index': '6'
    },
    {   #/html/body/div[11]/div[2]/div[1]/div/div/div/div[1]/div[2]/div[1]/form/div[2]/div[1]/div/input
        'key':'/html/body/div[8]/div[2]/div[1]/div/div/div/div[1]/div[2]/div[1]/form/div[2]/div[1]/div/input',
        'notes':'诊断选择',
        'index':'7'
    },
    {
        'key':'/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[2]/div[1]/div/div[3]/div/div[1]/div/input',
        'notes':'皮试医嘱界面',
        'index':'8'
    },
    {
        'key':'/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[2]/div[1]/div/div[3]/div/div[1]/div/input',
        'notes':'医嘱名称-初次',
        'index':'9'
    },
    {
        'key':'/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div/div/div/div[2]/div[2]/div[1]/div/div[1]/div/div[1]/div/input',
        'notes':'每次用量-初次',
        'index':'10'
    },
    {
        'key':'/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div/div/div/div[2]/div[2]/div[1]/div[5]/div[6]/div/div[1]/div/input',
        'notes':'疗程-初次',
        'index':'11'
    },
    {
        'key':'/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div/div[4]/div[2]/div/div/div/div[2]/div/div[1]/div/input',
        'notes':'刷卡',
        'index':'12'
    }
]


td=[
    {
        'key':'/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div/div/div[2]/div[1]/div[1]/div[2]/div[2]/div/div/div[1]/div[1]/div[2]/div/div[1]/table/tbody/tr/td[4]/div',
        'notes':'患者1',
        'index': '0'
    },
    {
        'key': '/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div/div/div[2]/div[1]/div[1]/div[2]/div[2]/div/div/div[1]/div[1]/div[2]/div/div[2]/table/tbody/tr/td[4]/div',
        'notes': '患者2',
        'index': '1'
    },
    {
        'key': '/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div/div/div[2]/div[1]/div[1]/div[2]/div[2]/div/div/div[1]/div[1]/div[2]/div/div[3]/table/tbody/tr/td[4]/div',
        'notes': '患者3',
        'index': '2'
    }
]

img=[
    {
        'key': '/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[2]/div[1]/div/div[2]/div/div[1]/div/img',
        'notes':'类型',
        'index':'0'
    },
    {

        'key':'/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div/div/div/div[2]/div[2]/div[1]/div[8]/div[3]/div/div[1]/div/img',
        'notes':'途径',
        'index':'1'
    },
    {                                                                                                                                                             #8
        'key':'/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div/div/div/div[2]/div[2]/div[1]/div[3]/div[4]/div/div[1]/div/img',
        'notes':'频次',
        'index':'2'
    },
    {
        'key':'/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div/div/div[2]/div[2]/div[2]/div[1]/div/div/div/div[2]/div[2]/div[1]/div[31]/div[9]/div/div[1]/div/img',
        'notes':'用药目的',
        'index':'3'
    },
                #/html/body/div[11]/div[2]/div[1]/div/div/div/div[1]/div[2]/div[1]/form
    {            #'/html/body/div[11]/div[2]/div[1]/div/div/div/div[1]/div[2]/div[1]/form/div[1]/div/div[1]/div/div[1]/div/img'
        'key':'/html/body/div[8]/div[2]/div[1]/div/div/div/div[1]/div[2]/div[1]/form/div[1]/div/div[1]/div/div[1]/div/img',
        'notes':'诊断类别',
        'index':'4'
    },
    {
        'key':'/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[2]/div[1]/div/div[2]/div/div[1]/div/img',
        'notes':'类型-皮试',
        'index':'5'
    },
    {
        'key':'/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div/div/div/div[2]/div[2]/div[1]/div/div[3]/div/div[1]/div/img',
        'notes':'途径-初次',
        'index':'6'
    },
    {
        'key':'/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div/div/div/div[2]/div[2]/div[1]/div[5]/div[4]/div/div[1]/div/img',
        'notes':'频次-初次',
        'index':'7'
    }

]

select=[
    {  # '/html/body/div[10]/div/div[1]'
       'key':'/html/body/div[11]/div/div[1]',
        'notes':'初步诊断',
        'index':'0'
    },
    {
        'key': '/html/body/div[11]/div/div[2]',
        'notes': '术后诊断',
        'index': '1'
    },
    {
        'key': '/html/body/div[11]/div/div[3]',
        'notes': '确诊诊断',
        'index': '2'
    },
    {
        'key':'/html/body/div[10]/div/',
        'notes':'医嘱类型',
        'index':'3'
    },
    {
        'key':'/html/body/div[10]/div/',
        'notes':'途径',
        'index':'4'
    },
    {
        'key':'/html/body/div[10]/div/',
        'notes':'频次',
        'index':'5'
    },
    {
        'key': '/html/body/div[10]/div/',
        'notes': '医嘱类型-初次',
        'index': '6'
    },

]

div=[
    {   #//*[@id="x-auto-379"]/div[2]/div[1]/div/div
        'key':'/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div/div',
        'notes':'医嘱区域',
        'index':'0'
    },
    {
        'key':'/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div/div/div[2]/div[1]/div[1]/div[2]/div[2]/div/div/div[1]/div[1]/div[2]',
        'notes':'患者列表',
        'index':'1'
    },
    {
        'key':'/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div/div/div',
        'notes':'开立医嘱',
        'index':'2'
    },
    {
        'key': '/html/body/div[1]/div/div[2]/div[2]/div/div[1]',
        'notes': '患者管理菜单',
        'index': '3'
    },
    {
        'key':'/html/body/div[1]/div/div[2]/div[2]/div/div[2]',
        'notes':'医嘱管理菜单',
        'index':'4'
    },
    {
        'key':'/html/body/div[8]/div/div/div[2]/div[2]/div/div[1]',
        'notes':'患者就诊记录',
        'index':'5'
    }
]
a = [
    {
        'key' : '/html/body/div[8]/div/div[5]/a',
        'notes':'门诊患者列表菜单',
        'index':'0'
    },
    {
        'key':'/html/body/div[10]/div/div[3]/a',
        'notes':'门诊医嘱开立菜单',
        'index':'1'
    }
]
