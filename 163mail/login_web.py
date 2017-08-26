# -*- coding:utf-8 -*-

from selenium import webdriver
from info import userinfo
from public import basic
import time

class login_exit():

    def __init__(self, url):

        self.url = url
        self.driver = webdriver.Chrome()

    def login_sina(self):
        name, password = userinfo.xinlangmail()
        driver = self.driver
        driver.get(self.url)
        time.sleep(1)
        basic.login(self, name, password)
        driver.implicitly_wait(10)
        uid = driver.find_element_by_css_selector("#greeting > span").text
        assert uid == name
        time.sleep(1)
        driver.find_element_by_class_name("wrWriteBtn").click()
        driver.implicitly_wait(10)
        driver.find_element_by_xpath('//*[@id="tr_to"]/td/ul/li/input').send_keys(name)
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="panel_left"]/form/div/table/tbody/tr[6]/td/input').send_keys("test")
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="panel_main"]/div[1]/span/span[1]/a').click()

        #basic.exit(self)
        #driver.find_element_by_link_text(u"[退出]").click()

    def stop_test(self):
        driver = self.driver
        driver.quit()





if __name__ == "__main__":
    url = "https://mail.sina.com.cn/?from=mail"
    test = login_exit(url)
    test.login_sina()
    test.stop_test()
