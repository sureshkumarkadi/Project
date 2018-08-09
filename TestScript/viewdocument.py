#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      suresh.kumar
#
# Created:     24/01/2017
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
sys.path.insert(0,folder_path+"\Env")
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
#filename = 'TestCase-100057-{0}.png'.format(ptime)
tf = 'test_viewdocument'
filename = 'Testcase-%s.png' %(tf)
path= setupValue().screenpath
fullpath = os.path.join(path,filename)

#Test case number = 100057
class Viewdocument(unittest.TestCase):
    def test_viewdocument(self):
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
            browser = LauncheTender1.list_Organisation(browser)
            time.sleep(1)
            browser = LauncheTender1.verifyorganisationdetails(browser)
            browser = LauncheTender1.list_project(browser)
            tenderDetails = Tenderdetails()
            time.sleep(1)
            browser = tenderDetails.Subcontratorproject(browser)
            browser = tenderDetails.suppliertender(browser)
            time.sleep(1)
            browser = tenderDetails.tenderdocument(browser)
            time.sleep(2)
            browser = tenderDetails.uploadTendererdocument(browser)
            time.sleep(1)
            browser = tenderDetails.closedocumentwindow(browser)
            time.sleep(1)
            tenderDetails_submit = SubmitTenderclass()
            time.sleep(3)
            browser = tenderDetails_submit.submitTender(browser)
            time.sleep(1)
            browser = tenderDetails_submit.confirmTendersubmission(browser)
            time.sleep(1)
            Userprofilemenu_logout = Userprofilemenu()
            browser = Userprofilemenu_logout.logout_eTender(browser)
            time.sleep(1)
            browser = LauncheTender1.estimatorValidlogin(browser)
            time.sleep(1)
            browser = tenderDetails.estimatorProject(browser)
            time.sleep(1)
            browser = tenderDetails.viewsupplierdetails(browser)
            time.sleep(1)
            document_count = DataDriver()
            documentcount_path = document_count.readfromXML(folder_path+'\Object\Object.xml','eTender','documentcountEstimator') #Delete option exists after uploading docs
            time.sleep(1)
            document_count = browser.find_element_by_xpath(documentcount_path) #Delete option
            time.sleep(1)
            documentcount = document_count.text
            self.assertEqual(documentcount,'2')
            time.sleep(1)
            browser = tenderDetails.opendocumentswindow(browser)
            time.sleep(1)
            document_count_view = DataDriver()
            document_count_viewlist = []
            documentcount__view_path = document_count_view.readfromXML(folder_path+'\Object\Object.xml','eTender','documentviewEstimator') #Delete option exists after uploading docs
            time.sleep(1)
            document_count_viewlist = browser.find_elements_by_xpath(documentcount__view_path)
            time.sleep(1)
            document_count_view1 = document_count_viewlist[0].text
            document_count_view2 = document_count_viewlist[1].text
            time.sleep(1)
            self.assertEqual(document_count_view1,'donotdeletefromDesktop.xlsx')
            self.assertEqual(document_count_view2,'donotdeletefromDesktop.xlsx')
            time.sleep(1)
            browser = tenderDetails.closedocumentwindow(browser)
            time.sleep(1)
            browser = Userprofilemenu_logout.logout_eTender(browser)
            time.sleep(1)
            reopenTender = ReopentenderusingRESTAPIclass()
            time.sleep(1)
            accesstoken = reopenTender.AuthunticateAPI()
            time.sleep(1)
            reopenTender.ReopentenderusingRESTAPI(accesstoken)
            time.sleep(1)
            browser = LauncheTender1.subcontractorValidlogin(browser)
            time.sleep(2)
            browser = LauncheTender1.list_Organisation(browser)
            time.sleep(1)
            browser = LauncheTender1.list_project(browser)
            time.sleep(1)
            browser = tenderDetails.Subcontratorproject(browser)
            time.sleep(1)
            browser = tenderDetails.suppliertender(browser)
            time.sleep(1)
            browser = tenderDetails.tenderdocument(browser)
            time.sleep(1)
            browser = tenderDetails.deletedocuments(browser)
            time.sleep(2)
            logs.info("Test Case No : 100057 Passed Successfully")
        except Exception:
            logs.error("Validation with Test Case No: 100057 failed")
            browser.save_screenshot(fullpath)
            traceback.print_exc(file=sys.stdout)
            self.fail("Test Case No: 100057 failed")
            browser.implicitly_wait(5)
        finally:
            LauncheTender1.closebrowser(browser)











