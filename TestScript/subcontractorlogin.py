#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      suresh.kumar
#
# Created:     25-08-2016
# Copyright:   (c) suresh.kumar 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import unittest
import sys
import time
import os
import traceback
from selenium.webdriver.support.ui import WebDriverWait
dir_path = os.path.dirname(os.path.realpath(__file__))
folder_path=os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0,folder_path+"\Library")
sys.path.insert(0,folder_path+"\Syslibrary")
sys.path.insert(0,folder_path+"\Data")
sys.path.insert(0,folder_path+"\Object")
from launcheTender import LauncheTenderclass
from datadriven import DataDriver
from setupenviron import setupValue
from logdriver import logvalue
logs=logvalue.logger
logclose=logvalue()
ftime = time.mktime(time.localtime())
ptime=time.strftime("%d-%m-%Y_%H%M%S", time.localtime(ftime))
#filename = 'TestCase-100003-{0}.png'.format(ptime)
tf = 'test_SubcontractorlogineTender'
filename = 'Testcase-%s.png' %(tf)
path= setupValue().screenpath
fullpath = os.path.join(path,filename)

#Test case no:100003
class Loginsubcontractor(unittest.TestCase):
    def test_SubcontractorlogineTender(self):
        try:
            browserInstance = setupValue()
            browser = browserInstance.setupfunction()
            browser.implicitly_wait(5)
            LauncheTender1 = LauncheTenderclass()
            browser = LauncheTender1.openURL(browser)
            browser.implicitly_wait(5)
            browser = LauncheTender1.subcontractorValidlogin(browser)
            browser.implicitly_wait(5)
            time.sleep(1)
            subcontractor_login = DataDriver()
            organisation_text=subcontractor_login.readfromXML(folder_path+'\Object\Object.xml','eTender','organisation-text') #organisation
            time.sleep(1)
            organisation = browser.find_element_by_link_text(organisation_text)
            #print organisation.text
            time.sleep(1)
            organisation1  = organisation.text
            time.sleep(1)
            self.assertEqual(organisation1,'GSE Civil Engineering Ltd')
            logs.info("Test Case No : 100003 Passed Successfully")
        except Exception:
            logs.error("Validation with Test Case No: 100003 failed")
            browser.save_screenshot(fullpath)
            traceback.print_exc(file=sys.stdout)
            self.fail("Test Case No: 100003 failed")
            browser.implicitly_wait(5)
        finally:
            LauncheTender1.closebrowser(browser)