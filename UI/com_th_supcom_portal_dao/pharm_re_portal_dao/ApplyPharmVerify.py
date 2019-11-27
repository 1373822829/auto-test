#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
药品数量验证
'''

import UI.com_th_supcom_api.common.Utility as Utility
import UI.common_th_supcom_config.url_config as path
from sqlalchemy import func
from UI.com_th_supcom_pojo.pharm_re_portal_pojo import DmsPhamBasicInfo,DmsPhamStock,DmsPhamOrg



#根据药品信息查询药品数量
#pham_name : 药品名称
#pham_spec : 药品规格
#org_address : 执行药房
def find_pham_num(pham_name,pham_spec,org_address):

    PhamBasicInfo = DmsPhamBasicInfo.PhamBasicInfo
    PhamStock = DmsPhamStock.PhamStock
    PhamOrg = DmsPhamOrg.PhamOrg
    session = Utility.db_session(path.DMS_DB_HOST)
    stmd = session.query(PhamOrg.org_id).filter(PhamOrg.org_address == org_address)
    sql = session.query(func.sum(func.floor(PhamStock.quantity/PhamBasicInfo.package_factor)),func.sum(func.mod(
                        PhamStock.quantity,PhamBasicInfo.package_factor))).filter(PhamStock.pham_std_code == PhamBasicInfo.pham_std_code,
                        PhamBasicInfo.pham_name == pham_name,PhamBasicInfo.pham_spec == pham_spec,PhamStock.dept_code == stmd)

    result = sql.one()
    return result


#根据药品信息查询药品基本信息对象
#pham_name : 药品名称
#pham_spec : 药品规格
def find_pham_basic_info(pham_name,pham_spec):
    PhamBasicInfo = DmsPhamBasicInfo.PhamBasicInfo
    session = Utility.db_session(path.DMS_DB_HOST)
    sql = session.query(PhamBasicInfo).filter(PhamBasicInfo.pham_name == pham_name,PhamBasicInfo.pham_spec == pham_spec)
    result = sql.first()
    return result


if __name__ == "__main__":
    # cache = {}
    # cache['处方单'] = {'02A201705-1600091': '门诊药房（光谷）','02A201705-1600092': '住院药房（光谷）'}
    # cache['verify'] = [['1', '', '氯化钠注射液', '3000ml27g@成都青山利康', '4袋', '23.20', '92.80', '2/日(Bid) 每次3000ml(1袋)', '', '口服', '', ' ']]
    # n = pham_verify(cache)
    # print(str(n[0])+'盒'+str(n[1])+'片')
    res = find_pham_basic_info('氯化钠注射液','3000ml27g@成都青山利康')
    print(res.retail_price*(res.dose_per_unit*res.package_factor))

    r = find_pham_num('氯化钠注射液','3000ml27g@成都青山利康','门诊药房（光谷）')
    print(str(r[0])+'.'+str(r[1]))




