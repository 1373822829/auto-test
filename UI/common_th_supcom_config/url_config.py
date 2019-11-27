#! /usr/bin/env python
#coding=utf-8
import getpass
import os
#portal登录地址
localhost = r'http://192.168.222.109:8080/portal/usercent'
#当前项目所在的路径
dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#制卡压缩包下载路径
download_dir = r"C:\Users\%s\Downloads"%getpass.getuser()
action_dir = dir.split("\\")[0]
#数据库连接地址
host = '192.168.222.120/ORCL'
#数据库登录地址
PCA_DB_HOST = "oracle+cx_oracle://pca:pca@"+host
PTS_DB_HOST = "oracle+cx_oracle://pts:pts@"+host
UUM_DB_HOST = "oracle+cx_oracle://uum:uum@"+host
BMS_DB_HOST = "oracle+cx_oracle://bms:bms@"+host
ISMS_DB_HOST = "oracle+cx_oracle://isms:isms@"+host
DMS_DB_HOST = "oracle+cx_oracle://dms:dms@"+host
#院区编码
HOSPITA_AREA_CODE = 'H0002'
#日志路径
log_dir= os.path.join(dir, r"temp\log\log.txt")
#打印标题
print_title = [u'将打印输出另存为',u'文件另存为']
#院区
HOSPITA_AREA = '光谷院区'
#院区code(光谷：2，中法：3)
HOSPITA_CODE = 2


