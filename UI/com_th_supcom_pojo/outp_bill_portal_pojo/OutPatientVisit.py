#! /usr/bin/env python
#coding=utf-8
'''
门诊挂号信息(就诊登记)
'''

from sqlalchemy import Column,String,Float,Integer,DATE
import UI.com_th_supcom_pojo.base_pojo.Base as obj

class OutPatientVisit(obj.Base):
    __tablename__ = 'outp_patient_visit'  # 表名
    outp_visit_id = Column(Integer,primary_key=True)  #主键
    registering_time = Column(DATE)          #挂号日期
    outp_special_name = Column(String(128))  #门诊专科名称
    outp_duration_code = Column(String(32))  #门诊时间段CODE（PTS0004）
    outp_type_code = Column(String(32))      #门诊类别CODE（PTS0001）
    hospital_area_code = Column(String(32))  #院区编码
    emp_no = Column(String(32))           #医生名字
    registry_flag = Column(Integer)

    def __repr__(self):
        return "<OutPatientVisit>"