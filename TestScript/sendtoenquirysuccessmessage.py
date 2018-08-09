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
from Tradexsuppliers import Tradexsupplier
from datadriven import DataDriver
from setupenviron import setupValue
from logouteTender import Userprofilemenu
from logdriver import logvalue
logs=logvalue.logger
logclose=logvalue()
ftime = time.mktime(time.localtime())
ptime=time.strftime("%d-%m-%Y_%H%M%S", time.localtime(ftime))
#filename = 'TestCase-100238-{0}.png'.format(ptime)
tf = 'test_sendtoenquirysuccessmessage'
filename = 'Testcase-%s.png' %(tf)
path= setupValue().screenpath
fullpath = os.path.join(path,filename)

#Test case Number = 100238
class Sendtoenquirysuccessmessage(unittest.TestCase):
    def test_sendtoenquirysuccessmessage(self):
        try:
            browserInstance = setupValue()
            browser = browserInstance.setupfunction()
            browser.implicitly_wait(5)
            time.sleep(1)
            LauncheTender1 = LauncheTenderclass()
            browser = LauncheTender1.openURL(browser)
            browser.implicitly_wait(5)
            time.sleep(1)
            browser = LauncheTender1.estimatorValidlogin(browser)
            time.sleep(1)
            tenderDetails = Tenderdetails()
            browser = tenderDetails.estimatorProject(browser)
            time.sleep(1)

            tradexsupplierDetails = Tradexsupplier()
            browser = tenderDetails.estimatortendertradex(browser)
            time.sleep(2)
            browser = tenderDetails.viewsupplierdetails(browser)
            time.sleep(1)
            browser = tradexsupplierDetails.estimatortradexaddsupplier(browser)
            time.sleep(2)
            browser = tradexsupplierDetails.entersupplier(browser)
            time.sleep(2)
            browser = tradexsupplierDetails.viewtradexsupplierdetails(browser)
            time.sleep(2)
            browser = tradexsupplierDetails.selectsuppliercontact(browser)
            time.sleep(2)
            browser = tradexsupplierDetails.sendenquirytosupplier(browser)
            time.sleep(2)

            sendenquirysuccessmessage = DataDriver()
            sendenquirysuccessmessage_path = sendenquirysuccessmessage.readfromXML(folder_path+'\Object\Tradex.xml','eTender','sendenquirysuccessmessage')
            time.sleep(1)
            sendenquirysuccessmessage_list = browser.find_element_by_xpath(sendenquirysuccessmessage_path) #send enquiry success message

            self.assertEqual(sendenquirysuccessmessage_list.text,'Tender enquiry has been sent to the selected supplier(s)')

            time.sleep(1)

            logs.info("Test Case No : 100238 Passed Successfully")
        except Exception:
            logs.error("Validation with Test Case No: 100238 failed")
            browser.save_screenshot(fullpath)
            traceback.print_exc(file=sys.stdout)
            self.fail("Test Case No: 100238 failed")
            browser.implicitly_wait(5)
        finally:
            LauncheTender1.closebrowser(browser)