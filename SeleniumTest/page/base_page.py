import shelve

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class BasePage():
    '''
    基本页，封装页面的基本属性
    '''
    _base_url="" #初始化网址
    def __init__(self,driver:webdriver=None):
        '''

        :param driver:
        '''
        self._driver=""
        #初始化webdriver.Chrome()对象
        if driver is None:
            self._driver=webdriver.Chrome()
            self._driver.implicitly_wait(5)
        else:
            self._driver=driver

        #当有网址重写不为空时，打开网站
        if self._base_url!="":
            self._driver.get(self._base_url)
            # 调用Shelve储存的cookies，跳过企业微信的登入
            db = shelve.open('../date/cookies.db')
            cookies = db['cookie']
            for cookie in cookies:
                if 'expiry' in cookie:
                    cookie.pop('expiry')
                self._driver.add_cookie(cookie)
            self._driver.get(self._base_url)

    def find(self,by,locator):
        '''
        封装查找元素的方法
        '''
        return self._driver.find_element(by,locator)