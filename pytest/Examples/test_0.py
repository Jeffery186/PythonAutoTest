import pytest


def setup():
    print('用例执行之前做的事情，打开浏览器')


class TestCase:

    # 测流程
    def setup_class(self):
        print('类的前置条件，打开浏览器')

    def teardown_class(self):
        print('类的后置条件')

    # 测浏览器

    def teardown(self):
        print('用例执行之后的事情')

    # 一条用例代表一个test方法
    # @pytest.mark.smoke # 指定执行用例
    # @pytest.mark.run(order=3) #指定用例执行顺序
    def test_01(self):
        print('第一条用例')
        assert 1 == '1'

    # @pytest.mark.run(order=1)
    def test_02(self):
        print('第二条用例')
        assert 1 == 1

    # @pytest.mark.run(order=2)
    def test_03(self):
        print('第三条用例')
        assert 1 == 2


# 执行
if __name__ == '__main__':
    pytest.main(['-s', '-v', '-m','smoke','test_0.py']) # -m 指定执行用例
