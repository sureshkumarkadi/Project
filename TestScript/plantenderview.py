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
from selenium.webdriver.common.action_chains import ActionChains
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
#filename = 'TestCase-100260-{0}.png'.format(ptime)
tf = 'test_Plantenderview'
filename = 'Testcase-%s.png' %(tf)
path= setupValue().screenpath
fullpath = os.path.join(path,filename)

#Test case Number = 100260
class Plantenderview(unittest.TestCase):
    def test_Plantenderview(self):
        try:
            browserInstance = setupValue()
            browser = browserInstance.setupfunction()
            browser.implicitly_wait(5)
            time.sleep(1)
            LauncheTender1 = LauncheTenderclass()
            browser = LauncheTender1.openURL(browser)
            time.sleep(1)
            browser = LauncheTender1.estimatorValidlogin(browser)
            time.sleep(5)
            tendertemplate = Tenderplans()
##            browser = tendertemplate.plantemplatemenu(browser)
##            time.sleep(1)
##            browser = tendertemplate.plantemplatebutton(browser)
##            time.sleep(1)
##            browser = tendertemplate.plantemplatecreation(browser)
##            time.sleep(1)
##            browser = tendertemplate.plantemplatecreationwithstages(browser)
##            time.sleep(1)
##            browser = tendertemplate.plantemplatesave(browser)
##            time.sleep(1)
            tenderDetails = Tenderdetails()

##            browser = tenderDetails.listProjectmenu(browser)
##            time.sleep(1)
            browser = tenderDetails.Subcontratorproject(browser)
            time.sleep(2)
            tenderclass = TenderClass()

            NewTender = tenderclass.TenderCreation(browser)
            #time.sleep(1)
            browser = tenderDetails.estimatortender2(browser)
            time.sleep(2)
            #browser = tendertemplate.tendereselection(browser)
            #time.sleep(1)
            browser = tendertemplate.estimatortenderpalntender(browser) #Go to Tender plan tender
            time.sleep(1)
            browser = tendertemplate.estimatortenderplan(browser) #Select plan template
            time.sleep(1)

            template_creation = DataDriver()
            time.sleep(1)
            tendertemplatename_path = template_creation.readfromXML(folder_path+'\Object\TenderplanObjects.xml','eTender','templatenamevalidate')
            tendertemplatename = browser.find_element_by_xpath(tendertemplatename_path)
            time.sleep(1)
            self.assertEqual(tendertemplatename.text,'procurement update')

            tendertemplatedescription_path = template_creation.readfromXML(folder_path+'\Object\TenderplanObjects.xml','eTender','templatedescriptionvalidate')
            tendertemplatedescription = browser.find_element_by_xpath(tendertemplatedescription_path)
            time.sleep(1)
            self.assertEqual(tendertemplatedescription.text,'procurement materialsupdate')
            time.sleep(1)
            logs.info("Test Case No : 100260 Passed Successfully")
            time.sleep(1)

            browser = tendertemplate.templateclose(browser)
            time.sleep(1)

        except Exception:
            logs.error("Validation with Test Case No: 100260 failed")
            browser.save_screenshot(fullpath)
            traceback.print_exc(file=sys.stdout)
            self.fail("Test Case No: 100260 failed")
            browser.implicitly_wait(5)
        finally:
            LauncheTender1.closebrowser(browser)

if __name__ == '__main__':
    unittest.main()