import unittest,time, os
from HTMLTestRunner import HTMLTestRunner
import UI.common_th_supcom_config.url_config as config


dir = config.dir
print(dir)
report_dir = os.path.join(dir, "test_report")
print(report_dir)

test_dir=report_dir
discover=unittest.defaultTestLoader.discover(test_dir,pattern='test_*.py')

# suite = unittest.TestSuite()
# suite.addTests(unittest.TestLoader().loadTestsFromTestCase())

if __name__=='__main__':
    now=time.strftime("%Y-%m-%d %H-%M-%S")
    filename=test_dir+'/'+now+'result.html'
    fp=open(filename,'wb')
    runner=HTMLTestRunner(stream=fp,title='测试报告',description='环境:windows 7 浏览器:chrome')
    runner.run(discover)
    fp.close()
    

