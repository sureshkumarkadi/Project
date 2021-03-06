#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      suresh.kumar
#
# Created:     14/04/2017
# Copyright:   (c) suresh.kumar 2016
# Licence:     <causeway licence>
#-------------------------------------------------------------------------------
from selenium.webdriver.support.ui import WebDriverWait
import unittest
import sys
import os
import time
import traceback
import xlrd
from babel import numbers

dir_path = os.path.dirname(os.path.realpath(__file__))
folder_path=os.path.abspath(os.path.join(dir_path, os.pardir))

book = xlrd.open_workbook(folder_path+'\Data\eTender.xls', formatting_info=True)
sheet = book.sheet_by_name('UpdateProjectDetails')

sys.path.insert(0,folder_path+"\Library")
sys.path.insert(0,folder_path+"\Syslibrary")
sys.path.insert(0,folder_path+"\Data")
sys.path.insert(0,folder_path+"\Object")
from launcheTender import LauncheTenderclass
from tenderDetails import Tenderdetails
from tenderDetails import SubmitTenderclass
from eTenderUpdateProjectDetails import updatedetails
from datadriven import DataDriver
from setupenviron import setupValue
from logouteTender import Userprofilemenu
from logdriver import logvalue
logs=logvalue.logger
logclose=logvalue()
ftime = time.mktime(time.localtime())
ptime=time.strftime("%d-%m-%Y_%H%M%S", time.localtime(ftime))
#filename = 'TestCase-100194-{0}.png'.format(ptime)
tf = 'test_updateindependentproject'
filename = 'Testcase-%s.png' %(tf)
path= setupValue().screenpath
fullpath = os.path.join(path,filename)

#Test case Number = 100194
class Updateindependentproject(unittest.TestCase):
    def test_updateindependentproject(self):
        try:
            i = 10
            while i<11:
                browserInstance = setupValue()
                browser = browserInstance.setupfunction()
                browser.implicitly_wait(5)
                time.sleep(1)
                LauncheTender1 = LauncheTenderclass()
                browser = LauncheTender1.openURL(browser)
                browser.implicitly_wait(5)
                time.sleep(1)
                browser = LauncheTender1.estimatorValidlogin(browser)
                time.sleep(1)
                Updatedetails = updatedetails()
                browser = Updatedetails.createproject(browser)
                time.sleep(2)
                rownum=(i)
                rows = sheet.row_values(rownum)

                projectname = rows[2]
                projectreference = rows[3]
                projectdescription = rows[4]
                projecttype = rows[5]
                projectvalue = rows[6]
                projectlocation1 = rows[7]

                time.sleep(1)
                browser = Updatedetails.updateprojectdetails(browser,projectname,projectreference,projectdescription,projecttype,projectvalue) #Pass the values from excel
                browser = Updatedetails.projectstartdate(browser)
                browser = Updatedetails.projectduedate(browser)

                time.sleep(2)
                browser = Updatedetails.saveprojectdetails(browser) #Save project

                time.sleep(3)
                browser = Updatedetails.updateproject(browser) # click on updateproject
                time.sleep(2)
                browser = Updatedetails.projectdetailsupdate(browser) # update project details
                time.sleep(2)
                browser = Updatedetails.saveprojectdetails(browser) #Click on Save project to update the details
                time.sleep(4)

                projectdetails = DataDriver()

                projectName_path = projectdetails.readfromXML(folder_path+'\Object\Pairwiserupdateproject.xml','eTender','projectname1')
                projectName = browser.find_element_by_xpath(projectName_path)
                self.assertEqual(projectName.text,'project')
                time.sleep(1)

                projectRefValueDuedate = []

                projectRefValueDuedate_path = projectdetails.readfromXML(folder_path+'\Object\Pairwiserupdateproject.xml','eTender','projectrefvaluedate')
                projectRefValueDuedate = browser.find_elements_by_xpath(projectRefValueDuedate_path)

                #print projectRefValueDuedate[2].text

                value = Updatedetails.projectcurrency()

                self.assertEqual(projectRefValueDuedate[0].text,'projectRef')
                self.assertEqual(projectRefValueDuedate[1].text,'Value:'+value)
                #self.assertEqual(projectRefValueDuedate[2].text,'Due Date:Aug 28, 2017')

                time.sleep(1)

                i = i + 1
                logs.info("Test Case No : 100194 Passed Successfully")

                browser = Updatedetails.updateproject(browser)
                time.sleep(2)
                browser = Updatedetails.deleteproject(browser)
                time.sleep(2)
        except Exception:
                logs.error("Validation with Test Case No: 100194 failed")
                browser.save_screenshot(fullpath)
                traceback.print_exc(file=sys.stdout)
                self.fail("Test Case No: 100194 failed")
                browser.implicitly_wait(5)
        finally:
                LauncheTender1.closebrowser(browser)