from Pytest.calculator import Calculator
import pytest

#
@pytest.fixture()
def calculate():
    '''
    在每条用例里加入开头，结尾
    :return: Calculator的实例对象
    '''
    print("开始计算")
    cal = Calculator()
    yield cal
    print("结束计算")


def pytest_collection_modifyitems(session,config,items):
    '''
    将测试文件中的unicode-escape编码转化为utf-8编码
    '''
    for item in items:
        item.name=item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid=item.nodeid.encode('utf-8').decode('unicode-escape')