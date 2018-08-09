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
#filename = 'TestCase-100039-{0}.png'.format(ptime)
tf = 'test_changepasswordform'
filename = 'Testcase-%s.png' %(tf)
path= setupValue().screenpath
fullpath = os.path.join(path,filename)

#Test case Number = 100039
class Changepasswordform(unittest.TestCase):
    def test_changepasswordform(self):
        try:
            browserInstance = setupValue()
            browser = browserInstance.setupfunction()
            browser.implicitly_wait(5)
            time.sleep(1)
            LauncheTender1 = LauncheTenderclass()
            browser = LauncheTender1.openURL(browser)
            time.sleep(1)
            browser = LauncheTender1.subcontractorValidlogin(browser)
            Userprofilemenu_changepasswordmenu = Userprofilemenu()
            time.sleep(1)
            browser = Userprofilemenu_changepasswordmenu.changePassword(browser)
            browser = Userprofilemenu_changepasswordmenu.changePasswordForm(browser)
            browser.implicitly_wait(5)
            time.sleep(1)
            eTchangepasswordform = DataDriver()
            changepasswordform_path = eTchangepasswordform.readfromXML(folder_path+'\Object\Object.xml','eTender','toastmessage')
            time.sleep(1)
            toastmessage = browser.find_element_by_xpath(changepasswordform_path) #toastmessage
            time.sleep(1)
            logs.info("Test Case No : 100039 Passed Successfully")
        except Exception:
            logs.error("Validation with Test Case No: 100039 failed")
            browser.save_screenshot(fullpath)
            traceback.print_exc(file=sys.stdout)
            self.fail("Test Case No: 100039 failed")
            browser.implicitly_wait(5)
        finally:
            LauncheTender1.closebrowser(browser)