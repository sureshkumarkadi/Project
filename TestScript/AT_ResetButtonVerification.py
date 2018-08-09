#-------------------------------------------------------------------------------
# Name:         AT_ResetButtonVerification
#
# Tast Case Id  100106
#
# Purpose:      To Verify Reset Button functionality with Add User screen
#
# Author:      mathew.jacob
#
# Created:     13/09/2016
# Copyright:   (c) mathew.jacob 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from selenium.webdriver.support.ui import WebDriverWait
import unittest
import sys
import os
import traceback
import time
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
#filename = 'TestCase-100106-{0}.png'.format(ptime)
tf = 'test_resetButton'
filename = 'Testcase-%s.png' %(tf)
path= setupValue().screenpath
fullpath = os.path.join(path,filename)
class ResetButtonInAddUser(unittest.TestCase):
    def test_resetButton(self):
        try:
            browserInstance = setupValue()
            browser = browserInstance.setupfunction()
            LauncheTender = LauncheTenderclass()
            logOut=Userprofilemenu()
            browser = LauncheTender.openURL(browser)
            browser.implicitly_wait(10)
            LauncheTender.subcontractorValidlogin(browser)
            orgInstance=Organizationclass()
            orgInstance.OpenaddUser(browser)
            time.sleep(2)
            p=browser.find_elements_by_xpath(orgLink.readfromXML(folder_path+'\Object\Object.xml','eTender','emailSearchbox'))
            time.sleep(2)
            p[1].send_keys(orgLink.readfromXML(folder_path+'\Data\Data.xml','eTender','userSaveEmail'))
            time.sleep(2)
            if (orgLink.readfromXML(folder_path+'\Data\Data.xml','eTender','userSaveEmail') in browser.page_source):
                p[1].clear()
                orgInstance.RemoveUserOrganization(browser)
            browser=orgInstance.AddUserOrganization(browser)
            self.assertTrue(orgLink.readfromXML(folder_path+'\Data\Data.xml','eTender','userSaveEmail') in browser.page_source)
            buttonValue=browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\Object.xml','eTender','resetButton'))
            time.sleep(5)
            buttonValue.click()
            time.sleep(5)
            self.assertFalse(orgLink.readfromXML(folder_path+'\Data\Data.xml','eTender','userSaveEmail') in browser.page_source)
            browser.implicitly_wait(20)
            logs.info("Test Case No : 100106 Passed Successfully")
        except Exception:
            logs.error("Validation with Test Case No: 100111 failed")
            browser.save_screenshot(fullpath)
            traceback.print_exc(file=sys.stdout)
            self.fail("Test Case No: 100105 failed")
        finally:
            browser=logOut.logout_eTender(browser)
            LauncheTender.closebrowser(browser)
