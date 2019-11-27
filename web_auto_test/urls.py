"""untitled1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url

from blog import views,tests
urlpatterns = [
    # url(r'^', views.login),
    url(r'^login/', views.login),
    url(r'^action/', views.action),
    url(r'^index/', views.index),
    url(r'^add_workstation/', views.add_workstation),
    url(r'^add_testcase/', views.add_testcase),
    url(r'^tabs/',views.load_base_html),
    url(r'^tab/',views.load_testcase_html),
    url(r'^testcase_detail/',views.load_testcase_detail),
    url(r'^load_workstation/',views.load_workstation),
    url(r'^load_action/',views.load_action),
    url(r'^addTestCaseDetail/',views.addTestCaseDetail),
    url(r'^updateTestCaseDetail/',views.updateTestCaseDetail),
    url(r'^deleteTestCaseDetail/',views.deleteTestCaseDetail),
    url(r'^updateWorkstation/',views.updateWorkstation),
    url(r'^updateTestCase/',views.updateTestCase),
    url(r'^deleteWorkstation/',views.deleteWorkstation),
    url(r'^deleteTestCase/',views.deleteTestCase),
    url(r'^moveUp/',views.moveUp),
    url(r'^moveDown/',views.moveDown),
    #上传文件
    url(r'^upLoadFile/',views.upLoadFile),
    #加载执行用例明细
    url(r'^case_detail/',views.load_case_detail),
    #加载所有的执行用例明细
    url(r'^case_details/',views.load_case_details),
    #加载用例下拉框
    url(r'^testcase_combobox/',views.load_testcase_combobox),
    #添加用例
    url(r'^addCaseDetail/',views.addCaseDetail),
    #删除用例
    url(r'^deleteCaseDetail/', views.deleteCaseDetail),
    #添加执行用例
    url(r'^addCase/', views.addCase),

]
