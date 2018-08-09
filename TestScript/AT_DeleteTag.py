#-------------------------------------------------------------------------------
# Name:         AT_DeleteTag.py
#
# Purpose:      To check deletion of tag is working fine
#
# Tast Case Id  100122
#
# Author:      mathew.jacob
#
# Created:     16/02/2017
#
# Copyright:   (c) Causeway Technologies 2016
#-------------------------------------------------------------------------------
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
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
#filename = 'TestCase-100122-{0}.png'.format(ptime)
tf = 'test_tagdeletion'
filename = 'Testcase-%s.png' %(tf)
path= setupValue().screenpath
fullpath = os.path.join(path,filename)

class DeleteTag(unittest.TestCase):
    def test_tagdeletion(self):
        try:
            browserInstance = setupValue()
            adminfunction=Adminclass()
            browser = browserInstance.setupfunction()
            LauncheTender = LauncheTenderclass()
            browser = LauncheTender.openURL(browser)
            browser = LauncheTender.estimatorValidlogin(browser)
            orgInstance=Organizationclass()
            adminfunction.OpenTags(browser)
            logOut=Userprofilemenu()
            fake = Factory.create()
            fakevalue=fake.name()
            tagString=str(fakevalue)
            adminfunction.TagCreation(browser,tagString)
            time.sleep(3)
            adminfunction.TagDeletion(browser,tagString)
            time.sleep(2)
            message= str('Tag '+tagString+' has been deleted')
            self.assertTrue(message in browser.page_source)
            time.sleep(2)
            browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\AdminEstimator.xml','eTender','TagNewSearchBox')).clear()
            browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\AdminEstimator.xml','eTender','TagNewSearchBox')).send_keys(tagString)
            try:
                browser.find_element_by_xpath(browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\AdminEstimator.xml','eTender','TagValue')))
            except NoSuchElementException:
                logs.info("Test Case No : 100122 Passed Successfully")
                return True
            return False
        except Exception:
            logs.error("Validation with Test Case No: 100122 failed")
            browser.save_screenshot(fullpath)
            traceback.print_exc(file=sys.stdout)
            self.fail("Test Case No: 100122 failed")
            browser.implicitly_wait(5)
        finally:
            browser=logOut.logout_eTender(browser)
            LauncheTender.closebrowser(browser)
