from time import sleep
import yaml
from SeleniumTest.page.main_page import MainPage



class Base():
    def setup(self):
        self.main = MainPage()

    def teardown(self):
        sleep(3)
        self.main._driver.quit()

