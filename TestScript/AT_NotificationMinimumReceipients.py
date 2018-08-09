#-------------------------------------------------------------------------------
# Name:         AT_NotificationMinimumReceipients
#
# Tast Case Id  100171
#
# Purpose:      TO verify Minimum one receipients required for notification
#
# Author:      mathew.jacob
#
# Created:     15/02/2017
#
# Copyright:   (c) Causeway Technologies 2016
#
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
#filename = 'TestCase-100171-{0}.png'.format(ptime)
tf = 'test_MinimumUsernotification'
filename = 'Testcase-%s.png' %(tf)
path= setupValue().screenpath
fullpath = os.path.join(path,filename)

#Test case no:100046
class NotificationMinimumUser(unittest.TestCase):
    def test_MinimumUsernotification(self):
        try:
            browserInstance = setupValue()
            adminfunction=Adminclass()
            logOut=Userprofilemenu()
            browser = browserInstance.setupfunction()
            browser.implicitly_wait(5)
            LauncheTender1 = LauncheTenderclass()
            browser = LauncheTender1.openURL(browser)
            browser = LauncheTender1.estimatorValidlogin(browser)
            adminfunction=Adminclass()
            adminfunction.OpenNotificationRecipients(browser)
            time.sleep(3)
            browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\Object.xml','eTender','adduserCheckbox')).click()
            browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\Object.xml','eTender','checkboxSelectedAll')).click()
            browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\Object.xml','eTender','saveButon')).click()
            time.sleep(2)
            self.assertTrue(orgLink.readfromXML(folder_path+'\Data\AdminEstimatorData.xml','eTender','NotificationMessage') in browser.page_source)
            logs.info("Test Case No : 100171 Passed Successfully")
        except Exception:
            logs.error("Validation with Test Case No: 100171 failed")
            browser.save_screenshot(fullpath)
            traceback.print_exc(file=sys.stdout)
            self.fail("Test Case No: 100171 failed")
            browser.implicitly_wait(5)
        finally:
            browser=logOut.logout_eTender(browser)
            LauncheTender1.closebrowser(browser)