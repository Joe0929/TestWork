from selenium.webdriver.common.by import By
from SeleniumTest.page.base_page import BasePage
from SeleniumTest.page.contact_page import ContactPage


class AddMenberPage(BasePage):
    '''
    添加联系人页面
    '''
    def add_menber(self,name,count,moblie):
        '''
        在添加联系人页面完成添加联系人操作
        :param name:添加成员的名字
        :param id:添加成员的账号
        :param moblie:添加成员的电话
        :return:
        '''
        self.find(By.NAME,'username').send_keys(name)
        self.find(By.ID,"memberAdd_acctid").send_keys(count)
        self.find(By.NAME, 'mobile').send_keys(moblie)
        self.find(By.CSS_SELECTOR,'.qui_btn.ww_btn.js_btn_save').click()
        return ContactPage(self._driver)
