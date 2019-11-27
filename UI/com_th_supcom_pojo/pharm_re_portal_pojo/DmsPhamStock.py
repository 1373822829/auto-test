#! /usr/bin/env python
#coding=utf-8
'''
本表用于记录库房药品的当前结存记录。
每库房每库存药品（品、规、厂商为主键）存在一条记录。包装、批次、有效期等质量与库存流通管理的信息，存放到其子表中。
'''
from sqlalchemy.orm import relationship, backref

import UI.com_th_supcom_pojo.base_pojo.Base as obj
from sqlalchemy import Column,String,Float,Integer,DATE

class PhamStock(obj.Base):
    __tablename__ = 'pham_stock_table'  # 表名
    stock_id = Column(Integer,primary_key=True) #主键
    dept_code = Column(String(30))  #库存机构ID
    pham_std_code = Column(String(30))  #药品ID
    pham_factory_name = Column(String(200))  #厂家名称
    quantity = Column(Integer)  #数量(基本数量)
    unit = Column(String(30))   #单位
    # pham_org = relationship("PhamOrg",backref = backref('pham_stock',order_by = dept_code))  #外键关联

    def __repr__(self):
        return "<PhamStock>"
