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
from datetime import timedelta
from datetime import datetime
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
#filename = 'TestCase-100266-{0}.png'.format(ptime)
tf = 'test_Plantemplatestagdurationupdation'
filename = 'Testcase-%s.png' %(tf)
path= setupValue().screenpath
fullpath = os.path.join(path,filename)

#Test case Number = 100266
class Plantemplatestagdurationupdation(unittest.TestCase):
    def test_Plantemplatestagdurationupdation(self):
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

            browser = tendertemplate.stagdurationupdate(browser) #Update duration
            time.sleep(2)

            browser = tendertemplate.tenderplansave(browser)#plan template save
            time.sleep(2)

            templateplanneddates1 = DataDriver()
            time.sleep(1)
            templateplanneddates = []
            templateplanneddates_path = templateplanneddates1.readfromXML(folder_path+'\Object\TenderplanObjects.xml','eTender','templateplanneddate')
            time.sleep(1)
            templateplanneddates = browser.find_elements_by_xpath(templateplanneddates_path)
            time.sleep(2)

            templatforecastdate1 = DataDriver()
            time.sleep(1)
            templatforecastdate = []
            templatforecastdate_path = templatforecastdate1.readfromXML(folder_path+'\Object\TenderplanObjects.xml','eTender','templateforecastdate')
            time.sleep(1)
            templatforecastdate = browser.find_elements_by_id(templatforecastdate_path)
            time.sleep(2)
            forecastdatestag6 = templatforecastdate[5].get_attribute('value')

            forecastdatestag7 = templatforecastdate[6].get_attribute('value')


            time.sleep(2)
            self.assertEqual(forecastdatestag6.strip(),templateplanneddates[6].text)

            time.sleep(1)
            forecastdate1 = datetime.strptime(forecastdatestag6.strip(),'%d-%b-%Y')

            add10days_to_forecastdate = forecastdate1 + timedelta(days=10)

            add10days_to_forecastdate1 = datetime.strftime(add10days_to_forecastdate,'%d-%b-%Y')

            self.assertEqual(add10days_to_forecastdate1,forecastdatestag7.strip())

            logs.info("Test Case No : 100266 Passed Successfully")
        except Exception:
            logs.error("Validation with Test Case No: 100266 failed")
            browser.save_screenshot(fullpath)
            traceback.print_exc(file=sys.stdout)
            self.fail("Test Case No: 100266 failed")
            browser.implicitly_wait(5)
        finally:
            time.sleep(1)
            LauncheTender1.closebrowser(browser)





















