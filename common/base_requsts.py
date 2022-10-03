import configparser

import requests


# 封装请求方法
class BaseRequest:
    # 只要用到这个类 就会进入到init这个函数中 记录用户的会话操作
    def __init__(self):
        self.session = requests.Session()
        con = configparser.ConfigParser()
        con.read('../config/env.ini')
        self.baseurl = con.get('tx-openapi', 'url')
    # 封装请求 method: post get put 等
    # 请求地址  url :不同的接口
    # 接口参数   不同的参数
    # 参数类型
    # 请求头 headers 数据类型等 不定 **kwargs
    def send_request(self, method, url, param_type, data, **kwargs):
        # 请求方式转成大写
        method = method.upper()
        # 参数类型转成大写
        param_type = param_type.upper()
        if method == 'GET':
            resp = self.session.request(method=method, url=url, params=data, **kwargs)
        elif method == "POST":
            if param_type == 'FROM':
                resp = self.session.request(method=method, url=self.baseurl+url, data=data, **kwargs)
            else:
                resp = self.session.request(method=method, url=self.baseurl+url, json=data, **kwargs)
        elif method == 'PUT':
            if param_type == 'FROM':
                resp = self.session.request(method=method, url=url, data=data, **kwargs)
            else:
                resp = self.session.request(method=method, url=url, json=data, **kwargs)
        else:
            print('检查你的请求内容')
        return resp

    def close_session(self):
        self.session.close()
if __name__ == '__main__':
    b=BaseRequest()
    b.send_request()