#! /usr/bin/env python
#coding=utf-8
'''
获取元素地址
'''



label = [
      {
          'key':'/html/body/div[1]/div/div[1]/div/div/div[1]/div/table/tbody/tr/td[2]/table/tbody/tr/td[1]/table/tbody/tr/td[2]/div',
          'notes':"已登陆账号",
          'index':'0'
      },
      {
          'key': '/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div[1]/div[3]/div[2]/div[1]/div/div[2]/div[  1]/div/table/tbody/tr/td[1]/table/tbody/tr/td[2]/div',
         'notes': "上笔挂号信息：",
          'index': '1'
      },
      {
         'key': '/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div[1]/div[3]/div[2]/div[1]/div/div[2]/div[1]/div/table/tbody/tr/td[1]/table/tbody/tr/td[4]/div',
        'notes': "应收：",
        'index': '2'
       },
      {
          'key': '',
          'notes': "实收",
          'index': '3'
      },
      {
          'key': '',
          'notes': "找零",
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
        'key': '',
        'notes': '',
        'index': '0'
    },
    {
        'key': '',
        'notes': '',
        'index': '1'
    },
    {            #/html/body/div[8]/div[2]/div[2]/div/div/div/div/div[1]/table/tbody/tr/td[1]/table/tbody/tr/td[2]/table/tbody/tr[2]/td[2]/em/button
        'key': '/html/body/div[9]/div[2]/div[2]/div/div/div/div/div[1]/table/tbody/tr/td[1]/table/tbody/tr/td[2]/table/tbody/tr[2]/td[2]/em/button',
        'notes':'否',
        'index': '2'
    },
    {
        'key': '/div/div[1]/div/div[1]/div/div/div[1]/div/table/tbody/tr/td[2]/table/tbody/tr/td[1]/table/tbody/tr/td[4]/table/tbody/tr[2]/td[2]/em/button',
        'notes':"系统配置",
        'index': '3'
    },
    {
        'key': '/html/body/div[1]/div/div[1]/div/div/div[1]/div/table/tbody/tr/td[2]/table/tbody/tr/td[1]/table/tbody/tr/td[3]/table/tbody/tr[2]/td[2]/em/button',
        'notes':"当前登陆科室",
        'index': '4'
    },
    {
        'key': '/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div/div[2]/div[1]/div/div[2]/div[1]/div/div[2]/div[1]/div/div/div/form/div[15]/div[1]/div/div[1]/table/tbody/tr[2]/td[2]/em/button',
        'notes': "取号",
        'index': '5'
    },
    {
        'key': '/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div/div[2]/div[1]/div/div[2]/div[1]/div/div[2]/div[1]/div/div/div/form/div[15]/div[1]/div/div[2]/table/tbody/tr[2]/td[2]/em/button',
        'notes': "预约挂号",
        'index': '6'
    },
    {
        'key': '/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div/div[2]/div[1]/div/div[2]/div[1]/div/div[2]/div[1]/div/div/div/form/div[15]/div[2]/div/div[1]/table/tbody/tr[2]/td[2]/em/button',
        'notes': "号表调整",
        'index': '7'
    },
    {
        'key': '/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div/div[2]/div[1]/div/div[2]/div[1]/div/div[2]/div[1]/div/div/div/form/div[15]/div[2]/div/div[2]/table/tbody/tr[2]/td[2]/em/button',
        'notes': "退号",
        'index': '8'
    },
    {
        'key': '/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div/div[2]/div[1]/div/div[2]/div[1]/div/div[2]/div[1]/div/div/div/form/div[15]/div[3]/div/div[1]/table/tbody/tr[2]/td[2]/em/button',
        'notes': "重置",
        'index': '9'
    },
    {
         'key': '/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div/div[2]/div[1]/div[1]/div[2]/div[1]/div/div[2]/div[1]/form/div/div/div[3]/table/tbody/tr[2]/td[2]/em/button',
         'notes': "刷新",
        'index': '10'
    },
    {
        'key':'/html/body/div[9]/div[2]/div[2]/div/div/div/div/div[1]/table/tbody/tr/td[1]/table/tbody/tr/td[1]/table/tbody/tr[2]/td[2]/em/button',
        'notes':'是',
        'index': '11'
    }
  ]

input = [
    {
        'key': '/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div/div[2]/div[1]/div/div[2]/div[1]/div/div[2]/div[1]/div/div/div/form/div[2]/div[1]/div/input',
        'notes': "姓名",
        'index': '0'
    },
    {
        'key': '/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div/div[2]/div[1]/div/div[2]/div[1]/div/div[2]/div[1]/div/div/div/form/div[3]/div[1]/div/input',
        'notes': "性别",
        'index': '1'
    },
    {
        'key':'/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div/div[2]/div[1]/div/div[2]/div[1]/div/div[2]/div[1]/div/div/div/form/div[4]/div[1]/div/input',
        'notes':"出生日期",
        'index': '2'
    },
    {
        'key':'/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div/div[2]/div[1]/div/div[2]/div[1]/div/div[2]/div[1]/div/div/div/form/div[5]/div[1]/div/input',
        'notes':"(F9)卡号",
        'index': '3'
    },
    {
        'key': '/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div/div[2]/div[1]/div/div[2]/div[1]/div/div[2]/div[1]/div/div/div/form/div[6]/div[1]/div/input',
        'notes': "F7专科",
        'index': '4'
    },
    {
        'key': '/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div/div[2]/div[1]/div/div[2]/div[1]/div/div[2]/div[1]/div/div/div/form/div[7]/div[1]/div/input',
        'notes': "专科名称",
        'index': '5'
    },
    {
        'key': '/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div/div[2]/div[1]/div/div[2]/div[1]/div/div[2]/div[1]/div/div/div/form/div[8]/div[1]/div/input',
        'notes': "费用类型",
        'index': '6'
    },
    {
        'key': '/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div/div[2]/div[1]/div/div[2]/div[1]/div/div[2]/div[1]/div/div/div/form/div[9]/div[1]/div/input',
        'notes': "就诊类型:",
        'index': '7'
    },
    {
        'key': '/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div/div[2]/div[1]/div/div[2]/div[1]/div/div[2]/div[1]/div/div/div/form/div[10]/div[1]/div/input',
        'notes': "病种类型",
        'index': '8'
    },
    {
        'key': '/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div/div[2]/div[1]/div/div[2]/div[1]/div/div[2]/div[1]/div/div/div/form/div[11]/div[1]/div/input',
        'notes': "费用",
        'index': '9'
    },
    {
        'key': '/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div/div[2]/div[1]/div/div[2]/div[1]/div/div[2]/div[1]/div/div/div/form/div[12]/div[1]/div/input',
        'notes': "实收",
        'index': '10'
    },
    {
        'key': '/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div/div[2]/div[1]/div/div[2]/div[1]/div/div[2]/div[1]/div/div/div/form/div[13]/div[1]/div/input',
        'notes': "找零",
        'index': '11'
    },
    {
        'key': '/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div/div[2]/div[1]/div/div[2]/div[1]/div/div[2]/div[1]/div/div/div/form/div[14]/div[1]/div/input',
        'notes': "余额",
        'index': '12'
    },
    {
        'key': '',
        'notes': "",
        'index': '13'
    },
    {
        'key':'',
        'notes':'',
        'index': '14'
    },
   {
        'key': '',
        'notes': "",
        'index': '15'
    },
    {
        'key': '',
        'notes': "",
        'index': '16'
    },
    {
        'key':'',
        'notes':"",
        'index':'17'
    },
    {
        'key': '',
        'notes': '',
        'index': '18'
    },
    {
        'key': '',
        'notes': '',
        'index': '19'
    },
    {
        'key':'',
        'notes':'',
        'index':'20'
    },
    {
        'key': '',
        'notes': '',
        'index': '21'
    },
    {
        'key':'',
        'notes':'',
        'index':'22'
    }
]



radiobutton = [
    {
        'key': '/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div/div[2]/div[1]/div[1]/div[2]/div[1]/div/div[2]/div[1]/form/div/div/div[2]/div/div[1]/div/table/tbody/tr/td[1]/div/input',
        'notes': "F3全部",
        'index': '0'
    },
    {
        'key': '/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div/div[2]/div[1]/div[1]/div[2]/div[1]/div/div[2]/div[1]/form/div/div/div[2]/div/div[1]/div/table/tbody/tr/td[3]/div/input',
        'notes': "专家",
        'index': '1'
    },
    {
        'key': '/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div/div[2]/div[1]/div[1]/div[2]/div[1]/div/div[2]/div[1]/form/div/div/div[2]/div/div[1]/div/table/tbody/tr/td[4]/div/input',
        'notes': "业余",
        'index': '2'
    },
    {
        'key': '/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div/div[2]/div[1]/div[1]/div[2]/div[1]/div/div[2]/div[1]/form/div/div/div[2]/div/div[1]/div/table/tbody/tr/td[5]/div/input',
        'notes': "保健",
        'index': '3'
    },
    {
        'key': '/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div/div[2]/div[1]/div[1]/div[2]/div[1]/div/div[2]/div[1]/form/div/div/div[2]/div/div[1]/div/table/tbody/tr/td[2]/div/input',
        'notes': "普通和急诊",
        'index': '4'
    },
    {
        'key': '/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div/div[2]/div[1]/div[1]/div[2]/div[1]/div/div[2]/div[1]/form/div/div/div[1]/div/div[1]/div/table/tbody/tr/td[1]/div/input',
        'notes': "F2全部",
        'index': '5'
    },
    {
        'key': '/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div/div[2]/div[1]/div[1]/div[2]/div[1]/div/div[2]/div[1]/form/div/div/div[1]/div/div[1]/div/table/tbody/tr/td[2]/div/input',
        'notes': "全天",
        'index': '6'
    },
    {
        'key': '/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div/div[2]/div[1]/div[1]/div[2]/div[1]/div/div[2]/div[1]/form/div/div/div[1]/div/div[1]/div/table/tbody/tr/td[3]/div/input',
        'notes': "上午",
        'index': '7'
    },
    {
        'key': '/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div/div[2]/div[1]/div[1]/div[2]/div[1]/div/div[2]/div[1]/form/div/div/div[1]/div/div[1]/div/table/tbody/tr/td[4]/div/input',
        'notes': "下午",
        'index': '8'
    },
    {
        'key': '/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div/div[2]/div[1]/div[1]/div[2]/div[1]/div/div[2]/div[1]/form/div/div/div[1]/div/div[1]/div/table/tbody/tr/td[5]/div/input',
        'notes': "晚上",
        'index': '9'
    },
]



span = [
    {
        'key': '/html/body/div[1]/div/div[2]/div[1]/div[2]/div[2]/div[2]/ul/li[1]/a[2]/em/span/span',
        'notes': "门诊挂号(就诊卡)",
        'index': '0'
    },
    {
        'key': '/html/body/div[1]/div/div[2]/div[2]/div/div[2]',
        'notes': '门诊缴费管理',
        'index': '1'
    },
    {
        'key': '/html/body/div[1]/div/div[2]/div[2]/div/div[3]',
        'notes': '欠费管理',
        'index': '2'
    },
    {
        'key': '/html/body/div[1]/div/div[2]/div[2]/div/div[4]',
        'notes': '门诊退费管理',
        'index': '3'
    },
    {
        'key': '/html/body/div[1]/div/div[2]/div[2]/div/div[5]',
        'notes': '门诊交账管理',
        'index': '4'
    },
    {
        'key': '/html/body/div[1]/div/div[2]/div[2]/div/div[6]',
        'notes': '发票打印管理',
        'index': '5'
    },
    {
        'key': '/html/body/div[1]/div/div[2]/div[2]/div/div[7]',
        'notes': '发票打印管理',
        'index': '6'
    },
    {
        'key': '/html/body/div[8]/div[2]/div[1]/div/div/div/div[2]/span',
        'notes': '挂号弹出框提示文本',
        'index': '7'
    }
]

div=[
    {
        'key':'/html/body/div[1]/div/div[2]/div[2]/div/div[1]',
        'notes':'门诊挂号菜单',
        'index':'0'
    },
    {
        'key': '',
        'notes': '',
        'index': '1'
    },
    {
        'key': '/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div/div[2]/div[1]/div[2]/div[2]/div[1]/div/div[2]/div[1]/div/div[1]/div[1]/div[2]/div',
        'notes': '挂号专科',
        'index': '2'
    },
    {   #['+i+']/table/tbody/tr/td['+j+']/div
        'key': '/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div/div[2]/div[1]/div[2]/div[2]/div[1]/div/div[2]/div[1]/div/div[1]/div[1]/div[2]/div/div',
        'notes': '挂号专科',
        'index': '3'
    },
    {
        'key': '/html/body/div[8]/div[1]/div/div/div',
        'notes': '门诊退号窗口表头区域',
        'index': '4'
    },
    {
        'key': '',
        'notes': '',
        'index': '5'
    },
]

form=[
    {
        'key':'/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div/div[2]/div[1]/div/div[2]/div[1]/div/div[2]/div[1]/div/div/div/form',
        'notes':'挂号表单',
        'index':'0'
    },
    {
        'key':'/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div/div[2]/div[1]/div[1]/div[2]/div[1]/div/div[2]/div[1]/form',
        'notes':'号源类型(单选框)',
        'index':'1'
    }
]

table=[
    {
        'key':'/html/body/div[8]/div[2]/div[2]/div/div/div/div/div[1]/table/tbody/tr/td[1]/table',
        'notes':'是否自费',
        'index':'0'
    }
]

a = [
    {
        'key' :'/html/body/div[8]/div/div[13]/a',
        'notes':'门诊挂号(就诊卡)',
        'index':'0'
    }
]