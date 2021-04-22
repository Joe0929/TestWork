import pytest
import yaml

from SeleniumTest.testcase.base import Base


def get_datas(self):
    '''
    从yaml文件中获取数据
    :return: 返回数据列表
    '''
    # 以utf-8的形式打开yaml文件并赋予给变量f
    with open("E:\Homework\SeleniumTest\date\datas.yaml", encoding='utf-8') as f:
        datas = yaml.safe_load(f)
    return datas


class TestCase(Base):

    @pytest.mark.parametrize('filepath', get_datas()['file path'])
    def test_import(self,filepath):
        result=self.main.goto_contact().goto_import_contact().import_contact(filepath).get_menber_list()
        assert '张三（导入）' in result

    @pytest.mark.parametrize('name,count,mobile',get_datas()['menber'])
    def test_add_menber(self,name,count,mobile):
        result=self.main.goto_contact().goto_add_menber().add_menber(name,count,mobile).get_menber_list()
        assert name in result

    @pytest.mark.parametrize('name', get_datas()['department'])
    def test_add_department(self,name):
        result=self.main.goto_contact().goto_add_department().add_department(name).get_department_list()
        assert name in result


