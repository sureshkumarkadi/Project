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
sys.path.insert(0,folder_path+"\Env")
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
#filename = 'TestCase-100222-{0}.png'.format(ptime)
tf = 'test_currencyintenderdetails'
filename = 'Testcase-%s.png' %(tf)
path= setupValue().screenpath
fullpath = os.path.join(path,filename)

#Test case Number = 100222
class Currencyintenderdetails(unittest.TestCase):
    def test_currencyintenderdetails(self):
        try:
            i = 10
            while i<11:
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
##                browser = LauncheTender1.switchOrganisation(browser)
##                time.sleep(2)
##                browser = LauncheTender1.selectsecondOrganisation(browser)
##                time.sleep(7)
                Updatedetails = updatedetails()
                browser = Updatedetails.updateproject(browser)
                rownum=(i)
                rows = sheet.row_values(rownum)

                projecttype = rows[5]

                time.sleep(1)
                browser = Updatedetails.projectdetailscurrencydollar(browser,projecttype) #Pass the values from excel
                time.sleep(1)
                browser = Updatedetails.saveprojectdetails(browser) #Save project

                time.sleep(2)
                tenderDetails = Tenderdetails()
                browser = tenderDetails.estimatorProject(browser)
                time.sleep(1)
                browser = tenderDetails.estimatortender1(browser)

                Currencyfortender = DataDriver()
                currencyfortender_path = Currencyfortender.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','currencyfortender') #Validate image id
                currencyfortender = browser.find_element_by_xpath(currencyfortender_path)
                self.assertEqual(currencyfortender.text,'Own rate ($)')
                time.sleep(1)

                browser = tenderDetails.listProjectmenu(browser)
                time.sleep(1)
                browser = Updatedetails.updateproject(browser)
                time.sleep(1)
                browser = Updatedetails.updateprojectdetailsbacktooriginal(browser,projecttype)
                time.sleep(1)
                browser = Updatedetails.saveprojectdetails(browser) #Save project

                time.sleep(3)
                i = i + 1
                logs.info("Test Case No : 100222 Passed Successfully")
        except Exception:
                logs.error("Validation with Test Case No: 100222 failed")
                browser.save_screenshot(fullpath)
                traceback.print_exc(file=sys.stdout)
                self.fail("Test Case No: 100222 failed")
                browser.implicitly_wait(5)
        finally:
                LauncheTender1.closebrowser(browser)

if __name__ == '__main__':
    unittest.main()