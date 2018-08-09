#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      mathew.jacob
#
# Created:     25/08/2016
# Copyright:   (c) mathew.jacob 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from selenium.webdriver.support.ui import WebDriverWait
import unittest
import time
import sys
import os
import traceback
dir_path = os.path.dirname(os.path.realpath(__file__))
folder_path=os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0,folder_path+"\Library")
sys.path.insert(0,folder_path+"\Syslibrary")
sys.path.insert(0,folder_path+"\Data")
sys.path.insert(0,folder_path+"\Object")
from datadriven import DataDriver
from logouteTender import Userprofilemenu
from launcheTender import LauncheTenderclass
from setupenviron import setupValue
from logdriver import logvalue
logs=logvalue.logger
logclose=logvalue()
ftime = time.mktime(time.localtime())
ptime=time.strftime("%d-%m-%Y_%H%M%S", time.localtime(ftime))
#filename = 'TestCase-100040-{0}.png'.format(ptime)
tf = 'test_loginwithchangepassword'
filename = 'Testcase-%s.png' %(tf)
path= setupValue().screenpath
fullpath = os.path.join(path,filename)

#Test case Number = 100040
class Loginwithchangepassword(unittest.TestCase):
    def test_loginwithchangepassword(self):
        try:
            browserInstance = setupValue()
            browser = browserInstance.setupfunction()
            browser.implicitly_wait(5)
            time.sleep(1)
            LauncheTender1 = LauncheTenderclass()
            browser = LauncheTender1.openURL(browser)
            Userprofilemenu_changepasswordmenu = Userprofilemenu()
            time.sleep(1)
            browser = Userprofilemenu_changepasswordmenu.subcontractorloginwithchangedpassword(browser)
            browser.implicitly_wait(5)
            time.sleep(1)
            subcontractor_login = DataDriver()
            organisation_text=subcontractor_login.readfromXML(folder_path+'\Object\Object.xml','eTender','organisation-text') #organisation
            time.sleep(3)
            organisation = browser.find_element_by_link_text(organisation_text)
            time.sleep(2)
            self.assertEqual(organisation.text,'GSE Civil Engineering Ltd')
            time.sleep(2)
            browser = Userprofilemenu_changepasswordmenu.changepasswordbacktoOriginal(browser)
            time.sleep(1)
            logs.info("Test Case No : 100040 Passed Successfully")
        except Exception:
            logs.error("Validation with Test Case No: 100040 failed")
            browser.save_screenshot(fullpath)
            traceback.print_exc(file=sys.stdout)
            self.fail("Test Case No: 100040 failed")
            browser.implicitly_wait(5)
        finally:
            LauncheTender1.closebrowser(browser)