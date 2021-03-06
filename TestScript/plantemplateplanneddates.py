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
from tenderDetails import Tenderdetails
from datadriven import DataDriver
from setupenviron import setupValue
from logouteTender import Userprofilemenu
from logdriver import logvalue
from TenderModification import TenderClass
logs=logvalue.logger
logclose=logvalue()
ftime = time.mktime(time.localtime())
ptime=time.strftime("%d-%m-%Y_%H%M%S", time.localtime(ftime))
#filename = 'TestCase-100277-{0}.png'.format(ptime)
tf = 'test_Plantemplateplanneddates'
filename = 'Testcase-%s.png' %(tf)
path= setupValue().screenpath
fullpath = os.path.join(path,filename)

#Test case Number = 100277
class Plantemplateplanneddates(unittest.TestCase):
    def test_Plantemplateplanneddates(self):
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
            tenderDetails = Tenderdetails()

            browser = tenderDetails.Subcontratorproject(browser)
            time.sleep(2)
            browser = tenderDetails.estimatortender2(browser)
            time.sleep(2)
            browser = tendertemplate.estimatortenderpalntender(browser) #Go to Tender plan tender
            #time.sleep(1)
            #browser = tendertemplate.estimatortenderplan(browser) #Select Tenderplan from dropdown list
            time.sleep(5)

            dateafter10days = tendertemplate.plantemplateplanneddates(browser) #Planned dates validation
            time.sleep(2)

            templateplanneddates1 = DataDriver()
            time.sleep(1)
            templateplanneddates = []
            templateplanneddates_path = templateplanneddates1.readfromXML(folder_path+'\Object\TenderplanObjects.xml','eTender','templateplanneddate')
            time.sleep(1)
            templateplanneddates = browser.find_elements_by_xpath(templateplanneddates_path)
            time.sleep(2)
            self.assertEqual(templateplanneddates[0].text,dateafter10days[0])
            self.assertEqual(templateplanneddates[1].text,dateafter10days[1])
            self.assertEqual(templateplanneddates[2].text,dateafter10days[2])
            self.assertEqual(templateplanneddates[3].text,dateafter10days[3])
            self.assertEqual(templateplanneddates[4].text,dateafter10days[4])
            self.assertEqual(templateplanneddates[5].text,dateafter10days[5])
            self.assertEqual(templateplanneddates[6].text,dateafter10days[6])

            logs.info("Test Case No : 100277 Passed Successfully")
        except Exception:
            logs.error("Validation with Test Case No: 100277 failed")
            browser.save_screenshot(fullpath)
            traceback.print_exc(file=sys.stdout)
            self.fail("Test Case No: 100277 failed")
            browser.implicitly_wait(5)
        finally:
            time.sleep(1)
            LauncheTender1.closebrowser(browser)