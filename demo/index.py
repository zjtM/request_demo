import requests
import re
import pymysql
from  axios import TestRequests  #导入模块
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys # 键盘事件
from selenium.webdriver.support.select import Select #下拉框选择
from selenium.webdriver.common.action_chains import ActionChains  #鼠标行为事件
# #连接数据库 需要得参数 host port user passwd db charset
# db = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='pydemodoutula', charset='utf8')

# cursor = db.cursor()  #数据库指针
# cursor.execute('select * from imgs') 
# print(cursor.fetchall())

# def getImagesList():
#     html = requests.get('http://www.doutula.com/photo/list/?page=3').text
#     #print(html)
#     reg = r'data-original="(.*?)".*? alt="(.*?)"'
#     reg = re.compile(reg, re.S)  # S 多行匹配  re 正则表达式
#     imageList = re.findall(reg, html)  # re.findall() 正则全文匹配  参数 (规则，匹配地址)
#     #print(imageList)

#     for i in imageList:
#         #print(i)
#         img_url = i[0]
#         img_title = i[1]
#         #print(img_title)
#         cursor.execute('insert into imgs (title,url) values ("{}","{}")'.format(img_title, img_url))
#         db.commit()

# getImagesList()
if __name__ == "__main__":  # 主程序入口
    # html = TestRequests()
    # print(html)
    # time.sleep(3)
    # result = html.run_main('post',url='http://wcrmmanagement.weixin.wuerp.com/Basics/CpnVip/SlecetCpnVippagingInfo',dtGridPager={"errorMsg":"","isExport":"false","pageSize":20,"startRecord":0,"nowPage":1,"recordCount":-1,"pageCount":-1,"parameters":{},"fastQueryParameters":{},"advanceQueryConditions":[],"advanceQuerySorts":[]})

    # print(result.status_code)
    # data = result.json()
    # print(data)
    # link = r'href=".*?"'
    # link = re.compile(link, re.S)
    # links = re.findall(link, result)
    # print(links)

    # for i in links:
    #     print(i)
    
    # driver = webdriver.Chrome()
    # driver.get("http://www.python.org")
    # assert "Python" in driver.title         #assert 断言
    # elem = driver.find_element_by_name("q")
    # print(elem)
    # elem.send_keys("pycon")
    # elem.send_keys(Keys.RETURN)
    # assert "No results found." not in driver.page_source

    # driver = webdriver.Chrome()
    # driver.get('http://127.0.0.1:5500/index.html')
    # elem = driver.find_element_by_id('kw') #找到id为kw的标签
    # elem.send_keys('Keys键盘事件') #向kw的标签中添加文本
    # btn = driver.find_element_by_tag_name('button')
    # btn.click() #按钮点击事件
    # elem.send_keys(Keys.RETURN) #Key.RETURN ----> 回车键
    # ipt = driver.find_elements_by_tag_name("input")
    # print(ipt)
    # sel = Select(driver.find_element_by_id("s1Id"))
    # for i in sel.options: #拿到的select为一个数组
    #     print(i.get_attribute("index"))
    #     item = i.get_attribute("index")
    #     btn.click()
    #     ipt[item+1].get_attribute("value")

        #print(select.text)
        #sel.select_by_index[]
        #print(select.index)
        #print(select.value)
    #sel.select_by_index(0)  #select 的三种选择方法 index，value visible_text
    #sel.select_by_value("殷桃")
    #sel.select_by_visible_text("橘子")


    #driver.quit()

    driver = webdriver.Chrome()
    driver.implicitly_wait(10) #隐式等待 全局等待10秒 
    #time.sleep(5) #显式等待，指定元素强制等待5秒
    driver.get('http://wcrmmanagement.weixin.wuerp.com/Login/Index')
    user = driver.find_element_by_id('user')
    user.send_keys('miscs3')
    psw = driver.find_element_by_id('psw')
    psw.send_keys('111111')
    code = driver.find_element_by_id('code')
    code.send_keys('1111')
    btn_log = driver.find_element_by_id('btn-log')
    btn_log.click()
    #windows = driver.window_handles
    #driver.switch_to.window(windows[-1])
    #driver.get('http://wcrmmanagement.weixin.wuerp.com/Index/Index')
    nav = driver.find_element_by_css_selector('#nav li:nth-child(3)')
    action = ActionChains(driver) #定义ActionChains
    action.move_to_element(nav).click(nav).perform() #鼠标移动到指定的元素上并点击
    vipRegister = driver.find_elements_by_css_selector('#nav li:nth-child(3) dl dd') #找出来是个伪数组
    print(vipRegister)
    action.move_to_element(vipRegister[0]).click().perform()

    #driver.quit()    

