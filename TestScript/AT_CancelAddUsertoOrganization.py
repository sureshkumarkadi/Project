#-------------------------------------------------------------------------------
# Name:         AT_CancelAddUsertoOrganization
#
# Tast Case Id  100103
#
# Purpose:      To Verify Cancel Button functionality with Add User screen
#
# Author:      mathew.jacob
#
# Created:     12/10/2016
# Copyright:   (c) (c) Causeway Technologies 2016
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
#filename = 'TestCase-100103-{0}.png'.format(ptime)
tf = 'test_cancelButton'
filename = 'Testcase-%s.png' %(tf)
path= setupValue().screenpath
fullpath = os.path.join(path,filename)
class CancelButtonInAddUser(unittest.TestCase):
    def test_cancelButton(self):
        try:
            browserInstance = setupValue()
            browser = browserInstance.setupfunction()
            LauncheTender = LauncheTenderclass()
            browser = LauncheTender.openURL(browser)
            logOut=Userprofilemenu()
            browser.implicitly_wait(10)
            LauncheTender.subcontractorValidlogin(browser)
            orgInstance=Organizationclass()
            orgInstance.OpenaddUser(browser)
            time.sleep(2)
            if (orgLink.readfromXML(folder_path+'\Data\Data.xml','eTender','userSaveEmail') in browser.page_source):
                orgInstance.RemoveUserOrganization(browser)
            orgInstance.AddUserOrganizationCancel(browser)
            time.sleep(2)
            orgInstance.OpenUserRole(browser)
            time.sleep(2)
            orgInstance.OpenaddUser(browser)
            time.sleep(2)
            self.assertFalse(orgLink.readfromXML(folder_path+'\Data\Data.xml','eTender','userSaveEmail') in browser.page_source)
            logs.info("Test Case No : 100103 Passed Successfully")
        except Exception:
            logs.error("Validation with Test Case No: 100103 failed")
            browser.save_screenshot(fullpath)
            traceback.print_exc(file=sys.stdout)
            self.fail("Test Case No: 100103 failed")
        finally:
            browser=logOut.logout_eTender(browser)
            LauncheTender.closebrowser(browser)
