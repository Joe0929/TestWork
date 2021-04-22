from time import sleep
from selenium.webdriver.common.by import By
from SeleniumTest.page.base_page import BasePage


class ContactPage(BasePage):
    '''
    通讯录页面
    '''

    def goto_add_menber(self):
        '''
        通过点击跳转到添加成员界面
        :return: 添加成员页面对象
        '''
        from SeleniumTest.page.add_menber_page import AddMenberPage
        sleep(5)
        self.find(By.XPATH,'//*[@class="ww_operationBar"]/a[1]').click()
        return AddMenberPage(self._driver)

    def goto_add_department(self):
        '''
        通过点击跳转到添加部门界面
        :return: 添加部门页面对象
        '''
        from SeleniumTest.page.add_department_page import AddDepartmentPage
        sleep(5)
        self.find(By.CSS_SELECTOR,'.js_add_sub_party').click()
        return AddDepartmentPage(self._driver)

    def goto_import_contact(self):
        '''
        通过点击跳转到导入通讯录页面
        :return: 导入通讯录页面对象
        '''
        from SeleniumTest.page.import_contact import ImportContactPage
        sleep(5)
        self.find(By.XPATH,'//*[@class="ww_operationBar"]/div[2]').click()
        self.find(By.LINK_TEXT,"文件导入").click()
        return ImportContactPage(self._driver)

    def get_menber_list(self):
        '''
        获取成员姓名列表
        :return: 包含所有成员姓名的列表
        '''
        sleep(2) #防止渲染导致无法查找到元素
        ele_list=self._driver.find_elements(By.CSS_SELECTOR,'.member_colRight_memberTable_td:nth-child(2)')
        name_list=[]
        for i in ele_list:
            name_list.append(i.text)
        return name_list

    def get_department_list(self):
        '''
        获取部门列表
        :return: 包含所有部门姓名的列表
        '''
        sleep(2) #防止渲染导致无法查找到元素
        ele_list=self._driver.find_elements(By.CSS_SELECTOR,'.jstree-anchor')
        department_list=[]
        for i in ele_list:
            department_list.append(i.text)
        return department_list