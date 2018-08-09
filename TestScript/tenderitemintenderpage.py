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
#filename = 'TestCase-100314-{0}.png'.format(ptime)
tf = 'test_Tenderitemintenderpage'
filename = 'Testcase-%s.png' %(tf)
path= setupValue().screenpath
fullpath = os.path.join(path,filename)

#Test case Number = 100314
class Tenderitemintenderpage(unittest.TestCase):
    def test_Tenderitemintenderpage(self):
        try:
            browserInstance = setupValue()
            browser = browserInstance.setupfunction()
            browser.implicitly_wait(5)
            time.sleep(1)
            LauncheTender1 = LauncheTenderclass()
            browser = LauncheTender1.openURL(browser)
            time.sleep(1)
            browser = LauncheTender1.estimatorValidlogin(browser)
            time.sleep(5)
            tendertemplate = Tenderplans()
            tenderDetails = Tenderdetails()
            itemdetails = ItemDetails()

            browser = tenderDetails.Subcontratorproject(browser)
            time.sleep(2)
            tenderclass = TenderClass()

            browser = itemdetails.localtender(browser) #Go to new tender
            time.sleep(1)
            #browser = itemdetails.estimatoritemdefault(browser) #Select Details from dropdown list
            #time.sleep(1)

            browser = itemdetails.edititems(browser) #click edit tender items button
            time.sleep(1)

            browser = itemdetails.additemclick(browser) #click add items button
            time.sleep(1)

            browser = itemdetails.additem(browser) #Enter item details to create new item
            time.sleep(1)

            browser = itemdetails.additemsave(browser) #Save item details
            time.sleep(1)

            browser = itemdetails.tenderlink(browser) #Click on tender at the top
            time.sleep(1)

            itemsintender1 = DataDriver()
            itemsintender = []
            time.sleep(1)
            itemsintender_path = itemsintender1.readfromXML(folder_path+'\Object\Itemsobject.xml','eTender','itemsintender')
            itemsintender = browser.find_elements_by_xpath(itemsintender_path)
            time.sleep(1)
            self.assertEqual(itemsintender[1].text,'10 mm brick')
            self.assertEqual(itemsintender[4].text,'General works')

            logs.info("Test Case No : 100314 Passed Successfully")
            time.sleep(1)

        except Exception:
            logs.error("Validation with Test Case No: 100314 failed")
            browser.save_screenshot(fullpath)
            traceback.print_exc(file=sys.stdout)
            self.fail("Test Case No: 100314 failed")
            browser.implicitly_wait(5)
        finally:
            LauncheTender1.closebrowser(browser)