#! /usr/bin/env python
#coding=utf-8
'''
门诊专科信息类
'''

from sqlalchemy import Column,String,Float,Integer
import UI.com_th_supcom_pojo.base_pojo.Base as obj
from sqlalchemy.orm import relationship

class OutpSpecialClinic(obj.Base):
    __tablename__ = 'outp_special_clinic' #表名
    outp_special_id = Column(Integer, primary_key=True)
    hospital_area_code = Column(String(32))  #院区编码
    special_clinic_code = Column(String(32))  #挂号专科代码
    special_clinic_name = Column(String(128)) #挂号专科名称
    sort_no = Column(Integer)  #排序号
    belong_clinic_code = Column(String(32))  #门诊科室

    def __repr__(self):
        return "<OutpSpecialClinic>"