"""
所有获取单个节点的方法：
find_element__id
find_element__name
find_element__xpath
find_element__link_text
find_element__partial_link_text
find_element__tag_name
find_element__class_name
find_element__css_selector
"""
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
input_first = browser.find_element_by_id('q')
input_second = browser.find_element_by_css_selector('#q')
input_third = browser.find_element_by_xpath('//*[@id="q"]')
print(input_first, input_second, input_third)
browser.close()
