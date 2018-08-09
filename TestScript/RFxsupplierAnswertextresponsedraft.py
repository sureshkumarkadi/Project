#-------------------------------------------------------------------------------
# Name:        Subcontractor
# Purpose:     Warning message to the User
#
# Author:      suresh.kumar
#
# Created:     02/08/2017
# Copyright:   (c) suresh.kumar 2017
# Licence:     <Causeway licence>
#-------------------------------------------------------------------------------
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
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
from datadriven import DataDriver
from setupenviron import setupValue
from logdriver import logvalue
from RFx import RFxQuestionnaire

logs=logvalue.logger
logclose=logvalue()
ftime = time.mktime(time.localtime())
ptime=time.strftime("%d-%m-%Y_%H%M%S", time.localtime(ftime))
#filename = 'TestCase-100291-{0}.png'.format(ptime)
tf = 'test_RFxsupplieranswertextresponsedraft'
filename = 'Testcase-%s.png' %(tf)
path= setupValue().screenpath
fullpath = os.path.join(path,filename)

#Test case Number = RFx-12
class RFxsupplieranswertextresponsedraft(unittest.TestCase):
    def test_RFxsupplieranswertextresponsedraft(self):
        try:
            browserInstance = setupValue()
            browser = browserInstance.setupfunction()
            LauncheTender1 = LauncheTenderclass()
            browser = LauncheTender1.openURL(browser)
            browser = LauncheTender1.subcontractorValidlogin(browser)
            browser = LauncheTender1.list_project(browser)
            tenderDetails = Tenderdetails()
            browser = tenderDetails.Subcontratorproject(browser)
            browser = tenderDetails.suppliersecondtender(browser)
            time.sleep(2)
            RFxAnswers = RFxQuestionnaire()

            browser = RFxAnswers.RFxQuestionsTabinsupplier(browser)
            time.sleep(1)

            browser = RFxAnswers.RFxTextresponseanswer(browser)
            time.sleep(1)

            browser = RFxAnswers.DraftRFxanswers(browser)
            time.sleep(1)

            RFxAnswerstab1 = DataDriver()
            time.sleep(1)
            RFxdraftsuccessmessage_path = RFxAnswerstab1.readfromXML(folder_path+'\Object\RFx.xml','eTender','draftmessageforsupplier')
            RFxdraftsuccessmessage = browser.find_element_by_xpath(RFxdraftsuccessmessage_path)
            time.sleep(1)

            self.assertEqual(RFxdraftsuccessmessage.text,'Draft responses saved.')

            logs.info("Test Case No : 100291 Passed Successfully")
        except Exception:
            logs.error("Validation with Test Case No: 100291 failed")
            browser.save_screenshot(fullpath)
            traceback.print_exc(file=sys.stdout)
            self.fail("Test Case No: 100291 failed")
            browser.implicitly_wait(5)
        finally:
            LauncheTender1.closebrowser(browser)

if __name__ == '__main__':
    unittest.main()