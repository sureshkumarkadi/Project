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
#filename = 'TestCase-Refurbishment-{0}.png'.format(ptime)
tf = 'test_updateprojectdetailsRefurbishment'
filename = 'Testcase-%s.png' %(tf)
path= setupValue().screenpath
fullpath = os.path.join(path,filename)

#Test case Number = Refurbishment
class UpdateprojectdetailsRefurbishment(unittest.TestCase):
    def test_updateprojectdetailsRefurbishment(self):
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
                browser = Updatedetails.updateproject(browser)
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

                time.sleep(2)

                Refurbishment1 = DataDriver()

                env = Refurbishment1.readfromXML(folder_path+'\Env\Setup.xml','eTender','env')


                if env == 'StageURL':

                    Refurbishment_path = Refurbishment1.readfromXML(folder_path+'\Object\PairwiserupdateprojectStaging.xml','eTender','Refurbishment') #Validate image id
                    Refurbishment = browser.find_element_by_xpath(Refurbishment_path)

                    time.sleep(2)
                    if Refurbishment.is_displayed():
                        print("pass")
                    else:
                        print("fail")

                elif env == 'PreStageURL':

                    Refurbishment_path = Refurbishment1.readfromXML(folder_path+'\Object\Pairwiserupdateproject.xml','eTender','Refurbishment') #Validate image id
                    Refurbishment = browser.find_element_by_xpath(Refurbishment_path)
                    time.sleep(2)
                    if Refurbishment.is_displayed():
                        print("pass")
                    else:
                        print("fail")

                elif env == 'MasterURL':

                    Refurbishment_path = Refurbishment1.readfromXML(folder_path+'\Object\PairwiserupdateprojectStaging.xml','eTender','Refurbishment') #Validate image id
                    Refurbishment = browser.find_element_by_xpath(Refurbishment_path)
                    time.sleep(2)
                    if Refurbishment.is_displayed():
                        print("pass")
                    else:
                        print("fail")

                browser = Updatedetails.saveprojectdetails(browser) #Save project

                time.sleep(3)
                i = i + 1
        except Exception:
                logs.error("Validation with Test Case No: Refurbishment failed")
                browser.save_screenshot(fullpath)
                traceback.print_exc(file=sys.stdout)
                self.fail("Test Case No: Refurbishment failed")
                browser.implicitly_wait(5)
        finally:
                LauncheTender1.closebrowser(browser)










