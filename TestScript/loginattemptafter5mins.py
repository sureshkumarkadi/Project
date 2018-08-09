#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      suresh.kumar
#
# Created:     25-08-2016
# Copyright:   (c) suresh.kumar 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import unittest
import sys
import time
import os
import traceback
from selenium.webdriver.support.ui import WebDriverWait
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
logs=logvalue.logger
logclose=logvalue()
ftime = time.mktime(time.localtime())
ptime=time.strftime("%d-%m-%Y_%H%M%S", time.localtime(ftime))
#filename = 'TestCase-TC1046-{0}.png'.format(ptime)
tf = 'test_loginattemptafter5mins'
filename = 'Testcase-%s.png' %(tf)
path= setupValue().screenpath
fullpath = os.path.join(path,filename)

#Test case no:TC1046
class Loginattemptafter5mins(unittest.TestCase):
    def test_loginattemptafter5mins(self):
        try:
            time.sleep(300)
            browserInstance = setupValue()
            browser = browserInstance.setupfunction()
            browser.implicitly_wait(5)
            time.sleep(1)
            LauncheTender1 = LauncheTenderclass()
            browser = LauncheTender1.openURL(browser)
            browser.implicitly_wait(5)
            time.sleep(1)
            browser = LauncheTender1.estimatorValidlogin(browser)
            time.sleep(4)
##            browser = LauncheTender1.switchOrganisation(browser)
##            time.sleep(1)
##            browser = LauncheTender1.selectsecondOrganisation(browser)
##            time.sleep(7)
            estimator_login = DataDriver()
            projectlist1 = estimator_login.readfromXML(folder_path+'\Object\Object.xml','eTender','projectlist') #Project
            time.sleep(3)
            project_list = browser.find_element_by_link_text(projectlist1)
            time.sleep(3)
            project_list1  = project_list.text
            self.assertEqual(project_list1,'Test Project')
            time.sleep(2)
            logs.info("Test Case No : 100046 Passed Successfully")
        except Exception:
            logs.error("Validation with Test Case No: 100046 failed")
            browser.save_screenshot(fullpath)
            traceback.print_exc(file=sys.stdout)
            self.fail("Test Case No: 100046 failed")
            browser.implicitly_wait(5)
        finally:
            LauncheTender1.closebrowser(browser)