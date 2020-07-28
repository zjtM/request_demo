import requests
import json
import ast
import time
import openpyxl 

class TestRequests():
    '''封装get请求'''
    def get(self,**kwargs): # **kwargs 任意添加多个参数，最后以对象集合的方式输出参数;
                            # *agrs 任意添加多个参数，最后以元组的形式输出参数
        headers = kwargs.get("headers")
        url = kwargs.get("url")
        try: #异常处理 ----> 正常流程
            result = requests.get(url= url,headers=headers)
            return result
        except Exception as e:  #异常处理
            print("get请求失败，%s" %e)

    def post(self,url,**kwargs):
        data= kwargs.get("data")
        json = kwargs.get("json")
        files = kwargs.get("files")
        params= kwargs.get("params")
        try:
            result = requests.post(url=url,params=params,json=json,data=data,files=files)
            return result
        except Exception as e:
            print("pos请求错误：%s" %e)
    def run_main(self,method,**kwargs):
        if method=="get":
            result = self.get(**kwargs)
            return result
        elif method == "post":
            result =self.post(**kwargs)
            return result
        else:
            print("请求方式错误!")

if __name__ == "__main__":
    # test= TestRequests()
    # result = test.run_main('get',url='http://apis.juhe.cn/simpleWeather/query',params={'key':'331eab8f3481f37868378fcdc76cb7cd','city':'上海'})
    # print(result)
#     test = TestRequests()
#     result = test.run_main('post',url='http://172.29.129.71:8061/Manage/GrpMnt/GetMdl?AppId=WUMMS01',headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36","Cookie" : "UsrToken=; UsrSessionID=b239930788ee493590d3a4af091c9098; loginTimes=0; %7b%22id%22%3a%2210001%22%2c%22name%22%3a%22webmaster%22%2c%22pwd%22%3a%2296e79218965eb72c92a549dd5a330112%22%2c%22pwddt%22%3a%220001-01-01T00%3a00%3a00%22%2c%22tel%22%3a%2215828289537%22%2c%22brth%22%3a%220001-01-01T00%3a00%3a00%22%2c%22sex%22%3a%221%22%2c%22orgid%22%3a%221010%22%2c%22dptid%22%3a%22333%22%2c%22pstid%22%3a%221010101%22%2c%22indt%22%3a%222018-04-12T00%3a00%3a00%22%2c%22chk%22%3a%22%22%2c%22stt%22%3a0%2c%22brf%22%3a%22123%22%2c%22deleted%22%3a%22N%22%2c%22uptr%22%3a%2210001%22%2c%22uptdtt%22%3a%222020-05-15T15%3a01%3a04.217%22%2c%22erpopr%22%3a%221001%22%2c%22rptname%22%3a%22%22%2c%22CurMdl%22%3anull%2c%22MdlPwrs%22%3anull%7d; user=10001"}
# )
    # url="http://172.29.129.71:8081/Manage/GrpMnt/GetMdl?AppId=WUMMS02"
    # headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36",
    # "Cookie" : "UsrToken=; UsrSessionID=cd350081d4d74b6c9e6811cdbe05890e; loginTimes=0; %7b%22id%22%3a%2210001%22%2c%22name%22%3a%22webmaster%22%2c%22pwd%22%3a%2296e79218965eb72c92a549dd5a330112%22%2c%22pwddt%22%3a%220001-01-01T00%3a00%3a00%22%2c%22tel%22%3a%2215828289537%22%2c%22brth%22%3a%222020-05-16T00%3a00%3a00%22%2c%22sex%22%3a%221%22%2c%22orgid%22%3a%220000%22%2c%22dptid%22%3a%22111%22%2c%22pstid%22%3a%22111%22%2c%22indt%22%3a%222020-05-11T00%3a00%3a00%22%2c%22chk%22%3a%22%22%2c%22stt%22%3a0%2c%22brf%22%3a%22123%22%2c%22deleted%22%3a%22N%22%2c%22uptr%22%3a%2210001%22%2c%22uptdtt%22%3a%222020-05-18T14%3a21%3a46.910484%22%2c%22erpopr%22%3a%221001%22%2c%22rptname%22%3a%22%22%2c%22CurMdl%22%3anull%2c%22MdlPwrs%22%3anull%7d; user=10001"}
    # response = requests.get(url, headers = headers )

    # with open("./911.txt", "w", encoding='utf-8') as f:
    #     f.write(response.text)
    #     f.close()


    # with open('911.txt', 'r', encoding='UTF-8') as f:
    #     load_dict = json.load(f)
    # newArr = load_dict[:]
    # for i in load_dict:
    #     if i['DataNode'] == "Add":
    #         newArr.remove(i)
    #     elif i['DataNode'] == "Edit":
    #         newArr.remove(i)
    #     elif i['DataNode'] == "Save":
    #         newArr.remove(i)
    #     elif i['DataNode'] == "Del":
    #         newArr.remove(i)
    #     elif i['DataNode'] == "Voided":
    #         newArr.remove(i)
    #     elif i['DataNode'] == "Prss":
    #         newArr.remove(i)
    #     elif i['DataNode'] == "EditPwd":
    #         newArr.remove(i)
    #     elif i['DataNode']:
    #         del i['DataNode']
    #         del i['open']
    #         del i['iconClose']
    #         del i['iconOpen']
    #         del i['SysID']
    #         del i['isParent']
    #         del i['url']
    #         del i['checked']
    #         del i['pId']
    # print(newArr)

    excel = openpyxl.load_workbook(r'C:\Users\Administrator\Desktop\文档\工作报告.xlsx')
    sheet = excel.get_sheet_by_name('Sheet2')
    print(list(sheet.values))
    
