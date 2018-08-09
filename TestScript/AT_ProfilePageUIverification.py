#-------------------------------------------------------------------------------
# Name:          AT_ProfilePageUIverification.py
#
# Tast Case Id  100097
#
# Purpose:      To Verify that new role can be added with user
#
# Author:      mathew.jacob
#
# Created:     21/11/2016
# Copyright:   (c) Causeway Technologies 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from selenium.webdriver.support.ui import WebDriverWait
import unittest
import sys
import os
import time
import traceback
dir_path = os.path.dirname(os.path.realpath(__file__))
folder_path=os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0,folder_path+"\Library")
sys.path.insert(0,folder_path+"\Env")
from launcheTender import LauncheTenderclass
from setupenviron import setupValue
from logdriver import logvalue
from OrganizationFunction import Organizationclass
from datadriven import DataDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
logs=logvalue.logger
logclose=logvalue()
orgLink=DataDriver()
ftime = time.mktime(time.localtime())
ptime=time.strftime("%d-%m-%Y_%H%M%S", time.localtime(ftime))
#filename = 'TestCase-100097-{0}.png'.format(ptime)
tf = 'test_ProfileUI'
filename = 'Testcase-%s.png' %(tf)
path= setupValue().screenpath
fullpath = os.path.join(path,filename)
class ProfileOrganizationUI(unittest.TestCase):
    def test_ProfileUI(self):
        try:
            browserInstance = setupValue()
            browser = browserInstance.setupfunction()
            LauncheTender = LauncheTenderclass()
            browser = LauncheTender.openURL(browser)
            browser= LauncheTender.subcontractorValidlogin(browser)
            orgInstance=Organizationclass()
            orgInstance.OpenProfilePage(browser)
            time.sleep(3)
            self.assertTrue(browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\Object.xml','eTender','nameinProfile')))
            self.assertTrue(browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\Object.xml','eTender','phoneinProfile')))
            self.assertTrue(browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\Object.xml','eTender','webinProfile')))
            self.assertTrue(browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\Object.xml','eTender','emailinprofile')))
            self.assertTrue(browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\Object.xml','eTender','addressinprofile')))
            self.assertTrue(browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\Object.xml','eTender','countyinprofile')))
            self.assertTrue(browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\Object.xml','eTender','countryinprofile')))
            self.assertTrue(browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\Object.xml','eTender','postalinprofile')))
            logs.info("Test Case No : 100097 Passed Successfully")
        except Exception:
            logs.error("Validation with Test Case No: 100097 failed")
            browser.save_screenshot(fullpath)
            traceback.print_exc(file=sys.stdout)
            self.fail("Test Case No: 100097 failed")
            browser.implicitly_wait(5)
        finally:
            browser=LauncheTender.closebrowser(browser)
            #logclose.closeLogger()

