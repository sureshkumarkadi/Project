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
#filename = 'TestCase-100140-{0}.png'.format(ptime)
tf = 'test_registerestimatorusertypes'
filename = 'Testcase-%s.png' %(tf)
path= setupValue().screenpath
fullpath = os.path.join(path,filename)

#Test case Number =100140
class Registerestimatorusertypes(unittest.TestCase):
    def test_registerestimatorusertypes(self):
        try:
            browserInstance = setupValue()
            browser = browserInstance.setupfunction()
            browser.implicitly_wait(5)
            LauncheTender1 = LauncheTenderclass()
            browser = LauncheTender1.openURL(browser)
            registration = RegistrationineT()
            browser = registration.register(browser)
            time.sleep(1)
            browser = registration.selectmaincontractorRole(browser)
            time.sleep(1)
            ValidateestimatorRoles = DataDriver()
            time.sleep(1)
            estimatorroles = []
            estimatorroles_path = ValidateestimatorRoles.readfromXML(folder_path+'\Object\Object.xml','eTender','estimatorroles')
            estimatorroles = browser.find_elements_by_xpath(estimatorroles_path)
            time.sleep(1)
            estimator = estimatorroles[0].text
            estimatoradmin = estimatorroles[1].text
            time.sleep(1)
            self.assertEqual(estimator, 'Estimator')
            self.assertEqual(estimatoradmin, 'Estimator Admin')
            logs.info("Test Case No : 100140 Passed Successfully")
        except Exception:
            logs.error("Validation with Test Case No: 100140 failed")
            browser.save_screenshot(fullpath)
            traceback.print_exc(file=sys.stdout)
            self.fail("Test Case No: 100140 failed")
            browser.implicitly_wait(5)
        finally:
            LauncheTender1.closebrowser(browser)