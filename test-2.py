#!/bin/env python
# dumb script to scrape service tags from dell's site

import time
from selenium                       import webdriver
from selenium.webdriver             import FirefoxOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by   import By
from selenium.webdriver.support.ui  import WebDriverWait
from selenium.webdriver.support     import expected_conditions as EC

# example real url http://www.dell.com/support/home/us/en/04/product-support/servicetag/JKZNHH2/research
servicetag = 'JKZNHH2'
start_url = 'http://www.dell.com/support/home/us/en/04/product-support/servicetag/@/overview'
base_url = 'http://www.dell.com/support/home/us/en/04/product-support/servicetag/@/research'
real_url = base_url.replace('@', servicetag)
outer_div_id = 'ps-inlineWarranty'

opts = FirefoxOptions()
#opts.add_argument("--headless")
#driver = webdriver.Firefox(options=opts)
print("start firefox")
driver = webdriver.Firefox()

print("wait for me to load a page")
time.sleep(10)

print("grab drive session id and executor url")
url = driver.command_executor._url       #"http://127.0.0.1:60622/hub"
session_id = driver.session_id            #'4e167f26-dc1d-4f51-a207-f761eaf73c31'

print("Use these two parameter to connect to your driver.")
driver = webdriver.Remote(command_executor=url,desired_capabilities={})
driver.session_id = session_id

print("I'm trying to grab the first url")
driver.get(real_url)

driver.implicitly_wait(33)
time.sleep(35)

driver.refresh

print("now i'm waiting")

driver.implicitly_wait(33)

#time.sleep(35)
#wait = WebDriverWait(driver, 33)
#wait.until(EC.presence_of_element_located((By.ID, outer_div_id)))

driver.refresh

#assert "Dell" in driver.title
#assert "No results found." not in driver.page_source
#elem = driver.find_element_by_class_name(output_box_class)


#print("trying the second url")
#driver.get(real_url)

print(driver.page_source)

#elem = driver.find_element("css selector", outer_div_id)
#print(elem.contents)

driver.close()

