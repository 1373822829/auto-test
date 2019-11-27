#! /usr/bin/env python
#coding=utf-8
'''
就诊卡挂失
'''

class InputLocator:

    name = '/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div/div[2]/div[1]/div/table/tbody/tr/td[2]/table/tbody/tr/td[1]/table/tbody/tr/td[2]/div/input' #患者姓名

    id_type = '/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div/div[2]/div[1]/div/table/tbody/tr/td[2]/table/tbody/tr/td[1]/table/tbody/tr/td[4]/div/input'  # 证件类型

    id_card = '/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div/div[2]/div[1]/div/table/tbody/tr/td[2]/table/tbody/tr/td[1]/table/tbody/tr/td[6]/div/input'#证件卡号

    phone_num = '/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div/div[2]/div[1]/div/table/tbody/tr/td[2]/table/tbody/tr/td[1]/table/tbody/tr/td[8]/div/input' #电话号

class DivLocator:

    checkbox = '/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div/div/table/tbody/tr/td[1]/div/div'#勾选患者信息框

    pai_list = '/html/body/div[9]/div[1]/div/div/div'  #患者卡列表区域

    checkbox_pai = '/html/body/div[9]/div[2]/div[1]/div/div/div/div/div[2]/div[1]/form/div/div[1]/div[1]/div[2]/div/div/table/tbody/tr/td[2]/div/div'#患者卡列表窗口下勾选患者信息框

class ButtonLocator:

    cancel_loss = '/html/body/div[9]/div[2]/div[2]/div/div/div/div/div[1]/table/tbody/tr/td[2]/table/tbody/tr/td[1]/table/tbody/tr/td[3]/table/tbody/tr[2]/td[2]/em/button'#取消挂失窗口中的取消挂失按钮