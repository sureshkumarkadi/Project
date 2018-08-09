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
from logdriver import logvalue
logs=logvalue.logger
logclose=logvalue()
ftime = time.mktime(time.localtime())
ptime=time.strftime("%d-%m-%Y_%H%M%S", time.localtime(ftime))
#filename = 'TestCase-100026-{0}.png'.format(ptime)
tf = 'test_clearmessageineditor'
filename = 'Testcase-%s.png' %(tf)
path= setupValue().screenpath
fullpath = os.path.join(path,filename)

#Test case number = 100026
class ClearmessageinEditor(unittest.TestCase):
    def test_clearmessageineditor(self):
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
            #browser = LauncheTender1.list_Organisation(browser)
            time.sleep(1)
            browser = LauncheTender1.verifyorganisationdetails(browser)
            browser = LauncheTender1.list_project(browser)
            tenderDetails = Tenderdetails()
            time.sleep(1)
            browser = tenderDetails.Subcontratorproject(browser)
            browser = tenderDetails.suppliertender(browser)
            time.sleep(1)
            browser = tenderDetails.Actionslist(browser)
            time.sleep(1)
            browser = tenderDetails.editmessageinEditor(browser)
            time.sleep(1)
            browser = tenderDetails.clearmessageineditor(browser)
            time.sleep(1)
            nomessage = DataDriver()
            nomessage_path = nomessage.readfromXML(folder_path+'\Object\Object.xml','eTender','notesinsendmessage')
            nomessage_ineditor = browser.find_element_by_xpath(nomessage_path)
            nomessage_ineditor1 = nomessage_ineditor.text
            self.assertEqual(nomessage_ineditor1,'')
            time.sleep(1)
            browser = tenderDetails.backtotenderdetailswindow(browser)
            time.sleep(1)
            Userprofilemenu_logout = Userprofilemenu()
            browser = Userprofilemenu_logout.logout_eTender(browser)
            time.sleep(1)
            logs.info("Test Case No : 100026 Passed Successfully")
        except Exception:
            logs.error("Validation with Test Case No: 100026 failed")
            browser.save_screenshot(fullpath)
            traceback.print_exc(file=sys.stdout)
            self.fail("Test Case No: 100026 failed")
            browser.implicitly_wait(5)
        finally:
            LauncheTender1.closebrowser(browser)