#-------------------------------------------------------------------------------
# Name:         AT_NotificationMessageTemplate
#
# Tast Case Id  100082
#
# Purpose       TO verify notification message option in Notification messages section
#
# Author:      mathew.jacob
#
# Created:     15/03/2017
#
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
sys.path.insert(0,folder_path+"\Syslibrary")
sys.path.insert(0,folder_path+"\Data")
sys.path.insert(0,folder_path+"\Object")
from launcheTender import LauncheTenderclass
from datadriven import DataDriver
from setupenviron import setupValue
from logdriver import logvalue
from AdminEstimator import Adminclass
from logouteTender import Userprofilemenu
orgLink=DataDriver()
logs=logvalue.logger
logclose=logvalue()
ftime = time.mktime(time.localtime())
ptime=time.strftime("%d-%m-%Y_%H%M%S", time.localtime(ftime))
#filename = 'TestCase-100082-{0}.png'.format(ptime)
tf = 'test_MessageTemplateOption'
filename = 'Testcase-%s.png' %(tf)
path= setupValue().screenpath
fullpath = os.path.join(path,filename)

class NotificationMessageTemplate(unittest.TestCase):
    def test_MessageTemplateOption(self):
        try:
            browserInstance = setupValue()
            adminfunction=Adminclass()
            browser = browserInstance.setupfunction()
            LauncheTender = LauncheTenderclass()
            logOut=Userprofilemenu()
            browser = LauncheTender.openURL(browser)
            browser = LauncheTender.estimatorValidlogin1(browser)
            adminfunction=Adminclass()
            adminfunction.NotificationMessages(browser)
            time.sleep(3)
            browser.find_element_by_link_text(orgLink.readfromXML(folder_path+'\Data\AdminEstimatorData.xml','eTender','MessageLinkSelection')).click()
            time.sleep(3)
            rValue=str(orgLink.readfromXML(folder_path+'\Data\AdminEstimatorData.xml','eTender','MessageLinkSelection'))
            TextMessage ='Notification message '+'-'+' '+rValue
            self.assertTrue(TextMessage in browser.page_source)
            self.assertTrue('User' in browser.page_source)
            self.assertTrue('Organisation' in browser.page_source)
            self.assertTrue('Project' in browser.page_source)
            self.assertTrue('Tender' in browser.page_source)
        except Exception:
            logs.error("Validation with Test Case No: 100082 failed")
            browser.save_screenshot(fullpath)
            traceback.print_exc(file=sys.stdout)
            self.fail("Test Case No: 100082 failed")
            browser.implicitly_wait(5)
        finally:
            browser=logOut.logout_eTender(browser)
            LauncheTender.closebrowser(browser)