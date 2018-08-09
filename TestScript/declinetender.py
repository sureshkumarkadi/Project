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
from tenderDetails import Tenderdetails
from tenderDetails import SubmitTenderclass
from datadriven import DataDriver
from setupenviron import setupValue
from logdriver import logvalue
logs=logvalue.logger
logclose=logvalue()
ftime = time.mktime(time.localtime())
ptime=time.strftime("%d-%m-%Y_%H%M%S", time.localtime(ftime))
#filename = 'TestCase-100036-{0}.png'.format(ptime)
tf = 'test_declinetender'
filename = 'Testcase-%s.png' %(tf)
path= setupValue().screenpath
fullpath = os.path.join(path,filename)

#Test case number = 100036
class Declinetender(unittest.TestCase):
    def test_declinetender(self):
        try:
            browserInstance = setupValue()
            browser = browserInstance.setupfunction()
            browser.implicitly_wait(5)
            LauncheTender1 = LauncheTenderclass()
            browser = LauncheTender1.openURL(browser)
            browser.implicitly_wait(5)
            browser = LauncheTender1.subcontractorValidlogin(browser)
            browser = LauncheTender1.verifyorganisationdetails(browser)
            browser = LauncheTender1.list_project(browser)
            tenderDetails = Tenderdetails()
            browser = tenderDetails.Subcontratorproject(browser)
            browser = tenderDetails.suppliertender(browser)
            tenderDetails_decline = SubmitTenderclass()
            browser.implicitly_wait(5)
            browser = tenderDetails_decline.declineTender(browser)
            browser.implicitly_wait(5)
            confirmdecline = DataDriver()
            confirmdecline_path = confirmdecline.readfromXML(folder_path+'\Object\Object.xml','eTender','confirmdecline')
            confirmdecline_element = browser.find_element_by_xpath(confirmdecline_path) #Verifying Webelement for Confirm decline button

            if confirmdecline_element.is_displayed():
                print("pass")
            else:
                print("fail")

            logs.info("Test Case No : 100036 Passed Successfully")
        except Exception:
            logs.error("Validation with Test Case No: 100036 failed")
            browser.save_screenshot(fullpath)
            traceback.print_exc(file=sys.stdout)
            self.fail("Test Case No: 100036 failed")
            browser.implicitly_wait(5)
        finally:
            LauncheTender1.closebrowser(browser)