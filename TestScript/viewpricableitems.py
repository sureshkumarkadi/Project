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
from logdriver import logvalue
logs=logvalue.logger
logclose=logvalue()
ftime = time.mktime(time.localtime())
ptime=time.strftime("%d-%m-%Y_%H%M%S", time.localtime(ftime))
#filename = 'TestCase-100061-{0}.png'.format(ptime)
tf = 'test_viewpricableitems'
filename = 'Testcase-%s.png' %(tf)
path= setupValue().screenpath
fullpath = os.path.join(path,filename)

#Test case Number = 100061
class Viewpricableitems(unittest.TestCase):
    def test_viewpricableitems(self):
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
            time.sleep(1)
            browser = tenderDetails.estimatorProject(browser)
            browser = tenderDetails.estimatortender(browser)
            browser = tenderDetails.selectFilter(browser)
            time.sleep(1)
            browser = tenderDetails.selectpricableitems(browser)
            browser = tenderDetails.closefilter(browser)
            time.sleep(1)
            pricableitems_XML = DataDriver()
            pricableitems = []
            pricableitems_path = pricableitems_XML.readfromXML(folder_path+'\Object\Estimatorvalue.xml','eTender','pricableitems')
            pricableitems = browser.find_elements_by_xpath(pricableitems_path) #Webelement for values
            time.sleep(1)
            pricableitems1 =  pricableitems[1].text
            pricableitems2 =  pricableitems[4].text
            pricableitems3 =  pricableitems[7].text
            time.sleep(1)
            self.assertEqual(pricableitems1,'1000 x 600 mm high1')
            self.assertEqual(pricableitems2,'1000 x 900 mm high')
            self.assertEqual(pricableitems3,'1000 x 1200 mm high')
            logs.info("Test Case No : 100061 Passed Successfully")
        except Exception:
            logs.error("Validation with Test Case No: 100061 failed")
            browser.save_screenshot(fullpath)
            traceback.print_exc(file=sys.stdout)
            self.fail("Test Case No: 100061 failed")
            browser.implicitly_wait(5)
        finally:
            LauncheTender1.closebrowser(browser)