import unittest
from selenium import webdriver
from time import sleep

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()

    def setUp(self):
        url = "http://127.0.0.1/zentao/user-login-L3plbnRhby9teS5odG1s.html"
        self.driver.get(url)
        sleep(3)

    def get_login_username(self):
        try:
            text = self.driver.find_elements_by_css_selector('#userMenu>a')
            return text
        except:
            return ""

    def is_alter(self):
        try:
             alter = self.driver.switch_to.alert
             # text = alter.text
             # 点击确定
             alter.accept()
             # 点击取消
             # alter.dismiss()
             return True
        except:
            pass



    def test_01(self):
        self.driver.find_element_by_id('account').send_keys('admin')
        self.driver.find_element_by_name('password').send_keys('123456')
        self.driver.find_element_by_id('submit').click()

        # 判断是否登录成功
        sleep(4)
        text = self.get_login_username()
        print(text)
        self.assertEquals

    def test_02(self):
        self.driver.find_element_by_id('account').send_keys('admin1')
        self.driver.find_element_by_name('password').send_keys('1234567')
        self.driver.find_element_by_id('submit').click()

        # 判断是否登录成功
        sleep(4)
        text = self.get_login_username()
        print(text)
        self.assertTrue(text == "")


    def tearDown(self):
        # 调用alter弹窗
        self.is_alter()
        # 清除cookies信息
        self.driver.delete_all_cookies()
        #刷新浏览器
        self.driver.refresh()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()