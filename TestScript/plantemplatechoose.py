#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      suresh.kumar
#
# Created:     12/07/2017
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
from launcheTender import LauncheTenderclass
from Tenderplan import Tenderplans
from tenderDetails import Tenderdetails
from datadriven import DataDriver
from setupenviron import setupValue
from logouteTender import Userprofilemenu
from logdriver import logvalue
from TenderModification import TenderClass
logs=logvalue.logger
logclose=logvalue()
ftime = time.mktime(time.localtime())
ptime=time.strftime("%d-%m-%Y_%H%M%S", time.localtime(ftime))
#filename = 'TestCase-100261-{0}.png'.format(ptime)
tf = 'test_plantemplatechoose'
filename = 'Testcase-%s.png' %(tf)
path= setupValue().screenpath
fullpath = os.path.join(path,filename)

#Test case Number = 100261
class Plantemplatechoose(unittest.TestCase):
    def test_plantemplatechoose(self):
        try:
            browserInstance = setupValue()
            browser = browserInstance.setupfunction()
            browser.implicitly_wait(5)
            time.sleep(1)
            LauncheTender1 = LauncheTenderclass()
            browser = LauncheTender1.openURL(browser)
            time.sleep(1)
            browser = LauncheTender1.estimatorValidlogin(browser)
            time.sleep(1)
            tendertemplate = Tenderplans()
            tenderDetails = Tenderdetails()

            browser = tenderDetails.Subcontratorproject(browser)
            time.sleep(2)
            browser = tenderDetails.estimatortender2(browser)
            time.sleep(2)
            browser = tendertemplate.estimatortenderpalntender(browser) #Go to Tender plan tender
            time.sleep(1)
            browser = tendertemplate.estimatortenderplan(browser) #Select Tenderplan from dropdown list
            time.sleep(5)

            browser = tendertemplate.plantemplateselectionfromlist(browser)
            time.sleep(1)
            browser = tendertemplate.plantemplateselect(browser)
            time.sleep(2)

            templatestages1 = DataDriver()

            env = templatestages1.readfromXML(folder_path+'\Env\Setup.xml','eTender','env')

            if env == 'StageURL':

                templatestages = []
                templatestages_path = templatestages1.readfromXML(folder_path+'\Object\TenderplanObjects.xml','eTender','templatestages')
                time.sleep(1)
                templatestages = browser.find_elements_by_xpath(templatestages_path)
                time.sleep(1)
                self.assertEqual(templatestages[0].text,'Stag One Automation')
                self.assertEqual(templatestages[1].text,'Stag Two Automation')
                self.assertEqual(templatestages[2].text,'Automation Stage')
                self.assertEqual(templatestages[3].text,'StagDelete')
                self.assertEqual(templatestages[4].text,'Stag Three Automation')
                self.assertEqual(templatestages[5].text,'Stag Four Automation')
                self.assertEqual(templatestages[6].text,'Stag Five Automation')

            elif env == 'PreStageURL':

                templatestages = []
                templatestages_path = templatestages1.readfromXML(folder_path+'\Object\TenderplanObjects.xml','eTender','templatestages')
                time.sleep(1)
                templatestages = browser.find_elements_by_xpath(templatestages_path)
                time.sleep(1)

                self.assertEqual(templatestages[0].text,'Stag One Automation')
                self.assertEqual(templatestages[1].text,'Stag Two Automation')
                self.assertEqual(templatestages[2].text,'Automation Stage')
                self.assertEqual(templatestages[3].text,'StagDelete')
                self.assertEqual(templatestages[4].text,'Stag Three Automation')
                self.assertEqual(templatestages[5].text,'Stag Four Automation')
                self.assertEqual(templatestages[6].text,'Stag Five Automation')

            elif env == 'MasterURL':

                templatestages = []
                templatestages_path = templatestages1.readfromXML(folder_path+'\Object\TenderplanObjects.xml','eTender','templatestages')
                time.sleep(1)
                templatestages = browser.find_elements_by_xpath(templatestages_path)
                time.sleep(1)
                self.assertEqual(templatestages[0].text,'Stag One Automation')
                self.assertEqual(templatestages[1].text,'Stag Two Automation')
                self.assertEqual(templatestages[2].text,'Automation Stage')
                self.assertEqual(templatestages[3].text,'StagDelete')
                self.assertEqual(templatestages[4].text,'Stag Three Automation')
                self.assertEqual(templatestages[5].text,'Stag Four Automation')
                self.assertEqual(templatestages[6].text,'Stag Five Automation')

            logs.info("Test Case No : 100261 Passed Successfully")
        except Exception:
            logs.error("Validation with Test Case No: 100261 failed")
            browser.save_screenshot(fullpath)
            traceback.print_exc(file=sys.stdout)
            self.fail("Test Case No: 100261 failed")
            browser.implicitly_wait(5)
        finally:
            time.sleep(1)
            LauncheTender1.closebrowser(browser)