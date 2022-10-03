# 测试文件以test_开头 或以_test结尾
# 测试类以Test开头 并且不能带有init方法  类名用大驼峰
# 测试函数以test_开头
# 断言使用assert
import configparser
import pytest
class TestPyCase:
    # 前置条件
    # def setup(self):
    #     print('用例执行之前做的事情')
    # def teardown(self):
    #     print('用例执行之后做的事情')
    # 前置条件方法2
    def setup_class(self):
        print('当前类下所有用例执行之前的做的事情')

    def teardown_class(self):
        print('当前类下所有用例执行之后做的事情')

    # 一个函数代表一条用例
    # 指定顺序去运行某一条用例
    @pytest.mark.run(order=2)
    # @pytest.mark.smoke
    def test_add(self):
        print('第一条用例')
        # 断言 判断预期结果是否相等
        assert 1 == 1
    # 指定只执行某一条冒烟用例

    @pytest.mark.run(order=1)
    def test_edit(self):
        print('第二条用例')
        assert 1 == 1
    def test_read(self):
        con=configparser.ConfigParser()
        con.read('../config/env.ini',encoding='utf-8')
        conf=con.get('tx-openapi','url')
        print(conf)



# 运行用例
# 两种方式
'''
1.终端使用命令
2.main 回车
'''
if __name__ == '__main__':
    # 输入main+回车 后在main中运行文件 可运行单个文件mian()中输入单个文件名称
    # '-s','v',让用例结果更加详细
    pytest.main(["-sv","testcase/test_pyt_002.py"])
