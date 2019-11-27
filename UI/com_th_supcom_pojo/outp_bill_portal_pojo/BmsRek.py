#! /usr/bin/env python
#coding=utf-8
'''
结算表
'''

import UI.com_th_supcom_pojo.base_pojo.Base as obj
from sqlalchemy import Column,String,Float,Integer,DATE

class Rek(obj.Base):
    __tablename__ = 'rek'  # 表名
    id = Column(Integer,primary_key=True) #主键
    rek_no = Column(String(50))  #单号
    rek_type = Column(String(50))  #结算类型
    patient_id = Column(String(13))  #患者id
    charge_type = Column(String(11))  #费别
    costs = Column(Float)   #总费用
    area = Column(String(10)) #院区
    settle_type = Column(String(10))  #"收费类型 0：正常 1：冲负 2：退费"
    in_out_flag = Column(String(5))   #门诊住院标识

    def __repr__(self):
        return "<Rek>"
