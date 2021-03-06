#-------------------------------------------------------------------------------
# Name:         AT_NotificationTemplateSave
#
# Tast Case Id  100181
#
# Purpose       TO verify that notification message is saving in the template
#
# Author:      mathew.jacob
#
# Created:     16/03/2017
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
#filename = 'TestCase-100181-{0}.png'.format(ptime)
tf = 'test_MessageTemplateSave'
filename = 'Testcase-%s.png' %(tf)
path= setupValue().screenpath
fullpath = os.path.join(path,filename)

class NotificationTemplateSave(unittest.TestCase):
    def test_MessageTemplateSave(self):
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
            p=browser.find_element_by_class_name(orgLink.readfromXML(folder_path+'\Object\AdminEstimator.xml','eTender','TemplateTextBox'))
            p.clear()
            browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\AdminEstimator.xml','eTender','User')).click()
            time.sleep(1)
            browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\AdminEstimator.xml','eTender','Organization')).click()
            time.sleep(1)
            browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\AdminEstimator.xml','eTender','Project')).click()
            time.sleep(1)
            browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\AdminEstimator.xml','eTender','Tender')).click()
            time.sleep(3)
            browser.find_element_by_link_text(orgLink.readfromXML(folder_path+'\Object\AdminEstimator.xml','eTender','SaveBtn')).click()
            time.sleep(2)
            browser.find_element_by_link_text(orgLink.readfromXML(folder_path+'\Data\AdminEstimatorData.xml','eTender','MessageLinkSelection')).click()
            time.sleep(2)
            Nuser=str("["+orgLink.readfromXML(folder_path+'\Data\AdminEstimatorData.xml','eTender','user')+"]")
            Norganization=str("["+orgLink.readfromXML(folder_path+'\Data\AdminEstimatorData.xml','eTender','organization')+"]")
            Nproject=str("["+orgLink.readfromXML(folder_path+'\Data\AdminEstimatorData.xml','eTender','project')+"]")
            Ntender=str("["+orgLink.readfromXML(folder_path+'\Data\AdminEstimatorData.xml','eTender','tender')+"]")
            time.sleep(2)
            self.assertTrue(Nuser in browser.page_source)
            self.assertTrue(Nuser in browser.page_source)
            self.assertTrue(Nuser in browser.page_source)
            self.assertTrue(Nuser in browser.page_source)

        except Exception:
            logs.error("Validation with Test Case No: 100181 failed")
            browser.save_screenshot(fullpath)
            traceback.print_exc(file=sys.stdout)
            self.fail("Test Case No: 100181 failed")
            browser.implicitly_wait(5)
        finally:
            browser=logOut.logout_eTender(browser)
            LauncheTender.closebrowser(browser)