#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      mathew.jacob
#
# Created:     25/08/2016
# Copyright:   (c) mathew.jacob 2016
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
from tenderDetails import Tenderdetails
from datadriven import DataDriver
from setupenviron import setupValue
from logdriver import logvalue
logs=logvalue.logger
logclose=logvalue()
ftime = time.mktime(time.localtime())
ptime=time.strftime("%d-%m-%Y_%H%M%S", time.localtime(ftime))
#filename = 'TestCase-100008-{0}.png'.format(ptime)
tf = 'test_ColumnsinTradeList'
filename = 'Testcase-%s.png' %(tf)
path= setupValue().screenpath
fullpath = os.path.join(path,filename)

#Test case Number = 100008
class ColumnsinTradeList(unittest.TestCase):
    def test_ColumnsinTradeList(self):
        try:
            browserInstance = setupValue()
            browser = browserInstance.setupfunction()
            browser.implicitly_wait(5)
            LauncheTender1 = LauncheTenderclass()
            browser = LauncheTender1.openURL(browser)
            browser.implicitly_wait(5)
            browser = LauncheTender1.subcontractorValidlogin(browser)
            browser = LauncheTender1.list_Organisation(browser)
            browser = LauncheTender1.verifyorganisationdetails(browser)
            browser = LauncheTender1.list_project(browser)
            tenderDetails = Tenderdetails()
            time.sleep(1)
            browser = tenderDetails.Subcontratorproject(browser)
            browser = tenderDetails.verifyColumnsinTradeList(browser)
            time.sleep(1)
            columns_XML = DataDriver()
            columns_path = columns_XML.readfromXML(folder_path+'\Object\Object.xml','eTender','tradecolumns')
            trade_columns = []
            time.sleep(1)
            trade_columns = browser.find_elements_by_xpath(columns_path)
            time.sleep(1)
            browser.implicitly_wait(5)
            tradecolumn1 = trade_columns[0].text
            tradecolumn2 = trade_columns[1].text
            tradecolumn3 = trade_columns[2].text
            time.sleep(1)
            tradecolumn4 = trade_columns[3].text
##            tradecolumn5 = trade_columns[4].text
##            tradecolumn6 = trade_columns[5].text
##            time.sleep(1)
##            tradecolumn7 = trade_columns[6].text
            self.assertEqual(tradecolumn1,'DOMESTIC')
            #self.assertEqual(tradecolumn2,'Received date:May 14, 2018')
            time.sleep(1)
            #self.assertEqual(tradecolumn3,'Due date:Jul 25, 2018')
            self.assertEqual(tradecolumn4,'Responded date:')
            time.sleep(1)
##            self.assertEqual(tradecolumn5,'Received date')
##            self.assertEqual(tradecolumn6,'Due date')
##            time.sleep(1)
##            self.assertEqual(tradecolumn7,'Document')
            logs.info("Test Case No : 100008 Passed Successfully")
        except Exception:
            logs.error("Validation with Test Case No: 100008 failed")
            browser.save_screenshot(fullpath)
            traceback.print_exc(file=sys.stdout)
            self.fail("Test Case No: 100008 failed")
            browser.implicitly_wait(5)
        finally:
            LauncheTender1.closebrowser(browser)

if __name__ == '__main__':
    unittest.main()