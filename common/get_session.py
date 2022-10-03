import configparser

import  requests

from common.base_requsts import BaseRequest


class Getsession():
    def __init__(self):
        #初始化  获取env.ini配置文件 取出获取token需要的密钥
        self.baserequest=BaseRequest()
        conf=configparser.ConfigParser()
        conf.read('../config/env.ini',encoding='utf-8')
        self.clinetid=conf.get('tx-openapi',"clientId")
        self.clientsecret=conf.get('tx-openapi','clientSecret')
        # self.url=conf.get('tx-openapi','url')
    def get_session(self):
        #
        url='/auth/v1/access_token/token'
        data={
            "clientId": self.clinetid, "clientSecret":self.clientsecret
        }
        resp=self.baserequest.send_request(method='post',url=url,param_type='json',data=data)
        token=resp.json()['data']['accessToken']
        print('获取的token：{}'.format(token))
        return token
if __name__ == '__main__':
    t=Getsession()
    t.get_session()