# coding:utf-8

'''
日志函数，处理脚本执行过程中的日志写入，以及错误码对照
'''
import logging, os
import ctypes

import logging
import time
import sys
import os


import UI.common_th_supcom_config.url_config as config

# ! /usr/bin/env python
# coding=gbk
import logging, os


class Logger:
    def __init__(self, path, clevel=logging.DEBUG, Flevel=logging.DEBUG):
        self.logger = logging.getLogger(path)
        self.logger.setLevel(logging.DEBUG)
        # fmt = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', '%Y-%m-%d %H:%M:%S')
        fmt = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # 设置CMD日志
        sh = logging.StreamHandler()
        sh.setFormatter(fmt)
        sh.setLevel(clevel)
        # 设置文件日志
        file_path=config.log_dir
        fh = logging.FileHandler(file_path)
        fh.setFormatter(fmt)
        fh.setLevel(Flevel)
        self.logger.addHandler(sh)
        self.logger.addHandler(fh)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warn(self, message):
        self.logger.warn(message)

    def error(self, message):
        self.logger.error(message)

    def cri(self, message):
        self.logger.critical(message)

    def exception(self, message):
        self.logger.exception(message)


if  __name__ == "__main__":
    pass
