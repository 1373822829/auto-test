'''
检验医嘱元素
'''

div = [
    {
        'key':'/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div/div[1]/div[2]/div[1]/div/div/div',
        'notes':'检验等医嘱按钮区域',
        'index':'0'
    },
    ##根据窗口打开的数量body/div[8+n]
    {
        'key' : '/html/body/div[10]/div[2]/div[1]/div/div/div/div[1]',
        'notes':'检验项目区域',
        'index':'1'
    },
    {
        'key':'/html/body/div[10]/div[2]/div[1]/div/div/div/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[1]/div[2]/div',
        'notes':'检验项目名称区域',
        'index':'2'
    },
    {
        'key':'/html/body/div[13]/div',
        'notes':'执行科室列表',
        'index':'3'
    },
    {
        'key':'/html/body/div[10]/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div[2]/div/div[1]/div[1]/div[2]',
        'notes':'检验项目明细列表',
        'index':'4'
    },
    {
        'key':'/html/body/div[10]/div[2]/div[1]/div/div/div/div[2]/div[3]',
        'notes':'临床诊断/检验目的',
        'index':'5'
    },
    {
        'key':'/html/body/div[13]/div',
        'notes':'标本',
        'index':'6'
    }
]

table = [
    {
        'key':'/html/body/div[10]/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div[1]/div/table',
        'notes':'项目名称表头',
        'index':'0'
    },
   {
        'key':'/html/body/div[10]/div[2]/div[2]/div/div/div/div/div[1]/table/tbody/tr/td[2]/table/tbody/tr/td[1]/table',
        'notes':'保存检验医嘱区域',
        'index':'1'
    }
]

