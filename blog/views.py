# encodeing=utf8
import json
import os

import sys

from django.db.models import QuerySet
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import Context
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect, ensure_csrf_cookie, csrf_exempt

from UI.com_th_supcom_portal_main import test_main
from blog.admin import find_all_workstation, find_all_testcase, findTestCaseDetail, findAction, findTestCaseAction, \
    findTestCaseCombobox
from blog.models import Workstation, Test_Case, Action, Test_Case_Detail, User, Data, Case, Case_Detail
from django.core.files.uploadedfile import TemporaryUploadedFile


# Create your views here.


# 登录
@csrf_exempt
def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username=username)
        if user.exists():
            pwd = user.get(username=username).password
            if password == pwd:
                return HttpResponseRedirect('/index/?username=' + username)
            else:
                return render(request, "login.html", {'data': '密码错误!'})
        else:
            return render(request, "login.html", {'data': '用户不存在!'})
    return render(request, "login.html")


# 加载工作站树
@csrf_exempt
def index(request):
    user = User.objects.get(username=request.GET.get('username'))
    user_name = user.user
    testcase = Test_Case.objects.all()
    case = Case.objects.all()
    workstation_list = find_all_workstation()
    testcase_data = []
    for test in case:
        testcase_data.append({'id': test.id, 'text': test.name})
    workstation_data = []
    for workstation in workstation_list:
        workstation['children'] = []
        workstation['iconCls'] = "icon-folder"
        for test in testcase:
            if test.workstation == workstation['text']:
                workstation['iconCls'] = ""
                workstation['children'].append({'id': test.id, 'text': test.testcase_name, 'url': 'base.html'})
        workstation_data.append(workstation)
    data = [{'id': 1, 'text': '用例管理', 'children': workstation_data},
            {'id': 2, 'text': '用例执行', 'children': testcase_data}]
    return render(request, "admin.html", {'data': data, 'user_name': user_name})


# 加载执行用例明细
@csrf_exempt
def load_case_detail(request):
    if request.method == 'POST':
        id = request.POST.get('case_id')
        case_detail = Case_Detail.objects.filter(case_id=id)
        case_detail_list = []
        for case in case_detail:
            case_detail_dict = {'id': case.id, 'case_name': case.case_name, 'case_num': case.case_num,
                                'testcase_id': case.testcase_id,
                                'workstation': case.workstation, 'data': case.data, 'case_id': case.case_id,
                                'detail': '<a href="">详情</a>'}
            case_detail_list.append(case_detail_dict)
        return HttpResponse(json.dumps(case_detail_list))


# 加载用例执行
@csrf_exempt
def load_case_details(request):
    if request.method == "POST":
        # id = request.POST.get('case_id')
        test_case_detail_list = Test_Case_Detail.objects.all()
        test_case_list = Test_Case.objects.all()
        data = []
        i = 1
        num = ''
        for test_case in test_case_list:
            for test_case_detail in test_case_detail_list:
                if test_case.id == test_case_detail.testcase_id:
                    if num == test_case_detail.testcase_id:
                        continue
                    num = test_case_detail.testcase_id
                    case_details = {'case_num': i, 'case_name': test_case.testcase_name,
                                    'workstation': test_case.workstation, 'data': test_case_detail.data,
                                    'testcase_id': test_case.id}
                    i += 1
                    data.append(case_details)
        return HttpResponse(json.dumps(data))


@csrf_exempt
def add_workstation(request):
    if request.method == 'POST':
        workstation = request.POST.get('workstation')
        master_id = Workstation.objects.latest('master_id').master_id + 1
        workstation_dict = {'workstation_name': workstation, 'master_id': master_id}
        Workstation.objects.create(**workstation_dict)
        return HttpResponse(json.dumps('保存成功!'))


@csrf_exempt
def add_testcase(request):
    if request.method == 'POST':
        workstation = request.POST.get('workstation')
        testcase_name = request.POST.get('testcase_name')
        test_case = Test_Case.objects.filter(testcase_name=testcase_name)
        if test_case.exists():
            return HttpResponse(json.dumps({'status': 0, 'data': '用例名已存在!'}))
        testcase_name_dict = {'workstation': workstation, 'testcase_name': testcase_name}
        Test_Case.objects.create(**testcase_name_dict)
        return HttpResponse(json.dumps({'status': 1, 'data': '保存成功!'}))


# 加载测试用例
def load_base_html(request):
    return render(request, "base.html")


# 加载用例执行
def load_testcase_html(request):
    return render(request, "testcase.html")


@csrf_exempt
def load_testcase_detail(request):
    if request.method == 'POST':
        testcase_id = request.POST.get('testcase_id')
        testcase_detail = findTestCaseDetail(testcase_id)
        return HttpResponse(json.dumps(testcase_detail))


# 加载工作站
def load_workstation(request):
    workstation_list = find_all_workstation()
    data = []
    for workstation in workstation_list:
        data.append(workstation)
    return HttpResponse(json.dumps({'workstation': data}))


# 加载用例下拉框
def load_testcase_combobox(request):
    if request.method == 'GET':
        action_list = findTestCaseCombobox()
        return HttpResponse(json.dumps(action_list))


# 加载action下拉框
def load_action(request):
    if request.method == 'GET':
        workstation = request.GET.get('workstation')
        print(workstation)
        action_list = findAction(workstation)
        return HttpResponse(json.dumps(action_list))


@csrf_exempt
def addTestCaseDetail(request):
    if request.method == 'POST':
        testcase_name = request.POST.get('testcase_name')
        testcase_id = request.POST.get('testcase_id')
        workstation = request.POST.get('workstation')
        action = request.POST.get('action')
        runtime = request.POST.get('runtime')
        sheet_name = request.POST.get('sheet_name')
        get_value_way = request.POST.get('get_value_way')
        iscache = request.POST.get('iscache')
        data = request.POST.get('data')
        testcase_num = request.POST.get('testcase_num')
        testcase_detail_dict = {'testcase_name': testcase_name, 'workstation': workstation, 'action': action,
                                'runtime': runtime, 'testcase_id': testcase_id,
                                'sheet_name': sheet_name, 'get_value_way': get_value_way, 'iscache': iscache,
                                'data': data, 'testcase_num': testcase_num}
        Test_Case_Detail.objects.create(**testcase_detail_dict)
        return HttpResponse(json.dumps('保存成功!'))


@csrf_exempt
def updateTestCaseDetail(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        testcase_num = request.POST.get('testcase_num')
        testcase_detail = Test_Case_Detail.objects.get(test_case_detail=id)
        testcase_detail.testcase_id = request.POST.get('testcase_id')
        testcase_detail.testcase_name = request.POST.get('testcase_name')
        testcase_detail.workstation = request.POST.get('workstation')
        testcase_detail.action = request.POST.get('action')
        testcase_detail.runtime = request.POST.get('runtime')
        testcase_detail.sheet_name = request.POST.get('sheet_name')
        testcase_detail.get_value_way = request.POST.get('get_value_way')
        testcase_detail.iscache = request.POST.get('iscache')
        testcase_detail.testcase_num = testcase_num
        if int(testcase_num) == 1:
            Test_Case_Detail.objects.filter(testcase_id=request.POST.get('testcase_id')).update(
                data=request.POST.get('data'))
            testcase_detail.data = request.POST.get('data')
            testcase_detail.save()
        else:
            testcase_detail.save()
        return HttpResponse(json.dumps('修改成功!'))


@csrf_exempt
def deleteTestCaseDetail(request):
    if request.method == "POST":
        id = request.POST.get('id')
        testcase_id = Test_Case_Detail.objects.get(test_case_detail_id=id).testcase_id
        case_detail = Case_Detail.objects.filter(testcase_id=testcase_id)
        if case_detail.exists():
            return HttpResponse(json.dumps({'status': 0, 'message': '请先删除执行用例!'}))
        Test_Case_Detail.objects.get(test_case_detail_id=id).delete()
        return HttpResponse(json.dumps({'status': 1, 'message': '删除成功!'}))


@csrf_exempt
def updateWorkstation(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        workstation_name = request.POST.get('workstation_name')
        # 判断工作站是否存在
        try:
            work = Workstation.objects.get(workstation_name=workstation_name)
            return HttpResponse(json.dumps({'status': 0, 'message': '工作站已存在!'}))
        except Exception as e:
            workstation = Workstation.objects.get(id=id)
            workstation.workstation_name = workstation_name
            workstation.save()
            return HttpResponse(json.dumps({'status': 1, 'message': '修改成功!'}))


@csrf_exempt
def updateTestCase(request):
    try:
        if request.method == 'POST':
            id = request.POST.get('id')
            testcase_name = request.POST.get('testcase_name')
            testcase = Test_Case.objects.filter(id=id)
            # 判断用户名是否存在
            test = Test_Case.objects.filter(testcase_name=testcase_name)
            if testcase.exists() and not test.exists():
                testcase.testcase_name = testcase_name
                testcase.save()
            else:
                return HttpResponse(json.dumps({'status': 0, 'message': '用例名已存在!'}))
            return HttpResponse(json.dumps({'status': 1, 'message': '修改成功!'}))
    except Exception as e:
        return HttpResponse(json.dumps({'status': 0, 'message': e}))


@csrf_exempt
def deleteWorkstation(request):
    if request.method == "POST":
        workstation = Workstation.objects.get(id=request.POST.get('id'))
        workstation.delete()
        return HttpResponse(json.dumps('工作站删除成功!'))


@csrf_exempt
def deleteTestCase(request):
    if request.method == "POST":
        testcase_detail = Test_Case_Detail.objects.filter(testcase_id=request.POST.get('id'))
        if testcase_detail.exists():
            testcase_detail.delete()
        testcase = Test_Case.objects.get(id=request.POST.get('id'))
        testcase.delete()
        return HttpResponse(json.dumps('用例删除成功!'))


# 用例上移
@csrf_exempt
def moveUp(requet):
    if requet.method == "POST":
        testcase_detail = Test_Case_Detail.objects.get(test_case_detail_id=requet.POST.get('id'))
        up_testcase_detail = Test_Case_Detail.objects.get(test_case_detail_id=requet.POST.get('up_id'))
        testcase_detail.testcase_num = requet.POST.get('up_testcase_num')
        up_testcase_detail.testcase_num = requet.POST.get('testcase_num')
        testcase_detail.save()
        up_testcase_detail.save()
        return HttpResponse(json.dumps('上移成功!'))


# 用例下移
@csrf_exempt
def moveDown(requet):
    if requet.method == "POST":
        testcase_detail = Test_Case_Detail.objects.get(test_case_detail_id=requet.POST.get('id'))
        down_testcase_detail = Test_Case_Detail.objects.get(test_case_detail_id=requet.POST.get('down_id'))
        testcase_detail.testcase_num = requet.POST.get('down_testcase_num')
        down_testcase_detail.testcase_num = requet.POST.get('testcase_num')
        testcase_detail.save()
        down_testcase_detail.save()
        return HttpResponse(json.dumps('下移成功!'))


# 添加执行用例
@csrf_exempt
def addCaseDetail(request):
    try:
        if request.method == "POST":
            data = request.POST.getlist('data')
            case_id = request.POST.get('case_id')
            case_details = eval(data[0])
            for case_detail in case_details:
                case = Case_Detail.objects.filter(testcase_id=case_detail['testcase_id'])
                if not case.exists():
                    case_detail['case_id'] = case_id
                    Case_Detail.objects.create(**case_detail)
                else:
                    return HttpResponse(json.dumps({'status': 0, 'message': '%s用例已存在!' % case_detail['case_name']}))
            return HttpResponse(json.dumps({'status': 1, 'message': '保存成功!'}))

    except Exception as e:
        return HttpResponse(json.dumps({'status': '0', 'message': e}))


# 删除执行用例的用例
@csrf_exempt
def deleteCaseDetail(request):
    if request.method == 'POST':
        # 获取要删除的所有id
        print(request.POST.getlist('data')[0])
        print(type(eval(request.POST.getlist('data')[0])))
        ids = eval(request.POST.getlist('data')[0])
        for id in ids:
            case_detail = Case_Detail.objects.filter(id=id)
            if case_detail.exists():
                case_detail.delete()
            else:
                return HttpResponse(json.dumps({'status': 0, 'message': '不存在该用例!'}))
        return HttpResponse(json.dumps({'status': 1, 'message': '用例删除成功!'}))


# 执行用例入口
def action(request):
    try:
        if 'HTTP_X_FORWARDED_FOR' in request.META:
            ip = request.META['HTTP_X_FORWARDED_FOR']
        else:
            ip = request.META['REMOTE_ADDR']
        print(ip)
        id = request.GET.get('id')
        list_action = findTestCaseAction(id)
        print(list_action)
        testRegMaanger = test_main.testRegManager(list_action, ip)
        testRegMaanger.iterator()
    except Exception as e:
        return HttpResponse(json.dumps(e))


@csrf_exempt
# 添加执行用例
def addCase(request):
    if request.method == "POST":
        # 获取执行用例名
        name = request.POST.get('name')
        case = Case.objects.filter(name=name)
        if case.exists():
            return HttpResponse(json.dumps({'status': 0, 'message': '用例名已存在!'}))
        Case.objects.create(**{'name': name})
        return HttpResponse(json.dumps({'status': 1, 'message': '用例添加成功!'}))


# 上传文件
@csrf_exempt
def upLoadFile(request):
    try:
        if request.method == "POST":
            testcase_id = request.POST.get('testcase_id')
            data = Data.objects.filter(testcase_id=testcase_id)
            file = request.FILES.get('file')
            file_name = None
            if data.exists():
                # 如果测试用例存在excel数据，则进行覆盖操作
                file_name = data.first().test_data_name
            else:
                data_list = {'testcase_id': testcase_id, 'test_data_name': file.name}
                Data.objects.create(**data_list)
                file_name = file.name
            f = open(os.path.join(r"C:\Users\Administrator\PycharmProjects\untitled1\UI\file", file_name), "wb")
            for chunck in file.chunks():
                f.write(chunck)
            f.close()
            return HttpResponse("上传成功")
    except Exception as e:
        return HttpResponse("上传失败")


if __name__ == '__main__':
    list = Workstation.objects.all()
    print(list)
