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
#from Organisationprofile import OrganisationProfile
from setupenviron import setupValue
from logdriver import logvalue
#from logouteTender import Userprofilemenu
from Hint import HintInteract
logs=logvalue.logger
logclose=logvalue()
ftime = time.mktime(time.localtime())
ptime=time.strftime("%d-%m-%Y_%H%M%S", time.localtime(ftime))
#filename = 'TestCase-TC1508-{0}.png'.format(ptime)
tf = 'test_hintinSuperadminafterLogout'
filename = 'Testcase-%s.png' %(tf)
path= setupValue().screenpath
fullpath = os.path.join(path,filename)

#Test case no:TC1508
class HintinSuperadminafterLogout(unittest.TestCase):
    def test_hintinSuperadminafterLogout(self):
        try:
            browserInstance = setupValue()
            browser = browserInstance.setupfunction()
            browser.implicitly_wait(5)
            time.sleep(1)
            LauncheTender1 = LauncheTenderclass()
            browser = LauncheTender1.openURL(browser)
            browser.implicitly_wait(5)
            browser = LauncheTender1.superAdminValidlogin(browser)
            Hintdisplay = HintInteract()
            browser = Hintdisplay.systemfiledsmenu(browser)
            time.sleep(1)

            hint = DataDriver()
            time.sleep(1)

            self.assertFalse('System1' in browser.page_source)
            self.assertFalse('System field Creation can be done here' in browser.page_source)
            self.assertFalse('Items1' in browser.page_source)
            self.assertFalse('Total items1' in browser.page_source)
            self.assertFalse('Done' in browser.page_source)
            time.sleep(1)

            logs.info("Test Case No : TC1508 Passed Successfully")
        except Exception:
            logs.error("Validation with Test Case No: TC1508 failed")
            browser.save_screenshot(fullpath)
            traceback.print_exc(file=sys.stdout)
            self.fail("Test Case No: TC1508 failed")
            browser.implicitly_wait(5)
        finally:
            time.sleep(1)
            LauncheTender1.closebrowser(browser)