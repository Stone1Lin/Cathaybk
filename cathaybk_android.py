#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from os import path

CUR_DIR = path.dirname(path.abspath(__file__))
APPIUM = 'http://localhost:4723'

CAPS = {
    'platformName': 'Android',
    'platformVersion': '12.0',
    'deviceName': 'Android Emulator',
    'automationName': 'UIAutomator2',
    'browserName': 'Chrome'
}

driver = webdriver.Remote(
    command_executor=APPIUM,
    desired_capabilities=CAPS
)

driver.get('https://www.cathaybk.com.tw/cathaybk/')
driver.save_screenshot("step1.png")

# 左上 menu
prod_list_elem = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "//div[@class='cubre-o-header__burger']")
    ))
prod_list_elem.click()

prod_intro_elem = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "//div[contains(text(), '產品介紹')]")
    ))
prod_intro_elem.click()

cred_card_elem = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable(
        (By.XPATH, "//div[@class='cubre-a-menuSortBtn' and contains(text(), '信用卡')]")
    ))
cred_card_elem.click()
driver.save_screenshot("step2.png")

count = len(driver.find_elements(
    By.XPATH, "//div[@class='cubre-a-menuSortBtn cubre-u-mbOnly' and contains(text(), '信用卡')]/following-sibling::a")
)

print(count)  # 共8個

driver.quit()
