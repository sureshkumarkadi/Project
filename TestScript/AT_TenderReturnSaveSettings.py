#-------------------------------------------------------------------------------
# Name:         AT_TenderReturnSaveSettings
#
# Tast Case Id  100381
#
# Purpose:      To Verify that Save option for Tender Return Verificaiton working
#
# Author:      mathew.jacob
#
# Created:     04/12/2017
# Copyright:   (c) Causeway Technologies 2017
#-------------------------------------------------------------------------------

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException
import unittest
import sys
import os
import time
import traceback
from faker import Factory
from datetime import datetime,date

dir_path = os.path.dirname(os.path.realpath(__file__))
folder_path=os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0,folder_path+"\Library")
sys.path.insert(0,folder_path+"\Env")
from launcheTender import LauncheTenderclass
from setupenviron import setupValue
from logdriver import logvalue
from datadriven import DataDriver
from TenderModification import TenderClass
from logouteTender import Userprofilemenu
from AdminEstimator import Adminclass
from OrganizationFunction import Organizationclass
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
logs=logvalue.logger
orgLink=DataDriver()
ftime = time.mktime(time.localtime())
ptime=time.strftime("%d-%m-%Y_%H%M%S", time.localtime(ftime))
#filename = 'TestCase-100381-{0}.png'.format(ptime)
tf = 'test_TenderReturnSaveVerify'
filename = 'Testcase-%s.png' %(tf)
path= setupValue().screenpath
fullpath = os.path.join(path,filename)
class TenderVerifySave(unittest.TestCase):
    def test_TenderReturnSaveVerify(self):
        try:
            browserInstance = setupValue()
            browser = browserInstance.setupfunction()
            browser.implicitly_wait(10)
            LauncheTender = LauncheTenderclass()
            TenderAction=TenderClass()
            adminfunction=Adminclass()
            logOut=Userprofilemenu()
            browser = LauncheTender.openURL(browser)
            browser = LauncheTender.estimatorValidlogin1(browser)
            time.sleep(3)
            adminfunction.GeneralSettings(browser)
            time.sleep(2)
            try:
                ButtonTrue=browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\GeneralSettings.xml','eTender','TenderReturnTrue'))
                ButtonTrue.click()
                browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\GeneralSettings.xml','eTender','SaveBtn')).click()
                time.sleep(2)
                adminfunction.OpenTags(browser)
                adminfunction.GeneralSettings(browser)
                time.sleep(2)
                try:
                    browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\GeneralSettings.xml','eTender','TenderReturnFalse'))
                except NoSuchElementException:
                    return False
            except NoSuchElementException:
                try:
                    ButtonFalse=browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\GeneralSettings.xml','eTender','TenderReturnFalse'))
                    ButtonFalse.click()
                    time.sleep(2)
                    browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\GeneralSettings.xml','eTender','SaveBtn')).click()
                    adminfunction.OpenTags(browser)
                    adminfunction.GeneralSettings(browser)
                    time.sleep(2)
                    try:
                        browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\GeneralSettings.xml','eTender','TenderReturnTrue'))
                    except NoSuchElementException:
                        return False
                except NoSuchElementException:
                    return False
            logs.info("Test Case No : 100381 Passed Successfully")
            return True
        except Exception:
            logs.error("Test Case No: 100381 failed")
            browser.save_screenshot(fullpath)
            traceback.print_exc(file=sys.stdout)
            self.fail("Test Case No: 100381 failed")
        finally:
            browser=logOut.logout_eTender(browser)
            LauncheTender.closebrowser(browser)