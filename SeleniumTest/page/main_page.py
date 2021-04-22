from selenium.webdriver.common.by import By
from SeleniumTest.page.add_menber_page import AddMenberPage
from SeleniumTest.page.base_page import BasePage
from SeleniumTest.page.contact_page import ContactPage
from SeleniumTest.page.import_contact import ImportContactPage


class MainPage(BasePage):
    '''企业微信首页'''
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"
    def goto_contact(self):
        self.find(By.ID,'menu_contacts').click()
        return ContactPage(self._driver)

    def goto_add_menber(self):
        self.find(By.CSS_SELECTOR,'.ww_indexImg_AddMember').click()
        return AddMenberPage(self._driver)