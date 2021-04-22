from time import sleep
from selenium.webdriver.common.by import By
from SeleniumTest.page.base_page import BasePage
from SeleniumTest.page.contact_page import ContactPage


class AddDepartmentPage(BasePage):
    '''
    添加部门页面
    '''
    def add_department(self,name):
        '''
        完成添加部门操作
        :param Text: 添加部门名字
        :return: 返回通讯录页面对象
        '''
        self.find(By.NAME,'name').send_keys(name)
        self.find(By.XPATH,'//*[@class="qui_dialog_foot ww_dialog_foot"]/a[1]').click()
        sleep(2)
        self.find(By.ID,'menu_contacts').click()
        return ContactPage(self._driver)
