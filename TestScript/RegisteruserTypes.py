#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      suresh.kumar
#
# Created:     25/08/2016
# Copyright:   (c) suresh.kumar 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
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
from Registration import RegistrationineT
#from DBConnectMySQLdeleteORG import deleteorganisation
from datadriven import DataDriver
from setupenviron import setupValue
from logdriver import logvalue
logs=logvalue.logger
logclose=logvalue()
ftime = time.mktime(time.localtime())
ptime=time.strftime("%d-%m-%Y_%H%M%S", time.localtime(ftime))
#filename = 'TestCase-100139-{0}.png'.format(ptime)
tf = 'test_registerusertypes'
filename = 'Testcase-%s.png' %(tf)
path= setupValue().screenpath
fullpath = os.path.join(path,filename)

#Test case Number =100139
class Registerusertypes(unittest.TestCase):
    def test_registerusertypes(self):
        try:
            browserInstance = setupValue()
            browser = browserInstance.setupfunction()
            browser.implicitly_wait(5)
            LauncheTender1 = LauncheTenderclass()
            browser = LauncheTender1.openURL(browser)
            registration = RegistrationineT()
            browser = registration.register(browser)
            time.sleep(1)
            ValidatecontractorRole = DataDriver()
            time.sleep(1)
            contractorrole = []
            supplier_path = ValidatecontractorRole.readfromXML(folder_path+'\Object\Object.xml','eTender','contractorrole')
            contractorrole = browser.find_elements_by_xpath(supplier_path)
            time.sleep(1)
            #maincontractor_path = ValidatesupplierRole.readfromXML(folder_path+'\Object\Object.xml','eTender','selectmaincontractorrole')
            #contractorrole = browser.find_element_by_xpath(maincontractor_path)
            time.sleep(1)
            if contractorrole[0].is_displayed() and contractorrole[1].is_displayed():
                print("pass")
            else:
                self.fail("Validation with Test Case No: 100139 failed")
            time.sleep(1)
            logs.info("Test Case No : 100139 Passed Successfully")
        except Exception:
            logs.error("Validation with Test Case No: 100139 failed")
            browser.save_screenshot(fullpath)
            traceback.print_exc(file=sys.stdout)
            self.fail("Test Case No: 100139 failed")
            browser.implicitly_wait(5)
        finally:
            LauncheTender1.closebrowser(browser)