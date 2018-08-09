#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      suresh.kumar
#
# Created:     25/08/2016
# Copyright:   (c) Causeway
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
##from RESTAPI import ReopentenderusingRESTAPIclass
from RESTAPIStaging import ReopentenderusingRESTAPIclass
from datadriven import DataDriver
from setupenviron import setupValue
from logouteTender import Userprofilemenu
from logdriver import logvalue
logs=logvalue.logger
logclose=logvalue()
ftime = time.mktime(time.localtime())
ptime=time.strftime("%d-%m-%Y_%H%M%S", time.localtime(ftime))
#filename = 'TestCase-100186-{0}.png'.format(ptime)
tf = 'test_createtenderdetialsfromapi'
filename = 'Testcase-%s.png' %(tf)
path= setupValue().screenpath
fullpath = os.path.join(path,filename)


#Test case Number = 100186
class Createtenderdetialsfromapi(unittest.TestCase):
    def test_createtenderdetialsfromapi(self):
        try:
            browserInstance = setupValue()
            browser = browserInstance.setupfunction()
            tenderDetails = Tenderdetails()
            time.sleep(1)
            browser.implicitly_wait(5)
            time.sleep(1)
            createproject = ReopentenderusingRESTAPIclass()
            time.sleep(1)
            accesstoken = createproject.AuthunticateAPI()
            time.sleep(1)
            idValue = createproject.Createproject(accesstoken)
            time.sleep(2)
            createproject.Createtender(idValue,accesstoken)
            time.sleep(2)
            LauncheTender1 = LauncheTenderclass()
            time.sleep(1)
            browser = LauncheTender1.openURL(browser)
            browser.implicitly_wait(5)
            browser = LauncheTender1.estimatorValidlogin(browser)
            time.sleep(1)
##            browser = LauncheTender1.switchOrganisation(browser)
##            time.sleep(1)
##            browser = LauncheTender1.selectfirstOrganisation(browser)
##            time.sleep(7)
            browser = tenderDetails.estimatorprojectAPI(browser)
            time.sleep(1)
            browser = tenderDetails.estimatortender(browser)
            time.sleep(2)
            itemdescription = DataDriver()
            itemdescription_path = itemdescription.readfromXML(folder_path+'\Object\SwitchOrganisation.xml','eTender','itemdescription') #Item-descrition
            time.sleep(1)
            item_description = browser.find_element_by_xpath(itemdescription_path) #Webelement for Item description
            time.sleep(1)
            itemdescription = item_description.text
            time.sleep(1)
            self.assertEqual(itemdescription,'65 mm thick')
            time.sleep(2)
            createproject.Deleteproject(idValue,accesstoken)
            time.sleep(2)
##            browser = LauncheTender1.switchOrganisation(browser)
##            time.sleep(1)
##            browser = LauncheTender1.selectsecondOrganisation(browser)
##            time.sleep(1)
            logs.info("Test Case No : 100186 Passed Successfully")
        except Exception:
            logs.error("Validation with Test Case No: 100186 failed")
            browser.save_screenshot(fullpath)
            traceback.print_exc(file=sys.stdout)
            self.fail("Test Case No: 100186 failed")
            browser.implicitly_wait(5)
        finally:
            LauncheTender1.closebrowser(browser)

if __name__ == '__main__':
    unittest.main()