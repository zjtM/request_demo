from Logs.log import log1
from Common.Base_test import webRequests
# try:
#     log1.info('test')
#     r = 10/0
#     log1.info("result:",r)
# except ZeroDivisionError as e:
#     log1.error("报错信息", exc_info=1)
# log1.info("end")

# url = 'https://www.sojson.com/open/api/weather/json.shtml'
# payload = {'city':'上海'}
# s=webRequests()
# s.get(url,params=payload)

'''
response = {'errno': 0, 'msg': 'success', 'result': {'id': '5b4dc7111c0ab20001c3c481', 'cname': '测试001', 'desc': '测试机器人', 'type': 0, 'settings': {'failAction': ['偶母鸡啊', '我不告诉你']}, 'lastView': '2018-07-17T18:38:09.250849551+08:00', 'nickname': '小可爱', 'age': 0, 'gender': 'male', 'hometown': '北京', 'speciality': '打游戏'}}

s = webRequests()
r = s.getdict(response,"failAction")
print('---------')
print(r)
'''

#configparser增删改查测试
'''
section = 'login'
username = '测试'
password = '一下'
 
s = webRequests()
 
s.config_write(section)
log1.info("写入section:%s" % section)
s.config_write(section,'username',username)
log1.info("写入%s下的用户名是：%s" %(section,username))
s.config_write(section,'password',password)
log1.info("写入%s下的密码是：%s" %(section,password))
 
url = s.config_get('test','url',url='test/test1')
get_username = s.config_get(section,'username')
log1.info("读取的用户名:%s" % get_username)
get_password = s.config_get(section,'password')
log1.info("读取的密码:%s" % get_password)
 
s.config_delete(section,'usrename',)
log1.info("删除%s下的username" % section)
s.config_delete(section,'password')
log1.info("删除%s下的password" % section)
s.config_delete(section)
log1.info("删除%s" % section)
'''