#! /usr/bin/env python
#coding=utf-8
'''
药房码表
'''
from sqlalchemy.orm import relationship, backref

import UI.com_th_supcom_pojo.base_pojo.Base as obj
from sqlalchemy import Column,String

class PhamOrg(obj.Base):
    __tablename__ = 'pham_org'  # 表名
    org_id = Column(String(30),primary_key=True) #主键   机构编码
    org_brief_code = Column(String(30))  #机构简码
    org_type = Column(String(1))  #药房药库属性（0：药房；1：药库）
    org_address = Column(String(100))  #药库药房地址
    belong_org_code = Column(String(30))  #归属药房代码
    # pham_stock = relationship("PhamStock",backref = backref('pham_org',order_by = org_id))   #外键关联

    def __repr__(self):
        return "<PhamOrg>"
