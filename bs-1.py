#!/bin/env python
# dumb script to scrape service tags from dell's site

import requests
from bs4 import BeautifulSoup

dell_tag_site = 'https://www.dell.com/support/home/en-us?app=products'
input_box_name = 'entry-main-input-home'
output_box_class = 'warrantyExpiringLabel mb-0 ml-1 mr-1'
servicetag = 'J5F09R1'
base_url = 'http://www.dell.com/support/home/us/en/04/product-support/servicetag/J5F09R1/research/'
#base_url = 'http://www.dell.com/support/home/us/en/04/product-support/servicetag/@/research'

page = requests.get(base_url)
print(page.text)

with open(page) as fp:
    soup = BeautifulSoup(fp)

#soup = BeautifulSoup("<html>data</html>")
print(soup.text)


