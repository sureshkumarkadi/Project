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
from tenderDetails import SubmitTenderclass
from datadriven import DataDriver
from setupenviron import setupValue
from logouteTender import Userprofilemenu
from logdriver import logvalue
logs=logvalue.logger
logclose=logvalue()
ftime = time.mktime(time.localtime())
ptime=time.strftime("%d-%m-%Y_%H%M%S", time.localtime(ftime))
#filename = 'TestCase-100058-{0}.png'.format(ptime)
tf = 'test_notesinEstimator'
filename = 'Testcase-%s.png' %(tf)
path= setupValue().screenpath
fullpath = os.path.join(path,filename)

#Test case Number = 100058
class Notesinestimator(unittest.TestCase):
    def test_notesinEstimator(self):
        try:
            browserInstance = setupValue()
            browser = browserInstance.setupfunction()
            browser.implicitly_wait(5)
            time.sleep(1)
            LauncheTender1 = LauncheTenderclass()
            browser = LauncheTender1.openURL(browser)
            browser.implicitly_wait(5)
            time.sleep(1)
            browser = LauncheTender1.subcontractorValidlogin(browser)
            browser = LauncheTender1.verifyorganisationdetails(browser)
            browser = LauncheTender1.list_project(browser)
            tenderDetails = Tenderdetails()
            time.sleep(1)
            browser = tenderDetails.Subcontratorproject(browser)
            browser = tenderDetails.suppliertender(browser)
            time.sleep(1)
            browser = tenderDetails.hoverThemousefornoteButton(browser)
            browser = tenderDetails.dialogueBoxtoAddaNote(browser)
            time.sleep(1)
            browser = tenderDetails.addingNotes(browser)
            enteredNotes = DataDriver()
            time.sleep(1)
            click_notesbubble = []
            clicknotesbubble_path = enteredNotes.readfromXML(folder_path+'\Object\Object.xml','eTender','clicknotesbubble')
            time.sleep(1)
            click_notesbubble = browser.find_elements_by_xpath(clicknotesbubble_path) #Click on Notes bubble
            click_notesbubble[4].click()
            time.sleep(2)
            enterednotes_path = enteredNotes.readfromXML(folder_path+'\Object\Object.xml','eTender','addingnotes') #adding notes
            time.sleep(1)
            enterednotes = browser.find_element_by_xpath(enterednotes_path) #Webelement for entered notes
            time.sleep(1)
            subcontractornotes = enterednotes.text
            addingnotes = DataDriver()
            savenotes_path = addingnotes.readfromXML(folder_path+'\Object\Object.xml','eTender','savenotes')
            Save_Notes = browser.find_element_by_xpath(savenotes_path) #Save button
            time.sleep(1)
            Save_Notes.click()
            time.sleep(1)
            SubmitTender = SubmitTenderclass()
            browser = SubmitTender.submitTender(browser)
            time.sleep(1)
            browser = SubmitTender.confirmTendersubmission(browser)
            Userprofilemenu_logout = Userprofilemenu()
            time.sleep(1)
            browser = Userprofilemenu_logout.logout_eTender(browser)
            browser = LauncheTender1.estimatorValidlogin(browser)
            time.sleep(1)
            browser = tenderDetails.estimatorProject(browser)
            browser = tenderDetails.estimatortender(browser)
            time.sleep(3)
            browser = tenderDetails.notesinEstimator(browser)
            estimatornotes = DataDriver()
            time.sleep(1)
            notesinestimator_path = estimatornotes.readfromXML(folder_path+'\Object\Object.xml','eTender','NotesinEstimatorLogin')
            text_noteswindow_Estimatorlogin = browser.find_element_by_xpath(notesinestimator_path) #Notes in Estimator Login
            time.sleep(1)
            time.sleep(1)
            estimatornotes1 = text_noteswindow_Estimatorlogin.text
            time.sleep(1)
            browser.implicitly_wait(5)
            if subcontractornotes == estimatornotes1:
                print("pass")
            else:
                print("fail")
            time.sleep(1)
            #estimatornotes1 = DataDriver()
            cancelwindow_path = estimatornotes.readfromXML(folder_path+'\Object\Object.xml','eTender','cancelwindow')
            cancel_notewindow = browser.find_element_by_xpath(cancelwindow_path) # Click on cancel link
            time.sleep(1)
            cancel_notewindow.click()
            time.sleep(1)
            logs.info("Test Case No : 100058 Passed Successfully")
        except Exception:
            logs.error("Validation with Test Case No: 100058 failed")
            browser.save_screenshot(fullpath)
            traceback.print_exc(file=sys.stdout)
            self.fail("Test Case No: 100058 failed")
            browser.implicitly_wait(5)
        finally:
            LauncheTender1.closebrowser(browser)