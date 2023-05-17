#!/bin/env python
# dumb script to scrape service tags from dell's site

from selenium                       import webdriver
from selenium.webdriver             import FirefoxOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by   import By
#from selenium.webdriver.support.ui  import WebDriverWait
#from selenium.webdriver.support     import expected_conditions as EC

# example real url http://www.dell.com/support/home/us/en/04/product-support/servicetag/JKZNHH2/research
servicetag_old   = 'J8T3ND2'
servicetag_new   = 'J5F09R1'
st_set = {'J8T3ND2', 'J5F09R1'}
dell_url         = 'https://www.dell.com/support/home/en-us'
outer_div_id     = 'ps-inlineWarranty'
outer_div_class1 = 'flex-wrap d-flex-inline align-items-center mb-1 mb-lg-0'
outer_div_class2 = 'flex-wrap'
input_box_id     = 'mh-search-input'
specs_link       = 'quicklink-sysconfig'
export_link      = 'current-config-export'

opts = FirefoxOptions()
#opts.add_argument("--headless")
#driver = webdriver.Firefox(options=opts)
driver = webdriver.Firefox()

for st in st_set:

  driver.get(dell_url)
  
  driver.implicitly_wait(10)
  
  # find the search box, clear it then type the service tag into it
  # supposedly this will bypass the bot challenge that comes up if you try to hit the result page directly
  elem = driver.find_element(By.ID, input_box_id)
  elem.clear()
  elem.send_keys(st + Keys.RETURN)
  
  driver.implicitly_wait(33)
  
  driver.find_element(By.ID, specs_link).click();
  driver.implicitly_wait(3)
  
  driver.find_element(By.ID, export_link).click();
  
  #wait = WebDriverWait(driver, 33)
  #wait.until(EC.presence_of_element_located((By.ID, outer_div_id)))
  #elem = driver.find_element_by_class_name(output_box_class)
  #driver.get(real_url)
  
  #print("i'm going to try to get the elements by class name now")
  
  myselector = 'p.warrantyExpiringLabel'
  print(st + ' ' + driver.find_element(By.CSS_SELECTOR, myselector).text)
  
