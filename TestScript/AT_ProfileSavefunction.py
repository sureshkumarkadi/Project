#-------------------------------------------------------------------------------
# Name:         AT_ProfileSavefunction.py
#
# Tast Case Id  100100
#
# Purpose:      To Verify that Save functionality is working fine in profile page
#
# Author:      mathew.jacob
#
# Created:     24/11/2016
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
#filename = 'TestCase-100100-{0}.png'.format(ptime)
tf = 'test_ProfileSave'
filename = 'Testcase-%s.png' %(tf)
path= setupValue().screenpath
fullpath = os.path.join(path,filename)
class ProfileSaveButton(unittest.TestCase):
    def test_ProfileSave(self):
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
            textvalue=orgLink.readfromXML(folder_path+'\Data\Data.xml','eTender','nametextprofile')
            savebutton=browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\Object.xml','eTender','saveinprofile'))
            browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\Object.xml','eTender','namevalueprofile')).clear()
            browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\Object.xml','eTender','namevalueprofile')).send_keys(textvalue)
            time.sleep(2)
            browser.execute_script("arguments[0].scrollIntoView(true);", savebutton)
            savebutton.click()
            orgInstance.OpenaddUser(browser)
            orgInstance.OpenProfilePage(browser)
            time.sleep(2)
            self.assertEquals(browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\Object.xml','eTender','namevalueprofile')).get_attribute('value'),orgLink.readfromXML(folder_path+'\Data\Data.xml','eTender','nametextprofile'))
            logs.info("Test Case No : 100100 Passed Successfully")
        except Exception:
            logs.error("Validation with Test Case No: 100100 failed")
            browser.save_screenshot(fullpath)
            traceback.print_exc(file=sys.stdout)
            self.fail("Test Case No: 100100 failed")
        finally:
            browser=logOut.logout_eTender(browser)
            LauncheTender.closebrowser(browser)
            #logclose.closeLogger()

