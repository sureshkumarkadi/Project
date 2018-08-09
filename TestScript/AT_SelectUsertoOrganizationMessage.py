#-------------------------------------------------------------------------------
# Name:         AT_SelectUsertoOrganizationMessage
#
# Tast Case Id  100138
#
# Purpose:      To Verify that user friendly message shows while adding user to organization without selecting any user
#
# Author:      mathew.jacob
#
# Created:     13/10/2016
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
orgLink=DataDriver()
ftime = time.mktime(time.localtime())
ptime=time.strftime("%d-%m-%Y_%H%M%S", time.localtime(ftime))
#filename = 'TestCase-100138-{0}.png'.format(ptime)
tf = 'test_messageforAddUser'
filename = 'Testcase-%s.png' %(tf)
path= setupValue().screenpath
fullpath = os.path.join(path,filename)

class SelectUserMessage(unittest.TestCase):
      def test_messageforAddUser(self):
        try:
            browserInstance = setupValue()
            browser = browserInstance.setupfunction()
            LauncheTender = LauncheTenderclass()
            browser = LauncheTender.openURL(browser)
            browser= LauncheTender.subcontractorValidlogin(browser)
            browser.implicitly_wait(10)
            orgInstance=Organizationclass()
            orgInstance.OpenaddUser(browser)
            addusertoOrg=orgLink.readfromXML(folder_path+'\Object\Object.xml','eTender','adduserOrganisation')
            browser.find_element_by_xpath(addusertoOrg).click()
            browser.find_element_by_id(orgLink.readfromXML(folder_path+'\Object\Object.xml','eTender','adduserSavebutton')).click()
            time.sleep(3)
            self.assertTrue(orgLink.readfromXML(folder_path+'\Data\Data.xml','eTender','warninginUser') in browser.page_source)
            logs.info("Test Case No : 100138 Passed Successfully")
        except Exception:
            logs.error("Validation with Test Case No: 100138 failed")
            browser.save_screenshot(fullpath)
            traceback.print_exc(file=sys.stdout)
            self.fail("Test Case No: 100138 failed")
        finally:
            browser=LauncheTender.closebrowser(browser)
