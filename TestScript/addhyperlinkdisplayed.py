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
#filename = 'TestCase-TC1039-{0}.png'.format(ptime)
tf = 'test_addhyperlinkdisplayed'
filename = 'Testcase-%s.png' %(tf)
path= setupValue().screenpath
fullpath = os.path.join(path,filename)

#Test case Number = TC1039
class Addhyperlinkdisplayed(unittest.TestCase):
    def test_addhyperlinkdisplayed(self):
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

            hyperlink1 = DataDriver()
            time.sleep(1)
            hyperlinkdisplayed_path = hyperlink1.readfromXML(folder_path+'\Object\Project.xml','eTender','hyperlink')
            hyperlinkdisplayed = browser.find_element_by_xpath(hyperlinkdisplayed_path) #Xpath for hover
            time.sleep(2)
            self.assertEqual(hyperlinkdisplayed.text,'Add hyperlink')
            logs.info("Test Case No : TC1039 Passed Successfully")
        except Exception:
            logs.error("Validation with Test Case No: TC1039 failed")
            browser.save_screenshot(fullpath)
            traceback.print_exc(file=sys.stdout)
            self.fail("Test Case No: TC1039 failed")
            browser.implicitly_wait(5)
        finally:
            LauncheTender1.closebrowser(browser)