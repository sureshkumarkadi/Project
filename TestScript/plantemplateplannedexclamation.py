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
#filename = 'TestCase-100279-{0}.png'.format(ptime)
tf = 'test_Plantemplateplannedexclamation'
filename = 'Testcase-%s.png' %(tf)
path= setupValue().screenpath
fullpath = os.path.join(path,filename)

#Test case Number = 100279
class Plantemplateplannedexclamation(unittest.TestCase):
    def test_Plantemplateplannedexclamation(self):
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

            templateplanneddates1 = DataDriver()
            time.sleep(1)
            templateplanneddates = []
            templateplanneddates_path = templateplanneddates1.readfromXML(folder_path+'\Object\TenderplanObjects.xml','eTender','templateplanneddate')
            time.sleep(1)
            templateplanneddates = browser.find_elements_by_xpath(templateplanneddates_path)

            stag1planneddate = templateplanneddates[0].text

            planneddatestag1 = datetime.datetime.strptime(stag1planneddate , '%d-%b-%Y')

            time.sleep(2)

            planneddatestag1weekno1 = planneddatestag1.weekday()


            if planneddatestag1weekno1>=5:
                stag1dateplanned = 1

            else:
                stag1dateplanned = 0


            stag2planneddate = templateplanneddates[1].text


            planneddatestag2 = datetime.datetime.strptime(stag2planneddate , '%d-%b-%Y')

            time.sleep(2)

            planneddatestag2weekno1 = planneddatestag2.weekday()


            if planneddatestag2weekno1>=5:
                stag2dateplanned = 1

            else:
                stag2dateplanned = 0


            stag3planneddate = templateplanneddates[2].text


            planneddatestag3 = datetime.datetime.strptime(stag3planneddate , '%d-%b-%Y')

            time.sleep(2)

            planneddatestag3weekno1 = planneddatestag3.weekday()


            if planneddatestag3weekno1>=5:
                stag3dateplanned = 1

            else:
                stag3dateplanned = 0


            stag4planneddate = templateplanneddates[3].text


            planneddatestag4 = datetime.datetime.strptime(stag4planneddate , '%d-%b-%Y')

            time.sleep(2)

            planneddatestag4weekno1 = planneddatestag4.weekday()


            if planneddatestag4weekno1>=5:
                stag4dateplanned = 1

            else:
                stag4dateplanned = 0


            stag5planneddate = templateplanneddates[4].text


            planneddatestag5 = datetime.datetime.strptime(stag5planneddate , '%d-%b-%Y')

            time.sleep(2)

            planneddatestag5weekno1 = planneddatestag5.weekday()


            if planneddatestag5weekno1>=5:
                stag5dateplanned = 1

            else:
                stag5dateplanned = 0


            stag6planneddate = templateplanneddates[5].text


            planneddatestag6 = datetime.datetime.strptime(stag6planneddate , '%d-%b-%Y')

            time.sleep(2)

            planneddatestag6weekno1 = planneddatestag6.weekday()


            if planneddatestag6weekno1>=5:
                stag6dateplanned = 1

            else:
                stag6dateplanned = 0


            stag7planneddate = templateplanneddates[6].text


            planneddatestag7 = datetime.datetime.strptime(stag7planneddate , '%d-%b-%Y')

            time.sleep(2)

            planneddatestag7weekno1 = planneddatestag7.weekday()


            if planneddatestag7weekno1>=5:
                stag7dateplanned = 1

            else:
                stag7dateplanned = 0


            planneddates  =  stag1dateplanned + stag2dateplanned + stag3dateplanned + stag4dateplanned + stag5dateplanned + stag6dateplanned + stag7dateplanned


            if planneddates == 0:
                print("There are no weekends")
            elif planneddates == 1:
                    planneddateexclamation1 = DataDriver()
                    time.sleep(1)
                    planneddateexclamation = []
                    planneddateexclamation_path = planneddateexclamation1.readfromXML(folder_path+'\Object\TenderplanObjects.xml','eTender','planneddateexclamation')
                    time.sleep(1)
                    planneddateexclamation = browser.find_element_by_xpath(planneddateexclamation_path)
                    if planneddateexclamation.is_displayed():
                        print("Day is weekend hence planneddateexclamation is present")
            elif planneddates>=2:
                    planneddateexclamation1 = DataDriver()
                    time.sleep(1)
                    planneddateexclamation = []
                    planneddateexclamation_path = planneddateexclamation1.readfromXML(folder_path+'\Object\TenderplanObjects.xml','eTender','planneddateexclamation')
                    time.sleep(1)
                    planneddateexclamation = browser.find_elements_by_xpath(planneddateexclamation_path)
                    for exclamation in planneddateexclamation:
                        print (exclamation)
                    time.sleep(2)
                    if exclamation.is_displayed():
                        print("Day is weekend hence planneddateexclamation is present")
            logs.error("Validation with Test Case No: 100279 passed")
        except Exception:
            logs.error("Validation with Test Case No: 100279 failed")
            browser.save_screenshot(fullpath)
            traceback.print_exc(file=sys.stdout)
            self.fail("Test Case No: 100279 failed")
            browser.implicitly_wait(5)
        finally:
            time.sleep(1)
            LauncheTender1.closebrowser(browser)


















