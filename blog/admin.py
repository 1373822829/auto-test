
from django.contrib import admin

# Register your models here.
from blog.models import Workstation,Test_Case,Test_Case_Detail,Action


# 查询所有的工作站
def find_all_workstation():
    workstation = Workstation.objects.all()
    workstation_list = []
    for work in workstation:
        workstation_list.append({'id':work.id,'text':work.workstation_name})
    return workstation_list


#查询所有的测试用例
def find_all_testcase():
    testcase = Test_Case.objects.all()
    testcase_list = []
    for test in testcase:
        testcase_list.append(test.testcase_name)
    return testcase_list

#将查询的对象列表转换为dict方便json转换
def findTestCaseDetail(testcase_id):
    testcase_detail_list = Test_Case_Detail.objects.filter(testcase_id=testcase_id).order_by('testcase_num')
    data = []
    for testcase_detail in testcase_detail_list:
        if '0'==testcase_detail.iscache:
            iscache = '否'
        if '1'==testcase_detail.iscache:
            iscache = '是'
        testcase_detail_dict = {
                                'id':testcase_detail.test_case_detail_id,'testcase_num':testcase_detail.testcase_num,'testcase_id':testcase_detail.testcase_id,
                                'testcase_name':testcase_detail.testcase_name,'workstation':testcase_detail.workstation,
                                'action':testcase_detail.action,'data':testcase_detail.data,'sheet_name':testcase_detail.sheet_name,
                                'get_value_way':testcase_detail.get_value_way,'iscache':iscache,'runtime':testcase_detail.runtime}
        data.append(testcase_detail_dict)
    return {'data':data}

#将查询的数据转换为list_action字典
def findTestCaseAction(testcase_id):
    testcase_detail_list = Test_Case_Detail.objects.filter(testcase_id=testcase_id).order_by('testcase_num')
    print(testcase_detail_list[0].data.replace(u'\u202a', u' '))
    data = []
    for testcase_detail in testcase_detail_list:
        path = testcase_detail.data.replace(u'\u202a', u'')

        data.append([testcase_detail.workstation,testcase_detail.action,
                     testcase_detail.sheet_name,testcase_detail.get_value_way,testcase_detail.runtime])
    data.append({'path':path})
    return data

#将查询的测试用例对象转换为两个dict
def findAction(name):
    if name!=None:
        workstation = Workstation.objects.filter(workstation_name=name)
        action_list = Action.objects.filter(master_id=workstation[0].master_id)
    else:
        action_list = Action.objects.all()
    action_data = []
    sheet_name_data = []
    for action in action_list:
        action_dict = {'id':action.id,'text':action.action_name}
        sheet_name_dict = {'id':action.id,'text':action.sheet_name}
        action_data.append(action_dict)
        sheet_name_data.append(sheet_name_dict)
    return {'action':action_data,'sheet_name':sheet_name_data}

def findTestCaseCombobox():
    testcase = Test_Case.objects.all()
    data = []
    for test in testcase:
        testcase_dict = {'id':test.id,'text':test.testcase_name}
        data.append(testcase_dict)
    return data
