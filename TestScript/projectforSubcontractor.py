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
from datadriven import DataDriver
from setupenviron import setupValue
from logdriver import logvalue
logs=logvalue.logger
logclose=logvalue()
ftime = time.mktime(time.localtime())
ptime=time.strftime("%d-%m-%Y_%H%M%S", time.localtime(ftime))
#filename = 'TestCase-100007-{0}.png'.format(ptime)
tf = 'test_tenderdetails'
filename = 'Testcase-%s.png' %(tf)
path= setupValue().screenpath
fullpath = os.path.join(path,filename)

#Test case no:100007
class tradeslistSubcontractor(unittest.TestCase):
    def test_tenderdetails(self):
        try:
            browserInstance = setupValue()
            browser = browserInstance.setupfunction()
            browser.implicitly_wait(5)
            LauncheTender1 = LauncheTenderclass()
            browser = LauncheTender1.openURL(browser)
            browser.implicitly_wait(5)
            browser = LauncheTender1.subcontractorValidlogin(browser)
            browser = LauncheTender1.list_Organisation(browser)
            browser = LauncheTender1.verifyorganisationdetails(browser)
            browser = LauncheTender1.list_project(browser)
            tenderDetails = Tenderdetails()
            browser = tenderDetails.Subcontratorproject(browser)
            browser.implicitly_wait(5)
            tradelist = DataDriver()
            trades = []
            tradefirst_path = tradelist.readfromXML(folder_path+'\Object\Object.xml','eTender','quicktenders')
            trades = browser.find_elements_by_xpath(tradefirst_path) #Trades list
            time.sleep(3)
            #tradesecond_path = tradelist.readfromXML(folder_path+'\Object\Object.xml','eTender','tradesecondsub')
            #tradesecond = browser.find_element_by_xpath(tradesecond_path) #Trades list
            #time.sleep(1)
            trade1 = trades[0].text
            trade2 = trades[1].text
            self.assertEqual(trade1,'A - Preliminaries - A1303 - Te..')
            self.assertEqual(trade2,'A - Preliminaries - A1304 - Ed..')
            logs.info("Test Case No : 100007 Passed Successfully")
        except Exception:
            logs.error("Validation with Test Case No: 100007 failed")
            browser.save_screenshot(fullpath)
            traceback.print_exc(file=sys.stdout)
            self.fail("Test Case No: 100007 failed")
            browser.implicitly_wait(5)
        finally:
            LauncheTender1.closebrowser(browser)

if __name__ == '__main__':
    unittest.main()