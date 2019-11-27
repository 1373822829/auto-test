#! /usr/bin/env python
#coding=utf-8
'''
票据库房
'''

import UI.com_th_supcom_pojo.base_pojo.Base as obj
from sqlalchemy import Column,String,Float,Integer,DATE

class TicketDept(obj.Base):
    __tablename__ = 'isms_ticket_dept'  # 表名
    ticket_dept_code = Column(Integer,primary_key=True) #票据库房编码
    ticket_dept_name = Column(String(300))  #票据库房名称
    ticket_dept_level = Column(String(300))  #库房级别
    ticket_dept_emp_code = Column(String(13))  #管理用户编码
    ticket_dept_org_code = Column(String(13))  #管理机构编码

    def __repr__(self):
        return "<TicketDept>"
