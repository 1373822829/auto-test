#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
挂号验证
'''
import re
import UI.com_th_supcom_api.common.Utility as Utility
import UI.common_th_supcom_config.test_case_config.TestCaseCodeTable as table
import UI.com_th_supcom_pojo.outp_bill_portal_pojo.PcaPrepayAccountMaster as master
import UI.com_th_supcom_pojo.outp_bill_portal_pojo.PcaPrepayAccountIndex as index
import UI.com_th_supcom_pojo.outp_bill_portal_pojo.OutpRegMaster as RegMaster
import UI.com_th_supcom_pojo.outp_bill_portal_pojo.OutpSpecialClinic as SpecialClinic
import UI.common_th_supcom_config.url_config as path
import datetime
import UI.com_th_supcom_pojo.outp_bill_portal_pojo.OutPatientVisit as PatientVist
import UI.com_th_supcom_pojo.uum_portal_pojo.User as User
from sqlalchemy import func
from UI.com_th_supcom_pojo.outp_bill_portal_pojo import BmsBillItem
from UI.com_th_supcom_pojo.outp_bill_portal_pojo import BmsRek
from UI.com_th_supcom_pojo.outp_bill_portal_pojo import IsmsTicketDept
from UI.com_th_supcom_pojo.outp_bill_portal_pojo import IsmsTicketDictionary
from UI.com_th_supcom_pojo.outp_bill_portal_pojo import IsmsTicketStock
'''
查询患者余额
tets_case:测试用例
'''
def outp_balance(test_case):
    dict = table.patient_visit_card
    card = re.sub('[^0-9]', '', test_case[dict['patient_card']].split('=')[0])
    session = Utility.db_session(path.PCA_DB_HOST)
    Index = index.PcaPrepayAccountIndex
    Master = master.PcaPrepayAccountMaster
    sql = session.query(Index, Master).filter(Index.account_index == Master.account_index,Index.card_no == card,Master.account_type == 'O')
    if sql.all() == []:
        return None
    result = sql.one()
    session.close()
    return result

'''
查询已挂数，当前号
tets_case:测试用例
'''

def outp_regist_master(test_case):
    dict = table.patient_visit_card
    reg_date = datetime.date.today()
    reg_type_refer = {'普通': '1', '急诊': '2', '专家': '3', '特需': '4', '节假日': '5', '残疾': '6', '老年': '7', '保健': '8',
                      '义诊': '9', '简易': '10'}
    outp_duration_refer = {'全天': '1', '上午': '2', '下午': '3', '晚上': '4'}
    Master = RegMaster.OutpRegMaster
    Clinic = SpecialClinic.OutpSpecialClinic
    session = Utility.db_session(path.PTS_DB_HOST)
    str = session.query(Master,Clinic).filter(Master.belong_dept_code == Clinic.belong_clinic_code).\
        filter(Master.outp_date == reg_date,Master.hospital_area_code == path.HOSPITA_AREA_CODE,Clinic.special_clinic_name == test_case[dict['special_name']]).\
        filter( Master.outp_type_code == reg_type_refer[test_case[dict['special_type']]],Master.outp_duration_code == outp_duration_refer[test_case[dict['outp_time']]])
    if test_case[dict['doctor_name']].strip() == '':
        if str.all() == []:
            return None
        else:
            result = str.first()
    else:
        session_user = Utility.db_session(path.UUM_DB_HOST)
        UUM = User.User
        user = session_user.query(UUM).filter(UUM.people_name == test_case[dict['doctor_name']]).one()
        sql = str.filter(Master.emp_no == user.user_name)
        if sql.all() == []:
            return None
        result = sql.first()
        session_user.close()
    session.close()
    return result


'''
查询门办中挂号数
tets_case:测试用例
'''

def outp_patient_visit(test_case):
    dict = table.patient_visit_card
    reg_date = datetime.date.today()
    reg_type_refer = {'普通': '1', '急诊': '2', '专家': '3', '特需': '4', '节假日': '5', '残疾': '6', '老年': '7', '保健': '8',
                      '义诊': '9', '简易': '10'}
    outp_duration_refer = {'全天': '1', '上午': '2', '下午': '3', '晚上': '4'}
    Vist = PatientVist.OutPatientVisit
    session_visit = Utility.db_session(path.PTS_DB_HOST)
    str = session_visit.query(func.count(Vist.outp_visit_id)).filter(Vist.registering_time>reg_date,Vist.outp_special_name == test_case[dict['special_name']],
                                                                  Vist.outp_duration_code == outp_duration_refer[test_case[dict['outp_time']]],
                                                                  Vist.outp_type_code == reg_type_refer[test_case[dict['special_type']]],
                                                                  Vist.hospital_area_code == path.HOSPITA_AREA_CODE,
                                                                     Vist.registry_flag != 2)
    if test_case[dict['doctor_name']].strip() == '':
        result = str.one()
    else:
        session_user = Utility.db_session(path.UUM_DB_HOST)
        UUM = User.User
        user = session_user.query(UUM).filter(UUM.people_name == test_case[dict['doctor_name']]).one()
        sql = str.filter(Vist.emp_no == user.user_name)
        if sql.all() == []:
            return None
        result = sql.one()
        session_user.close()
    session_visit.close()
    return result

'''
查询门办中退号数
tets_case:测试用例
'''
def retreat_sign(test_case):
    dict = table.patient_visit_card
    reg_date = datetime.date.today()
    reg_type_refer = {'普通': '1', '急诊': '2', '专家': '3', '特需': '4', '节假日': '5', '残疾': '6', '老年': '7', '保健': '8',
                      '义诊': '9', '简易': '10'}
    outp_duration_refer = {'全天': '1', '上午': '2', '下午': '3', '晚上': '4'}
    Vist = PatientVist.OutPatientVisit
    session_visit = Utility.db_session(path.PTS_DB_HOST)
    str = session_visit.query(func.count(Vist.outp_visit_id)).filter(Vist.registering_time>reg_date,Vist.outp_special_name == test_case[dict['special_name']],
                                                                  Vist.outp_duration_code == outp_duration_refer[test_case[dict['outp_time']]],
                                                                  Vist.outp_type_code == reg_type_refer[test_case[dict['special_type']]],
                                                                  Vist.hospital_area_code == path.HOSPITA_AREA_CODE,
                                                                     Vist.registry_flag == 2)
    if test_case[dict['doctor_name']].strip() == '':
        result = str.one()
    else:
        session_user = Utility.db_session(path.UUM_DB_HOST)
        UUM = User.User
        user = session_user.query(UUM).filter(UUM.people_name == test_case[dict['doctor_name']]).one()
        sql = str.filter(Vist.emp_no == user.user_name)
        if sql.all() == []:
            return None
        result = sql.one()
        session_user.close()
    session_visit.close()
    return result

'''
根据申请单号查询消费凭证号
'''
def find_rek_no(apply_id):
    BillItem = BmsBillItem.BillItem
    Rek = BmsRek.Rek
    session = Utility.db_session(path.BMS_DB_HOST)
    settle_type_list = ['0','1','2']
    for settle_type in settle_type_list:
        str = session.query(Rek,BillItem).filter(Rek.id == BillItem.rek_id).filter(Rek.area == path.HOSPITA_AREA_CODE,Rek.settle_type == settle_type
                                                                                   ,BillItem.apply_id == apply_id,Rek.in_out_flag == 'O')
        if settle_type == '0':
            result = str.first()
        elif settle_type != '0' and str.all()!=[]:
            result = []
    return result

'''
查询最小票据号
'''
def find_min_ticket(username,ticket_name):
    dept_org_codes = str(path.HOSPITA_CODE)+'%'
    TicketDept = IsmsTicketDept.TicketDept
    TicketDictionary = IsmsTicketDictionary.TicketDictionary
    TicketStock = IsmsTicketStock.TicketStock
    session = Utility.db_session(path.ISMS_DB_HOST)
    sql = session.query(func.min(TicketStock.ticket_start_number)).filter(TicketStock.ticket_dept_code == TicketDept.ticket_dept_code,
                                                                     TicketStock.ticket_dictionary_code == TicketDictionary.ticket_dictionary_code,
                                                                     TicketDept.ticket_dept_name.like('%'+username),TicketDictionary.ticket_name == ticket_name,
                                                                     TicketDept.ticket_dept_org_code.like(dept_org_codes))
    print(sql)
    result = sql.one()
    return result

'''
根据消费流水号查询机制号
'''
def find_mechanism_numbe(rek_no_list):
    BillItem = BmsBillItem.BillItem
    Rek = BmsRek.Rek
    session = Utility.db_session(path.BMS_DB_HOST)
    sql = session.query(BillItem.branch_no).filter(BillItem.rek_id.in_(session.query(Rek.id).filter(Rek.rek_no.in_(rek_no_list)))).group_by(BillItem.branch_no)
    if sql.all != []:
        return sql.one()
    else:
        return None



if __name__ == "__main__":
    cache = {}
    cache['verify'] = ['口腔科', '专家', '陈卫民', '教授', '下午', '0', '', '30']
    test_case = {'患者卡号':'%E?;1004627675=99015017425?+E?'}
    n =  outp_balance(test_case)
    print(n.PcaPrepayAccountIndex.account_index)
    # print(outp_patient_visit(cache).reg_type_refer)
    # test_case = {'门诊时间': '全天', '患者姓名': '杨俊熙', '医生': '', '门诊科室': '内科门诊', '就诊时间': '2017-06-28',
    #   '患者卡号': '%E?;1004627675=99015017425?+E?', '专科名称': '门诊内科', '号源类别': '普通'}
    # #
    # res =  outp_regist_master(test_case)
    # print(res.OutpRegMaster.current_no)
    # print(res.registration_limits-res.current_limits)
    res = find_min_ticket('李金芳','住院结算发票')
    print(res[0])
    # r = find_mechanism_numbe(['02-10010-10016055','02-10010-10015835'])
    # print(r)
    # rs = find_rek_no('02D2017061200055')
    # print(rs)
    # test_case = {'门诊时间': '全天', '患者姓名': '杨俊熙', '医生': '', '门诊科室': '眼科门诊', '就诊时间': '2017-06-30',
    #              '患者卡号': '%E?;1004627675=99015017425?+E?', '专科名称': '急诊眼科', '号源类别': '急诊'}
    # r = outp_regist_master(test_case)
    # print(r)

