#! /usr/bin/env python
#coding=utf-8
'''
门诊挂号信息(就诊登记)
'''

from sqlalchemy import Column,String,Float,Integer,DATE
import UI.com_th_supcom_pojo.base_pojo.Base as obj


class User(obj.Base):
    __tablename__ = 'uum_user'  # 表名
    id = Column(Integer,primary_key=True)  #主键
    people_name = Column(String(128))
    user_name = Column(String(128))

    def __repr__(self):
        return "<User>"