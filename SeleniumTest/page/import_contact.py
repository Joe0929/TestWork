from time import sleep

from selenium.webdriver.common.by import By

from SeleniumTest.page.base_page import BasePage
from SeleniumTest.page.contact_page import ContactPage


class ImportContactPage(BasePage):
    '''
    导入成员页面
    '''
    def import_contact(self,filepath):
        '''

        :param filepath: 需要导入的文件地址
        :return: 通讯录页面对象
        '''
        sleep(2)
        self.find(By.ID,'js_upload_file_input').send_keys(filepath)
        self.find(By.ID,'submit_csv').click()
        self.find(By.ID,'reloadContact').click()
        return ContactPage(self._driver)
