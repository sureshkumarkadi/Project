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
#filename = 'TestCase-TC1034-{0}.png'.format(ptime)
tf = 'test_invitecolleagueloggeduser'
filename = 'Testcase-%s.png' %(tf)
path= setupValue().screenpath
fullpath = os.path.join(path,filename)

#Test case number = TC1034
class Invitecolleagueloggeduser(unittest.TestCase):
    def test_invitecolleagueloggeduser(self):
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
            emailinvite1 = DataDriver()
            emailinvite_path = emailinvite1.readfromXML(folder_path+'\Object\Itemsobject.xml','eTender','emailinvite')
            time.sleep(1)
            emailinvite = browser.find_element_by_xpath(emailinvite_path) #Verifying option for email invite
            self.assertFalse('Subcontractor@etender.com' in browser.page_source)
            logs.info("Test Case No : TC1034 Passed Successfully")
        except Exception:
            logs.error("Validation with Test Case No: TC1034 failed")
            browser.save_screenshot(fullpath)
            traceback.print_exc(file=sys.stdout)
            self.fail("Test Case No: TC1034 failed")
            browser.implicitly_wait(5)
        finally:
            LauncheTender1.closebrowser(browser)