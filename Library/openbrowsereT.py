#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      suresh.kumar
#
# Created:     01-09-2016
# Copyright:   (c) suresh.kumar 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from selenium import webdriver
import time
class openbrowsereTender():
    def open_browser(self):
            browser = webdriver.Firefox()
            browser.implicitly_wait(5)
            browser.get('http://bg-etender-ui:8080/etender/#/login')
            time.sleep(2)
            assert browser.title == 'Causeway eTender'
            return browser