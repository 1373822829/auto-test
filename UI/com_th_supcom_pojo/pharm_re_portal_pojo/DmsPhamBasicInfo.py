#! /usr/bin/env python
#coding=utf-8
'''
药品信息
'''

import UI.com_th_supcom_pojo.base_pojo.Base as obj
from sqlalchemy import Column,String,Float,Integer,DATE

class PhamBasicInfo(obj.Base):
    __tablename__ = 'pham_basic_info'  # 表名
    pham_std_code = Column(String(30),primary_key=True) #主键   药品编码
    pham_code = Column(String(30))  #分类编码，国家标准
    pham_cate_code = Column(String(20))  #西药、中成药、中草药、普通耗材等
    pham_name = Column(String(100))  #标准名称
    pham_unit = Column(String(20))  #一般对应项目最小包装单位(基本单位)最小可使用单位
    package_unit = Column(String(20))   #零售包装单位
    package_factor = Column(Float)   #零售价包装单位中含有基本单位的数量（如果是药品的话）
    pham_spec = Column(String(100))    #药品规格
    dose_per_unit = Column(Float)    #-最小单位与剂量单位换算系数，包装单位与医疗单位换算系数(标准单位下的含量)
    retail_price = Column(Float)     #零售价


    def __repr__(self):
        return "<PhamBasicInfo>"
