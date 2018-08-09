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
import datetime
import traceback
dir_path = os.path.dirname(os.path.realpath(__file__))
folder_path=os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0,folder_path+"\Library")
sys.path.insert(0,folder_path+"\Syslibrary")
sys.path.insert(0,folder_path+"\Data")
sys.path.insert(0,folder_path+"\Object")
from launcheTender import LauncheTenderclass
from eTenderUpdateProjectDetails import updatedetails
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
#filename = 'TestCase-100290-{0}.png'.format(ptime)
tf = 'test_Plantemplatestagstatuscompleted'
filename = 'Testcase-%s.png' %(tf)
path= setupValue().screenpath
fullpath = os.path.join(path,filename)

#Test case Number = 100290
class Plantemplatestagstatuscompleted(unittest.TestCase):
    def test_Plantemplatestagstatuscompleted(self):
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
            tenderclass = TenderClass()
            browser = tendertemplate.estimatortenderpalntender(browser) #Go to Tender plan tender
            #time.sleep(1)
            #browser = tendertemplate.estimatortenderplan(browser) #Select Tenderplan from dropdown list
            time.sleep(5)

            browser = tendertemplate.tenderplansave(browser)
            time.sleep(2)

            Stagstatus1 = DataDriver()
            time.sleep(1)
            selecteditems = []
            stagstatus_path = Stagstatus1.readfromXML(folder_path+'\Object\TenderplanObjects.xml','eTender','stagstatus')
            stagstatus = browser.find_element_by_xpath(stagstatus_path)
            time.sleep(1)

            self.assertEqual(stagstatus.text,'Completed')

            logs.info("Test Case No : 100290 Passed Successfully")
            time.sleep(2)
            browser = tenderDetails.Subcontratorproject(browser)
            time.sleep(1)
            browser = tendertemplate.TenderDeletion(browser)
            time.sleep(1)
        except Exception:
            logs.error("Validation with Test Case No: 100290 failed")
            browser.save_screenshot(fullpath)
            traceback.print_exc(file=sys.stdout)
            self.fail("Test Case No: 100290 failed")
            browser.implicitly_wait(5)
        finally:
            LauncheTender1.closebrowser(browser)