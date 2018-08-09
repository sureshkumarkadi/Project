#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      suresh.kumar
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
from UserProfile import UserProfileinfo
from tenderDetails import SubmitTenderclass
from datadriven import DataDriver
from setupenviron import setupValue
from logouteTender import Userprofilemenu
from logdriver import logvalue
logs=logvalue.logger
logclose=logvalue()
ftime = time.mktime(time.localtime())
ptime=time.strftime("%d-%m-%Y_%H%M%S", time.localtime(ftime))
#filename = 'TestCase-100190-{0}.png'.format(ptime)
tf = 'test_UserProfileinfoupdate'
filename = 'Testcase-%s.png' %(tf)
path= setupValue().screenpath
fullpath = os.path.join(path,filename)

#Test case Number = 100190
class UserProfileinfoupdate(unittest.TestCase):
    def test_UserProfileinfoupdate(self):
        try:
            browserInstance = setupValue()
            browser = browserInstance.setupfunction()
            browser.implicitly_wait(5)
            time.sleep(1)
            LauncheTender1 = LauncheTenderclass()
            browser = LauncheTender1.openURL(browser)
            time.sleep(1)
            browser = LauncheTender1.estimatorValidlogin(browser)
            time.sleep(1)
            userprofile = UserProfileinfo()
            browser = userprofile.userprofilelink(browser)
            time.sleep(1)
            browser = userprofile.UserProfilePageUpdate(browser)
            time.sleep(1)
            userName = DataDriver()
            time.sleep(1)
            username = []
            username_path = userName.readfromXML(folder_path+'\\Object\\UserProfileObject.xml','eTender','username')
            username = browser.find_elements_by_xpath(username_path) #username in Estimator Login
            username2 = username[0].text
            time.sleep(1)
            username3 = username2.strip()
            time.sleep(1)
            self.assertEqual(username3,'suresh1 kumar1')
            time.sleep(2)
            logs.info("Test Case No : 100190 Passed Successfully")
        except Exception:
            logs.error("Validation with Test Case No: 100190 failed")
            browser.save_screenshot(fullpath)
            traceback.print_exc(file=sys.stdout)
            self.fail("Test Case No: 100190 failed")
            browser.implicitly_wait(5)
        finally:
            time.sleep(2)
            browser = userprofile.UserProfilePageUpdatebacktoOriginal(browser)
            LauncheTender1.closebrowser(browser)