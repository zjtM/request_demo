import unittest
import sys
sys.path.append('..')

from Common.Base_test import webRequests
from Logs.log import log1

class weather(unittest.TestCase):

    def test_weather(self):
        '''查询天气'''
        case_name = '查询天气'
        log1.info('执行测试用例：%s' %case_name)
        try:
            weather = webRequests()
            url = weather.config_get('test','url',url='')
            #payloda = {'city':'上海'}
            status_code,response_json = weather.get(url)
            message = weather.getdict(response_json,'message')
            test1 = self.assertEqual(status_code,200)
            test2 = self.assertEqual(message,'Success !')
            print(test1)
            print(test2)
            if test1 == None and test2 == None:
                log1.info('pass')
        except BaseException as f:
            log1.error('错误: %s' % case_name, exc_info=1)
            raise