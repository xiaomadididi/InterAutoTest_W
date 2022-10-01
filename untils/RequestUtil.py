#创建封装get方法
import requests


def request_get(url,headers):
#发送request get 请求
    r=requests.get(url,headers=headers)
#获取结果响应内容
    code=r.status_code

#