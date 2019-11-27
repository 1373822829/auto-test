'''
检查医嘱元素
'''

div = [
    {
        'key':'/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div/div[1]/div[2]/div[1]/div/div/div',
        'notes':'检查等医嘱按钮区域',
        'index':'0'
    },
    ##根据窗口打开的数量body/div[8+n]
    {
        'key' : '/html/body/div[9]/div[2]/div[1]/div/div/div/div[1]',
        'notes':'检查项目区域',
        'index':'1'
    },
    {
        'key':'/html/body/div[9]/div[2]/div[1]/div/div/div/div[2]/div',
        'notes':'检查申请单表头区域',
        'index':'2'
    },
    {
        'key':'/html/body/div[13]/div',
        'notes':'执行科室列表',
        'index':'3'
    }
]

table = [
    {
        'key':'/html/body/div[9]/div[2]/div[2]/div/div/div/div/div[1]/table/tbody/tr/td[2]/table/tbody/tr/td[1]/table',
        'notes':'保存检查医嘱区域'
    }
]

fieldset = [
    {    #
        'key': '/html/body/div[9]/div[2]/div[1]/div/div/div/div[2]/fieldset[1]',
        'notes': '基本信息区域',
        'index': '0'
    },
    {
        'key': '/html/body/div[9]/div[2]/div[1]/div/div/div/div[2]/fieldset[2]',
        'notes': '部位或方法分组',
        'index': '1'
    },
    {
        'key': '/html/body/div[9]/div[2]/div[1]/div/div/div/div[2]/fieldset[3]',
        'notes': '部位或方法',
        'index': '2'
    },
    {
        'key': '/html/body/div[9]/div[2]/div[1]/div/div/div/div[2]/fieldset[4]',
        'notes': '附加项目',
        'index': '3'
    }

]

