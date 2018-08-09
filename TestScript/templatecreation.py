#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      suresh.kumar
#
# Created:     12/07/2017
# Copyright:   (c) suresh.kumar 2017
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
sys.path.insert(0,folder_path+"\Syslibrary")
sys.path.insert(0,folder_path+"\Data")
sys.path.insert(0,folder_path+"\Object")
from launcheTender import LauncheTenderclass
from Tenderplan import Tenderplans
from tenderDetails import SubmitTenderclass
from datadriven import DataDriver
from setupenviron import setupValue
from logouteTender import Userprofilemenu
from logdriver import logvalue
logs=logvalue.logger
logclose=logvalue()
ftime = time.mktime(time.localtime())
ptime=time.strftime("%d-%m-%Y_%H%M%S", time.localtime(ftime))
#filename = 'TestCase-100245-{0}.png'.format(ptime)
tf = 'test_Templatecreation'
filename = 'Testcase-%s.png' %(tf)
path= setupValue().screenpath
fullpath = os.path.join(path,filename)

#Test case Number = 100245
class Templatecreation(unittest.TestCase):
    def test_Templatecreation(self):
        try:
            browserInstance = setupValue()
            browser = browserInstance.setupfunction()
            browser.implicitly_wait(5)
            time.sleep(1)
            LauncheTender1 = LauncheTenderclass()
            browser = LauncheTender1.openURL(browser)
            time.sleep(1)
            browser = LauncheTender1.estimatorValidlogin(browser)
            time.sleep(1)
            tendertemplate = Tenderplans()
            browser = tendertemplate.plantemplatemenu(browser)
            time.sleep(1)
            browser = tendertemplate.plantemplatebutton(browser)
            time.sleep(1)
            browser = tendertemplate.plantemplatecreation(browser)
            time.sleep(3)

            tender_template = DataDriver()
            time.sleep(1)
            tendertemplatename_path = tender_template.readfromXML(folder_path+'\Object\TenderplanObjects.xml','eTender','listtemplatename')
            tendertemplatename = browser.find_element_by_xpath(tendertemplatename_path)
            time.sleep(1)
            self.assertEqual(tendertemplatename.text,'procurement')
            time.sleep(1)

            tendertemplatedescription_path = tender_template.readfromXML(folder_path+'\Object\TenderplanObjects.xml','eTender','listtemplatedescription')
            tendertemplatedescription = browser.find_element_by_xpath(tendertemplatedescription_path)
            time.sleep(1)
            self.assertEqual(tendertemplatedescription.text,'procurement materials')
            time.sleep(1)
            logs.info("Test Case No : 100245 Passed Successfully")
        except Exception:
            logs.error("Validation with Test Case No: 100245 failed")
            browser.save_screenshot(fullpath)
            traceback.print_exc(file=sys.stdout)
            self.fail("Test Case No: 100245 failed")
            browser.implicitly_wait(5)
        finally:
            LauncheTender1.closebrowser(browser)
















