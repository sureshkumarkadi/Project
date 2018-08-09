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
#filename = 'TestCase-TC1026-{0}.png'.format(ptime)
tf = 'test_documentlinkfileURL'
filename = 'Testcase-%s.png' %(tf)
path= setupValue().screenpath
fullpath = os.path.join(path,filename)

#Test case Number = TC1026-1
class DocumentlinkfileURL(unittest.TestCase):
    def test_documentlinkfileURL(self):
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
            self.assertTrue('http://bg-etender-fs:8080/fileserver/api/file/raw/5a7445cd0ee3c5610bdcde35' in browser.page_source)
            logs.info("Test Case No : TC1026 Passed Successfully")
        except Exception:
            logs.error("Validation with Test Case No: TC1026 failed")
            browser.save_screenshot(fullpath)
            traceback.print_exc(file=sys.stdout)
            self.fail("Test Case No: TC1026 failed")
            browser.implicitly_wait(5)
        finally:
            LauncheTender1.closebrowser(browser)