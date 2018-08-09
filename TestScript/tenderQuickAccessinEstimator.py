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
import sys
import time
import os
import traceback
dir_path = os.path.dirname(os.path.realpath(__file__))
folder_path=os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0,folder_path+"\Library")
sys.path.insert(0,folder_path+"\Syslibrary")
sys.path.insert(0,folder_path+"\Data")
sys.path.insert(0,folder_path+"\Object")
from launcheTender import LauncheTenderclass
from launcheTender import Quicklyaccessingtendersclass
from tenderDetails import Tenderdetails
from datadriven import DataDriver
from setupenviron import setupValue
from logdriver import logvalue
logs=logvalue.logger
logclose=logvalue()
ftime = time.mktime(time.localtime())
ptime=time.strftime("%d-%m-%Y_%H%M%S", time.localtime(ftime))
#filename = 'TestCase-100063-{0}.png'.format(ptime)
tf = 'test_tenderquickaccessinestimator'
filename = 'Testcase-%s.png' %(tf)
path= setupValue().screenpath
fullpath = os.path.join(path,filename)

#Test case number = 100063
class Tenderquickaccessinestimator(unittest.TestCase):
    def test_tenderquickaccessinestimator(self):
        try:
            browserInstance = setupValue()
            browser = browserInstance.setupfunction()
            browser.implicitly_wait(5)
            LauncheTender1 = LauncheTenderclass()
            browser = LauncheTender1.openURL(browser)
            browser.implicitly_wait(5)
            browser = LauncheTender1.estimatorValidlogin(browser)
            Quickaccess = Quicklyaccessingtendersclass()
            browser = Quickaccess.tenderQuickAccess(browser)
            tenderslist = []
            quicktenders = DataDriver()
            time.sleep(2)
            quicktenders_path = quicktenders.readfromXML(folder_path+'\Object\Object.xml','eTender','quicktenders')
            time.sleep(2)
            tenderslist = browser.find_elements_by_xpath(quicktenders_path) #tenders list in Quick tender access
            time.sleep(2)
            firsttender  =  tenderslist[0].text
            secondtender =  tenderslist[1].text
            thirdtender =  tenderslist[2].text
            time.sleep(2)
            self.assertEqual(firsttender,'A - Preliminaries - A1303 - Temp Proppin')
            self.assertEqual(secondtender,'A - Preliminaries - A1304 - Edge Protect')
            self.assertEqual(thirdtender,'TenderforTradex')

            logs.info("Test Case No : 100063 Passed Successfully")
        except Exception:
            logs.error("Validation with Test Case No: 100063 failed")
            browser.save_screenshot(fullpath)
            traceback.print_exc(file=sys.stdout)
            self.fail("Test Case No: 100063 failed")
            browser.implicitly_wait(5)
        finally:
            LauncheTender1.closebrowser(browser)