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
from selenium import webdriver
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
#filename = 'TestCase-100357-{0}.png'.format(ptime)
tf = 'test_TenderverificationOFF'
filename = 'Testcase-%s.png' %(tf)
path= setupValue().screenpath
fullpath = os.path.join(path,filename)

#Test case Number = 100357
class TenderverificationOFF(unittest.TestCase):
    def test_TenderverificationOFF(self):
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
            tenderverifybutton1 = DataDriver()
            tenderverifybutton = []
            tenderverifybutton_path = tenderverifybutton1.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','tenderverifybutton')
            time.sleep(1)
            tenderverifybutton = browser.find_elements_by_xpath(tenderverifybutton_path) #Webelement for values
            time.sleep(1)
            if len(tenderverifybutton) == 6:
                print("Tender verification button is not present")
            else:
                self.fail("Tender verification button is present")

            logs.info("Test Case No : 100357 Passed Successfully")
        except Exception:
            logs.error("Validation with Test Case No: 100357 failed")
            browser.save_screenshot(fullpath)
            traceback.print_exc(file=sys.stdout)
            self.fail("Test Case No: 100357 failed")
            browser.implicitly_wait(5)
        finally:
            reopenTender = ReopentenderusingRESTAPIclass()
            time.sleep(1)
            accesstoken = reopenTender.AuthunticateAPI()
            time.sleep(1)
            reopenTender.ReopentenderusingRESTAPI(accesstoken)
            time.sleep(1)
            LauncheTender1.closebrowser(browser)