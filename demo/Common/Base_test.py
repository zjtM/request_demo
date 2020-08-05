import unittest
import requests
import json
import configparser
import sys
sys.path.append('..')
from Logs.log import log1
import getcwd
import os

path = getcwd.get_cwd()
config_path = os.path.join(path,'Config/config.ini')

class webRequests(unittest.TestCase):

    def get(self,url,params=None,headers=None,files=None):
        '''封装get方法，return响应码和相应内容'''
        try:
            result = requests.get(url,params=params,headers=headers,files=files)
            log1.info('请求内容：%s' %params)
            log1.info('响应码：%d' % result.status_code)
            response_json = result.json()
            log1.info('响应内容：%s' % response_json)
            return result.status_code, response_json
        except BaseException as e:
            log1.error('请求失败', exc_info=1)

    def post(self,url,data=None,headers=None,files=None):
        try:
            result = requests.post(url,data=data,headers= headers,files = files)
            log1.info('请求内容：%s' %data)
            log1.info('响应码：%d' %result.status_code)
            response_json = result.json()
            log1.info('响应体：%s' %response_json)
            return response_json,result.status_code
        except BaseException as e:
            log1.error("请求失败！", exc_info=1)

    #提交json格式时，转格式
    def post_json(self,url,data=None,headers=None):
        try:
            data = json.dumps(data).encode('utf-8')# python数据类型转化成json类型
            result = requests.post(url,data=data,headers=headers)
            log1.info('请求内容：%s' %data)
            log1.info('响应代码：%d' %result.status_code)
            response_json = result.json()
            log1.info('响应体：%s' %response_json)
            return response_json,result.status_code
        except BaseException as e:
            log1.error('请求失败！', exc_info=1)

    #提取嵌套字典里的某一项字段
    def getdict(self,dict1,obj,default=None):
        '''
            遍历字典，得到值
            dict1 需要遍历的字典
            obj 目标值
        '''
        for k,v in dict1.items(): #k --> 属性， v--> 属性值
            print("k %s" %k)
            print("v %s" %v)
            if k == obj:
                return v
            else:
                if type(v) is dict:
                    re = self.getdict(v,obj,default) #当有嵌套的字典时，嵌套的那部分重新进入到此循环遍历所有值，有目标值返回，没有返回上一个字典继续遍历。递归遍历。
                    print("re %s" %re)
                    print(default)
                    if re is not default:
                        return re

    def config_get(self,section,key,url=None):
        '''读取配置文件值，并返回'''
        config = configparser.ConfigParser()
        config.read(config_path,encoding="utf-8-sig")
        if key =='url':
            config_url = config.get(section,key)
            url = config_url + url
            log1.info('请求的url: %s' %url)
            return url
        else:
            config_get=config.get(section,key)
            return config_get

    def config_write(self, section, key = None, value = None):
        '''往配置文件写入键值对'''
        config = configparser.ConfigParser()
        config.read(config_path,encoding='utf-8-sig')
        if key is not None and value is not None: #如果键值对不为空，直接修改
            config.set(section,key,value)
            with open(config_path,'w',encoding='utf-8') as f:
                config.write(f)
        else:
            config.add_section(section) #如果没有section 先设置section 在设置值
            with open(config_path,'w',encoding='utf-8') as f:
                config.write(f)
            
    def config_delete(self,section,key=None,value=None):
        #删除配置文件中的section
        config = configparser.ConfigParser()
        config.read(config_path,encoding='utf-8-sig')
        if key is not None:
            config.remove_option(section,key)
            with open(config_path,'w',encoding='utf-8') as f:
                config.write(f)
        else:
            config.remove_section(section)
            with open(config_path,'w',encoding='utf-8') as f:
                config.write(f)

    def config_options(self,section):
        #读取section下的所有键
        config = configparser.ConfigParser()
        config.read(config_path,encoding='utf-8-sig')
        username = config.options(section)
        return username

    def config_addkey(self,user):
        '''遍历获得配置文件收件人email'''
        sum = 0
        L = []
        for i in user:
            if sum < len(user):
                emails = self.config_get('addressed', i)
                L.append(emails)
                sum += 1
        return L