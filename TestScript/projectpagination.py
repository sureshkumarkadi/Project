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
#filename = 'TestCase-100209-{0}.png'.format(ptime)
tf = 'test_projectpagination'
filename = 'Testcase-%s.png' %(tf)
path= setupValue().screenpath
fullpath = os.path.join(path,filename)

#Test case Number = 100209
class Projectpagination(unittest.TestCase):
    def test_projectpagination(self):
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
                time.sleep(5)
##                browser = LauncheTender1.switchOrganisation(browser)
##                time.sleep(1)
##                browser = LauncheTender1.selectfirstOrganisation(browser)
##                time.sleep(7)
                project_pagination = DataDriver()
                projectpagination = []

                projectlength_path =project_pagination.readfromXML(folder_path+'\Object\Project.xml','eTender','project')
                projectscount=browser.find_elements_by_xpath(projectlength_path)
                projectcount = len(projectscount)
                if projectcount == 20:
                    try:
                        projectpagination_path =project_pagination.readfromXML(folder_path+'\Object\Project.xml','eTender','projectpagination')
                        projectpagination=browser.find_elements_by_xpath(projectpagination_path)
                        time.sleep(1)
                        projectpagination[1].click()
                        time.sleep(4)
                    except:
                        print("Projects less than 20 hence there is no pagination in this page.")

        except Exception:
                logs.error("Validation with Test Case No: 100209 failed")
                browser.save_screenshot(fullpath)
                traceback.print_exc(file=sys.stdout)
                self.fail("Test Case No: 100209 failed")
                browser.implicitly_wait(5)
        finally:
                LauncheTender1.closebrowser(browser)





















