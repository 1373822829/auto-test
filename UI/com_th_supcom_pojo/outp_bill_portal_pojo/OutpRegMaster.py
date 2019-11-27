#! /usr/bin/env python
#coding=utf-8
'''
门诊号池类
'''

from sqlalchemy import Column,String,Float,Integer,DATE
import UI.com_th_supcom_pojo.base_pojo.Base as obj

class OutpRegMaster(obj.Base):
    __tablename__ = 'outp_reg_master' #表名

    master_id = Column(Integer, primary_key=True)  #主键

    hospital_area_code = Column(String(32))  #院区编码

    outp_date = Column(DATE)   #门诊日期

    outp_special_id = Column(Integer)  #门诊专科id

    reside_dept_code = Column(String(32))    #门诊科室CODE

    belong_dept_code = Column(String(32))  #所属专科CODE

    emp_no = Column(String(32))   #医生CODE

    outp_type_code = Column(String(32))  #挂号类别CODE

    outp_duration_code = Column(String(32))  #门诊时间CODE

    registration_limits = Column(Integer)     #限号数

    current_limits = Column(Integer)   #当前可用数

    current_no = Column(Integer)    #挂号室当前号池的序号

    sort_no = Column(Integer)       #生成号源的的显示顺序

    def __repr__(self):
        return "<OutpRegMaster>"
