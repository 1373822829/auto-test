from django.db import models

# Create your models here.
import os

class Workstation(models.Model):
    id = models.IntegerField(primary_key=True)
    workstation_name = models.CharField(max_length=255, null=True)
    master_id = models.IntegerField()

    class Meta:
        db_table = "work_station"

class Action(models.Model):
    id = models.IntegerField(primary_key=True)
    action_name = models.CharField(max_length=255,null=True)
    sheet_name = models.CharField(max_length=50)
    master_id = models.CharField(max_length=50,null=True)

    class Meta:
         db_table = "action"

class Test_Case(models.Model):
    id = models.IntegerField(primary_key=True)
    testcase_name = models.CharField(max_length=100,null=True)
    workstation = models.CharField(max_length=100,null=True)
    class Meta:
        db_table = "test_case"

class Test_Case_Detail(models.Model):
    test_case_detail_id = models.IntegerField(primary_key=True)
    testcase_id = models.IntegerField()
    testcase_num = models.IntegerField()
    testcase_name = models.CharField(max_length=50)
    workstation = models.CharField(max_length=50,null=True)
    action = models.CharField(max_length=50,null=True)
    data = models.CharField(max_length=50)
    sheet_name = models.CharField(max_length=50,null=True)
    get_value_way = models.CharField(max_length=50,null=True)
    iscache = models.IntegerField()
    runtime = models.IntegerField()

    def __unicode__(self):
        return self.testcase_num

    class Meta:
        db_table = "test_case_detail"

#测试数据表
class Data(models.Model):
    id = models.IntegerField(primary_key=True)
    test_data_name = models.CharField(max_length=255,null=True)
    testcase_id = models.IntegerField()
    class Meta:
        db_table = "data"

#执行用例明细表
class Case_Detail(models.Model):
    id = models.IntegerField(primary_key=True)
    case_name = models.CharField(max_length=255,null=True)
    case_num = models.IntegerField()
    workstation = models.CharField(max_length=255,null=True)
    data = models.CharField(max_length=255,null=True)
    case_id = models.IntegerField()
    testcase_id = models.IntegerField()
    class Meta:
        db_table = "case_detail"

#执行用例表
class Case(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255,null=True)
    class Meta:
        db_table = "case"

#用户表
class User(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=100,null=True)
    password = models.CharField(max_length=200,null=True)
    user = models.CharField(max_length=300,null=True)
    class Meta:
        db_table = "user"
