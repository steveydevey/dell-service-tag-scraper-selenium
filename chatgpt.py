#!/bin/env python
# dumb script to scrape service tags from dell's site

import time # can I just get rid of this?
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

servicetag = 'J5F09R1'
start_url = 'http://www.dell.com/support/home/us/en/04/product-support/servicetag/@/overview'
base_url = 'http://www.dell.com/support/home/us/en/04/product-support/servicetag/@/research'
real_url = base_url.replace('@', servicetag)
outer_div_id = 'ps-inlineWarranty'


driver = webdriver.Firefox()
driver.get(start_url)

print("I tried to grab the first url")

time.sleep(31)
print("now i'm waiting")

driver.get(real_url)
print("trying the second url")

elem = driver.find_element("css selector", outer_div_id)

print(elem.contents)

driver.close()

