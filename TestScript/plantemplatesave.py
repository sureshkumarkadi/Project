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
#filename = 'TestCase-100258-{0}.png'.format(ptime)
tf = 'test_Plantemplatesave'
filename = 'Testcase-%s.png' %(tf)
path= setupValue().screenpath
fullpath = os.path.join(path,filename)

#Test case Number = 100258
class Plantemplatesave(unittest.TestCase):
    def test_Plantemplatesave(self):
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

            todaydate2 = tendertemplate.gettodaydate() #Get todaysdate
            time.sleep(1)

            browser = tendertemplate.stagactualdate(browser)
            time.sleep(3)

            browser = tendertemplate.tenderplansave(browser)
            time.sleep(2)

            Stagstatus1 = DataDriver()
            time.sleep(1)
            selecteditems = []
            stagstatus_path = Stagstatus1.readfromXML(folder_path+'\Object\TenderplanObjects.xml','eTender','stagstatus')
            stagstatus = browser.find_element_by_xpath(stagstatus_path)
            time.sleep(1)

            self.assertEqual(stagstatus.text,'Completed')

            todaysdate = []

            todaysdate1 = DataDriver()
            time.sleep(1)
            todaysdate_path = todaysdate1.readfromXML(folder_path+'\Object\TenderplanObjects.xml','eTender','actualdate')
            time.sleep(1)
            todaysdate = browser.find_elements_by_xpath(todaysdate_path)
            time.sleep(1)
            todaysdate4 = todaysdate[0].get_attribute('value')
            time.sleep(1)
            todaysdate2 = str(todaysdate4)
            todaysdate3 = todaysdate2.strip()
            time.sleep(1)

            self.assertEqual(todaysdate3,todaydate2)

            logs.info("Test Case No : 100258 Passed Successfully")
        except Exception:
            logs.error("Validation with Test Case No: 100258 failed")
            browser.save_screenshot(fullpath)
            traceback.print_exc(file=sys.stdout)
            self.fail("Test Case No: 100258 failed")
            browser.implicitly_wait(5)
        finally:
            time.sleep(2)
            LauncheTender1.closebrowser(browser)




























