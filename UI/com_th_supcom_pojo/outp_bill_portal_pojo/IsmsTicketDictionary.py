#! /usr/bin/env python
#coding=utf-8
'''
票据字典
'''

import UI.com_th_supcom_pojo.base_pojo.Base as obj
from sqlalchemy import Column,String,Integer,DATE

class TicketDictionary(obj.Base):
    __tablename__ = 'isms_ticket_dictionary'  # 表名
    ticket_dictionary_code = Column(Integer,primary_key=True) #票据库房编码
    ticket_name = Column(String(300))  #票据名称
    ticket_number_length = Column(Integer)  #票据票号长度
    dictionary_create_emp_code = Column(String(13))  #票据字典版本创建人编码
    dictionary_create_date = Column(DATE)  #票据字典创建日期
    is_fine_management = Column(String(1))  #是否精细化管理 0：否，1：是
    dictionary_is_waste = Column(String(1))  #是否作废 0：作废，1：正常使用
    dictionary_waste_emp_code = Column(String(13)) #作废操作人编码
    dictionary_waste_date = Column(DATE)   #作废日期
    dictionary_waste_note = Column(String(300))  #作废说明

    def __repr__(self):
        return "<TicketDictionary>"