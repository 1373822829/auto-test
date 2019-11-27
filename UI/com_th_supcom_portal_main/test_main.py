#! /usr/bin/env python
#coding=utf-8
'''

'''
import math
import random

import UI.com_th_supcom_api.common.Utility as utility
import UI.com_th_supcom_api.common.Common as Common
import os,sys,time
import UI.common_th_supcom_config.work_bench_config.WorkBenchUrl as work
import UI.common_th_supcom_config.test_case_config.TestCaseUrl as file
import UI.com_th_supcom_api.common.Log as Log

#日志对象初始化

from UI.com_th_supcom_api.common.Cache import Cache

log = Log.Logger(__name__)


dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
for root, dirs, files in os.walk(dir):
    if 'service' in root:
        sys.path.append(root)




class testRegManager:

    def __init__(self,List_action,ip):
        #浏览器对象
        self. browser = Common.browser(ip)
        self.cachedata = Cache({})
        self.List_action = List_action


    #[['portal登陆', 'login', 'uum_portal.xlsx','  随机','1'],[]]
    # 获取所需的测试用例
    @staticmethod
    def BuildTestCase(test_case,List_action):
        for action in List_action:
            if not isinstance(action,list):
                continue
            if not action[1] in test_case.keys():
                if action[2] == '/':
                    test_case[action[1]] = None
                else:
                    sheet_name = work.action_to_testcase1.get(action[2])
                    test_case[action[1]] = utility.GetTestcase(List_action[-1].get('path'),sheet_name)

    @staticmethod
    def callmoudle(browser,cachedata,List_action,test_case):

        try:
            # key,value相互转换
            dictionary = {value: key for key, value in work.action_to_testcase1.items()}
            for workstation in List_action:
                if not isinstance(workstation,list):
                    continue
                moudel_list = work.workstation_include_moudle[workstation[0]]
                for moudel in moudel_list:
                    action = __import__(moudel.split('.')[-1])
                    method_name = 'test_' + dictionary.get(workstation[1])
                    if hasattr(action,method_name):
                         fun = getattr(action,method_name)
                         if test_case[workstation[1]] is None:
                             fun(browser,cachedata)
                         else:
                             if int(workstation[4]) == 0:   #执行次数如果为0，跳过改脚本
                                 break
                             # 执行次数大于用例数据，执行用例所有数据
                             if int(workstation[4])>len(test_case[workstation[1]]):
                                 workstation[4] = test_case[workstation[1]]

                             for i in range(int(workstation[4])):
                                 if workstation[3].strip() == '随机':
                                     num = random.randint(0,int(workstation[4])-1)
                                 if workstation[3].strip() == '顺序':
                                     num = i
                                 fun(browser,test_case[workstation[1]][num],cachedata)

        except Exception as e:
            # utility.SaveLog(e, 1)
            log.exception(e)
            utility.capture(browser,'fail')




    def iterator(self):
        test_case = {}
        self.BuildTestCase(test_case,self.List_action)
        for num in range(0,1):
           if num > 1:
               t = testRegManager(self.List_action)
               t.callmoudle(t.browser,t.cachedata,t.List_action,test_case)
               Common.tear_down(t.browser)
           else:
                 self.callmoudle(self.browser,self.cachedata,self.List_action,test_case)
                 Common.tear_down(self.browser)














