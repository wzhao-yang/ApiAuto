# coding:utf-8
import unittest
import HTMLTestRunner

from Run.run_main import RunMain

# from util.send_email import send_email

"""
HTMLTestRunner,主要便于查看生成的测试报告
下载地址：https://pypi.org/project/html-testRunner/1.0.3/
http://tungwaiyip.info/software/HTMLTestRunner.html
修改方法：
第94行，将import StringIO修改成import io
第539行，将self.outputBuffer = StringIO.StringIO()修改成self.outputBuffer = io.StringIO()
第642行，将if not rmap.has_key(cls):修改成if not cls in rmap:
第766行，将uo = o.decode('latin-1')修改成uo = e
第775行，将ue = e.decode('latin-1')修改成ue = e
第631行，将print >> sys.stderr, '\nTime Elapsed: %s' % (self.stopTime-self.startTime)修改成print(sys.stderr, '\nTime Elapsed: %s' % (self.stopTime-self.startTime))
"""


class TestMethod(unittest.TestCase):

    def setUp(self):
        self.run = RunMain()

    def test_01(self):
        RunMain.run_case(self)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestMethod('test_01'))
    file_path = '../Report/111kkkk.html'
    with open(file_path,'wb') as f:
        runner = HTMLTestRunner.HTMLTestRunner(stream=f,title="测试执行情况",description="接口自动化测试报告")
        runner.run(suite)
    f.close()
    unittest.main()

