#-------------------------------------------------------------------------------
# Name:         AT_StartDateAsForeCast.py
#
# Tast Case Id  100306
#
# Purpose:      TO Verify that Forcast date as start date in tender
#
# Author:      mathew.jacob
#
# Created:     28/09/2017
# Copyright:   (c) Causeway Technologies 2017
#-------------------------------------------------------------------------------

from selenium.webdriver.support.ui import WebDriverWait
import unittest
import sys
import os
import time
import traceback
from datetime import datetime,date

dir_path = os.path.dirname(os.path.realpath(__file__))
folder_path=os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0,folder_path+"\Library")
sys.path.insert(0,folder_path+"\Env")
from launcheTender import LauncheTenderclass
from setupenviron import setupValue
from logdriver import logvalue
from datadriven import DataDriver
from TenderModification import TenderClass
from logouteTender import Userprofilemenu
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
logs=logvalue.logger
orgLink=DataDriver()
ftime = time.mktime(time.localtime())
ptime=time.strftime("%d-%m-%Y_%H%M%S", time.localtime(ftime))
#filename = 'TestCase-100306-{0}.png'.format(ptime)
tf = 'test_ForeCastDate'
filename = 'Testcase-%s.png' %(tf)
path= setupValue().screenpath
fullpath = os.path.join(path,filename)
class StartDateAsForecast(unittest.TestCase):
    def test_ForeCastDate(self):
        try:
            browserInstance = setupValue()
            browser = browserInstance.setupfunction()
            browser.implicitly_wait(10)
            LauncheTender = LauncheTenderclass()
            TenderAction=TenderClass()
            logOut=Userprofilemenu()
            browser = LauncheTender.openURL(browser)
            browser = LauncheTender.estimatorValidlogin1(browser)
            time.sleep(3)
            ProjName=TenderAction.ProjectCreation(browser)
            TenderAction.OpenProject(ProjName,browser)
            dateflag=0
            NewTender=TenderAction.TenderCreationwithStartDate(browser,dateflag)
            time.sleep(3)
            Datevalue=TenderAction.startdate
            Startdate = datetime.strptime(Datevalue, '%d-%b-%Y')
            time.sleep(3)
            TenderAction.OpenDetails(browser,NewTender)
            time.sleep(3)
            TenderAction.OpenTenderPlan(browser)
            time.sleep(3)
            browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','SelectTemplate')).click()
            time.sleep(3)
            p=browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','PlanTemplateSearch'))
            time.sleep(2)
            p.send_keys(orgLink.readfromXML(folder_path+'\Data\TenderData.xml','eTender','TemplateData'))
            checkbox=browser.find_elements_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','TemplateCheckbox'))
            time.sleep(2)
            checkbox[1].click()
            browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','SelectPlanBtn')).click()
            time.sleep(3)
            foreText=browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','ForeCastDateText')).get_attribute('value')
            Foredate=datetime.strptime(Datevalue, '%d-%b-%Y')
            self.assertEquals(Startdate,Foredate)
            logs.info("Test Case No : 100306 Passed Successfully")
        except Exception:
            logs.error("Validation with Test Case No: 100306 failed")
            browser.save_screenshot(fullpath)
            traceback.print_exc(file=sys.stdout)
            self.fail("Test Case No: 100306 failed")
        finally:
            browser=logOut.logout_eTender(browser)
            LauncheTender.closebrowser(browser)

