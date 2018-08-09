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
#filename = 'TestCase-TC1028-{0}.png'.format(ptime)
tf = 'test_addexternalURL'
filename = 'Testcase-%s.png' %(tf)
path= setupValue().screenpath
fullpath = os.path.join(path,filename)

#Test case Number = TC1028
class AddexternalURL(unittest.TestCase):
    def test_addexternalURL(self):
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
            browser = tenderDetails.projectdocIcon(browser)
            time.sleep(1)

            browser = tenderDetails.addhyperlinkclick(browser)
            time.sleep(1)

            browser = tenderDetails.externaldocumentasfile(browser)
            time.sleep(1)

            Documentname1 = DataDriver()
            time.sleep(1)
            Documentname_path = Documentname1.readfromXML(folder_path+'\Object\Project.xml','eTender','externaldocumentname')
            Documentname = browser.find_element_by_xpath(Documentname_path)
            time.sleep(1)
            self.assertEqual(Documentname.text,'ExternalURLasfile')
            logs.info("Test Case No : TC1028 Passed Successfully")
        except Exception:
            logs.error("Validation with Test Case No: TC1028 failed")
            browser.save_screenshot(fullpath)
            traceback.print_exc(file=sys.stdout)
            self.fail("Test Case No: TC1028 failed")
            browser.implicitly_wait(5)
        finally:
            LauncheTender1.closebrowser(browser)

if __name__ == '__main__':
    unittest.main()