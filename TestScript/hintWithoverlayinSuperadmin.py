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
#filename = 'TestCase-TC1073-{0}.png'.format(ptime)
tf = 'test_hintWithoverlayinSuperadmin'
filename = 'Testcase-%s.png' %(tf)
path= setupValue().screenpath
fullpath = os.path.join(path,filename)

#Test case no:TC1073
class HintWithoverlayinSuperadmin(unittest.TestCase):
    def test_hintWithoverlayinSuperadmin(self):
        try:
            browserInstance = setupValue()
            browser = browserInstance.setupfunction()
            browser.implicitly_wait(5)
            time.sleep(1)
            LauncheTender1 = LauncheTenderclass()
            browser = LauncheTender1.openURL(browser)
            browser.implicitly_wait(5)
            browser = LauncheTender1.superAdminValidlogin(browser)
            time.sleep(1)
            Hintdisplay = HintInteract()
            browser = Hintdisplay.systemcurrencymenu(browser)
            time.sleep(1)

            #browser = Hintdisplay.showhints(browser)
            #time.sleep(2)

            overlay1 = DataDriver()
            overlay_path = overlay1.readfromXML(folder_path+'\Object\Hint.xml','eTender','overlaybackground')
            overlay = browser.find_element_by_xpath(overlay_path)
            time.sleep(1)

            if overlay.is_displayed():
                print("Overlay background exists")
            else:
                self.fail("Overlay background color does not exists")

            logs.info("Test Case No : TC1073 Passed Successfully")
        except Exception:
            logs.error("Validation with Test Case No: TC1073 failed")
            browser.save_screenshot(fullpath)
            traceback.print_exc(file=sys.stdout)
            self.fail("Test Case No: TC1073 failed")
            browser.implicitly_wait(5)
        finally:
            time.sleep(1)
            LauncheTender1.closebrowser(browser)