#测试用例参照表

user_login = {'username':'用户名','psw':'密码'}

patient_visit_card = {
    'patient_card':'患者卡号','patient_name':'患者姓名','special_type':'号源类别',
    'special_num':'专科编码','special_name':'专科名称','doctor_name':'医生','outp_time':'门诊时间',
    'regist_fee':'挂号费','reside_dept':'专科门诊'
}

cpoe_out_order = {
    'patient_card':'患者卡号','patient_name':'患者姓名','cpoe_type':'医嘱类型',
    'cpoe_name':'医嘱名称拼音码', 'is_outpresc':'是否带药','dosage':'每次用量'  ,'way':'途径',
    'frequency':'频次','course_treat':'疗程','treat_pur':'用药目的','pham_name':'医嘱名称',
    'pham_spec':'药品规格','org_address':'执行科室'
}

diagnose = { 'patient_card':'患者卡号','patient_name':'患者姓名','dia_type':'诊断类别',
    'dia_name':'诊断名称'}

ers_cpoe_table = {
    'patient_card':'患者卡号',  'patient_name':'患者姓名','cpoe_name':'医嘱名称',
    'execute_depat':'执行科室','ers_combin_part':'检查部位/方法分组','ers_part':'部位/方法',
    'add_item':'附加项目'
}

ins_cpoe = {
    'patient_name':'患者姓名','patient_card':'患者卡号','ins_item':'检验项目',
    'item_name':'项目名称','ins_detail':'检验明细','specimen':'标本',
    'execute_depat':'执行科室','clinic_diagnose':'临床诊断','ins_aim':'检验目的'
}

get_hospital_card = {

    'patient_card':'患者卡号',
    'patient_name': '患者姓名',
    'sex': '性别',
    'birthday': '生日',
    'phone': '电话',
    'phone1': '确认电话',
    'charge_type': '费别',

}

prepayment = {

    'patient_card': '患者卡号',
    'patient_name': '患者姓名',
    'payment_code': '支付方式',
    'recharge_number': '充值数',

}

loss = {
    'name':'患者姓名','id_card':'患者身份证号','phone_num':'电话号'
}

plus_sign = {
    'patient_card':'患者卡号','name':'患者姓名','special_name':'专科名称','clinic':'门诊科室',
    'clinic_code':'门诊科室编码','doctor_name':'医生','doctor_code':'医生编码','outp_time':'门诊时间',
    'special_type':'号源类别','regist_fee':'挂号费'
}


leave_sign = {
    'patient_card':'患者卡号','name':'患者姓名','special_name':'专科名称','reside_dept':'门诊科室',
    'visit_time':'就诊时间','doctor_name':'医生','outp_time':'门诊时间','special_type':'号源类别',
    'regist_fee':'挂号费'
}

repair_reg = {
    'patient_card':'患者卡号','name':'患者姓名','special_name':'专科名称','doctor_name':'医生',
    'outp_time':'门诊时间','special_type':'号源类别',
}