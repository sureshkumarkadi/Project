#-------------------------------------------------------------------------------
# Name:         AT_RemoveUserfromOrganization
#
# Tast Case Id  100105
#
# Purpose:      To Verify that user can remove from the system
#
# Author:      mathew.jacob
#
# Created:     19/09/2016
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
from logouteTender import Userprofilemenu
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
logs=logvalue.logger
orgLink=DataDriver()
ftime = time.mktime(time.localtime())
ptime=time.strftime("%d-%m-%Y_%H%M%S", time.localtime(ftime))
#filename = 'TestCase-100105-{0}.png'.format(ptime)
tf = 'test_removeUsertoOrg'
filename = 'Testcase-%s.png' %(tf)
path= setupValue().screenpath
fullpath = os.path.join(path,filename)
class RemoveUserOrganization(unittest.TestCase):
    def test_removeUsertoOrg(self):
        try:
            browserInstance = setupValue()
            browser = browserInstance.setupfunction()
            LauncheTender = LauncheTenderclass()
            browser = LauncheTender.openURL(browser)
            browser= LauncheTender.subcontractorValidlogin(browser)
            browser.implicitly_wait(10)
            orgInstance=Organizationclass()
            logOut=Userprofilemenu()
            orgInstance.OpenaddUser(browser)
            browser.implicitly_wait(10)
            browser=orgInstance.AddUserOrganization(browser)
            time.sleep(3)
            browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\Object.xml','eTender','saveButon')).click()
            self.assertTrue(orgLink.readfromXML(folder_path+'\Data\Data.xml','eTender','userSaveEmail') in browser.page_source)
            orgInstance.RemoveUserOrganization(browser)
            self.assertFalse(orgLink.readfromXML(folder_path+'\Data\Data.xml','eTender','userSaveEmail') in browser.page_source)
            time.sleep(2)
            logs.info("Test Case No : 100105 Passed Successfully")
        except Exception:
            logs.error("Validation with Test Case No: 100111 failed")
            browser.save_screenshot(fullpath)
            traceback.print_exc(file=sys.stdout)
            self.fail("Test Case No: 100105 failed")
            browser.implicitly_wait(5)
        finally:
            browser=logOut.logout_eTender(browser)
            LauncheTender.closebrowser(browser)
