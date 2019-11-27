#! /usr/bin/env python
#coding=utf-8
'''
费用明细表
'''

import UI.com_th_supcom_pojo.base_pojo.Base as obj
from sqlalchemy import Column,String,Float,Integer,DATE

class BillItem(obj.Base):
    __tablename__ = 'bill_item'  # 表名
    id = Column(Integer,primary_key=True) #主键
    refund_flag = Column(String(3)) #null表示未冲负 1表示已冲负
    rek_id = Column(Integer)  #结算标识号
    item_name = Column(String(200)) #项目名称
    apply_id = Column(String(40)) #申请单号
    ordered_by = Column(String(30))  #开单科室
    performed_by = Column(String(30)) #执行科室
    in_out_flag = Column(String(5))   #门诊住院标识
    branch_no = Column(String(50))   #机制号

    def __repr__(self):
        return "<BillItem>"
