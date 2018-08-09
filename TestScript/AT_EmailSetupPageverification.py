#-------------------------------------------------------------------------------
# Name:         AT_EmailSetupPageverification
#
# Tast Case Id  100361
#
# Purpose:      To Verify page EmailSetup
#
# Author:      mathew.jacob
#
# Created:     01/12/2017
# Copyright:   (c) Causeway Technologies 2017
#-------------------------------------------------------------------------------

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
import unittest
import sys
import os
import time
import traceback
from datetime import datetime,date

dir_path = os.path.dirname(os.path.realpath(__file__))
folder_path=os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0,folder_path+"\Library")
sys.path.insert(0,folder_path+"\Env")
from launcheTender import LauncheTenderclass
from setupenviron import setupValue
from logdriver import logvalue
from datadriven import DataDriver
from TenderModification import TenderClass
from logouteTender import Userprofilemenu
from AdminEstimator import Adminclass
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
logs=logvalue.logger
orgLink=DataDriver()
ftime = time.mktime(time.localtime())
ptime=time.strftime("%d-%m-%Y_%H%M%S", time.localtime(ftime))
#filename = 'TestCase-100361-{0}.png'.format(ptime)
tf = 'test_SetupEmailPage'
filename = 'Testcase-%s.png' %(tf)
path= setupValue().screenpath
fullpath = os.path.join(path,filename)
class EmailSetupPage(unittest.TestCase):
    def test_SetupEmailPage(self):
        try:
            browserInstance = setupValue()
            browser = browserInstance.setupfunction()
            browser.implicitly_wait(10)
            LauncheTender = LauncheTenderclass()
            TenderAction=TenderClass()
            logOut=Userprofilemenu()
            adminfunction=Adminclass()
            browser = LauncheTender.openURL(browser)
            browser = LauncheTender.estimatorValidlogin1(browser)
            time.sleep(3)
            adminfunction.EmailSetup(browser)
            time.sleep(2)
            self.assertTrue(browser.find_element_by_id(orgLink.readfromXML(folder_path+'\Data\EmailSetupData.xml','eTender','LogSelector')))
            self.assertTrue(browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Data\EmailSetupData.xml','eTender','CropImage')))
            self.assertTrue(browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Data\EmailSetupData.xml','eTender','Invitation')))
            self.assertTrue(browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Data\EmailSetupData.xml','eTender','ViewDetails')))
            self.assertTrue(browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Data\EmailSetupData.xml','eTender','ResetBtn')))
            self.assertTrue(browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Data\EmailSetupData.xml','eTender','SaveBtn')))
            logs.info("Test Case No : 100361 Passed Successfully")
        except Exception:
            logs.error("Test Case No: 100361 failed")
            browser.save_screenshot(fullpath)
            traceback.print_exc(file=sys.stdout)
            self.fail("Test Case No: 100361 failed")
        finally:
            browser=logOut.logout_eTender(browser)
            LauncheTender.closebrowser(browser)