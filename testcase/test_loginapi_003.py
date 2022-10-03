import requests
import pytest


# 定义登录方法
from common.base_requsts import BaseRequest
class TestLoginCase():
    def __init__(self):
        self.baserequest=BaseRequest()
    def test_login(self):
        # 定义测试数据
        # basereques = BaseRequest()
        url = "https://qw-openapi-tx.dustess.com/auth/v1/access_token/token"
        data = {"clientId": "cfqaExrfLXyGb", "clientSecret": "2VIAy1VxiHXh6ZB6F13gtsm38WMrn0OS"}
        # 发送请求
        res =self.baserequest.send_request(method='post',url=url,param_type='json',data=data)
        # 输出结果 取出token值
        re=res.json()['data']['accessToken']
        print(re)
        return re

l = TestLoginCase()
l.test_login()
if __name__ == '__main__':
    pytest.main(['test_loginapi_003.py'])
# # 查询工单详情
#     def check(self):
#         url = "https://qw-openapi-tx.dustess.com/work-order/api/v1/ticket/detail"
#         data1 = {"ticketId": "626a980e8d180e5d01e5e62b", "currentUserId": "498"}
#         headers = {
#             "accessToken": LoginCase.login()
#         }
#         # 发送请求
#         res = requests.post(url, headers=headers, json=data1,)
#         # 输出结果
#
#         print(res.json())
#
#
# if __name__ == "__main__":
#     L1=LoginCase
#     L1.login()
