
# -*- coding:utf-8 -*-


import unittest
import HTMLTestRunner,sys



#测试用例



class MyTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass


    def testCase1(self):
        self.assertEqual(2,2,"testError")


    def testCase2(self):
        self.assertEqual(2,3,"testError")


#添加Suite

def Suite():
    suiteTest = unittest.TestSuite()
    suiteTest.addTest(MyTestCase("testCase1"))
    suiteTest.addTest(MyTestCase("testCase2"))
    return suiteTest


if __name__ == '__main__':
    #确定生成报告的路径
    filePath = "//Users//Mr_Chen//Desktop//PythonWork//pyResult.html"
    fp = open(filePath,'wb')

    #生成报告的Title,描述
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='Python Test Report',description='This  is Python  Report')
    runner.run(Suite())

