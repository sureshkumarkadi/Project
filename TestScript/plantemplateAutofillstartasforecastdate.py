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
#filename = 'TestCase-100320-{0}.png'.format(ptime)
tf = 'test_plantemplateAutofillstartasforecastdate'
filename = 'Testcase-%s.png' %(tf)
path= setupValue().screenpath
fullpath = os.path.join(path,filename)

#Test case Number = 100320
class PlantemplateAutofillstartasforecastdate(unittest.TestCase):
    def test_plantemplateAutofillstartasforecastdate(self):
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

            tenderclass = TenderClass()

            NewTender = tenderclass.TenderCreation(browser)
            time.sleep(3)

            browser = tenderDetails.estimatortender2(browser)
            time.sleep(2)

            browser = tendertemplate.estimatortenderpalntender(browser) #Go to Tender plan tender
            time.sleep(1)
            browser = tendertemplate.estimatortenderplan(browser) #Select plan template
            time.sleep(2)

            browser = tendertemplate.plantemplateselectionfromlist(browser) # choose plan from the list
            time.sleep(1)
            browser = tendertemplate.plantemplateselect(browser) # Save the plan
            time.sleep(5)

            browser = tendertemplate.autofillselect(browser) # select Auto fille
            time.sleep(1)

            browser = tendertemplate.datepickerselectforautofill(browser) # select date picker
            time.sleep(1)

            browser = tendertemplate.selectstartdateasforecast(browser) # select the forecast date
            time.sleep(1)

            browser = tendertemplate.forecastdatesave(browser) # Save the details
            time.sleep(2)

            dateafter10days = tendertemplate.plantemplatestartdateasforecastdate(browser) #forecast dates validation
            time.sleep(2)

            templatforecastdate1 = DataDriver()
            time.sleep(1)
            templatforecastdate = []
            templatforecastdate_path = templatforecastdate1.readfromXML(folder_path+'\Object\TenderplanObjects.xml','eTender','templateforecastdate')
            time.sleep(1)
            templatforecastdate = browser.find_elements_by_id(templatforecastdate_path)
            time.sleep(2)
            forecastdatestag1 = templatforecastdate[0].get_attribute('value')
            forecastdatestag2 = templatforecastdate[1].get_attribute('value')
            forecastdatestag3 = templatforecastdate[2].get_attribute('value')
            forecastdatestag4 = templatforecastdate[3].get_attribute('value')
            forecastdatestag5 = templatforecastdate[4].get_attribute('value')
            forecastdatestag6 = templatforecastdate[5].get_attribute('value')
            forecastdatestag7 = templatforecastdate[6].get_attribute('value')

            time.sleep(2)
            self.assertEqual(forecastdatestag1.strip(),dateafter10days[0])
            self.assertEqual(forecastdatestag2.strip(),dateafter10days[1])
            self.assertEqual(forecastdatestag3.strip(),dateafter10days[2])
            self.assertEqual(forecastdatestag4.strip(),dateafter10days[3])
            self.assertEqual(forecastdatestag5.strip(),dateafter10days[4])
            self.assertEqual(forecastdatestag6.strip(),dateafter10days[5])
            self.assertEqual(forecastdatestag7.strip(),dateafter10days[6])

            logs.info("Test Case No : 100320 Passed Successfully")
            time.sleep(1)
            browser = tendertemplate.tenderplansave(browser)
            time.sleep(1)
            browser = tenderDetails.Subcontratorproject(browser)
            time.sleep(1)
            browser = tendertemplate.TenderDeletion(browser)
            time.sleep(1)
            browser = tendertemplate.plantemplatemenu(browser)
            time.sleep(1)
            browser = tendertemplate.plantemplateselection(browser)
            time.sleep(1)
            browser = tendertemplate.plantemplatedelete(browser)
            time.sleep(1)
        except Exception:
            logs.error("Validation with Test Case No: 100320 failed")
            browser.save_screenshot(fullpath)
            traceback.print_exc(file=sys.stdout)
            self.fail("Test Case No: 100320 failed")
            browser.implicitly_wait(5)
        finally:
            LauncheTender1.closebrowser(browser)