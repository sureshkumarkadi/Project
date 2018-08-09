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
import time
import os
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
from Itemdetails import ItemDetails
from datadriven import DataDriver
from setupenviron import setupValue
from logdriver import logvalue
logs=logvalue.logger
logclose=logvalue()
ftime = time.mktime(time.localtime())
ptime=time.strftime("%d-%m-%Y_%H%M%S", time.localtime(ftime))
#filename = 'TestCase-TC1033-{0}.png'.format(ptime)
tf = 'test_invitecolleaguesearch'
filename = 'Testcase-%s.png' %(tf)
path= setupValue().screenpath
fullpath = os.path.join(path,filename)

#Test case number = TC1033
class Invitecolleaguesearch(unittest.TestCase):
    def test_invitecolleaguesearch(self):
        try:
            browserInstance = setupValue()
            browser = browserInstance.setupfunction()
            browser.implicitly_wait(5)
            time.sleep(1)
            LauncheTender1 = LauncheTenderclass()
            browser = LauncheTender1.openURL(browser)
            browser = LauncheTender1.subcontractorValidlogin(browser)
            time.sleep(1)
            browser = LauncheTender1.list_project(browser)
            tenderDetails = Tenderdetails()
            time.sleep(1)
            browser = tenderDetails.Subcontratorproject(browser)
            browser = tenderDetails.suppliertender(browser)
            itemDetails_actions = ItemDetails()
            time.sleep(1)
            browser = itemDetails_actions.moreactions(browser)
            time.sleep(1)
            browser = itemDetails_actions.invitecolleague(browser)
            time.sleep(1)

            browser = itemDetails_actions.invitecolleagueSearch(browser)
            time.sleep(2)
            emailSearch1 = DataDriver()
            emailSearch = []
            emailSearch_path = emailSearch1.readfromXML(folder_path+'\Object\Itemsobject.xml','eTender','searchemail')
            time.sleep(1)
            emailSearch = browser.find_elements_by_xpath(emailSearch_path) #Verifying search results
            self.assertEqual(emailSearch[0].text,'dummy12@etender.com')
            #if len(emailSearch) == 1 and (self.assertEqual(emailSearch[0].text,'dummy12@etender.com')):
            if len(emailSearch) == 1:
                print("pass")
            else:
                self.fail("Validation with Test Case No: TC1033 failed")
            logs.info("Test Case No : TC1033 Passed Successfully")
        except Exception:
            logs.error("Validation with Test Case No: TC1033 failed")
            browser.save_screenshot(fullpath)
            traceback.print_exc(file=sys.stdout)
            self.fail("Test Case No: TC1033 failed")
            browser.implicitly_wait(5)
        finally:
            LauncheTender1.closebrowser(browser)