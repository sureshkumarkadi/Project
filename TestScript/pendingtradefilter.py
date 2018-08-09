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
#filename = 'TestCase-100308-{0}.png'.format(ptime)
tf = 'test_pendingtradefilter'
filename = 'Testcase-%s.png' %(tf)
path= setupValue().screenpath
fullpath = os.path.join(path,filename)

#Test case Number = 100308
class Pendingtradefilter(unittest.TestCase):
    def test_pendingtradefilter(self):
        try:
                browserInstance = setupValue()
                browser = browserInstance.setupfunction()
                browser.implicitly_wait(5)
                time.sleep(1)
                LauncheTender1 = LauncheTenderclass()
                browser = LauncheTender1.openURL(browser)
                browser.implicitly_wait(5)
                time.sleep(1)
                browser = LauncheTender1.subcontractorloginPendingtrades(browser)
                time.sleep(2)
                browser = LauncheTender1.switchOrganisation(browser)
                time.sleep(1)
                browser = LauncheTender1.selectfirstOrganisationPtrades(browser)
                time.sleep(3)

                tenderDetails = Tenderdetails()
                browser = tenderDetails.SubcontratorprojectPtrade(browser)
                time.sleep(1)

                browser = tenderDetails.Selectpendingtrades(browser)
                time.sleep(7)

                pending_trades = DataDriver()
                pendingtrades = []

                pendingtrades_path =pending_trades.readfromXML(folder_path+'\Object\Project.xml','eTender','pendingtradeslist')
                pendingtrades = browser.find_elements_by_xpath(pendingtrades_path)
                time.sleep(1)
                for pendingtrades1 in pendingtrades:
                    print (pendingtrades1.text)
                time.sleep(5)
                if pendingtrades[1].text == '':
                    print("fail")
                    self.fail("Test Case No: 100308 failed")
                else:
                    self.assertEqual(pendingtrades1.text,'Pending trades: 1')
                    logs.info("Test Case No : 100308 Passed Successfully")
                time.sleep(2)

        except Exception:
                logs.error("Validation with Test Case No: 100308 failed")
                browser.save_screenshot(fullpath)
                traceback.print_exc(file=sys.stdout)
                self.fail("Test Case No: 100308 failed")
                browser.implicitly_wait(5)
        finally:
                LauncheTender1.closebrowser(browser)