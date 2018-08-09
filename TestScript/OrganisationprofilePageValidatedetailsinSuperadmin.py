#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      suresh.kumar
#
# Created:     25-08-2016
# Copyright:   (c) suresh.kumar 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import unittest
import sys
import time
import os
import traceback
from selenium.webdriver.support.ui import WebDriverWait
dir_path = os.path.dirname(os.path.realpath(__file__))
folder_path=os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0,folder_path+"\Library")
sys.path.insert(0,folder_path+"\Syslibrary")
sys.path.insert(0,folder_path+"\Data")
sys.path.insert(0,folder_path+"\Object")
from launcheTender import LauncheTenderclass
from datadriven import DataDriver
from Organisationprofile import OrganisationProfile
from setupenviron import setupValue
from logdriver import logvalue
from logouteTender import Userprofilemenu
from Registration import RegistrationineT
logs=logvalue.logger
logclose=logvalue()
ftime = time.mktime(time.localtime())
ptime=time.strftime("%d-%m-%Y_%H%M%S", time.localtime(ftime))
#filename = 'TestCase-100187-{0}.png'.format(ptime)
tf = 'test_OrganisationprofileValidatedetailsinSuperadmin'
filename = 'Testcase-%s.png' %(tf)
path= setupValue().screenpath
fullpath = os.path.join(path,filename)

#Test case no:100187
class OrganisationprofileValidatedetailsinSuperadmin(unittest.TestCase):
    def test_OrganisationprofileValidatedetailsinSuperadmin(self):
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
            time.sleep(7)
##            browser = LauncheTender1.switchOrganisation(browser)
##            time.sleep(1)
##            browser = LauncheTender1.selectfirstOrganisation(browser)
##            time.sleep(7)
            Organizationprofile = OrganisationProfile()
            browser = Organizationprofile.OpenOrganisationProfilePage(browser)
            time.sleep(1)
            browser = Organizationprofile.OrganisationProfilePageUpdate(browser)
            time.sleep(2)

            logoutEstimator = Userprofilemenu()
            browser = logoutEstimator.logout_eTender(browser)
            time.sleep(1)

            browser = LauncheTender1.superAdminValidlogin(browser)
            registration = RegistrationineT()
            browser = registration.organisationmenu(browser)
            time.sleep(1)
            browser = registration.organisationsearch(browser)

            organisationprofilevalidateNPWE = DataDriver()
            organisationName_path = organisationprofilevalidateNPWE.readfromXML(folder_path+'\Object\OrgProfileObject.xml','eTender','organisationName') #organisationName
            time.sleep(3)
            organisationName = browser.find_element_by_xpath(organisationName_path)
            time.sleep(3)
            organisationName1  = organisationName.text
            self.assertEqual(organisationName1,'DownerMouchelTest')

            organisationPhone_path = organisationprofilevalidateNPWE.readfromXML(folder_path+'\Object\OrgProfileObject.xml','eTender','organisationphone') #organisationphone
            time.sleep(1)
            organisationPhone = browser.find_element_by_xpath(organisationPhone_path)
            time.sleep(1)
            organisationPhone1  = organisationPhone.text
            self.assertEqual(organisationPhone1,'08025226964')

            organisationWebsite_path = organisationprofilevalidateNPWE.readfromXML(folder_path+'\Object\OrgProfileObject.xml','eTender','organisationwebsite') #organisationwebsite
            time.sleep(1)
            organisationWebsite = browser.find_element_by_xpath(organisationWebsite_path)
            time.sleep(1)
            organisationWebsite1  = organisationWebsite.text
            self.assertEqual(organisationWebsite1,'www.downermouchelTest.com')
            time.sleep(2)

            organisationEmail_path = organisationprofilevalidateNPWE.readfromXML(folder_path+'\Object\OrgProfileObject.xml','eTender','organizationEmail') #organisationEmail
            time.sleep(1)
            organisationEmail = browser.find_element_by_xpath(organisationEmail_path)
            time.sleep(1)
            organisationEmail1  = organisationEmail.text
            self.assertEqual(organisationEmail1,'nagendra123@etender.com')
            time.sleep(2)
            logs.info("Test Case No : 100187 Passed Successfully")
            time.sleep(2)
            browser = registration.organisationdetailsclose(browser)
            time.sleep(1)
            browser = logoutEstimator.logout_eTender(browser)
            time.sleep(1)
            browser = LauncheTender1.estimatorValidlogin(browser)
            time.sleep(1)
        except Exception:
            logs.error("Validation with Test Case No: 100187 failed")
            browser.save_screenshot(fullpath)
            traceback.print_exc(file=sys.stdout)
            self.fail("Test Case No: 100187 failed")
            browser.implicitly_wait(5)
        finally:
            browser = Organizationprofile.OrganisationProfilePageUpdatetoOriginal(browser)
            time.sleep(3)
            browser = LauncheTender1.switchOrganisation(browser)
            time.sleep(1)
            browser = LauncheTender1.selectsecondOrganisation(browser)
            time.sleep(7)
            LauncheTender1.closebrowser(browser)









