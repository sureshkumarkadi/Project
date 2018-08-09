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
from datadriven import DataDriver
from setupenviron import setupValue
from logdriver import logvalue
logs=logvalue.logger
logclose=logvalue()
ftime = time.mktime(time.localtime())
ptime=time.strftime("%d-%m-%Y_%H%M%S", time.localtime(ftime))
#filename = 'TestCase-100024-{0}.png'.format(ptime)
tf = 'test_savingNotes'
filename = 'Testcase-%s.png' %(tf)
path= setupValue().screenpath
fullpath = os.path.join(path,filename)

#Test case number = 100024
class Savingnotes(unittest.TestCase):
    def test_savingNotes(self):
        try:
            browserInstance = setupValue()
            browser = browserInstance.setupfunction()
            browser.implicitly_wait(5)
            LauncheTender1 = LauncheTenderclass()
            browser = LauncheTender1.openURL(browser)
            browser.implicitly_wait(5)
            browser = LauncheTender1.subcontractorValidlogin(browser)
            browser = LauncheTender1.list_Organisation(browser)
            browser = LauncheTender1.verifyorganisationdetails(browser)
            browser = LauncheTender1.list_project(browser)
            tenderDetails = Tenderdetails()
            browser = tenderDetails.Subcontratorproject(browser)
            browser = tenderDetails.suppliertender(browser)
            browser = tenderDetails.hoverThemousefornoteButton(browser)
            browser = tenderDetails.dialogueBoxtoAddaNote(browser)
            browser = tenderDetails.addingNotes(browser)
            browser.implicitly_wait(5)
            dialogbox = DataDriver()
            dialogbox_path = dialogbox.readfromXML(folder_path+'\Object\Object.xml','eTender','dialogbox') #dialogbox
            add_noteswindow = browser.find_element_by_xpath(dialogbox_path) #Webelement for dialogbox
            print add_noteswindow.text
            windowtitle = add_noteswindow.text
            self.assertEqual(windowtitle,'Add a note')
            logs.info("Test Case No : 100024 Passed Successfully")
        except Exception:
            logs.error("Validation with Test Case No: 100024 failed")
            browser.save_screenshot(fullpath)
            traceback.print_exc(file=sys.stdout)
            self.fail("Test Case No: 100024 failed")
            browser.implicitly_wait(5)
        finally:
            LauncheTender1.closebrowser(browser)