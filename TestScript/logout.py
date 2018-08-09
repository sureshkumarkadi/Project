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
#filename = 'TestCase-100041-{0}.png'.format(ptime)
tf = 'test_LogouteTender'
filename = 'Testcase-%s.png' %(tf)
path= setupValue().screenpath
fullpath = os.path.join(path,filename)

#Test case Number = 100041
class LogouteTender(unittest.TestCase):
    def test_LogouteTender(self):
        try:
            browserInstance = setupValue()
            browser = browserInstance.setupfunction()
            browser.implicitly_wait(5)
            LauncheTender1 = LauncheTenderclass()
            browser = LauncheTender1.openURL(browser)
            browser = LauncheTender1.subcontractorValidlogin(browser)
            time.sleep(3)
            Userprofilemenu_logout = Userprofilemenu()
            browser = Userprofilemenu_logout.logout_eTender(browser)
            time.sleep(3)
            eTlogout = DataDriver()
            logout_path = eTlogout.readfromXML(folder_path+'\Object\Object.xml','eTender','submitButton')
            time.sleep(1)
            Logout = browser.find_element_by_id(logout_path) #Login button
            Logout1 = Logout.text
            time.sleep(1)
            self.assertEqual(Logout1, 'Log In')
            logs.info("Test Case No : 100041 Passed Successfully")
        except Exception:
            logs.error("Validation with Test Case No: 100041 failed")
            browser.save_screenshot(fullpath)
            traceback.print_exc(file=sys.stdout)
            self.fail("Test Case No: 100041 failed")
            browser.implicitly_wait(5)
        finally:
            LauncheTender1.closebrowser(browser)



