# -*- coding:utf-8 -*-
from selenium import webdriver

def login(self,username,password):
    driver = self.driver
    driver.find_element_by_id("freename").send_keys(username)
    driver.find_element_by_id("freepassword").send_keys(password)
    driver.find_element_by_link_text(u"登录").click()

def exit(self):
    driver = self.driver
    driver.find_element_by_link_text(u"[退出]").click()


def chrome(headless=False):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-gpu')
    if headless is True:
        chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    return driver
