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
import time
import os
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
from logouteTender import Userprofilemenu
##from RESTAPI import ReopentenderusingRESTAPIclass
from RESTAPIStaging import ReopentenderusingRESTAPIclass
from datadriven import DataDriver
from setupenviron import setupValue
from logdriver import logvalue
logs=logvalue.logger
logclose=logvalue()
ftime = time.mktime(time.localtime())
ptime=time.strftime("%d-%m-%Y_%H%M%S", time.localtime(ftime))
#filename = 'TestCase-100119-{0}.png'.format(ptime)
tf = 'test_declineStatusinEstiamtor'
filename = 'Testcase-%s.png' %(tf)
path= setupValue().screenpath
fullpath = os.path.join(path,filename)

#Test case number = 100119
class Declinestatusinestimator(unittest.TestCase):
    def test_declineStatusinEstiamtor(self):
        try:
            browserInstance = setupValue()
            browser = browserInstance.setupfunction()
            browser.implicitly_wait(5)
            time.sleep(1)
            LauncheTender1 = LauncheTenderclass()
            browser = LauncheTender1.openURL(browser)
            browser.implicitly_wait(5)
            time.sleep(1)
            browser = LauncheTender1.subcontractorValidlogin(browser)
            browser = LauncheTender1.verifyorganisationdetails(browser)
            browser = LauncheTender1.list_project(browser)
            time.sleep(1)
            tenderDetails = Tenderdetails()
            browser = tenderDetails.Subcontratorproject(browser)
            browser = tenderDetails.suppliertender(browser)
            time.sleep(1)
            tenderDetails_decline = SubmitTenderclass()
            browser.implicitly_wait(5)
            time.sleep(1)
            browser = tenderDetails_decline.declineTender(browser)
            browser = tenderDetails_decline.declineTenderSubmission(browser)
            time.sleep(1)
            Userprofilemenu_logout = Userprofilemenu()
            browser = Userprofilemenu_logout.logout_eTender(browser)
            time.sleep(1)
            browser = LauncheTender1.estimatorValidlogin(browser)
            time.sleep(1)
            browser = tenderDetails.estimatorProject(browser)
            time.sleep(1)
            browser = tenderDetails.estimatortender(browser)
            time.sleep(1)
            browser = tenderDetails.viewsupplierdetails(browser)
            time.sleep(1)
            browser = tenderDetails.tenderstatusinEstimator(browser)
            browser.implicitly_wait(5)

            declinestatus = DataDriver()
            #tenderstatus = []
            time.sleep(1)
            declinestatus_path = declinestatus.readfromXML(folder_path+'\Object\Object.xml','eTender','tenderstatusfordecline')
            tenderstatus = browser.find_element_by_xpath(declinestatus_path) #xpath for decline status in Estimator
            time.sleep(1)
            declinestatus = tenderstatus.text
            self.assertEqual(declinestatus,'Declined')
            logs.info("Test Case No : 100119 Passed Successfully")
        except Exception:
            logs.error("Validation with Test Case No: 100119 failed")
            browser.save_screenshot(fullpath)
            traceback.print_exc(file=sys.stdout)
            self.fail("Test Case No: 100119 failed")
            browser.implicitly_wait(5)
        finally:
            reopenTender = ReopentenderusingRESTAPIclass()
            time.sleep(1)
            accesstoken = reopenTender.AuthunticateAPI()
            time.sleep(1)
            reopenTender.ReopentenderusingRESTAPI(accesstoken)
            time.sleep(1)
            LauncheTender1.closebrowser(browser)