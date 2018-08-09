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
tf = 'test_TenderverificationONStatus'
filename = 'Testcase-%s.png' %(tf)
path= setupValue().screenpath
fullpath = os.path.join(path,filename)

#Test case Number = 100383
class TenderverificationONStatus(unittest.TestCase):
    def test_TenderverificationONStatus(self):
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
            browser = tenderDetails.generalsettings(browser)
            time.sleep(1)
            browser = tenderDetails.tenderverifyON(browser)
            time.sleep(1)
            browser = tenderDetails.generalsettingssave(browser)
            time.sleep(1)

            Userprofilemenu_logout = Userprofilemenu()
            time.sleep(1)
            browser = Userprofilemenu_logout.logout_eTender(browser)
            time.sleep(4)
            browser = LauncheTender1.subcontractorValidlogin(browser)
            browser = LauncheTender1.list_Organisation(browser)
            browser = LauncheTender1.verifyorganisationdetails(browser)
            browser = LauncheTender1.list_project(browser)
            time.sleep(1)
            browser = tenderDetails.Subcontratorproject(browser)
            browser = tenderDetails.suppliertender(browser)
            time.sleep(1)
            tenderDetails_submit = SubmitTenderclass()
            time.sleep(1)
            browser = tenderDetails_submit.submitTender(browser)
            time.sleep(1)
            browser = tenderDetails_submit.confirmTendersubmission(browser)
            time.sleep(1)
            Userprofilemenu_logout = Userprofilemenu()
            time.sleep(1)
            browser = Userprofilemenu_logout.logout_eTender(browser)
            time.sleep(2)
            browser = LauncheTender1.estimatorValidlogin(browser)
            time.sleep(2)
            browser = tenderDetails.estimatorProject(browser)
            time.sleep(1)
            browser = tenderDetails.estimatortender(browser)
            time.sleep(1)
            browser = tenderDetails.viewsupplierdetails(browser)
            time.sleep(2)
            tenderverifystatus1 = DataDriver()
            tenderverifystatus_path = tenderverifystatus1.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','tenderverifystatus')
            time.sleep(1)
            tenderverifystatus = browser.find_element_by_xpath(tenderverifystatus_path) #Webelement for values
            time.sleep(1)
            self.assertEqual(tenderverifystatus.text,'Review pending')
            logs.info("Test Case No : 100383 Passed Successfully")
        except Exception:
            logs.error("Validation with Test Case No: 100383 failed")
            browser.save_screenshot(fullpath)
            traceback.print_exc(file=sys.stdout)
            self.fail("Test Case No: 100383 failed")
            browser.implicitly_wait(5)
        finally:
            LauncheTender1.closebrowser(browser)

if __name__ == '__main__':
    unittest.main()