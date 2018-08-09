#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      suresh.kumar
#
# Created:     25/08/2016
# Copyright:   (c) suresh.kumar 2016
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
sys.path.insert(0,folder_path+"\Syslibrary")
sys.path.insert(0,folder_path+"\Data")
sys.path.insert(0,folder_path+"\Object")
from launcheTender import LauncheTenderclass
from setupenviron import setupValue
from datadriven import DataDriver
from logdriver import logvalue
logs=logvalue.logger
logclose=logvalue()
ftime = time.mktime(time.localtime())
ptime=time.strftime("%d-%m-%Y_%H%M%S", time.localtime(ftime))
#filename = 'TestCase-100002-{0}.png'.format(ptime)
tf = 'test_openbrowser'
filename = 'Testcase-%s.png' %(tf)
path= setupValue().screenpath
fullpath = os.path.join(path,filename)

#Test case no:100002
class Browseropen(unittest.TestCase):
    def test_openbrowser(self):
        try:
            browserInstance = setupValue()
            browser = browserInstance.setupfunction()
            LauncheTender1 = LauncheTenderclass()
            browser = LauncheTender1.openURL(browser)
            browser.implicitly_wait(5)
            login = DataDriver()
            submitButton_id=login.readfromXML(folder_path+'\Object\Object.xml','eTender','submitButton') #Login button
            time.sleep(1)
            Login = browser.find_element_by_id(submitButton_id)
            Login1 = Login.text
            time.sleep(1)
            self.assertEqual(Login1, 'Log In')
            logs.info("Test Case No : 100002 Passed Successfully")
        except Exception:
            logs.error("Validation with Test Case No: 100002 failed")
            browser.save_screenshot(fullpath)
            traceback.print_exc(file=sys.stdout)
            self.fail("Test Case No: 100002 failed")
            browser.implicitly_wait(5)
        finally:
            LauncheTender1.closebrowser(browser)