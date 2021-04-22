import shelve
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Testgetcookies():
    '''用于获取cookie'''
    def test_case(self):
        option = Options()
        option.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=option)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.driver.implicitly_wait(5)
        cookies=self.driver.get_cookies()
        with shelve.open('../date/cookies.db') as db:
            db['cookie']=cookies
        sleep(3)
        self.driver.quit()