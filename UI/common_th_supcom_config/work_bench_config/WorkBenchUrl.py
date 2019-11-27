#! /usr/bin/env python
#coding=utf-8
'''
工作站参照
'''
import os
workstation_name_collation1 ={

    '门诊挂号收费工作台' : '门诊收费工作站',
    '门诊医生站' : '门诊医生站',
    '住院费用管理工作站' : '住院收费工作站',
    '入出院登记工作台' : '住院登记',
    '住院护士站' : '住院护士站',
    '门诊辅诊站' : '门诊辅诊工作站',
    '住院医生站' : '住院医生站',
    '医技工作站': '医技工作站',
    '检查预约' : '检查预约',
    '药房工作站' : '药房工作站',
    '基础费用管理' : '基础费用管理系统',
    '门诊办公室工作站':'门诊办公室',
    '入出院登记工作台':'入院登记'


}


#脚本和模块对应
workstation_include_moudle = {
    'portal登录' : ['usercenter.login',],
    '门诊收费工作站' : ['outp_bill_portal_service.reg_manager.PatientVisitCardService',
                       'outp_bill_portal_service.get_hospital_card.GetHospitalCardService',
                       'outp_bill_portal_service.arrearage_settle.ArrearageSettleAccounts',
                       'outp_bill_portal_service.arrearage_settle.PrePaidArrearageSettle',
                       'outp_bill_portal_service.out_bill_manager.PrepayService',
                       'outp_bill_portal_service.out_bill_print.InvoicePrint',
                       'outp_bill_portal_service.out_bill_print.InvoiceRecordQuery',
                       'outp_bill_portal_service.out_bill_refund.PrepaidRefundService',
                       'outp_bill_portal_service.out_bill_refund.RefundByExeDeptApply',
                       'outp_bill_portal_service.reg_manager.LossAttendanceCardService',
                       'outp_bill_portal_service.reg_manager.OutpPatientGetLeaveSignService',
                       'outp_bill_portal_service.reg_manager.OutpPatientGetPlusAndOrderSignService',
                       'outp_bill_portal_service.reg_manager.OutpPatientLeaveSignService',
                       'outp_bill_portal_service.reg_manager.OutpPatientOrderSignListService',
                       'outp_bill_portal_service.reg_manager.OutpPatientPlusSignService',
                       'outp_bill_portal_service.reg_manager.OutpPatientQuitSignListService',
                       'outp_bill_portal_service.reg_manager.OutpPatientRepairRegService',
                       'outp_bill_portal_service.reg_manager.PatientVisitButtonService',
                     ],
    '药房工作站' : ['pharm_re_portal_service.pds_pharm.PdsApplyPharmService',
                    'pharm_re_portal_service.pds_pharm.PdsOutDrugReturnService'
                  ],

    '门诊医生站' : ['outp_doctor_portal_service.adt_patient_manager.PatientListOutOrderService',
                     'outp_doctor_portal_service.cpoe_manager.BillPrintService',
                     'outp_doctor_portal_service.cpoe_manager.CpoeOutOrderService',
                     'outp_doctor_portal_service.cpoe_manager.CpoeSubmit',
                     'outp_doctor_portal_service.cpoe_manager.ErsCpoeOutOrderService',
                     'outp_doctor_portal_service.cpoe_manager.InsCpoeOutOrderService'
                     ],
    '检查预约' : ['sp_res_app_portal_service.crs_reservation_register.ReservationRegistService'],
    '基础费用管理': ['bill_base_portal_service.BusinessCardService'],
    '医技工作站': ['med_lab_bill_portal_service.outbill_pay_execute.PayOrgService'],
    '门诊办公室': ['outp_affairs_portal_service.outp_manager.OutpRegMasterPoolReviseService'],

}
#模块和测试用例对应
action_to_testcase = {
    'login' : 'uum_portal.xlsx',               #登录
    'regist' : 'outp_bill_portal.xlsx',        #挂号
    'patientList': '/',
    'apply_pharm': '/',                        #处方供药
    'workstation': '/',                        #医生站工作站选择
    'bill_print':'/',                          #单据打印
    'emr_pds':'outp_doctor_portal.xlsx',       #药疗医嘱
    'cpoe_submit':'/',                         #医嘱提交
    'emr_ers':'outp_doctor_portal.xlsx',       #检查医嘱
    'emr_ins':'outp_doctor_portal.xlsx',       #检验医嘱
    'diagnose' : 'outp_doctor_portal.xlsx',    #诊断
    'reservation_regist' : '/',                #预约登记
    'logout':'/',                              #退出登录
    'businessCard':'/',                        #制卡
    'get_hospital_card':'outp_bill_portal.xlsx', #办卡
    'prepayment':'outp_bill_portal.xlsx',       #预付费充值/退余额
    'pay_org':'/',                             #医技执行科室收费
    'revise':'outp_bill_portal.xlsx',      #号源调整
    'arrearage_settle_accounts':'/',       #欠费结账
    'arrearage_return_premium':'/',        #欠费退费
    'prepaid_arrearage_settle':'/',        #欠费记账
    'prepay':'/',                          #预付费缴费(执行科室)
    'invoice_print':'/',                   #发票打印
    'invoice_print_again':'/',             #发票重打
    'invoice_obsolete':'/',                #发票作废
    'pay_refund':'/',                      #预付费退费（窗口）
    'outbill_prepay_refuse':'/',           #预付费退费（执行科室退费）
    'loss_card':'outp_bill_portal.xlsx',    #就诊卡挂失
    'cancel_loss_card':'outp_bill_portal.xlsx', #就诊卡取消挂失
    'get_leave_sign':'outp_bill_portal.xlsx',     #取留号
    'get_plus_sign':'outp_bill_portal.xlsx',     #取加号，预约号
    'leave_sign':'outp_bill_portal.xlsx',        #留号
    'order_sign_list':'/',                     #内部挂号列表
    'plus_sign':'outp_bill_portal.xlsx',       #加号
    'quit_sign_list':'/',                     #退号信息列表
    'repair_reg':'outp_bill_portal.xlsx',      #补打挂号单
    'regist_button':'outp_bill_portal.xlsx',   #挂号页面按钮功能验证
    'pharm_return':'/',                        #处方退药
}

action_to_testcase2 = {
    '登录' : 'login',               #登录
    '挂号' : 'regist',        #挂号
    '患者列表': '/',
    '处方供药': '/',                        #处方供药
    '医生站工作站选择': '/',                        #医生站工作站选择
    '单据打印':'/',                          #单据打印
    '药疗医嘱':'emr_pds',       #药疗医嘱
    '医嘱提交':'/',                         #医嘱提交
    '检查医嘱':'emr_ers',       #检查医嘱
    '检验医嘱':'emr_ins',       #检验医嘱
    '诊断' : 'diagnose',    #诊断
    '预约登记' : '/',                #预约登记
    '退出登录':'/',                              #退出登录
    '制卡':'/',                        #制卡
    '办卡':'get_hospital_card', #办卡
    '预付费充值/退余额':'prepayment',       #预付费充值/退余额
    '医技执行科室收费':'/',                             #医技执行科室收费
    '号源调整':'revise',      #号源调整
    '欠费结账':'/',       #欠费结账
    '欠费退费':'/',        #欠费退费
    '欠费记账':'/',        #欠费记账
    '预付费缴费(执行科室)':'/',                          #预付费缴费(执行科室)
    '发票打印':'/',                   #发票打印
    '发票重打':'/',             #发票重打
    '发票作废':'/',                #发票作废
    '预付费退费（窗口）':'/',                      #预付费退费（窗口）
    '预付费退费（执行科室退费）':'/',           #预付费退费（执行科室退费）
    '就诊卡挂失':'loss_card',    #就诊卡挂失
    '就诊卡取消挂失':'cancel_loss_card', #就诊卡取消挂失
    '取留号':'get_leave_sign',     #取留号
    '取加号，预约号':'get_plus_sign',     #取加号，预约号
    '留号':'leave_sign',        #留号
    '内部挂号列表':'/',                     #内部挂号列表
    '加号':'plus_sign',       #加号
    '退号信息列表':'/',                     #退号信息列表
    '补打挂号单':'repair_reg',      #补打挂号单
    '挂号页面按钮功能验证':'regist_button',   #挂号页面按钮功能验证
    '处方退药':'/',                        #处方退药
}




#模块和测试用例对应
action_to_testcase1 = {
    'login' : '登录',               #登录
    'regist' : '挂号',        #挂号
    'patientList': '患者列表',
    'apply_pharm': '处方供药',                        #处方供药
    'workstation': '医生站工作站选择',                        #医生站工作站选择
    'bill_print':'单据打印',                          #单据打印
    'emr_pds':'药疗医嘱',       #药疗医嘱
    'cpoe_submit':'医嘱提交',                         #医嘱提交
    'emr_ers':'检查医嘱',       #检查医嘱
    'emr_ins':'检验医嘱',       #检验医嘱
    'diagnose' : '诊断',    #诊断
    'reservation_regist' : '预约登记',                #预约登记
    'logout':'退出登录',                              #退出登录
    'businessCard':'制卡',                        #制卡
    'get_hospital_card':'办卡', #办卡
    'prepayment':'预付费充值/退余额',       #预付费充值/退余额
    'pay_org':'医技执行科室收费',                             #医技执行科室收费
    'revise':'号源调整',      #号源调整
    'arrearage_settle_accounts':'欠费结账',       #欠费结账
    'arrearage_return_premium':'欠费退费',        #欠费退费
    'prepaid_arrearage_settle':'欠费记账',        #欠费记账
    'prepay':'预付费缴费(执行科室)',                          #预付费缴费(执行科室)
    'invoice_print':'发票打印',                   #发票打印
    'invoice_print_again':'发票重打',             #发票重打
    'invoice_obsolete':'发票作废',                #发票作废
    'pay_refund':'预付费退费（窗口）',                      #预付费退费（窗口）
    'outbill_prepay_refuse':'预付费退费（执行科室退费）',           #预付费退费（执行科室退费）
    'loss_card':'就诊卡挂失',    #就诊卡挂失
    'cancel_loss_card':'就诊卡取消挂失', #就诊卡取消挂失
    'get_leave_sign':'取留号',     #取留号
    'get_plus_sign':'取加号，预约号',     #取加号，预约号
    'leave_sign':'留号',        #留号
    'order_sign_list':'内部挂号列表',                     #内部挂号列表
    'plus_sign':'加号',       #加号
    'quit_sign_list':'退号信息列表',                     #退号信息列表
    'repair_reg':'补打挂号单',      #补打挂号单
    'regist_button':'挂号页面按钮功能验证',   #挂号页面按钮功能验证
    'pharm_return':'处方退药',                        #处方退药
}



#针对不同模块引用的测试用例相同
testcase = {
    'revise':'plug_sign',     #门办号源调整
    'cancel_loss_card':'loss_card',   #就诊卡取消挂失
    'regist_button':'regist',         #挂号页面按钮功能验证
}

