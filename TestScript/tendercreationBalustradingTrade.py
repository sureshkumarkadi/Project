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
import datetime

dir_path = os.path.dirname(os.path.realpath(__file__))
folder_path=os.path.abspath(os.path.join(dir_path, os.pardir))

book = xlrd.open_workbook(folder_path+'\Data\eTender - tendercreation.xls', formatting_info=True)
sheet = book.sheet_by_name('TenderCreation')

sys.path.insert(0,folder_path+"\Library")
sys.path.insert(0,folder_path+"\Syslibrary")
sys.path.insert(0,folder_path+"\Data")
sys.path.insert(0,folder_path+"\Object")
sys.path.insert(0,folder_path+"\Env")
from launcheTender import LauncheTenderclass
from tenderDetails import Tenderdetails
from tenderDetails import SubmitTenderclass
from eTenderUpdateProjectDetails import updatedetails
from datadriven import DataDriver
from setupenviron import setupValue
from logouteTender import Userprofilemenu
from TenderModificationPaiwiser import TenderClass
from logdriver import logvalue
logs=logvalue.logger
logclose=logvalue()
ftime = time.mktime(time.localtime())
ptime=time.strftime("%d-%m-%Y_%H%M%S", time.localtime(ftime))
#filename = 'TestCase-100368-{0}.png'.format(ptime)
tf = 'test_TendercreationBalustradingTrade'
filename = 'Testcase-%s.png' %(tf)
path= setupValue().screenpath
fullpath = os.path.join(path,filename)

#Test case Number = 100368
class TendercreationBalustradingTrade(unittest.TestCase):
    def test_TendercreationBalustradingTrade(self):
        try:
            i = 7
            while i<8:
                browserInstance = setupValue()
                browser = browserInstance.setupfunction()
                browser.implicitly_wait(5)
                time.sleep(1)
                LauncheTender1 = LauncheTenderclass()
                browser = LauncheTender1.openURL(browser)
                browser.implicitly_wait(5)
                time.sleep(1)
                browser = LauncheTender1.estimatorValidlogin(browser)
                time.sleep(1)
                tenderDetails = Tenderdetails()

                browser = tenderDetails.Subcontratorproject(browser)
                time.sleep(2)

                tenderclass = TenderClass()

                rownum=(i)
                rows = sheet.row_values(rownum)

                tendername = rows[1]
                tenderreference = rows[2]
                tenderdescription = rows[3]
                tendertype = rows[4]

                time.sleep(1)
                browser = tenderclass.TenderCreation(browser,tendername,tenderreference,tenderdescription,tendertype) #Pass the values from excel

                time.sleep(2)
                todaysdate = datetime.datetime.today().strftime('%d-%m-%Y')

                tendercreation = DataDriver()
                tenderstatus = []

                tenderstatus_path = tendercreation.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','tenderstatus') #Validate tender status
                tenderstatus = browser.find_elements_by_xpath(tenderstatus_path)

                self.assertEqual(tenderstatus[5].text,'Active')
                #self.assertEqual(tendertype,'TRADE')
                #self.assertEqual(tenderstatus[22].text,todaysdate)

                tendername_path = tendercreation.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','tenderName') #Validate tender name
                tendername = browser.find_elements_by_xpath(tendername_path)

                #self.assertEqual(tendername[7].text,'Balustrading1')

                time.sleep(3)
                i = i + 1
        except Exception:
                logs.error("Validation with Test Case No: 100368 failed")
                browser.save_screenshot(fullpath)
                traceback.print_exc(file=sys.stdout)
                self.fail("Test Case No: 100368")
                browser.implicitly_wait(5)
        finally:
                LauncheTender1.closebrowser(browser)

