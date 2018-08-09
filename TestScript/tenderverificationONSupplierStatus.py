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
#filename = 'TestCase-100358-{0}.png'.format(ptime)
tf = 'test_TenderverificationONSupplierStatus'
filename = 'Testcase-%s.png' %(tf)
path= setupValue().screenpath
fullpath = os.path.join(path,filename)

#Test case Number = 100358
class TenderverificationONSupplierStatus(unittest.TestCase):
    def test_TenderverificationONSupplierStatus(self):
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
            browser = LauncheTender1.subcontractorValidlogin(browser)
            #browser = LauncheTender1.list_Organisation(browser)
            #browser = LauncheTender1.verifyorganisationdetails(browser)
            browser = LauncheTender1.list_project(browser)
            time.sleep(1)
            browser = tenderDetails.Subcontratorproject(browser)
            time.sleep(2)
            tenderverifySupplierstatus1 = DataDriver()
            tenderverifySupplierstatus_path = tenderverifySupplierstatus1.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','tenderverifySupplierstatus')
            time.sleep(1)
            tenderverifySupplierstatus = browser.find_element_by_xpath(tenderverifySupplierstatus_path) #Webelement for values
            time.sleep(1)
            self.assertEqual(tenderverifySupplierstatus.text,'Review pending')
            logs.info("Test Case No : 100358 Passed Successfully")
        except Exception:
            logs.error("Validation with Test Case No: 100358 failed")
            browser.save_screenshot(fullpath)
            traceback.print_exc(file=sys.stdout)
            self.fail("Test Case No: 100358 failed")
            browser.implicitly_wait(5)
        finally:
            LauncheTender1.closebrowser(browser)

if __name__ == '__main__':
    unittest.main()