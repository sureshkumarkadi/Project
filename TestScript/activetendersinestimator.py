#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      suresh.kumar
#
# Created:     25/08/2016
# Copyright:   (c) mathew.jacob 2016
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
from tenderDetails import Tenderdetails
from tenderDetails import SubmitTenderclass
from datadriven import DataDriver
from setupenviron import setupValue
from logouteTender import Userprofilemenu
from logdriver import logvalue
logs=logvalue.logger
logclose=logvalue()
ftime = time.mktime(time.localtime())
ptime=time.strftime("%d-%m-%Y_%H%M%S", time.localtime(ftime))
#filename = 'TestCase-100050-{0}.png'.format(ptime)
tf = 'test_activetendersinEstimator'
filename = 'Testcase-%s.png' %(tf)
path= setupValue().screenpath
fullpath = os.path.join(path,filename)

#Test case Number = 100050
class Activetendersinestimator(unittest.TestCase):
    def test_activetendersinEstimator(self):
        try:
            browserInstance = setupValue()
            browser = browserInstance.setupfunction()
            browser.implicitly_wait(5)
            time.sleep(1)
            LauncheTender1 = LauncheTenderclass()
            browser = LauncheTender1.openURL(browser)
            browser.implicitly_wait(5)
            time.sleep(1)
            browser = LauncheTender1.estimatorValidlogin(browser)
            time.sleep(1)
            tenderDetails = Tenderdetails()
            browser = tenderDetails.estimatorProject(browser)
            browser = tenderDetails.activetendersInestimator(browser)
            time.sleep(2)
            activetendersinestimator = DataDriver()
            tendererslist = []
            time.sleep(1)
            tendererslist_path = activetendersinestimator.readfromXML(folder_path+'\Object\Object.xml','eTender','activetender1')
            tendererslist1 = browser.find_element_by_xpath(tendererslist_path) #Notes in Estimator Login
            time.sleep(1)

            tendererslist_path = activetendersinestimator.readfromXML(folder_path+'\Object\Object.xml','eTender','activetender2')
            tendererslist2 = browser.find_element_by_xpath(tendererslist_path) #Notes in Estimator Login

            activetender1 = tendererslist1.text
            activetender2 = tendererslist2.text

            time.sleep(1)
            browser.implicitly_wait(5)
            self.assertEqual(activetender1,'A - Preliminaries - A1303 - Temp Proppin')
            time.sleep(1)
            self.assertEqual(activetender2,'A - Preliminaries - A1304 - Edge Protect')
            time.sleep(2)
            logs.info("Test Case No : 100050 Passed Successfully")
        except Exception:
            logs.error("Validation with Test Case No: 100050 failed")
            browser.save_screenshot(fullpath)
            traceback.print_exc(file=sys.stdout)
            self.fail("Test Case No: 100050 failed")
            browser.implicitly_wait(5)
        finally:
            LauncheTender1.closebrowser(browser)