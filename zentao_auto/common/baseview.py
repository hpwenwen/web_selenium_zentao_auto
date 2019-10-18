from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

class BaseView():

    def __init__(self, driver:webdriver.Firefox, timeout):
        self.driver = driver
        self.timeout = timeout

    def is_get_element(self,loc):
        element = WebDriverWait(self.driver,self.timeout).until(EC.presence_of_element_located(loc))
        return element

    def get_element(self, *loc):
        element = WebDriverWait(self.driver, self.timeout).until(lambda x: x.find_element(*loc))
        return element

    def get_elements(self,*loc):
        return WebDriverWait(self.driver, self.timeout).until(lambda x: x.find_elements(*loc))

    def isSelected(self, loc):
        sel = self.get_element(loc)
        sel.is_selected()
        return True

    def is_excption(self,loc):
        try:
            self.get_element(loc)
            return True
        except:
            return False

    def is_excption2(self, loc):
        eles = self.get_elements(loc)
        if len(eles) == '0':
            return False
        elif len(eles) == '1':
            return True
        else:
            return True

    def is_html_title(self,_title):
        """检查页面标题的期望,如果标题匹配，则返回True，否则返回false。"""
        try:
            result = WebDriverWait(self.driver,self.timeout).until(EC.title_is(_title))
            return result
        except:
            return False

    def is_text_element(self,loc,_text):
        try:
            result = WebDriverWait(self.driver,self.timeout).until(EC.text_to_be_present_in_element(loc,_text))
            return result
        except:
            return False

    def move_to_element(self,loc):
        """鼠标悬停"""
        move = self.get_element(loc)
        ActionChains(driver).move_to_element(move).perform()

    def select_element_index(self, loc, index):
        """通过索引"""
        element = self.get_element(loc)
        Select(element).select_by_index(index)

    def select_element_value(self, loc, value):
        """通过值"""
        element = self.get_element(loc)
        Select(element).select_by_value()

    def select_element_text(self, loc, text):
        """通过文本"""
        element = self.get_element(loc)
        Select(element).select_by_visible_text(text)

    def js_scroll_end(self):
        """滚动到底部"""
        js = "window.scrollTo(0, document.body.scrollHeight)"
        self.driver.execute_script(js)

    def is_focus(self, loc):
        """聚焦"""
        element = self.get_element(loc)
        self.driver.execute_script("arguments[0].scrollIntoView();",element)

    def js_scroll_top(self):
        """滚动到顶部"""
        js = "window.scrollTo(0, 0)"
        self.driver.execute_script(js)


if __name__ == '__main__':
    driver = webdriver.Firefox()
    url = "http://127.0.0.1/zentao/user-login-L3plbnRhby9teS5odG1s.html"
    driver.get(url)
    zentao = BaseView(driver,5)
    zentao.get_element(By.ID, 'account').send_keys('admin')
    zentao.get_element(By.NAME, 'password').send_keys('123456')
    zentao.get_element(By.ID, 'submit').click()

    driver.quit()