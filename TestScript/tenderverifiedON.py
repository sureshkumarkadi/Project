#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      mathew.jacob
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
from tenderDetails import Tenderdetails
from tenderDetails import SubmitTenderclass
from datadriven import DataDriver
from setupenviron import setupValue
from logouteTender import Userprofilemenu
##from RESTAPI import ReopentenderusingRESTAPIclass
from RESTAPIStaging import ReopentenderusingRESTAPIclass
from logdriver import logvalue
logs=logvalue.logger
logclose=logvalue()
ftime = time.mktime(time.localtime())
ptime=time.strftime("%d-%m-%Y_%H%M%S", time.localtime(ftime))
#filename = 'TestCase-100383-{0}.png'.format(ptime)
tf = 'test_TenderverifiedON'
filename = 'Testcase-%s.png' %(tf)
path= setupValue().screenpath
fullpath = os.path.join(path,filename)

#Test case Number = 100383
class TenderverifiedON(unittest.TestCase):
    def test_TenderverifiedON(self):
        try:
            browserInstance = setupValue()
            browser = browserInstance.setupfunction()
            browser.implicitly_wait(5)
            time.sleep(1)
            LauncheTender1 = LauncheTenderclass()
            browser = LauncheTender1.openURL(browser)
            browser.implicitly_wait(5)
            time.sleep(1)
            tenderDetails = Tenderdetails()
            time.sleep(1)
            browser = LauncheTender1.estimatorValidlogin(browser)
            time.sleep(4)
            browser = tenderDetails.estimatorProject(browser)
            time.sleep(1)
            browser = tenderDetails.estimatortender(browser)
            time.sleep(1)
            browser = tenderDetails.clicktenderverifybutton(browser)
            time.sleep(1)
            browser = tenderDetails.tenderverifyconfirm(browser)
            time.sleep(1)
            tenderverified1 = DataDriver()
            tenderverified_path = tenderverified1.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','tenderverified')
            time.sleep(1)
            tenderverified = browser.find_element_by_xpath(tenderverified_path) #Webelement for values
            time.sleep(1)
            if tenderverified.is_displayed():
                print("Tender is verified")
            else:
                print("Tender is not verified")
                self.fail("Tender is not verified")
            logs.info("Test Case No : 100383 Passed Successfully")
        except Exception:
            logs.error("Validation with Tender is verified")
            browser.save_screenshot(fullpath)
            traceback.print_exc(file=sys.stdout)
            self.fail("Test Case No: 100383 failed")
            browser.implicitly_wait(5)
        finally:

            browser = tenderDetails.generalsettings(browser)
            time.sleep(1)
            browser = tenderDetails.tenderverifyOFF(browser)
            time.sleep(1)
            browser = tenderDetails.generalsettingssave(browser)
            time.sleep(1)
            reopenTender = ReopentenderusingRESTAPIclass()
            time.sleep(1)
            accesstoken = reopenTender.AuthunticateAPI()
            time.sleep(1)
            reopenTender.ReopentenderusingRESTAPI(accesstoken)
            time.sleep(1)
            LauncheTender1.closebrowser(browser)

if __name__ == '__main__':
    unittest.main()