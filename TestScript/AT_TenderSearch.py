#-------------------------------------------------------------------------------
# Name:         AT_TenderSearch.py
#
# Tast Case Id  100242
#
# Purpose:      TO Verify that search fucntionality with Tender page
#
# Author:      mathew.jacob
#
# Created:     03/07/2017
# Copyright:   (c) Causeway Technologies 2017
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
sys.path.insert(0,folder_path+"\Env")
from launcheTender import LauncheTenderclass
from setupenviron import setupValue
from logdriver import logvalue
from datadriven import DataDriver
from TenderModification import TenderClass
from logouteTender import Userprofilemenu
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
logs=logvalue.logger
orgLink=DataDriver()
ftime = time.mktime(time.localtime())
ptime=time.strftime("%d-%m-%Y_%H%M%S", time.localtime(ftime))
#filename = 'TestCase-100242-{0}.png'.format(ptime)
tf = 'test_TenderSearchfunction'
filename = 'Testcase-%s.png' %(tf)
path= setupValue().screenpath
fullpath = os.path.join(path,filename)
class TenderSearchClass(unittest.TestCase):
    def test_TenderSearchfunction(self):
        try:
            browserInstance = setupValue()
            browser = browserInstance.setupfunction()
            browser.implicitly_wait(10)
            LauncheTender = LauncheTenderclass()
            TenderAction=TenderClass()
            logOut=Userprofilemenu()
            browser = LauncheTender.openURL(browser)
            browser = LauncheTender.estimatorValidlogin(browser)
            time.sleep(3)
            ProjName=TenderAction.ProjectCreation(browser)
            TenderAction.OpenProject(ProjName,browser)
            NewTender=TenderAction.TenderCreation(browser)
            FalseNewTender=NewTender+"New"
            browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','TenderSearchBox')).send_keys(NewTender)
            self.assertTrue(NewTender in browser.page_source)
            time.sleep(2)
            browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','TenderSearchBox')).clear()
            browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','TenderSearchBox')).send_keys(FalseNewTender)
            self.assertFalse(FalseNewTender in browser.page_source)
            logs.info("Test Case No : 100242 Passed Successfully")
        except Exception:
            logs.error("Validation with Test Case No: 100242 failed")
            browser.save_screenshot(fullpath)
            traceback.print_exc(file=sys.stdout)
            self.fail("Test Case No: 100242 failed")
        finally:
            browser=logOut.logout_eTender(browser)
            LauncheTender.closebrowser(browser)

