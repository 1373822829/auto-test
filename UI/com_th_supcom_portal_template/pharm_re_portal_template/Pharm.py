# coding=utf-8
'''
药品验证
'''
import math

from UI.common_th_supcom_config.test_case_config.TestCaseCodeTable import cpoe_out_order

from UI.com_th_supcom_api.common import Utility

'''
供药验证
#pham_num : 药品库存
#pham_basic_info : 药品基本信息对象
#pds_emr : 药疗医嘱信息
'''
def appy_pham_temp(pham_num,pham_basic_info,pds_emr):
    if (pham_num and pham_basic_info) != None:
        total = math.ceil(pds_emr[cpoe_out_order['dosage']]/pham_basic_info.dose_per_unit*pham_basic_info.package_factor) #总量
        counts = total*pham_basic_info.retail_price   #总金额
        Utility.writeFile('药品名称：%s  药品规格：%s  总量：%s  总金额：%s 库存：%s'%(pham_basic_info.pham_name,pham_basic_info.pham_spec,total,counts,str(pham_num[0])+'.'+str(
            pham_num[1])))
