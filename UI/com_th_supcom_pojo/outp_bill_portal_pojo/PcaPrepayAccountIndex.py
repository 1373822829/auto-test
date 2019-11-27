#! /usr/bin/env python
#coding=utf-8
'''
账户主索引类
'''

from sqlalchemy import Column,String
import UI.com_th_supcom_pojo.base_pojo.Base as obj


class PcaPrepayAccountIndex(obj.Base):
    __tablename__ = 'pca_prepay_account_index'  # 表名
    account_index = Column(String(32),primary_key=True)
    card_no = Column(String(32))
    card_type = Column(String(32))
    def __repr__(self):
        return "<PcaPrepayAccountIndex>"




