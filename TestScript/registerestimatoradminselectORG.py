#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      suresh.kumar
#
# Created:     25/08/2016
# Copyright:   (c) suresh.kumar 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
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
from Registration import RegistrationineT
#from DBConnectMySQLdeleteORG import deleteorganisation
from datadriven import DataDriver
from setupenviron import setupValue
from logdriver import logvalue
logs=logvalue.logger
logclose=logvalue()
ftime = time.mktime(time.localtime())
ptime=time.strftime("%d-%m-%Y_%H%M%S", time.localtime(ftime))
#filename = 'TestCase-100168-{0}.png'.format(ptime)
tf = 'test_registerestimatoradminselectorg'
filename = 'Testcase-%s.png' %(tf)
path= setupValue().screenpath
fullpath = os.path.join(path,filename)

#Test case Number = 100168
class RegisterestimatoradminselectORG(unittest.TestCase):
    def test_registerestimatoradminselectorg(self):
        try:
            browserInstance = setupValue()
            browser = browserInstance.setupfunction()
            browser.implicitly_wait(5)
            LauncheTender1 = LauncheTenderclass()
            browser = LauncheTender1.openURL(browser)
            registration = RegistrationineT()
            browser = registration.register(browser)
            time.sleep(1)
            browser = registration.selectmaincontractorRole(browser)
            time.sleep(1)
            browser = registration.selectestimatoradminRole(browser)
            time.sleep(1)
            browser = registration.registrationForm(browser)
            time.sleep(1)
            browser = registration.organisationselect(browser)
            time.sleep(1)
            browser = registration.supplierRegistration(browser)
            time.sleep(1)
            browser = LauncheTender1.superAdminValidlogin(browser)
            time.sleep(1)
            browser = registration.supplierAuthorisation(browser)
            time.sleep(1)
            emailvalidate = DataDriver()
            validateemail = []
            time.sleep(1)
            emailvalidate_path = emailvalidate.readfromXML(folder_path+'\Object\Object.xml','eTender','emailvalidate')
            validateemail =browser.find_elements_by_xpath(emailvalidate_path)
            time.sleep(1)
            email = validateemail[1].text
            time.sleep(1)
            self.assertEqual(email,'test@etender.com')
            time.sleep(1)
            browser = registration.supplierAccept(browser)
            time.sleep(1)
            browser = registration.selectusersmenu(browser)
            time.sleep(1)
            browser = registration.suppliersearch(browser)
            time.sleep(1)
            browser = registration.supplierDeletion(browser)
            time.sleep(1)
            browser = registration.organisationmenu(browser)
            time.sleep(1)
            browser = registration.organisationsearchdelete(browser)
            time.sleep(1)
##            Delete = deleteorganisation()
##            browser = Delete.orgId(browser)
##            time.sleep(1)
##            browser = Delete.orguser(browser)
##            time.sleep(1)
##            browser = Delete.organisation(browser)
##            time.sleep(1)
            logs.info("Test Case No : 100168 Passed Successfully")
        except Exception:
            logs.error("Validation with Test Case No: 100168 failed")
            browser.save_screenshot(fullpath)
            traceback.print_exc(file=sys.stdout)
            self.fail("Test Case No: 100168 failed")
            browser.implicitly_wait(5)
        finally:
            LauncheTender1.closebrowser(browser)