#-------------------------------------------------------------------------------
# Name:         AT_FootnoteSettings
#
# Tast Case Id  100355
#
# Purpose:      To Verify that Foot Note is attaching with e-Mail template
#
# Author:      mathew.jacob
#
# Created:     01/12/2017
# Copyright:   (c) Causeway Technologies 2017
#-------------------------------------------------------------------------------

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
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
from selenium.common.exceptions import NoSuchElementException
logs=logvalue.logger
orgLink=DataDriver()
ftime = time.mktime(time.localtime())
ptime=time.strftime("%d-%m-%Y_%H%M%S", time.localtime(ftime))
#filename = 'TestCase-100355-{0}.png'.format(ptime)
tf = 'test_FootNote'
filename = 'Testcase-%s.png' %(tf)
path= setupValue().screenpath
fullpath = os.path.join(path,filename)
class FootNoteClass(unittest.TestCase):
    def test_FootNote(self):
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
            time.sleep(4)
            orgInstance=Organizationclass()
            orgInstance.OpenUserProfilePage(browser)
            time.sleep(2)
            browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\UserProfileObject.xml','eTender','SignatureBox')).clear()
            fakeValue = Factory.create()
            Signote=fakeValue.name()
            SignoteValue=str(Signote)
            browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\\Object\\UserProfileObject.xml','eTender','SignatureBox')).send_keys(SignoteValue)
            sbutton=browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\\Object\\UserProfileObject.xml','eTender','savebutton'))
            time.sleep(2)
            browser.execute_script("arguments[0].scrollIntoView(true);", sbutton)
            time.sleep(2)
            sbutton.click()
            adminfunction.EmailSetup(browser)
            time.sleep(2)
            footnote=browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\\Object\\EmailSetup.xml','eTender','FootNote')).get_attribute('innerText')
            time.sleep(2)
            time.sleep(3)
            sfootnote=str(footnote)
            sfootnote=sfootnote.strip()
            self.assertEquals(SignoteValue,sfootnote)
            logs.info("Test Case No : 100355 Passed Successfully")
        except Exception:
            logs.error("Test Case No: 100355 failed")
            browser.save_screenshot(fullpath)
            traceback.print_exc(file=sys.stdout)
            self.fail("Test Case No: 100355 failed")
        finally:
            browser=logOut.logout_eTender(browser)
            LauncheTender.closebrowser(browser)
