#-------------------------------------------------------------------------------
# Name:         AT_ProjectOpenOrganization.py
# Tast Case Id  100161
#
# Purpose:      To Verify that tender details for the organization is able to open from Project
#
# Author:      mathew.jacob
#
# Created:     20/12/2016
# Copyright:   (c) Causeway Technologies 2016
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
sys.path.insert(0,folder_path+"\Env")
from launcheTender import LauncheTenderclass
from setupenviron import setupValue
from logdriver import logvalue
from ProjectFunctions import Projectclass
from datadriven import DataDriver
from logouteTender import Userprofilemenu
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
logs=logvalue.logger
logclose=logvalue()
orgLink=DataDriver()
ftime = time.mktime(time.localtime())
ptime=time.strftime("%d-%m-%Y_%H%M%S", time.localtime(ftime))
#filename = 'TestCase-100161-{0}.png'.format(ptime)
tf = 'test_OpenOrganization'
filename = 'Testcase-%s.png' %(tf)
path= setupValue().screenpath
fullpath = os.path.join(path,filename)
class Organizationinproject(unittest.TestCase):
    def test_OpenOrganization(self):
        try:
            browserInstance = setupValue()
            browser = browserInstance.setupfunction()
            LauncheTender = LauncheTenderclass()
            browser = LauncheTender.openURL(browser)
            logOut=Userprofilemenu()
            browser= LauncheTender.subcontractorValidlogin(browser)
            projectInstance=Projectclass()
            time.sleep(3)
            projectInstance.Openorganization(browser)
            orglink=orgLink.readfromXML(folder_path+'\Data\Data.xml','eTender','Orgselection')
            browser.find_element_by_link_text(orglink).click()
            time.sleep(3)
            self.assertTrue(orgLink.readfromXML(folder_path+'\Data\Data.xml','eTender','Orgselection') in browser.page_source)
            logs.info("Test Case No : 100161 Passed Successfully")
        except Exception:
            logs.error("Validation with Test Case No: 100161 failed")
            browser.save_screenshot(fullpath)
            traceback.print_exc(file=sys.stdout)
            self.fail("Test Case No: 100161 failed")
            browser.implicitly_wait(5)
        finally:
            browser=logOut.logout_eTender(browser)
            LauncheTender.closebrowser(browser)


