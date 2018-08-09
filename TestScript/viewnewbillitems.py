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
sys.path.insert(0,folder_path+"\Env")
from launcheTender import LauncheTenderclass
from tenderDetails import Tenderdetails
from tenderDetails import SubmitTenderclass
from datadriven import DataDriver
from setupenviron import setupValue
from logouteTender import Userprofilemenu
from logdriver import logvalue
logs=logvalue.logger
logclose=logvalue()
ftime = time.mktime(time.localtime())
ptime=time.strftime("%d-%m-%Y_%H%M%S", time.localtime(ftime))
#filename = 'TestCase-100318-{0}.png'.format(ptime)
tf = 'test_viewnewbillitems'
filename = 'Testcase-%s.png' %(tf)
path= setupValue().screenpath
fullpath = os.path.join(path,filename)

#Test case Number = 100318
class Viewnewbillitems(unittest.TestCase):
    def test_viewnewbillitems(self):
        try:
            browserInstance = setupValue()
            browser = browserInstance.setupfunction()
            browser.implicitly_wait(5)
            LauncheTender1 = LauncheTenderclass()
            browser = LauncheTender1.openURL(browser)
            browser.implicitly_wait(5)
            browser = LauncheTender1.subcontractorValidlogin(browser)
            browser = LauncheTender1.list_Organisation(browser)
            browser = LauncheTender1.verifyorganisationdetails(browser)
            browser = LauncheTender1.list_project(browser)
            tenderDetails = Tenderdetails()
            browser = tenderDetails.Subcontratorproject(browser)
            browser = tenderDetails.suppliertender(browser)
            browser = tenderDetails.selectFilter(browser)
            time.sleep(1)
            browser = tenderDetails.selectnewbillitems(browser)
            browser = tenderDetails.closefilter(browser)
            time.sleep(1)
            newbillitems_XML = DataDriver()
            newbillitems = []
            newbillitems_path = newbillitems_XML.readfromXML(folder_path+'\Object\Estimatorvalue.xml','eTender','pricableitems')
            newbillitems = browser.find_elements_by_xpath(newbillitems_path) #Webelement for values
            time.sleep(1)
##            newbillitems1 =  newbillitems[1].text
##            newbillitems2 =  newbillitems[4].text
##            newbillitems3 =  newbillitems[7].text
            time.sleep(1)

            env = newbillitems_XML.readfromXML(folder_path+'\Env\Setup.xml','eTender','env')


            if env == 'StageURL':

                newbillitems1 =  newbillitems[1].text
                newbillitems2 =  newbillitems[4].text
                #newbillitems3 =  newbillitems[7].text

                self.assertEqual(newbillitems1,'New Bill item')
                #self.assertEqual(newbillitems2,'65 mm thick; curved work')
                self.assertEqual(newbillitems2,'80 mm thick')
                logs.info("Test Case No : 100318 Passed Successfully")

            if env == 'PreStageURL':

                newbillitems1 =  newbillitems[1].text
                newbillitems2 =  newbillitems[4].text
                newbillitems3 =  newbillitems[7].text

                self.assertEqual(newbillitems1,'New Bill item')
                self.assertEqual(newbillitems2,'80 mm thick')
                self.assertEqual(newbillitems3,'65 mm thick; curved work')
                logs.info("Test Case No : 100318 Passed Successfully")
        except Exception:
            logs.error("Validation with Test Case No: 100318 failed")
            browser.save_screenshot(fullpath)
            traceback.print_exc(file=sys.stdout)
            self.fail("Test Case No: 100318 failed")
            browser.implicitly_wait(5)
        finally:
            LauncheTender1.closebrowser(browser)