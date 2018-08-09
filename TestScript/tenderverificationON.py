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
#filename = 'TestCase-100356-{0}.png'.format(ptime)
tf = 'test_TenderverificationON'
filename = 'Testcase-%s.png' %(tf)
path= setupValue().screenpath
fullpath = os.path.join(path,filename)

#Test case Number = 100356
class TenderverificationON(unittest.TestCase):
    def test_TenderverificationON(self):
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
            browser = tenderDetails.estimatorProject(browser)
            time.sleep(1)
            browser = tenderDetails.estimatortender(browser)
            time.sleep(5)
            tenderverifybutton1 = DataDriver()
            tenderverifybutton = []
            tenderverifybutton_path = tenderverifybutton1.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','tenderverifybutton')
            time.sleep(1)
            tenderverifybutton = browser.find_elements_by_xpath(tenderverifybutton_path) #Webelement for values
            time.sleep(1)
            time.sleep(1)
            self.assertEqual(tenderverifybutton[2].text,'Verify' )
            logs.info("Test Case No : 100356 Passed Successfully")
        except Exception:
            logs.error("Validation with Test Case No: 100356 failed")
            browser.save_screenshot(fullpath)
            traceback.print_exc(file=sys.stdout)
            self.fail("Test Case No: 100356 failed")
            browser.implicitly_wait(5)
        finally:
            LauncheTender1.closebrowser(browser)

if __name__ == '__main__':
    unittest.main()