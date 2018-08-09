#-------------------------------------------------------------------------------
# Name:         AT_NotificationAddReceipients
#
# Tast Case Id  100170
#
# Purpose       To Verify adding receipients fucntionality with notification
#
# Author:      mathew.jacob
#
# Created:     15/02/2017
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
#filename = 'TestCase-100170-{0}.png'.format(ptime)
tf = 'test_AddUsernotification'
filename = 'Testcase-%s.png' %(tf)
path= setupValue().screenpath
fullpath = os.path.join(path,filename)

class NotificationaddUser(unittest.TestCase):
    def test_AddUsernotification(self):
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
            orgInstance.OpenaddUser(browser)
            browser=orgInstance.AddUserOrganization(browser)
            browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\Object.xml','eTender','saveButon')).click()
            adminfunction=Adminclass()
            adminfunction.OpenNotificationRecipients(browser)
            time.sleep(3)
            p=browser.find_elements_by_xpath(orgLink.readfromXML(folder_path+'\Object\Object.xml','eTender','emailrolebox'))
            time.sleep(2)
            p[1].send_keys(orgLink.readfromXML(folder_path+'\Data\Data.xml','eTender','userSaveEmail'))
            browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\Object.xml','eTender','adduserCheckbox')).click()
            browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\Object.xml','eTender','saveButon')).click()
            time.sleep(2)
            adminfunction.OpenTags(browser)
            adminfunction.OpenNotificationRecipients(browser)
            p=browser.find_elements_by_xpath(orgLink.readfromXML(folder_path+'\Object\Object.xml','eTender','emailrolebox'))
            p[1].send_keys(orgLink.readfromXML(folder_path+'\Data\Data.xml','eTender','userSaveEmail'))
            time.sleep(2)
            self.assertTrue(browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\AdminEstimator.xml','eTender','Usercheckbox')))

        except Exception:
            logs.error("Validation with Test Case No: 100170 failed")
            browser.save_screenshot(fullpath)
            traceback.print_exc(file=sys.stdout)
            self.fail("Test Case No: 100170 failed")
            browser.implicitly_wait(5)
        finally:
            browser=logOut.logout_eTender(browser)
            LauncheTender1.closebrowser(browser)