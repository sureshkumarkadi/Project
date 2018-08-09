#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      suresh.kumar
#
# Created:     25/08/2016
# Copyright:   (c) mathew.jacob 2016
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
#filename = 'TestCase-100243-{0}.png'.format(ptime)
tf = 'test_Plantemplate'
filename = 'Testcase-%s.png' %(tf)
path= setupValue().screenpath
fullpath = os.path.join(path,filename)

#Test case Number = 100243
class Plantemplate(unittest.TestCase):
    def test_Plantemplate(self):
        try:
                browserInstance = setupValue()
                browser = browserInstance.setupfunction()
                browser.implicitly_wait(5)
                time.sleep(1)
                LauncheTender1 = LauncheTenderclass()
                browser = LauncheTender1.openURL(browser)
                time.sleep(1)
                browser = LauncheTender1.estimatorValidlogin(browser)
                time.sleep(5)
                #browser = LauncheTender1.switchOrganisation(browser)
                time.sleep(1)
                #browser = LauncheTender1.selectsecondOrganisation(browser)
                #time.sleep(7)
                tendertemplate = Tenderplans()
                browser = tendertemplate.plantemplatemenu(browser)
                time.sleep(1)
                tender_template = DataDriver()
                time.sleep(1)
                tendertemplateheading_path = tender_template.readfromXML(folder_path+'\Object\TenderplanObjects.xml','eTender','plantemplateheading')
                tendertemplateheading = browser.find_element_by_xpath(tendertemplateheading_path) #tendertemplate heading
                time.sleep(1)
                self.assertEqual(tendertemplateheading.text,'Plan template listing')
                time.sleep(1)
                logs.info("Test Case No : 100243 Passed Successfully")
        except Exception:
            logs.error("Validation with Test Case No: 100243 failed")
            browser.save_screenshot(fullpath)
            traceback.print_exc(file=sys.stdout)
            self.fail("Test Case No: 100243 failed")
            browser.implicitly_wait(5)
        finally:
            time.sleep(1)
            LauncheTender1.closebrowser(browser)