#-------------------------------------------------------------------------------
# Name:         AT_ProfileResetfuncion.py
#
# Tast Case Id  100099
#
# Purpose:      To Verify that Reset buton on profile page is working
#
# Author:      mathew.jacob
#
# Created:     27/11/2016
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
from OrganizationFunction import Organizationclass
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
#filename = 'TestCase-100099-{0}.png'.format(ptime)
tf = 'test_ProfileReset'
filename = 'Testcase-%s.png' %(tf)
path= setupValue().screenpath
fullpath = os.path.join(path,filename)
class ProfileResetButton(unittest.TestCase):
    def test_ProfileReset(self):
        try:
            browserInstance = setupValue()
            browser = browserInstance.setupfunction()
            LauncheTender = LauncheTenderclass()
            logOut=Userprofilemenu()
            browser = LauncheTender.openURL(browser)
            browser= LauncheTender.subcontractorValidlogin(browser)
            orgInstance=Organizationclass()
            orgInstance.OpenProfilePage(browser)
            time.sleep(3)
            textvalue=orgLink.readfromXML(folder_path+'\Data\Data.xml','eTender','nametempprofile')
            Resetbuton=browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\Object.xml','eTender','resetinprofile'))
            browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\Object.xml','eTender','namevalueprofile')).clear()
            browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\Object.xml','eTender','namevalueprofile')).send_keys(textvalue)
            time.sleep(2)
            browser.execute_script("arguments[0].scrollIntoView(true);", Resetbuton)
            Resetbuton.click()
            time.sleep(2)
            self.assertNotEquals(browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\Object.xml','eTender','namevalueprofile')).get_attribute('value'),orgLink.readfromXML(folder_path+'\Data\Data.xml','eTender','nametempprofile'))
            logs.info("Test Case No : 100099 Passed Successfully")
        except Exception:
            logs.error("Validation with Test Case No: 100099 failed")
            browser.save_screenshot(fullpath)
            traceback.print_exc(file=sys.stdout)
            self.fail("Test Case No: 100099 failed")
        finally:
            browser=logOut.logout_eTender(browser)
            LauncheTender.closebrowser(browser)
            #logclose.closeLogger()

