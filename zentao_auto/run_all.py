#coding:utf-8
import HTMLTestRunner
import time
import unittest

casePath = 'D:\\Program Files\\web_auto\\zentao_auto\\case'
rule = "test*.py"

discover = unittest.defaultTestLoader.discover(start_dir=casePath,pattern=rule)
print(discover)

# new_time = time.strftime("%Y-%m-%d %H-%M-%S")

reportPath = 'D:\\Program Files\web_auto\\zentao_auto\\report'+" result.html"
fp = open(reportPath, "wb")
runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='Login',description='test zeotao',retry=1)

runner.run(discover)
fp.close()