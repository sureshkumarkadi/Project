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
from OrganizationFunction import Organizationclass
from Itemdetails import ItemDetails
from datadriven import DataDriver
from setupenviron import setupValue
from logdriver import logvalue
logs=logvalue.logger
logclose=logvalue()
ftime = time.mktime(time.localtime())
ptime=time.strftime("%d-%m-%Y_%H%M%S", time.localtime(ftime))
#filename = 'TestCase-TC1031-{0}.png'.format(ptime)
tf = 'test_verifycolleaguelist'
filename = 'Testcase-%s.png' %(tf)
path= setupValue().screenpath
fullpath = os.path.join(path,filename)

#Test case number = TC1031
class Verifycolleaguelist(unittest.TestCase):
    def test_verifycolleaguelist(self):
        try:
            browserInstance = setupValue()
            browser = browserInstance.setupfunction()
            browser.implicitly_wait(5)
            time.sleep(1)
            LauncheTender1 = LauncheTenderclass()
            browser = LauncheTender1.openURL(browser)
            browser = LauncheTender1.subcontractorValidlogin(browser)
            time.sleep(1)
            orgInstance=Organizationclass()
            orgInstance.OpenaddUser(browser)
            time.sleep(1)
            firstuser,seconduser = orgInstance.Userslist(browser)
            time.sleep(1)
            browser = LauncheTender1.list_Organisation(browser)
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
            currentorgemails1 = DataDriver()
            currentorgemails = []
            currentorgemails_path = currentorgemails1.readfromXML(folder_path+'\Object\Itemsobject.xml','eTender','currentorgemails')
            time.sleep(1)
            currentorgemails = browser.find_elements_by_xpath(currentorgemails_path) #Verifying current organisaion emails
            self.assertEqual(firstuser, currentorgemails[0].text)
            self.assertEqual(seconduser,currentorgemails[1].text)
            logs.info("Test Case No : TC1031 Passed Successfully")
        except Exception:
            logs.error("Validation with Test Case No: TC1031 failed")
            browser.save_screenshot(fullpath)
            traceback.print_exc(file=sys.stdout)
            self.fail("Test Case No: TC1031 failed")
            browser.implicitly_wait(5)
        finally:
            LauncheTender1.closebrowser(browser)