#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
挂号验证输出模板
'''
import UI.com_th_supcom_api.common.Utility as Utility

'''
患者费用
'''
def outp_fee_temp(object):
    if object != None:
        Utility.writeFile('患者id:' + str(object.PcaPrepayAccountIndex.card_no) + '   余额:' + str(object.PcaPrepayAccountMaster.balance))

'''
号源
'''
def outp_reg_source_temp(object):
    if object != None:
        Utility.writeFile('专科名称:'+str(object.OutpSpecialClinic.special_clinic_name)+'  号别:'+str(object.OutpRegMaster.outp_type_code)+
                          '  当前号:'+str(object.OutpRegMaster.current_no)+'  已挂数:'+str(object.OutpRegMaster.registration_limits-object.OutpRegMaster.current_limits)+
                          '  可挂号数:'+str(object.OutpRegMaster.current_limits)+'  限号数:'+str(object.OutpRegMaster.registration_limits))

'''
门办已挂数
'''
def outp_office_reg_source_temp(result):
    if result != None:
        Utility.writeFile('门办挂号数:'+ str(result[0]))