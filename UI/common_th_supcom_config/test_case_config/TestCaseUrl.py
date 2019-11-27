#! /usr/bin/env python
#coding=utf-8
'''
测试用例绝对路径
'''


import UI.common_th_supcom_config.url_config as path
import UI.com_th_supcom_api.common.Utility as utility

getUrl={

    'uum_portal': path.dir+'\\file\\uum_portal.xlsx',

    'outp_bill_portal': path.dir+'\\file\\outp_bill_portal.xlsx',

    'outp_doctor_portal' : path.dir+'\\file\\outp_doctor_portal.xlsx',

}


if __name__ == "__main__":

    l = utility.GetTestcase(getUrl['outp_doctor_portal'],'emr_pds')
    print(len(l))
