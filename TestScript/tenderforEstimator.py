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
from datadriven import DataDriver
from setupenviron import setupValue
from logdriver import logvalue
logs=logvalue.logger
logclose=logvalue()
ftime = time.mktime(time.localtime())
ptime=time.strftime("%d-%m-%Y_%H%M%S", time.localtime(ftime))
#filename = 'TestCase-100052-{0}.png'.format(ptime)
tf = 'test_tenderdetails'
filename = 'Testcase-%s.png' %(tf)
path= setupValue().screenpath
fullpath = os.path.join(path,filename)



#Test case no:100052
class tradeslistEstimator(unittest.TestCase):
    def test_tenderdetails(self):
        try:
            browserInstance = setupValue()
            browser = browserInstance.setupfunction()
            browser.implicitly_wait(5)
            LauncheTender1 = LauncheTenderclass()
            browser = LauncheTender1.openURL(browser)
            browser.implicitly_wait(5)
            browser = LauncheTender1.estimatorValidlogin(browser)
            tenderDetails = Tenderdetails()
            browser = tenderDetails.estimatorProject(browser)
            time.sleep(1)
            browser = tenderDetails.estimatortender(browser)
            time.sleep(3)
            itemdescription = DataDriver()
            itemdescription_path = itemdescription.readfromXML(folder_path+'\Object\Object.xml','eTender','itemdescription') #Item-descrition
            item_description = browser.find_element_by_xpath(itemdescription_path) #Webelement for Item description
            itemdescription = item_description.text
            self.assertEqual(itemdescription,'1000 x 600 mm high1')
            logs.info("Test Case No : 100052 Passed Successfully")
        except Exception:
            logs.error("Validation with Test Case No: 100052 failed")
            browser.save_screenshot(fullpath)
            traceback.print_exc(file=sys.stdout)
            self.fail("Test Case No: 100052 failed")
            browser.implicitly_wait(5)
        finally:
            LauncheTender1.closebrowser(browser)