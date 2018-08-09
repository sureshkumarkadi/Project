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
from datadriven import DataDriver
from setupenviron import setupValue
from logdriver import logvalue
logs=logvalue.logger
logclose=logvalue()
ftime = time.mktime(time.localtime())
ptime=time.strftime("%d-%m-%Y_%H%M%S", time.localtime(ftime))
#filename = 'TestCase-100004-{0}.png'.format(ptime)
tf = 'test_OrganidetailsofOrganisation'
filename = 'Testcase-%s.png' %(tf)
path= setupValue().screenpath
fullpath = os.path.join(path,filename)

#Test case no:100004
class detailsofOrganisation(unittest.TestCase):
    def test_OrganidetailsofOrganisation(self):
        try:
            browserInstance = setupValue()
            browser = browserInstance.setupfunction()
            browser.implicitly_wait(5)
            LauncheTender1 = LauncheTenderclass()
            browser = LauncheTender1.openURL(browser)
            browser.implicitly_wait(5)
            browser = LauncheTender1.subcontractorValidlogin(browser)
            browser = LauncheTender1.list_Organisation(browser)
            browser = LauncheTender1.verifyorganisationdetails(browser)
            browser.implicitly_wait(5)

            orgDetails = DataDriver()
            organisation1_text=orgDetails.readfromXML(folder_path+'\Object\Object.xml','eTender','organisation-text') #organisation
            organisation = browser.find_element_by_link_text(organisation1_text)
            browser.implicitly_wait(5)

            pending_tenders = []
            pendingTrades_count=orgDetails.readfromXML(folder_path+'\Object\Object.xml','eTender','pendingTrades') #pending trades
            pending_tenders = browser.find_elements_by_xpath(pendingTrades_count)
            browser.implicitly_wait(5)

            org_website = orgDetails.readfromXML(folder_path+'\Object\Object.xml','eTender','orgwebsite') #organisation website
            organisation_website = browser.find_element_by_link_text(org_website)
            browser.implicitly_wait(5)

            organisation1    = organisation.text
            pending_tenders1 = pending_tenders[1].text
            organisation_website1 = organisation_website.text
            self.assertEqual(organisation1,'GSE Civil Engineering Ltd')
            self.assertEqual(pending_tenders1,'Pending trades: 2')
            self.assertEqual(organisation_website1,'http://www.gse-group.co.uk/')
            logs.info("Test Case No : 100004 Passed Successfully")
        except Exception:
            logs.error("Validation with Test Case No: 100004 failed")
            browser.save_screenshot(fullpath)
            traceback.print_exc(file=sys.stdout)
            self.fail("Test Case No: 100004 failed")
            browser.implicitly_wait(5)
        finally:
            LauncheTender1.closebrowser(browser)