#!/bin/env python
# dumb script to scrape service tags from dell's site

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

dell_tag_site = 'https://www.dell.com/support/home/en-us?app=products'
input_box_name = 'entry-main-input-home'
output_box_class = 'warrantyExpiringLabel mb-0 ml-1 mr-1'
servicetag = 'JKZNHH2'
base_url = 'http://www.dell.com/support/home/us/en/04/product-support/servicetag/@/research'


driver = webdriver.Firefox()
driver.get(dell_tag_site)

assert "Dell" in driver.title

# elem = driver.find_element(By.NAME, "q")
elem = driver.find_element(By.NAME, input_box_name)
elem.clear()
elem.send_keys(servicetag + Keys.RETURN)

assert "No results found." not in driver.page_source

elem = driver.find_element_by_class_name(output_box_class)

print(elem.contents)

driver.close()



