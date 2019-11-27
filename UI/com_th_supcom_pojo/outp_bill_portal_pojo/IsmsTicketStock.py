#! /usr/bin/env python
#coding=utf-8
'''
票据库存
'''

import UI.com_th_supcom_pojo.base_pojo.Base as obj
from sqlalchemy import Column,String,Integer,DATE

class TicketStock(obj.Base):
    __tablename__ = 'isms_ticket_stock'  # 表名
    ticket_dept_code = Column(Integer,primary_key=True) #库房编码
    ticket_dictionary_code = Column(Integer)  #票据字典编码
    ticket_version = Column(String(30))  #票据版本号
    ticket_start_number = Column(String(30))  #票据起始号码
    ticket_end_number = Column(String(30))  #票据结束号码
    stock_number = Column(Integer)  #票据库存数量
    unit_code = Column(String(13))  #数量使用单位编码
    stock_create_date = Column(DATE)   #库存创建日期
    ticket_stock_code = Column(Integer)  #库存编码

    def __repr__(self):
        return "<TicketStock>"