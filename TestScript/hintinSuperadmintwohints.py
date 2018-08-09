#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      suresh.kumar
#
# Created:     25-08-2016
# Copyright:   (c) suresh.kumar 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import unittest
import sys
import time
import os
import traceback
from selenium.webdriver.support.ui import WebDriverWait
dir_path = os.path.dirname(os.path.realpath(__file__))
folder_path=os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0,folder_path+"\Library")
sys.path.insert(0,folder_path+"\Syslibrary")
sys.path.insert(0,folder_path+"\Data")
sys.path.insert(0,folder_path+"\Object")
from launcheTender import LauncheTenderclass
from datadriven import DataDriver
#from Organisationprofile import OrganisationProfile
from setupenviron import setupValue
from logdriver import logvalue
#from logouteTender import Userprofilemenu
from Hint import HintInteract
logs=logvalue.logger
logclose=logvalue()
ftime = time.mktime(time.localtime())
ptime=time.strftime("%d-%m-%Y_%H%M%S", time.localtime(ftime))
#filename = 'TestCase-TC1507-{0}.png'.format(ptime)
tf = 'test_hintinSuperadmintwohints'
filename = 'Testcase-%s.png' %(tf)
path= setupValue().screenpath
fullpath = os.path.join(path,filename)

#Test case no:TC1507
class HintinSuperadmintwohints(unittest.TestCase):
    def test_hintinSuperadmintwohints(self):
        try:
            browserInstance = setupValue()
            browser = browserInstance.setupfunction()
            browser.implicitly_wait(5)
            time.sleep(1)
            LauncheTender1 = LauncheTenderclass()
            browser = LauncheTender1.openURL(browser)
            browser.implicitly_wait(5)
            browser = LauncheTender1.superAdminValidlogin(browser)
            Hintdisplay = HintInteract()
            browser = Hintdisplay.systemfiledsmenu(browser)
            time.sleep(1)

            hint = DataDriver()
            time.sleep(1)
            hinttitle = browser.find_element_by_xpath(hint.readfromXML(folder_path+'\Object\Hint.xml','eTender','hinttitle')) # validating hint title
            self.assertEqual(hinttitle.text,'System1')

            hintcontent = browser.find_element_by_xpath(hint.readfromXML(folder_path+'\Object\Hint.xml','eTender','hintcontent')) # validating hint content
            self.assertEqual(hintcontent.text,'System field Creation can be done here')

            hintdone = browser.find_element_by_xpath(hint.readfromXML(folder_path+'\Object\Hint.xml','eTender','hintbutton')) # validating hint done text
            self.assertEqual(hintdone.text,'Next')

            browser = Hintdisplay.nexthint(browser)
            time.sleep(1)

            hinttitle = browser.find_element_by_xpath(hint.readfromXML(folder_path+'\Object\Hint.xml','eTender','hinttitle')) # validating hint title
            self.assertEqual(hinttitle.text,'Items1')

            hintcontent = browser.find_element_by_xpath(hint.readfromXML(folder_path+'\Object\Hint.xml','eTender','hintcontent')) # validating hint content
            self.assertEqual(hintcontent.text,'Total items1')

            hintdone = browser.find_element_by_xpath(hint.readfromXML(folder_path+'\Object\Hint.xml','eTender','hintbutton')) # validating hint done text
            self.assertEqual(hintdone.text,'Done')
            time.sleep(1)

            logs.info("Test Case No : TC1507 Passed Successfully")
        except Exception:
            logs.error("Validation with Test Case No: TC1507 failed")
            browser.save_screenshot(fullpath)
            traceback.print_exc(file=sys.stdout)
            self.fail("Test Case No: TC1507 failed")
            browser.implicitly_wait(5)
        finally:
            time.sleep(1)
            LauncheTender1.closebrowser(browser)