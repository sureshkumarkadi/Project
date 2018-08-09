#-------------------------------------------------------------------------------
# Name:         AT_TaskSchedulerReset.py
#
# Purpose:      To verify Reset functionality in Task Scheduler
#
# Tast Case Id  100180
#
# Author:      mathew.jacob
#
# Created:     17/02/2017
#
# Copyright:   (c) Causeway Technologies 2016
#-------------------------------------------------------------------------------


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
from datadriven import DataDriver
from setupenviron import setupValue
from logdriver import logvalue
from AdminEstimator import Adminclass
from logouteTender import Userprofilemenu
orgLink=DataDriver()
logs=logvalue.logger
ftime = time.mktime(time.localtime())
ptime=time.strftime("%d-%m-%Y_%H%M%S", time.localtime(ftime))
#filename = 'TestCase-100180-{0}.png'.format(ptime)
tf = 'test_TaskSchedulerReset'
filename = 'Testcase-%s.png' %(tf)
path= setupValue().screenpath
fullpath = os.path.join(path,filename)

class ResetTaskScheduler(unittest.TestCase):
    def test_TaskSchedulerReset(self):
        try:
            browserInstance = setupValue()
            adminfunction=Adminclass()
            browser = browserInstance.setupfunction()
            LauncheTender = LauncheTenderclass()
            logOut=Userprofilemenu()
            browser = LauncheTender.openURL(browser)
            browser = LauncheTender.estimatorValidlogin(browser)
            adminfunction.OpenTaskScheduler(browser)
            time.sleep(4)
            p=browser.find_elements_by_xpath(orgLink.readfromXML(folder_path+'\Object\AdminEstimator.xml','eTender','DueDateReminder'))
            DueValue=p[0].get_attribute('value')
            DueNewvalue=int(DueValue)+1
            p[0].clear()
            p[0].send_keys(DueNewvalue)
            Acceptreminder=p[1].get_attribute('value')
            Acceptnewreminder=int(Acceptreminder)+1
            p[1].clear()
            p[1].send_keys(Acceptnewreminder)
            browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\AdminEstimator.xml','eTender','ResetButton')).click()
            time.sleep(4)
            p1New=browser.find_elements_by_xpath(orgLink.readfromXML(folder_path+'\Object\AdminEstimator.xml','eTender','TenderReminder'))
            DueValueLatest=p1New[0].get_attribute('value')
            AcceptLatest=p1New[1].get_attribute('value')
            self.assertNotEquals(int(DueValueLatest),DueNewvalue)
            self.assertNotEquals(int(AcceptLatest),Acceptnewreminder)
        except Exception:
            logs.error("Validation with Test Case No: 100180 failed")
            browser.save_screenshot(fullpath)
            traceback.print_exc(file=sys.stdout)
            self.fail("Test Case No: 100180 failed")
            browser.implicitly_wait(5)
        finally:
            browser=logOut.logout_eTender(browser)
            LauncheTender.closebrowser(browser)