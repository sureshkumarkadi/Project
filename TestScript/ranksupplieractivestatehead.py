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
#from Tradexsuppliers import TradexsupplierRanksupplier
from Tradexsuppliers import Ranksupplier
from datadriven import DataDriver
from setupenviron import setupValue
from logouteTender import Userprofilemenu
from logdriver import logvalue
logs=logvalue.logger
logclose=logvalue()
ftime = time.mktime(time.localtime())
ptime=time.strftime("%d-%m-%Y_%H%M%S", time.localtime(ftime))
#filename = 'TestCase-TC - 1014-{0}.png'.format(ptime)
tf = 'test_Ranksupplieractivestate'
filename = 'Testcase-%s.png' %(tf)
path= setupValue().screenpath
fullpath = os.path.join(path,filename)

#Test case Number = Rank-3
class Ranksupplieractivestate(unittest.TestCase):
    def test_Ranksupplieractivestate(self):
        try:
            browserInstance = setupValue()
            browser = browserInstance.setupfunction()
            #browser.implicitly_wait(5)
            #time.sleep(1)
            LauncheTender1 = LauncheTenderclass()
            browser = LauncheTender1.openURL(browser)
            browser.implicitly_wait(10)
            #time.sleep(1)
            browser = LauncheTender1.estimatorValidlogin(browser)
            #time.sleep(7)
            tenderDetails = Tenderdetails()
            browser = tenderDetails.estimatorProject(browser)
            #time.sleep(1)

            rankDetails = Ranksupplier()
            browser = tenderDetails.estimatortendertradex(browser)
            #time.sleep(2)

            browser = rankDetails.ranksupplier(browser)
            #time.sleep(2)

            browser = rankDetails.ranksupplieractivestate(browser)
            time.sleep(2)

            ranklink = DataDriver()
            ranksupplieractive_path = ranklink.readfromXML(folder_path+'\Object\Tradex.xml','eTender','rankingon')
            #time.sleep(1)
            ranksupplieractive = browser.find_element_by_xpath(ranksupplieractive_path) #ranksupplier active state
            #time.sleep(1)

            if ranksupplieractive.is_displayed():
                print ("pass")
            else:
                self.fail("Validation with Test Case No: Rank-3 failed")

            rankheading_path = ranklink.readfromXML(folder_path+'\Object\Tradex.xml','eTender','rankdisplay')
            #time.sleep(1)
            rankheading = browser.find_elements_by_xpath(rankheading_path) #rank heading
            #time.sleep(1)
            self.assertEqual(rankheading[1].text,'Rank')

            ranknumber_path = ranklink.readfromXML(folder_path+'\Object\Tradex.xml','eTender','ranknumber')
            #time.sleep(1)
            ranknumber = browser.find_elements_by_xpath(ranknumber_path) #rank heading
            #time.sleep(1)

            self.assertEqual(ranknumber[0].text,'1')
            self.assertEqual(ranknumber[6].text,'2')

            logs.info("Test Case No : Rank-3 Passed Successfully")
        except Exception:
            logs.error("Validation with Test Case No: Rank-3 failed")
            browser.save_screenshot(fullpath)
            traceback.print_exc(file=sys.stdout)
            self.fail("Test Case No: Rank-3 failed")
            browser.implicitly_wait(5)
        finally:
            LauncheTender1.closebrowser(browser)

if __name__ == '__main__':
    unittest.main()