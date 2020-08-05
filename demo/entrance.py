import Test_Case.test_weather
import Common.my_email

import unittest
import HTMLTestRunnerCN
import os
import getcwd

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(Test_Case.test_weather.weather('test_weather'))
    path = getcwd.get_cwd()
    file_path = os.path.join(path,'report/测试报告.html')
    fp = open(file_path,'wb')
    runner = HTMLTestRunnerCN.HTMLTestReportCN(
        stream= fp,
        title='测试报告',
        description='描述'
    )
    runner.run(suite)
    fp.close()

    Common.my_email.mail()