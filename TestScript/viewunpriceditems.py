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
from RESTAPIStaging import ReopentenderusingRESTAPIclass
#from DBConnectMySQLdeleteORG import deleteorganisation
logs=logvalue.logger
logclose=logvalue()
ftime = time.mktime(time.localtime())
ptime=time.strftime("%d-%m-%Y_%H%M%S", time.localtime(ftime))
#filename = 'TestCase-100319-{0}.png'.format(ptime)
tf = 'test_viewunpriceditems'
filename = 'Testcase-%s.png' %(tf)
path= setupValue().screenpath
fullpath = os.path.join(path,filename)

#Test case Number = 100319
class Viewunpriceditems(unittest.TestCase):
    def test_viewunpriceditems(self):
        try:
##            browserInstance = setupValue()
##            browser = browserInstance.setupfunction()
##            browser.implicitly_wait(5)
##            LauncheTender1 = LauncheTenderclass()
##            browser = LauncheTender1.openURL(browser)
##            browser.implicitly_wait(5)
##            browser = LauncheTender1.subcontractorValidlogin(browser)
##            browser = LauncheTender1.list_Organisation(browser)
##            browser = LauncheTender1.verifyorganisationdetails(browser)
##            browser = LauncheTender1.list_project(browser)
##            tenderDetails = Tenderdetails()
##            browser = tenderDetails.Subcontratorproject(browser)
##            browser = tenderDetails.suppliertender(browser)
##            time.sleep(1)
            additem = ReopentenderusingRESTAPIclass()
            accesstoken = additem.AuthunticateAPI()
            additem.Additem(accesstoken)
##            browser = tenderDetails.selectFilter(browser)
##            time.sleep(1)
##            browser = tenderDetails.selectunpriceditems(browser)
##            browser = tenderDetails.closefilter(browser)
##            time.sleep(1)
##            unpriceditems_XML = DataDriver()
##            unpriceditems = []
##            unpriceditems_path = unpriceditems_XML.readfromXML(folder_path+'\Object\Estimatorvalue.xml','eTender','pricableitems')
##            unpriceditems = browser.find_elements_by_xpath(unpriceditems_path) #Webelement for values
##            time.sleep(1)
##            unpriceditems1 =  unpriceditems[1].text
##            time.sleep(1)
##            self.assertEqual(unpriceditems1,'Unpriced item')
##            logs.info("Test Case No : 100319 Passed Successfully")
        except Exception:
            logs.error("Validation with Test Case No: 100319 failed")
            #browser.save_screenshot(fullpath)
            traceback.print_exc(file=sys.stdout)
            self.fail("Test Case No: 100319 failed")
            browser.implicitly_wait(5)
        finally:
            #Deleteitem = deleteorganisation()
            #Deleteitem.deleteitem()
            time.sleep(1)
            #LauncheTender1.closebrowser(browser)





