# # 步骤1.导入包
# import requests
# # 步骤2 发送请求
# r=requests.get("http://www.baidu.com")
# # 步骤3.打印结果
# print(r)
# ===获取token
# 1.导入包
# import token
import configparser

import pytest
import requests

#
from common.base_requsts import BaseRequest
from common.get_session import Getsession


class TestWrok:


    # 函数与函数之间变量不能相互使用  则可以将变量变为全局变量 类变量 供各函数使用
    token = None
    basel = None
    # url = None
    session=None

    # 接口地址放在外层 用例执行之前 先拿到接口的项目信息 接口地址
    # 读取ini文件
    # setup 用例执行前需要做的工作
    @classmethod
    def setup_class(cls):
        # 调用封装的接口类
        TestWrok.basel = BaseRequest()
        TestWrok.session=Getsession()
    @classmethod
    def teardown_class(cls):
        print("结束")

    #查询工单详情
    def test_check(self):
        url = '/work-order/api/v1/ticket/detail'
        data1 = {"ticketId": "626a980e8d180e5d01e5e62b", "currentUserId": "498"}
        headers = {
            "accessToken":TestWrok.session.get_session()
        }
        # 发送请求

        resp = TestWrok.basel.send_request(method='post', url=url, param_type='json', data=data1, headers=headers)
        # 输出结果
        res = resp.json()['msg']
        assert res == '成功'
        print('查询工单详情执行成功')
        print(resp.json())
    #新建工单字段==名称重复用例
    def  test_work_field_add(self):
        '''
        1.获取url
        2.获取headers
        3.获取data
        4.发送请求
        :return:
        '''
        url='/work-order/api/v1/field/add'
        headers={
            'accessToken':TestWrok.session.get_session()
        }
        data={
            'name':'自动化接口字段_myf2',
            'type':'0',
            'optional':[],
            'uid':'498'
        }
        resp=TestWrok.basel.send_request(method="post",url=url,param_type='json',data=data,headers=headers)
        res=resp.json()['msg']
        assert res=='服务端错误：名称重复'
        print(resp.json())
        print("这是新建工单字段的用例")

if __name__ == "__main__":
    pytest.main(['-sv', 'testcase/test_work.py'])
