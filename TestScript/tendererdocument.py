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
#filename = 'TestCase-100029-{0}.png'.format(ptime)
tf = 'test_tendererdocment'
filename = 'Testcase-%s.png' %(tf)
path= setupValue().screenpath
fullpath = os.path.join(path,filename)

#Test case number = 100029
class Tendererdocument(unittest.TestCase):
    def test_tendererdocment(self):
        try:
            browserInstance = setupValue()
            browser = browserInstance.setupfunction()
            browser.implicitly_wait(5)
            time.sleep(1)
            LauncheTender1 = LauncheTenderclass()
            browser = LauncheTender1.openURL(browser)
            browser.implicitly_wait(5)
            time.sleep(1)
            browser = LauncheTender1.subcontractorValidlogin(browser)
            browser = LauncheTender1.list_Organisation(browser)
            time.sleep(1)
            browser = LauncheTender1.verifyorganisationdetails(browser)
            browser = LauncheTender1.list_project(browser)
            tenderDetails = Tenderdetails()
            time.sleep(1)
            browser = tenderDetails.Subcontratorproject(browser)
            browser = tenderDetails.suppliertender(browser)
            browser = tenderDetails.Actionslist(browser)
            time.sleep(1)
            browser = tenderDetails.tenderdocument(browser)
            time.sleep(1)
            browser.implicitly_wait(5)
            uploaddoc = DataDriver()
            uploaddoc_path = uploaddoc.readfromXML(folder_path+'\Object\Object.xml','eTender','uploaddocument') #window title
            time.sleep(1)
            upload_document = browser.find_element_by_xpath(uploaddoc_path) #Webelement for window title
            time.sleep(1)
            uploaddocument = upload_document.text
            self.assertEqual(uploaddocument,'Tenderer document(s)')
            time.sleep(2)
            logs.info("Test Case No : 100029 Passed Successfully")
        except Exception:
            logs.error("Validation with Test Case No: 100029 failed")
            browser.save_screenshot(fullpath)
            traceback.print_exc(file=sys.stdout)
            self.fail("Test Case No: 100029 failed")
            browser.implicitly_wait(5)
        finally:
            LauncheTender1.closebrowser(browser)