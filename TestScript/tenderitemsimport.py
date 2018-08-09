#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      suresh.kumar
#
# Created:     12/07/2017
# Copyright:   (c) suresh.kumar 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
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
from Tenderplan import Tenderplans
from tenderDetails import Tenderdetails
from Itemdetails import ItemDetails
from datadriven import DataDriver
from setupenviron import setupValue
from logouteTender import Userprofilemenu
from logdriver import logvalue
from TenderModification import TenderClass
logs=logvalue.logger
logclose=logvalue()
ftime = time.mktime(time.localtime())
ptime=time.strftime("%d-%m-%Y_%H%M%S", time.localtime(ftime))
#filename = 'TestCase-100317-{0}.png'.format(ptime)
tf = 'test_Tenderitemsimport'
filename = 'Testcase-%s.png' %(tf)
path= setupValue().screenpath
fullpath = os.path.join(path,filename)

#Test case Number = 100317
class Tenderitemsimport(unittest.TestCase):
    def test_Tenderitemsimport(self):
        try:

            browserInstance = setupValue()
            browser = browserInstance.setupfunction()
            browser.implicitly_wait(5)
            time.sleep(1)

            setup = DataDriver()

            env = setup.readfromXML(folder_path+'\Env\Setup.xml','eTender','browser')


            if env == 'firefox':
                LauncheTender1 = LauncheTenderclass()
                browser = LauncheTender1.openURL(browser)
                time.sleep(1)
                browser = LauncheTender1.estimatorValidlogin1(browser)
                time.sleep(5)
                tendertemplate = Tenderplans()
                tenderDetails = Tenderdetails()
                itemdetails = ItemDetails()

                browser = tenderDetails.Subcontratorproject(browser)
                time.sleep(2)
                tenderclass = TenderClass()

                browser = tendertemplate.estimatortenderpalntender(browser) #Go to new tenderE:\etender\TestScript\tenderitemsimport.py
                time.sleep(1)
                browser = itemdetails.estimatoritemdefault(browser) #Select Details from dropdown list
                time.sleep(1)

                browser = itemdetails.edititems(browser) #click edit tender items button
                time.sleep(1)

                browser = itemdetails.importlink(browser) #Click on Import link
                time.sleep(1)

                browser = itemdetails.importitems(browser) #Import Items from excel
                time.sleep(1)

                browser = itemdetails.additemsave(browser) #Save item details
                time.sleep(1)

                importitems_excel = DataDriver()
                time.sleep(1)
                importitemsexcel_path = importitems_excel.readfromXML(folder_path+'\Object\Itemsobject.xml','eTender','itemsintender')
                importitemsexcel = browser.find_elements_by_xpath(importitemsexcel_path)
                time.sleep(1)
                self.assertEqual(importitemsexcel[1].text,'GROUNDWORK')
                time.sleep(2)

                validateitemsexcel_path = importitems_excel.readfromXML(folder_path+'\Object\Itemsobject.xml','eTender','itemdescription')
                validateitemsexcel = browser.find_element_by_xpath(validateitemsexcel_path)
                time.sleep(1)
                self.assertEqual(validateitemsexcel.text,'machine loading')
                time.sleep(2)

                logs.info("Test Case No : 100317 Passed Successfully")
                time.sleep(1)
            elif env == 'chrome':
                print("chrome does not support uploading documents using AUTOIT")

        except Exception:
            logs.error("Validation with Test Case No: 100317 failed")
            browser.save_screenshot(fullpath)
            traceback.print_exc(file=sys.stdout)
            self.fail("Test Case No: 100317 failed")
            browser.implicitly_wait(5)
        finally:
            LauncheTender1 = LauncheTenderclass()
            LauncheTender1.closebrowser(browser)


























