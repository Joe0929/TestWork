import allure
import pytest
import yaml
#coding=utf-8


def get_datas():
    '''
    从yaml文件中获取数据
    :return: 返回数据列表
    '''
    with open("E:\Homework\Pytest\datas.yaml",encoding='utf-8') as f:  #以utf-8的形式打开yaml文件并赋予给变量f
        datas = yaml.safe_load(f)
    return datas

print(get_datas())

class TestCalaculator:

    @allure.story('测试加法运算')
    @pytest.mark.parametrize('arg1,arg2,expect',get_datas()['add']['dates'],ids=get_datas()['add']['ids'])
    def test_add(self,calculate,arg1,arg2,expect):
        assert expect == round(calculate.add(arg1,arg2),2)

    @allure.story('测试减法运算')
    @pytest.mark.parametrize('arg1,arg2,expect',get_datas()['sub']['dates'],ids=get_datas()['sub']['ids'])
    def test_sub(self,calculate,arg1,arg2,expect):
        assert expect == round(calculate.sub(arg1,arg2),2)

    @allure.story('测试乘法运算')
    @pytest.mark.parametrize('arg1,arg2,expect',get_datas()['mul']['dates'],ids=get_datas()['mul']['ids'])
    def test_mul(self,calculate,arg1,arg2,expect):
        assert expect == round(calculate.mul(arg1,arg2),2)

    @allure.story('测试除法运算')
    @pytest.mark.parametrize('arg1,arg2,expect', get_datas()['div']['dates'],ids=get_datas()['div']['ids'])
    def test_div(self,calculate,arg1,arg2,expect):
        assert expect == round(calculate.div(arg1,arg2),2)
