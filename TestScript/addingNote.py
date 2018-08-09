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
import time
import os
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
tf = 'test_addingNotes'
filename = 'Testcase-%s.png' %(tf)
path= setupValue().screenpath
fullpath = os.path.join(path,filename)

#Test case number = 100024
class Addingnotes(unittest.TestCase):
    def test_addingNotes(self):
        try:
            browserInstance = setupValue()
            browser = browserInstance.setupfunction()
            browser.implicitly_wait(5)
            time.sleep(1)
            LauncheTender1 = LauncheTenderclass()
            browser = LauncheTender1.openURL(browser)
            browser.implicitly_wait(5)
            time.sleep(2)
            browser = LauncheTender1.subcontractorValidlogin(browser)
            #browser = LauncheTender1.list_Organisation(browser)
            time.sleep(1)
            browser = LauncheTender1.verifyorganisationdetails(browser)
            browser = LauncheTender1.list_project(browser)
            tenderDetails = Tenderdetails()
            time.sleep(1)
            browser = tenderDetails.Subcontratorproject(browser)
            browser = tenderDetails.suppliertender(browser)
            time.sleep(1)
            browser = tenderDetails.hoverThemousefornoteButton(browser)
            browser = tenderDetails.dialogueBoxtoAddaNote(browser)
            browser = tenderDetails.addingNotes(browser)
            time.sleep(3)
            enteredNotes = DataDriver()
            click_notesbubble = []
            clicknotesbubble_path = enteredNotes.readfromXML(folder_path+'\Object\Object.xml','eTender','clicknotesbubble')
            time.sleep(1)
            click_notesbubble = browser.find_elements_by_xpath(clicknotesbubble_path) #Click on Notes bubble
            time.sleep(3)
            click_notesbubble[4].click()
            enterednotes_path = enteredNotes.readfromXML(folder_path+'\Object\Object.xml','eTender','addingnotes') #adding notes
            time.sleep(1)
            enterednotes = browser.find_element_by_xpath(enterednotes_path) #Webelement for entered notes
            actualnotes = enterednotes.text
            time.sleep(1)
            self.assertEqual(actualnotes,'Notes 1')
            savenotes_path = enteredNotes.readfromXML(folder_path+'\Object\Object.xml','eTender','savenotes')
            Save_Notes = browser.find_element_by_xpath(savenotes_path) #Save button
            Save_Notes.click()
            time.sleep(2)
            browser = tenderDetails.deleteNotes(browser)
            time.sleep(1)
            logs.info("Test Case No : 100024 Passed Successfully")
        except Exception:
            logs.error("Validation with Test Case No: 100024 failed")
            browser.save_screenshot(fullpath)
            traceback.print_exc(file=sys.stdout)
            self.fail("Test Case No: 100024 failed")
            browser.implicitly_wait(5)
        finally:
            LauncheTender1.closebrowser(browser)