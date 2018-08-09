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
from UserProfile import UserProfileinfo
from setupenviron import setupValue
from logdriver import logvalue
from logouteTender import Userprofilemenu
from Registration import RegistrationineT
logs=logvalue.logger
logclose=logvalue()
ftime = time.mktime(time.localtime())
ptime=time.strftime("%d-%m-%Y_%H%M%S", time.localtime(ftime))
#filename = 'TestCase-100191-{0}.png'.format(ptime)
tf = 'test_UserprofileValidatedetailsinSuperadmin'
filename = 'Testcase-%s.png' %(tf)
path= setupValue().screenpath
fullpath = os.path.join(path,filename)

#Test case no:100191
class UserprofileValidatedetailsinSuperadmin(unittest.TestCase):
    def test_UserprofileValidatedetailsinSuperadmin(self):
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
            time.sleep(2)
            userprofile = UserProfileinfo()
            browser = userprofile.userprofilelink(browser)
            time.sleep(1)
            browser = userprofile.UserProfilePageUpdate(browser)
            time.sleep(2)

            logoutEstimator = Userprofilemenu()
            browser = logoutEstimator.logout_eTender(browser)
            time.sleep(1)

            browser = LauncheTender1.superAdminValidlogin(browser)
            registration = RegistrationineT()
            time.sleep(3)
            browser = registration.selectusersmenu(browser)
            time.sleep(1)
            browser = registration.usersearch(browser)
            time.sleep(1)
            browser = registration.userdetails(browser)
            time.sleep(1)

            userprofilevalidateFLEP = DataDriver()
            userfirstName_path = userprofilevalidateFLEP.readfromXML(folder_path+'\\Object\\UserProfileObject.xml','eTender','firstnameindetails') #Firstname #FLEP -->Firstname , LastName , Email and Phone
            time.sleep(3)
            userfirstName = browser.find_element_by_xpath(userfirstName_path)
            time.sleep(3)
            userfirstName1  = userfirstName.text
            self.assertEqual(userfirstName1,'suresh1')

            userLastName_path = userprofilevalidateFLEP.readfromXML(folder_path+'\\Object\\UserProfileObject.xml','eTender','lastnameindetails') #LastName
            time.sleep(3)
            userLastName = browser.find_element_by_xpath(userLastName_path)
            time.sleep(3)
            userLastName1  = userLastName.text
            self.assertEqual(userLastName1,'kumar1')

            useremail_path = userprofilevalidateFLEP.readfromXML(folder_path+'\\Object\\UserProfileObject.xml','eTender','emaildetails') #Email
            time.sleep(3)
            useremail = browser.find_element_by_xpath(useremail_path)
            time.sleep(3)
            useremail1  = useremail.text
            self.assertEqual(useremail1,'AutomationTestTwo@etender.com')
            time.sleep(2)

            usermobile_path = userprofilevalidateFLEP.readfromXML(folder_path+'\\Object\\UserProfileObject.xml','eTender','phonedetails') #MobilePhone
            time.sleep(3)
            usermobile = browser.find_element_by_xpath(usermobile_path)
            time.sleep(3)
            usermobile1  = usermobile.text
            self.assertEqual(usermobile1,'9342733658')
            time.sleep(2)

            logs.info("Test Case No : 100191 Passed Successfully")
            time.sleep(2)
            browser = registration.userdetailsclose(browser)
            time.sleep(1)
            browser = logoutEstimator.logout_eTender(browser)
            time.sleep(1)
        except Exception:
            logs.error("Validation with Test Case No: 100191 failed")
            browser.save_screenshot(fullpath)
            traceback.print_exc(file=sys.stdout)
            self.fail("Test Case No: 100191 failed")
            browser.implicitly_wait(5)
        finally:
            browser = LauncheTender1.estimatorValidlogin(browser)
            time.sleep(1)
            userprofile = UserProfileinfo()
            browser = userprofile.userprofilelink(browser)
            time.sleep(1)
            browser = userprofile.UserProfilePageUpdatebacktoOriginal(browser)
            time.sleep(1)
            LauncheTender1.closebrowser(browser)

if __name__ == '__main__':
    unittest.main()