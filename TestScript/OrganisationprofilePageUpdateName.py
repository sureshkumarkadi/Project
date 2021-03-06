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
logs=logvalue.logger
logclose=logvalue()
ftime = time.mktime(time.localtime())
ptime=time.strftime("%d-%m-%Y_%H%M%S", time.localtime(ftime))
#filename = 'TestCase-100066-{0}.png'.format(ptime)
tf = 'test_OrganisationprofileupdateName'
filename = 'Testcase-%s.png' %(tf)
path= setupValue().screenpath
fullpath = os.path.join(path,filename)

#Test case no:100066
class OrganisationprofileUpdateName(unittest.TestCase):
    def test_OrganisationprofileupdateName(self):
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
            time.sleep(1)
            organisationprofileupdateName = DataDriver()
            organisationprofileName = organisationprofileupdateName.readfromXML(folder_path+'\Object\OrgProfileObject.xml','eTender','organisationname') #Project
            time.sleep(3)
            organisationprofileName1 = browser.find_element_by_xpath(organisationprofileName)
            time.sleep(3)
            organisationprofileName2  = organisationprofileName1.text
            self.assertEqual(organisationprofileName2,'DownerMouchelTest')
            time.sleep(2)
            logs.info("Test Case No : 100066 Passed Successfully")
            browser = Organizationprofile.OrganisationProfilePageUpdatetoOriginal(browser)
            time.sleep(2)
            browser = LauncheTender1.switchOrganisation(browser)
            time.sleep(2)
            browser = LauncheTender1.selectsecondOrganisation(browser)
            time.sleep(5)
        except Exception:
            logs.error("Validation with Test Case No: 100066 failed")
            browser.save_screenshot(fullpath)
            traceback.print_exc(file=sys.stdout)
            self.fail("Test Case No: 100066 failed")
            browser.implicitly_wait(5)
        finally:
            LauncheTender1.closebrowser(browser)











