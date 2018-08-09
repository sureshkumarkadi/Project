#-------------------------------------------------------------------------------
# Name:          AT_UserProfileUIverification
#
# Tast Case Id  100157
#
# Purpose:      To Verify UI elements in User Profile page
#
# Author:      mathew.jacob
#
# Created:     07/12/2016
# Copyright:   (c) Causeway Technologies 2016

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
#filename = 'TestCase-100157-{0}.png'.format(ptime)
tf = 'test_userProfileUI'
filename = 'Testcase-%s.png' %(tf)
path= setupValue().screenpath
fullpath = os.path.join(path,filename)
class UserProfileUI(unittest.TestCase):
    def test_userProfileUI(self):
        try:
            browserInstance = setupValue()
            browser = browserInstance.setupfunction()
            LauncheTender = LauncheTenderclass()
            browser = LauncheTender.openURL(browser)
            browser= LauncheTender.subcontractorValidlogin(browser)
            logOut=Userprofilemenu()
            orgInstance=Organizationclass()
            orgInstance.OpenUserProfilePage(browser)
            time.sleep(3)
            self.assertTrue(browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\\Object\\UserProfileObject.xml','eTender','title')))
            self.assertTrue(browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\\Object\\UserProfileObject.xml','eTender','Firstname')))
            self.assertTrue(browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\\Object\\UserProfileObject.xml','eTender','lastname')))
            self.assertTrue(browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\\Object\\UserProfileObject.xml','eTender','jobtitle')))
            self.assertTrue(browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\\Object\\UserProfileObject.xml','eTender','email')))
            self.assertTrue(browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\\Object\\UserProfileObject.xml','eTender','mphone')))
            self.assertTrue(browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\\Object\\UserProfileObject.xml','eTender','phone')))
            self.assertTrue(browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\\Object\\UserProfileObject.xml','eTender','linkedin')))
            self.assertTrue(browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\\Object\\UserProfileObject.xml','eTender','address')))
            self.assertTrue(browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\\Object\\UserProfileObject.xml','eTender','eFootNote')))
##            self.assertTrue(browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\UserProfileObject.xml','eTender','county')))
##            self.assertTrue(browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\UserProfileObject.xml','eTender','country')))
##            self.assertTrue(browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\UserProfileObject.xml','eTender','pcode')))
            self.assertTrue(browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\\Object\\UserProfileObject.xml','eTender','image')))
            logs.info("Test Case No : 100157 Passed Successfully")
        except Exception:
            logs.error("Validation with Test Case No: 100157 failed")
            browser.save_screenshot(fullpath)
            traceback.print_exc(file=sys.stdout)
            self.fail("Test Case No: 100157 failed")
            browser.implicitly_wait(5)
        finally:
            browser=logOut.logout_eTender(browser)
            LauncheTender.closebrowser(browser)


