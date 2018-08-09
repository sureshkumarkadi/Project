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
from setupenviron import setupValue
from logdriver import logvalue
logs=logvalue.logger
logclose=logvalue()
ftime = time.mktime(time.localtime())
ptime=time.strftime("%d-%m-%Y_%H%M%S", time.localtime(ftime))
#filename = 'TestCase-TC1066-{0}.png'.format(ptime)
tf = 'test_estimatorinvalidpassword'
filename = 'Testcase-%s.png' %(tf)
path= setupValue().screenpath
fullpath = os.path.join(path,filename)

#Test case no:TC1066
class Estimatorinvalidpassword(unittest.TestCase):
    def test_estimatorinvalidpassword(self):
        try:
            browserInstance = setupValue()
            browser = browserInstance.setupfunction()
            browser.implicitly_wait(5)
            time.sleep(1)
            LauncheTender1 = LauncheTenderclass()
            browser = LauncheTender1.openURL(browser)
            browser.implicitly_wait(5)
            time.sleep(1)
            counter = 0
            for counter1 in range(counter,5):
                browser = LauncheTender1.estimatorinvalidpassword(browser)
                time.sleep(1)
                estimator_invalidlogin1 = DataDriver()
                estimatorinvalidlogin_path = estimator_invalidlogin1.readfromXML(folder_path+'\Object\Object.xml','eTender','invalidlogin') #Invalid login
                time.sleep(2)
                estimatorinvalidlogin = browser.find_element_by_xpath(estimatorinvalidlogin_path)
                time.sleep(1)
                self.assertEqual(estimatorinvalidlogin.text,'Invalid login. Please try again!')
                counter = counter + 1
                time.sleep(2)
            logs.info("Test Case No : TC1066 Passed Successfully")
        except Exception:
            logs.error("Validation with Test Case No: TC1066 failed")
            browser.save_screenshot(fullpath)
            traceback.print_exc(file=sys.stdout)
            self.fail("Test Case No: TC1066 failed")
            browser.implicitly_wait(5)
        finally:
            LauncheTender1.closebrowser(browser)