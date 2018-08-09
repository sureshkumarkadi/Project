#-------------------------------------------------------------------------------
# Name:         AT_RemoveRoletoUser.py
#
# Tast Case Id  100112
#
# Purpose:      To Verify that role can be removed from the user
#
# Author:      mathew.jacob
#
# Created:     19/09/2016
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
orgLink=DataDriver()
ftime = time.mktime(time.localtime())
ptime=time.strftime("%d-%m-%Y_%H%M%S", time.localtime(ftime))
#filename = 'TestCase-100112-{0}.png'.format(ptime)
tf = 'test_removeroletoUser'
filename = 'Testcase-%s.png' %(tf)
path= setupValue().screenpath
fullpath = os.path.join(path,filename)
class RemoveRoletoUserInOrg(unittest.TestCase):
    def test_removeroletoUser(self):
        try:
            browserInstance = setupValue()
            browser = browserInstance.setupfunction()
            LauncheTender = LauncheTenderclass()
            browser = LauncheTender.openURL(browser)
            browser= LauncheTender.subcontractorValidlogin(browser)
            orgInstance=Organizationclass()
            logOut=Userprofilemenu()
            orgInstance.OpenaddUser(browser)
            browser=orgInstance.AddUserOrganization(browser)
            time.sleep(3)
            browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\Object.xml','eTender','saveButon')).click()
            orgInstance.OpenUserRole(browser)
            time.sleep(2)
            p=browser.find_elements_by_xpath(orgLink.readfromXML(folder_path+'\Object\Object.xml','eTender','emailrolebox'))
            p[1].send_keys(orgLink.readfromXML(folder_path+'\Data\Data.xml','eTender','userSaveEmail'))
            time.sleep(2)
            browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\Object.xml','eTender','adduserCheckbox')).click()
            time.sleep(2)
            browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\Object.xml','eTender','managerole')).click()
            time.sleep(2)
            Checkbox1= browser.find_elements_by_xpath(orgLink.readfromXML(folder_path+'\Object\Object.xml','eTender','adduserCheckbox'))
            Checkbox1[0].click()
            time.sleep(3)
            browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\Object.xml','eTender','checkboxSelectedAll')).click()
            time.sleep(3)
            Checkbox2= browser.find_elements_by_xpath(orgLink.readfromXML(folder_path+'\Object\Object.xml','eTender','adduserCheckbox'))
            Checkbox2[1].click()
            time.sleep(2)
            browser.find_element_by_id(orgLink.readfromXML(folder_path+'\Object\Object.xml','eTender','updatebutton')).click()
            time.sleep(2)
            buttonValue=browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\Object.xml','eTender','saveButon')).click()
            time.sleep(3)
            browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\Object.xml','eTender','resetButton')).click()
            time.sleep(3)
            self.assertFalse(orgLink.readfromXML(folder_path+'\Data\Data.xml','eTender','SupAdmin') in browser.page_source)
            logs.info("Test Case No : 100112 Passed Successfully")
        except Exception:
            logs.error("Validation with Test Case No: 100112 failed")
            browser.save_screenshot(fullpath)
            traceback.print_exc(file=sys.stdout)
            self.fail("Test Case No: 100112 failed")
            browser.implicitly_wait(5)
        finally:
            browser=logOut.logout_eTender(browser)
            LauncheTender.closebrowser(browser)

