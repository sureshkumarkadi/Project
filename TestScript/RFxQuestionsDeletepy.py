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
from RFx import RFxQuestionnaire
logs=logvalue.logger
logclose=logvalue()
ftime = time.mktime(time.localtime())
ptime=time.strftime("%d-%m-%Y_%H%M%S", time.localtime(ftime))
#filename = 'TestCase-RFX-{0}.png'.format(ptime)
tf = 'test_RFxQuestionsdelete'
filename = 'Testcase-%s.png' %(tf)
path= setupValue().screenpath
fullpath = os.path.join(path,filename)

#Test case Number = RFX-13
class RFxQuestionsdelete(unittest.TestCase):
    def test_RFxQuestionsdelete(self):
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
            tenderDetails = Tenderdetails()
            time.sleep(1)
            browser = tenderDetails.Subcontratorproject(browser)
            time.sleep(2)
            browser = tenderDetails.estimatortender1(browser)
            time.sleep(2)

            RFxQuestions = RFxQuestionnaire()

            browser = RFxQuestions.RFxQuestionsTab(browser)
            time.sleep(2)

            browser = RFxQuestions.deleteQuestions(browser)
            time.sleep(2)

            RFxaddquestion1 = DataDriver()

            addquestionserialnum_path = RFxaddquestion1.readfromXML(folder_path+'\Object\RFx.xml','eTender','addquestionserialnum')
            addquestionserialnum = browser.find_elements_by_xpath(addquestionserialnum_path)
            time.sleep(1)
            self.assertEqual(len(addquestionserialnum),1)

            logs.info("Test Case No : RFX Passed Successfully")
            time.sleep(1)
        except Exception:
            logs.error("Validation with Test Case No: RFX failed")
            browser.save_screenshot(fullpath)
            traceback.print_exc(file=sys.stdout)
            self.fail("Test Case No: RFX failed")
            browser.implicitly_wait(5)
        finally:
            LauncheTender1.closebrowser(browser)

if __name__ == '__main__':
    unittest.main()