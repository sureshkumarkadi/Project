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
from tenderDetails import SubmitTenderclass
from datadriven import DataDriver
from setupenviron import setupValue
from logouteTender import Userprofilemenu
from logdriver import logvalue
logs=logvalue.logger
logclose=logvalue()
ftime = time.mktime(time.localtime())
ptime=time.strftime("%d-%m-%Y_%H%M%S", time.localtime(ftime))
#filename = 'TestCase-100249-{0}.png'.format(ptime)
tf = 'test_Plantemplateupdation'
filename = 'Testcase-%s.png' %(tf)
path= setupValue().screenpath
fullpath = os.path.join(path,filename)

#Test case Number = 100249
class Plantemplateupdation(unittest.TestCase):
    def test_Plantemplateupdation(self):
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
            browser = tendertemplate.plantemplatemenu(browser)
            time.sleep(1)
            browser = tendertemplate.plantemplatebutton(browser)
            time.sleep(1)
            browser = tendertemplate.plantemplatecreation(browser)
            time.sleep(1)
            browser = tendertemplate.plantemplatecreationwithstages(browser)
            time.sleep(1)
            browser = tendertemplate.plantemplatesave(browser)
            time.sleep(1)
            browser = tendertemplate.plantemplateselection(browser)
            time.sleep(1)
            browser = tendertemplate.plantemplateupdation(browser)
            time.sleep(1)

            browser = tendertemplate.templatedetialsupdation(browser)
            time.sleep(1)
            browser = tendertemplate.plantemplateupdateduration(browser)
            time.sleep(1)
            browser = tendertemplate.plantemplateupdate(browser)
            time.sleep(1)


            template_updation = DataDriver()
            time.sleep(1)
            tendertemplatenameupadate = []
            tendertemplatenameupadate_path = template_updation.readfromXML(folder_path+'\Object\TenderplanObjects.xml','eTender','templatedetailsvalidate')
            tendertemplatenameupadate = browser.find_elements_by_xpath(tendertemplatenameupadate_path)
            time.sleep(1)
            self.assertEqual(tendertemplatenameupadate[2].text,'procurement update')
            self.assertEqual(tendertemplatenameupadate[3].text,'procurement materialsupdate')

            logs.info("Test Case No : 100249 Passed Successfully")
        except Exception:
            logs.error("Validation with Test Case No: 100249 failed")
            browser.save_screenshot(fullpath)
            traceback.print_exc(file=sys.stdout)
            self.fail("Test Case No: 100249 failed")
            browser.implicitly_wait(5)
        finally:
            #browser = tendertemplate.plantemplateselection(browser)
            #time.sleep(1)
            #browser = tendertemplate.plantemplatedelete(browser)
            #time.sleep(1)
            LauncheTender1.closebrowser(browser)































