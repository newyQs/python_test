"""
所有获取多个节点的方法：
find_elements__id
find_elements__name
find_elements__xpath
find_elements__link_text
find_elements__partial_link_text
find_elements__tag_name
find_elements__class_name
find_elements__css_selector
"""
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
lis = browser.find_elements_by_css_selector('.service-bd li')
# lis = browser.find_elements(By.CSS_SELECTOR, '.service-bd li')
print(lis)
browser.close()
