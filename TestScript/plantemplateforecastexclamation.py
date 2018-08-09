#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      suresh.kumar
#
# Created:     30/07/2017
# Copyright:   (c) suresh.kumar 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from selenium.webdriver.support.ui import WebDriverWait
import unittest
import sys
import os
import time
import traceback
import datetime
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
#filename = 'TestCase-100270-{0}.png'.format(ptime)
tf = 'test_Plantemplateforecastexclamation'
filename = 'Testcase-%s.png' %(tf)
path= setupValue().screenpath
fullpath = os.path.join(path,filename)

#Test case Number = 100270
class Plantemplateforecastexclamation(unittest.TestCase):
    def test_Plantemplateforecastexclamation(self):
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

            templateforecastdates1 = DataDriver()
            time.sleep(1)
            templateforecastdates = []
            templateforecastdates_path = templateforecastdates1.readfromXML(folder_path+'\Object\TenderplanObjects.xml','eTender','templateforecastdate')
            time.sleep(1)
            templateforecastdates = browser.find_elements_by_id(templateforecastdates_path)

            stag1forecastdate = templateforecastdates[0].get_attribute('value').strip()


            forecastdatestag1 = datetime.datetime.strptime(stag1forecastdate , '%d-%b-%Y')

            time.sleep(2)

            forecastdatestag1weekno1 = forecastdatestag1.weekday()


            if forecastdatestag1weekno1>=5:
                stag1dateforecast = 1

            else:
                stag1dateforecast = 0


            stag2forecastdate = templateforecastdates[1].get_attribute('value').strip()


            forecastdatestag2 = datetime.datetime.strptime(stag2forecastdate , '%d-%b-%Y')

            time.sleep(2)

            forecastdatestag2weekno1 = forecastdatestag2.weekday()


            if forecastdatestag2weekno1>=5:
                stag2dateforecast = 1

            else:
                stag2dateforecast = 0


            stag3forecastdate = templateforecastdates[2].get_attribute('value').strip()


            forecastdatestag3 = datetime.datetime.strptime(stag3forecastdate , '%d-%b-%Y')

            time.sleep(2)

            forecastdatestag3weekno1 = forecastdatestag3.weekday()


            if forecastdatestag3weekno1>=5:
                stag3dateforecast = 1

            else:
                stag3dateforecast = 0


            stag4forecastdate = templateforecastdates[3].get_attribute('value').strip()


            forecastdatestag4 = datetime.datetime.strptime(stag4forecastdate , '%d-%b-%Y')

            time.sleep(2)

            forecastdatestag4weekno1 = forecastdatestag4.weekday()


            if forecastdatestag4weekno1>=5:
                stag4dateforecast = 1

            else:
                stag4dateforecast = 0


            stag5forecastdate = templateforecastdates[4].get_attribute('value').strip()


            forecastdatestag5 = datetime.datetime.strptime(stag5forecastdate , '%d-%b-%Y')

            time.sleep(2)

            forecastdatestag5weekno1 = forecastdatestag5.weekday()


            if forecastdatestag5weekno1>=5:
                stag5dateforecast = 1

            else:
                stag5dateforecast = 0


            stag6forecastdate = templateforecastdates[5].get_attribute('value').strip()


            forecastdatestag6 = datetime.datetime.strptime(stag6forecastdate , '%d-%b-%Y')

            time.sleep(2)

            forecastdatestag6weekno1 = forecastdatestag6.weekday()


            if forecastdatestag6weekno1>=5:
                stag6dateforecast = 1

            else:
                stag6dateforecast = 0


            stag7forecastdate = templateforecastdates[6].get_attribute('value').strip()


            forecastdatestag7 = datetime.datetime.strptime(stag7forecastdate , '%d-%b-%Y')

            time.sleep(2)

            forecastdatestag7weekno1 = forecastdatestag7.weekday()


            if forecastdatestag7weekno1>=5:
                stag7dateforecast = 1

            else:
                stag7dateforecast = 0


            forecastdates  =  stag1dateforecast + stag2dateforecast + stag3dateforecast + stag4dateforecast + stag5dateforecast + stag6dateforecast + stag7dateforecast


            if forecastdates == 0:
                print("There are no weekends")
            elif forecastdates == 1:
                    forecastdateexclamation1 = DataDriver()
                    time.sleep(1)
                    forecastdateexclamation = []
                    forecastdateexclamation_path = forecastdateexclamation1.readfromXML(folder_path+'\Object\TenderplanObjects.xml','eTender','forecastdateexclamation')
                    time.sleep(1)
                    forecastdateexclamation = browser.find_element_by_xpath(forecastdateexclamation_path)
                    time.sleep(2)
                    if forecastdateexclamation.is_displayed():
                        print("Day is weekend hence forecastdateexclamation is present")
            elif forecastdates>=2:
                    forecastdateexclamation1 = DataDriver()
                    time.sleep(1)
                    forecastdateexclamation = []
                    forecastdateexclamation_path = forecastdateexclamation1.readfromXML(folder_path+'\Object\TenderplanObjects.xml','eTender','forecastdateexclamation')
                    time.sleep(1)
                    forecastdateexclamation = browser.find_elements_by_xpath(forecastdateexclamation_path)
                    for exclamation in forecastdateexclamation:
                        print (exclamation)
                    time.sleep(2)
                    if exclamation.is_displayed():
                        print("Day is weekend hence forecastdateexclamation is present")
            logs.error("Validation with Test Case No: 100270 passed")
        except Exception:
            logs.error("Validation with Test Case No: 100270 failed")
            browser.save_screenshot(fullpath)
            traceback.print_exc(file=sys.stdout)
            self.fail("Test Case No: 100270 failed")
            browser.implicitly_wait(5)
        finally:
            time.sleep(1)
            LauncheTender1.closebrowser(browser)


















