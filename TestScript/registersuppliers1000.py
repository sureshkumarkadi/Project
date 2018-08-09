#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      suresh.kumar
#
# Created:     25/08/2016
# Copyright:   (c) suresh.kumar 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import unittest
import sys
import os
import time
import traceback
import xlrd
book = xlrd.open_workbook('E:\PythonScripts\SubbyratesfromUI.xls', formatting_info=True)
sheet = book.sheet_by_name('Rates')
dir_path = os.path.dirname(os.path.realpath(__file__))
folder_path=os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0,folder_path+"\Library")
sys.path.insert(0,folder_path+"\Syslibrary")
sys.path.insert(0,folder_path+"\Data")
sys.path.insert(0,folder_path+"\Object")
from launcheTender import LauncheTenderclass
from Registration import RegistrationineT
#from DBConnectMySQLdeleteORG import deleteorganisation
from datadriven import DataDriver
from setupenviron import setupValue
from logdriver import logvalue
logs=logvalue.logger
logclose=logvalue()
ftime = time.mktime(time.localtime())
ptime=time.strftime("%d-%m-%Y_%H%M%S", time.localtime(ftime))
filename = 'TestCase-100164-{0}.png'.format(ptime)
path= setupValue().screenpath
fullpath = os.path.join(path,filename)

#Test case Number = 100164
class RegistersupplierselectORG(unittest.TestCase):
    def test_registersupplierselectorg(self):
        try:
            i = 0
            while i<46:
                browserInstance = setupValue()
                browser = browserInstance.setupfunction()
                browser.implicitly_wait(5)
                LauncheTender1 = LauncheTenderclass()
                browser = LauncheTender1.openURL(browser)
                registration = RegistrationineT()
                browser = registration.register(browser)
                time.sleep(1)
                #browser = registration.selectsupplierRole(browser)
                browser = registration.selectmaincontractorRole(browser)
                time.sleep(1)
                browser = registration.selectestimatoradminRole(browser)
                time.sleep(1)
                rownum=(i)
                rows = sheet.row_values(rownum)
                supplier_register = DataDriver()
                supplier_register_email_path =supplier_register.readfromXML(folder_path+'\Object\Object.xml','eTender','supplier-email')
                supplier_register_email = browser.find_element_by_xpath(supplier_register_email_path)
                supplier_register_email.send_keys(rows[0])
                time.sleep(3)
                supplier_register_password_path =supplier_register.readfromXML(folder_path+'\Object\Object.xml','eTender','supplier-password')
                supplier_register_password = browser.find_element_by_xpath(supplier_register_password_path)
                supplier_register_password.send_keys(int(rows[1]))
                time.sleep(1)
                supplier_register_confirmpassword_path =supplier_register.readfromXML(folder_path+'\Object\Object.xml','eTender','supplier-confirmpassword')
                supplier_register_confirmpassword = browser.find_element_by_xpath(supplier_register_confirmpassword_path)
                supplier_register_confirmpassword.send_keys(int(rows[1]))
                time.sleep(1)

                supplier_register_firstname_path =supplier_register.readfromXML(folder_path+'\Object\Object.xml','eTender','supplier-firstname')
                supplier_register_firstname = browser.find_element_by_xpath(supplier_register_firstname_path)
                supplier_register_firstname_data =supplier_register.readfromXML(folder_path+'\Data\Data.xml','eTender','supplier-firstname')
                supplier_register_firstname.send_keys(supplier_register_firstname_data)
                time.sleep(1)

                supplier_register_lastname_path =supplier_register.readfromXML(folder_path+'\Object\Object.xml','eTender','supplier-lastname')
                supplier_register_lastname = browser.find_element_by_xpath(supplier_register_lastname_path)
                supplier_register_lastname_data =supplier_register.readfromXML(folder_path+'\Data\Data.xml','eTender','supplier-lastname')
                supplier_register_lastname.send_keys(supplier_register_lastname_data)
                time.sleep(1)

                supplier_register_mobile_path =supplier_register.readfromXML(folder_path+'\Object\Object.xml','eTender','supplier-mobile')
                supplier_register_mobile = browser.find_element_by_xpath(supplier_register_mobile_path)
                supplier_register_mobile_data =supplier_register.readfromXML(folder_path+'\Data\Data.xml','eTender','supplier-mobile')
                supplier_register_mobile.send_keys(supplier_register_mobile_data)
                time.sleep(1)

                supplier_register_phone_path =supplier_register.readfromXML(folder_path+'\Object\Object.xml','eTender','supplier-phone')
                supplier_register_phone = browser.find_element_by_xpath(supplier_register_phone_path)
                supplier_register_phone_data =supplier_register.readfromXML(folder_path+'\Data\Data.xml','eTender','supplier-phone')
                supplier_register_phone.send_keys(supplier_register_phone_data)
                time.sleep(1)

                supplier_register_Nextbutton_path =supplier_register.readfromXML(folder_path+'\Object\Object.xml','eTender','Nextbutton')
                supplier_register_Nextbutton = browser.find_element_by_xpath(supplier_register_Nextbutton_path)
                supplier_register_Nextbutton.click()
                time.sleep(5)
                browser = registration.organisationselectLOAD(browser)
                time.sleep(1)
                browser = registration.supplierRegistration(browser)
                time.sleep(2)
##                browser = LauncheTender1.superAdminValidlogin(browser)
##                time.sleep(1)
##                browser = registration.supplierAuthorisationLOAD(browser)
##                time.sleep(1)
##                browser = registration.supplierselection(browser)
##                time.sleep(1)
##                browser = registration.supplierAccept(browser)
##                time.sleep(2)
                LauncheTender1.closebrowser(browser)
                i = i + 1
        except Exception:
            logs.error("Validation with Test Case No: User creation failed")
            browser.save_screenshot(fullpath)
            traceback.print_exc(file=sys.stdout)
            self.fail("Test Case No: User creation failed")
            browser.implicitly_wait(5)

if __name__ == '__main__':
    unittest.main()












