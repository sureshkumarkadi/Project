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
#filename = 'TestCase-TC1044-{0}.png'.format(ptime)
tf = 'test_invalidloginattemptafter5times'
filename = 'Testcase-%s.png' %(tf)
path= setupValue().screenpath
fullpath = os.path.join(path,filename)

#Test case no:TC1044
class Invalidloginattemptafter5times(unittest.TestCase):
    def test_invalidloginattemptafter5times(self):
        try:
            browserInstance = setupValue()
            browser = browserInstance.setupfunction()
            browser.implicitly_wait(5)
            time.sleep(1)
            LauncheTender1 = LauncheTenderclass()
            browser = LauncheTender1.openURL(browser)
            time.sleep(1)
            browser = LauncheTender1.estimatorinvalidpassword(browser)
            time.sleep(1)
            estimator_invalidloginattempt1 = DataDriver()
            messageafterunsuccessattempts_path = estimator_invalidloginattempt1.readfromXML(folder_path+'\Object\Object.xml','eTender','messageafterunsuccessattempts') #Invalid loginmessageafterunsuccessattempts
            messageafterunsuccessattempts = browser.find_element_by_xpath(messageafterunsuccessattempts_path)
            time.sleep(1)
            self.assertEqual(messageafterunsuccessattempts.text,'The maximum number of login attempts has been reached. Please try again in 5 minutes')
            logs.info("Test Case No : TC1044 Passed Successfully")
        except Exception:
            logs.error("Validation with Test Case No: TC1044 failed")
            browser.save_screenshot(fullpath)
            traceback.print_exc(file=sys.stdout)
            self.fail("Test Case No: TC1044 failed")
            browser.implicitly_wait(5)
        finally:
            LauncheTender1.closebrowser(browser)