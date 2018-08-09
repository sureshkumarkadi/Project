#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      suresh.kumar
#
# Created:     14/04/2017
# Copyright:   (c) suresh.kumar 2016
# Licence:     <causeway licence>
#-------------------------------------------------------------------------------
from selenium.webdriver.support.ui import WebDriverWait
import unittest
import sys
import os
import time
import traceback
import xlrd

dir_path = os.path.dirname(os.path.realpath(__file__))
folder_path=os.path.abspath(os.path.join(dir_path, os.pardir))

book = xlrd.open_workbook(folder_path+'\Data\eTender.xls', formatting_info=True)
sheet = book.sheet_by_name('UpdateProjectDetails')

sys.path.insert(0,folder_path+"\Library")
sys.path.insert(0,folder_path+"\Syslibrary")
sys.path.insert(0,folder_path+"\Data")
sys.path.insert(0,folder_path+"\Object")
from launcheTender import LauncheTenderclass
from tenderDetails import Tenderdetails
from tenderDetails import SubmitTenderclass
from eTenderUpdateProjectDetails import updatedetails
from datadriven import DataDriver
from setupenviron import setupValue
from logouteTender import Userprofilemenu
from logdriver import logvalue
logs=logvalue.logger
logclose=logvalue()
ftime = time.mktime(time.localtime())
ptime=time.strftime("%d-%m-%Y_%H%M%S", time.localtime(ftime))
#filename = 'TestCase-100208-{0}.png'.format(ptime)
tf = 'test_Projectdetails'
filename = 'Testcase-%s.png' %(tf)
path= setupValue().screenpath
fullpath = os.path.join(path,filename)

#Test case Number = 100208
class Projectdetails(unittest.TestCase):
    def test_Projectdetails(self):
        try:
                browserInstance = setupValue()
                browser = browserInstance.setupfunction()
                browser.implicitly_wait(5)
                time.sleep(1)
                LauncheTender1 = LauncheTenderclass()
                browser = LauncheTender1.openURL(browser)
                browser.implicitly_wait(5)
                time.sleep(1)
                browser = LauncheTender1.estimatorValidlogin(browser)
                time.sleep(5)
##                browser = LauncheTender1.switchOrganisation(browser)
##                time.sleep(1)
##                browser = LauncheTender1.selectfirstOrganisation(browser)
##                time.sleep(7)
                Updatedetails = updatedetails()

                project_details = DataDriver()

                projectdetails = []

                projectvaluedetails_path =project_details.readfromXML(folder_path+'\Object\Project.xml','eTender','projectvaluelabel')
                projectdetails=browser.find_elements_by_xpath(projectvaluedetails_path)
                for projectvaluedetails1 in projectdetails:
                    print (projectvaluedetails1.text)
                self.assertEqual(projectvaluedetails1.text,'Value:')
                time.sleep(2)

                projectduedatedetails_path =project_details.readfromXML(folder_path+'\Object\Project.xml','eTender','projectduedatelabel')
                projectdetails=browser.find_elements_by_xpath(projectduedatedetails_path)
                for projectduedatedetails1 in projectdetails:
                    print (projectduedatedetails1.text)
                self.assertEqual(projectduedatedetails1.text,'Due Date:')
                time.sleep(1)

        except Exception:
                logs.error("Validation with Test Case No: 100208 failed")
                browser.save_screenshot(fullpath)
                traceback.print_exc(file=sys.stdout)
                self.fail("Test Case No: 100208 failed")
                browser.implicitly_wait(5)
        finally:
                LauncheTender1.closebrowser(browser)






















