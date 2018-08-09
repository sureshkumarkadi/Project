#-------------------------------------------------------------------------------
# Name:         AT_ProfileLocationSetfunction.py
#
# Tast Case Id  100098
#
# Purpose:      To Verify that location is able to set by google search in profile page
#
# Author:      mathew.jacob
#
# Created:     26/11/2016
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
#filename = 'TestCase-100098-{0}.png'.format(ptime)
tf = 'test_Profilelocation'
filename = 'Testcase-%s.png' %(tf)
path= setupValue().screenpath
fullpath = os.path.join(path,filename)
class Profilelocationselection(unittest.TestCase):
    def test_Profilelocation(self):
        try:
            browserInstance = setupValue()
            browser = browserInstance.setupfunction()
            LauncheTender = LauncheTenderclass()
            logOut=Userprofilemenu()
            browser = LauncheTender.openURL(browser)
            browser= LauncheTender.subcontractorValidlogin(browser)
            orgInstance=Organizationclass()
            orgInstance.OpenProfilePage(browser)
            time.sleep(2)
            textvalue=orgLink.readfromXML(folder_path+'\Data\Data.xml','eTender','locationtext')
            time.sleep(2)
            savebutton=browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\Object.xml','eTender','saveinprofile'))
            browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\Object.xml','eTender','locationprofile')).send_keys(textvalue)
            p=browser.find_elements_by_css_selector(orgLink.readfromXML(folder_path+'\Object\Object.xml','eTender','locationLink'))
            p[0].click()
            time.sleep(2)
            self.assertEqual(browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\Object.xml','eTender','addresstextbox')).get_attribute('value'),orgLink.readfromXML(folder_path+'\Data\Data.xml','eTender','addresstext'))
            time.sleep(2)
            browser.execute_script("arguments[0].scrollIntoView(true);", savebutton)
            savebutton.click()
            orgInstance.OpenaddUser(browser)
            orgInstance.OpenProfilePage(browser)
            time.sleep(2)
            self.assertEqual(browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\Object.xml','eTender','addresstextbox')).get_attribute('value'),orgLink.readfromXML(folder_path+'\Data\Data.xml','eTender','addresstext'))
            logs.info("Test Case No : 100098 Passed Successfully")
        except Exception:
            logs.error("Validation with Test Case No: 100098 failed")
            browser.save_screenshot(fullpath)
            traceback.print_exc(file=sys.stdout)
            self.fail("Test Case No: 100098 failed")
        finally:
            browser=logOut.logout_eTender(browser)
            LauncheTender.closebrowser(browser)
            #logclose.closeLogger()

