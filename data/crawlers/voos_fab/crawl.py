#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 23:01:27 2017

@author: lucianoviola
"""
import requests
#import argparse
import re
from selenium import webdriver
import os
import pdb
from time import sleep
from tqdm import tqdm
#from seleniumrequests import Chrome

#os.chdir('/Users/lucianoviola/projects/upperEchelon/data/crawlers/voos_fab')

# year to crawl
#YEAR = 2015
START_URL = 'http://fab.mil.br/voos'
PDF_OUTPUT = 'output/'

   
YEARS = {
     '2013':5,
     '2014':4,
     '2015':3,
     '2016':2,
     '2017':1
    }

def fetch_urls(START_URL):  
    # ADD DOCSTRING
    
    options = [1,2,3,4,5]
    chromedriver = "./chromedriver"
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chromedriver)
    driver.get(START_URL)
    urls_list = []
    sleep(1)
    option = 2
    print('fetching urls...')
    for option in options:
        print(option)
        XPATH_YEAR_SELECTOR = '//*[@id="VoosForm_ano"]/option[{}]'.format(option)
        driver.find_element_by_xpath(XPATH_YEAR_SELECTOR).click()
        driver.find_element_by_css_selector('.form-button').click()
        sleep(4)
    
        # get urls
        divs = driver.find_elements_by_css_selector('.datadia a')
        urls = [div.get_attribute('href') for div in divs]
        urls_list += urls
        sleep(3)
    print(urls_list)
    return urls_list

def download_pdfs(urls):
    # ADD DOCTSRING
    
    print('dowloading {} pdfs...'.format(len(urls)))
    pdb.set_trace()
    for pdf_url in tqdm(urls):
        #print(i,)
        #pdb.set_trace()
        response = requests.get(pdf_url)
        date  = re.search('voos\/(\d*)',pdf_url).group(1)
        with open('output/voos_{}.pdf'.format(date),'wb') as f:
            f.write(response.content)
          
if __name__ == '__main__':
    urls_list = fetch_urls(START_URL)
    download_pdfs(urls_list)
    