#-------------------------------------------------------------------------------
# Name:         AT_CreateNewTag.py
#
# Purpose:      To check addition of new tag is working fine
#
# Tast Case Id  100177
#
# Author:      mathew.jacob
#
# Created:     16/02/2017
#
# Copyright:   (c) Causeway Technologies 2016
#-------------------------------------------------------------------------------

from selenium.webdriver.support.ui import WebDriverWait
import unittest
import sys
import os
import time
import traceback
from faker import Factory
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
from AdminEstimator import Adminclass
from OrganizationFunction import Organizationclass
from logouteTender import Userprofilemenu
orgLink=DataDriver()
logs=logvalue.logger
logclose=logvalue()
ftime = time.mktime(time.localtime())
ptime=time.strftime("%d-%m-%Y_%H%M%S", time.localtime(ftime))
#filename = 'TestCase-100177-{0}.png'.format(ptime)
tf = 'test_newtagcreation'
filename = 'Testcase-%s.png' %(tf)
path= setupValue().screenpath
fullpath = os.path.join(path,filename)

class CreateNewTag(unittest.TestCase):
    def test_newtagcreation(self):
        try:
            browserInstance = setupValue()
            adminfunction=Adminclass()
            browser = browserInstance.setupfunction()
            browser.implicitly_wait(5)
            LauncheTender1 = LauncheTenderclass()
            logOut=Userprofilemenu()
            browser = LauncheTender1.openURL(browser)
            browser = LauncheTender1.estimatorValidlogin(browser)
            orgInstance=Organizationclass()
            adminfunction.OpenTags(browser)
            fake = Factory.create()
            fakevalue=fake.name()
            tagString=str(fakevalue)
            adminfunction.TagCreation(browser,tagString)
            time.sleep(2)
            message= str('Tag '+tagString+' has been created')
            self.assertTrue(message in browser.page_source)
            browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\AdminEstimator.xml','eTender','TagSearchBox')).send_keys(tagString)
            time.sleep(2)
            self.assertEquals(browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\AdminEstimator.xml','eTender','TagValue')).get_attribute('innerHTML'),tagString)
        except Exception:
            logs.error("Validation with Test Case No: 100177 failed")
            browser.save_screenshot(fullpath)
            traceback.print_exc(file=sys.stdout)
            self.fail("Test Case No: 100177 failed")
            browser.implicitly_wait(5)
        finally:
            browser=logOut.logout_eTender(browser)
            LauncheTender1.closebrowser(browser)