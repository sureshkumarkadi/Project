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
from logdriver import logvalue
logs=logvalue.logger
logclose=logvalue()
ftime = time.mktime(time.localtime())
ptime=time.strftime("%d-%m-%Y_%H%M%S", time.localtime(ftime))
#filename = 'TestCase-100002-{0}.png'.format(ptime)
tf = 'test_openbrowser'
filename = 'Testcase-%s.png' %(tf)
path= setupValue().screenpath
fullpath = os.path.join(path,filename)

#Test case no:100002
class LoginAction(unittest.TestCase):
    def test_openbrowser(self):
        try:
            launcheTender1 = LauncheTenderclass()
            browser = launcheTender1.launchetender()
            Login = browser.find_element_by_xpath("//button[@id='submitButton']") #Login button
            Login1 = Login.text
            self.assertEqual(Login1, 'Log In')
            #browser.close()
            logs.info("Test Case No : 100002 Passed Successfully")
        except Exception:
            logs.error("Validation with Test Case No: 100002 failed")
            browser.save_screenshot(fullpath)
            traceback.print_exc(file=sys.stdout)
            self.fail("Test Case No: 100002 failed")
            browser.implicitly_wait(5)
