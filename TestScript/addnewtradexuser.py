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
from Tradexsuppliers import Tradexsupplier
from datadriven import DataDriver
from setupenviron import setupValue
from logouteTender import Userprofilemenu
from logdriver import logvalue
logs=logvalue.logger
logclose=logvalue()
ftime = time.mktime(time.localtime())
ptime=time.strftime("%d-%m-%Y_%H%M%S", time.localtime(ftime))
#filename = 'TestCase-TC - 1005-{0}.png'.format(ptime)
tf = 'test_addnewtradexuser'
filename = 'Testcase-%s.png' %(tf)
path= setupValue().screenpath
fullpath = os.path.join(path,filename)

#Test case Number = TC - 1005
class Addnewtradexuser(unittest.TestCase):
    def test_addnewtradexuser(self):
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
##            browser = LauncheTender1.switchOrganisation(browser)
##            time.sleep(1)
##            browser = LauncheTender1.selectsecondOrganisation(browser)
##            time.sleep(7)
            tenderDetails = Tenderdetails()
            browser = tenderDetails.estimatorProject(browser)
            time.sleep(1)

            tradexsupplierDetails = Tradexsupplier()
            browser = tenderDetails.estimatortendertradex(browser)
            time.sleep(2)
            browser = tenderDetails.viewsupplierdetails(browser)
            time.sleep(1)
            browser = tradexsupplierDetails.estimatortradexaddsupplier(browser)
            time.sleep(2)
            browser = tradexsupplierDetails.entersupplier(browser)
            time.sleep(2)
            browser = tradexsupplierDetails.viewtradexsupplierdetails(browser)
            time.sleep(1)
            browser = tradexsupplierDetails.addnewtradexuser(browser)
            time.sleep(2)

            usercontactdetails = DataDriver()
            tradename_path = usercontactdetails.readfromXML(folder_path+'\Object\Tradex.xml','eTender','tradename')
            time.sleep(1)
            tradename = browser.find_element_by_xpath(tradename_path) #Contact details list
            time.sleep(1)

            tradeemail_path = usercontactdetails.readfromXML(folder_path+'\Object\Tradex.xml','eTender','tradeemail')
            time.sleep(1)
            tradeemail = browser.find_element_by_xpath(tradeemail_path) #Contact details list
            time.sleep(1)
            self.assertEqual(tradename.text,'plywood')
            self.assertEqual(tradeemail.text,'plywood@newuser.com')
            time.sleep(1)

            browser = tradexsupplierDetails.closetradexuserwindow(browser)
            time.sleep(1)
            browser = tradexsupplierDetails.closetradexsupplierwindow(browser)
            time.sleep(1)

            logs.info("Test Case No : TC - 1005 Passed Successfully")
        except Exception:
            logs.error("Validation with Test Case No: TC - 1005 failed")
            browser.save_screenshot(fullpath)
            traceback.print_exc(file=sys.stdout)
            self.fail("Test Case No: TC - 1005 failed")
            browser.implicitly_wait(5)
        finally:
            LauncheTender1.closebrowser(browser)

if __name__ == '__main__':
    unittest.main()