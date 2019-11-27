#! /usr/bin/env python
#coding=utf-8
'''
账户记录类
'''

from sqlalchemy import Column,String,Float,DateTime
import UI.com_th_supcom_pojo.base_pojo.Base as obj


class PcaPrepayAccountMaster(obj.Base):
    __tablename__ = 'pca_prepay_account_master' #表名
    account_index = Column(String(32), primary_key=True)
    balance = Column(Float)
    account_type = Column(String(2))
    create_time = Column(DateTime)
    def __repr__(self):
        return "<PcaPrepayAccountMaster>"
