#-------------------------------------------------------------------------------
# Name:         AT_ResponseToExcel
#
# Tast Case Id  100341
#
# Purpose:      To Verify that export to excel functionality is working in Tender details page
#
# Author:      mathew.jacob
#
# Created:     27/10/2017
# Copyright:   (c) Causeway Technologies 2017
#-------------------------------------------------------------------------------

from selenium.webdriver.support.ui import WebDriverWait
import unittest
import sys
import os
import os.path

import time
import traceback
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
from selenium.common.exceptions import NoSuchElementException
logs=logvalue.logger
orgLink=DataDriver()
ftime = time.mktime(time.localtime())
ptime=time.strftime("%d-%m-%Y_%H%M%S", time.localtime(ftime))
#filename = 'TestCase-100341-{0}.png'.format(ptime)
tf = 'test_ExcelDetailsExport'
filename = 'Testcase-%s.png' %(tf)
path= setupValue().screenpath
fullpath = os.path.join(path,filename)
downloadfile=orgLink.readfromXML(folder_path+'\Data\TenderData.xml','eTender','ExportDetailsFileName')
dpath=setupValue().downloadpath
dpathfile=os.path.join(dpath,downloadfile)
class ExportToDetailsExcel(unittest.TestCase):
    def test_ExcelDetailsExport(self):
        try:
            browserInstance = setupValue()
            browser = browserInstance.setupfunction()
            browser.implicitly_wait(10)
            LauncheTender = LauncheTenderclass()
            TenderAction=TenderClass()
            logOut=Userprofilemenu()
            time.sleep(2)
            browser = LauncheTender.openURL(browser)
            browser = LauncheTender.estimatorValidlogin1(browser)
            time.sleep(3)
            ProjName=TenderAction.ProjectCreation(browser)
            TenderAction.OpenProject(ProjName,browser)
            NewTender=TenderAction.TenderCreation(browser)
            downloadfile=NewTender+".xlsx"
            dpath=setupValue().downloadpath
            dpathfile=os.path.join(dpath,downloadfile)
            time.sleep(2)
            TenderAction.OpenDetails(browser,NewTender)
            time.sleep(2)
            browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','ExportDetailButton')).click()
            time.sleep(2)
            os.path.exists(dpathfile)
            if os.path.isfile(dpathfile):
                os.remove(dpathfile)
            else:
                raise OSError
            logs.info("Test Case No : 100341 Passed Successfully")
        except NoSuchElementException:
            logs.error("Validation with Test Case No: 100341 failed")
            browser.save_screenshot(fullpath)
            traceback.print_exc(file=sys.stdout)
            self.fail("Test Case No: 100341 failed")
        except OSError:
            self.fail("Test Case No: 100341 failed - File doesn't exists")
        except Exception:
            logs.error("Validation with Test Case No: 100341 failed")
            browser.save_screenshot(fullpath)
            traceback.print_exc(file=sys.stdout)
            self.fail("Test Case No: 100341 failed")
        finally:
            browser=logOut.logout_eTender(browser)
            LauncheTender.closebrowser(browser)