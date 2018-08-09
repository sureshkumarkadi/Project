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
tf = 'test_Ranksupplierinactivestate'
filename = 'Testcase-%s.png' %(tf)
path= setupValue().screenpath
fullpath = os.path.join(path,filename)

#Test case Number = Rank-2
class Ranksupplierinactivestate(unittest.TestCase):
    def test_Ranksupplierinactivestate(self):
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
            time.sleep(7)
            tenderDetails = Tenderdetails()
            browser = tenderDetails.estimatorProject(browser)
            time.sleep(1)

            rankDetails = Ranksupplier()
            browser = tenderDetails.estimatortendertradex(browser)
            time.sleep(2)

            browser = rankDetails.ranksupplier(browser)
            time.sleep(2)

            ranklink = DataDriver()
            ranksupplierlabel_path = ranklink.readfromXML(folder_path+'\Object\Tradex.xml','eTender','ranksupplierlabel')
            time.sleep(1)
            ranksupplierlabel = browser.find_element_by_xpath(ranksupplierlabel_path) #ranksupplier label
            time.sleep(1)
            self.assertEqual(ranksupplierlabel.text,'Rank suppliers')
            time.sleep(1)

            ranksupplierinactive_path = ranklink.readfromXML(folder_path+'\Object\Tradex.xml','eTender','rankingoff')
            time.sleep(1)
            ranksupplierinactive = browser.find_element_by_xpath(ranksupplierinactive_path) #ranksupplier inactive state
            time.sleep(1)

            rankdisplay_path = ranklink.readfromXML(folder_path+'\Object\Tradex.xml','eTender','rankdisplay')
            time.sleep(1)
            rankdisplay = browser.find_elements_by_xpath(rankdisplay_path) #ranksupplier inactive state
            time.sleep(1)

            if len(rankdisplay) == 10:
                print("pass")
            else:
                self.fail("Validation with Test Case No: Rank-2 failed")

            if ranksupplierinactive.is_displayed():
                print ("pass")
            else:
                self.fail("Validation with Test Case No: Rank-2 failed")

            logs.info("Test Case No : Rank-2 Passed Successfully")
        except Exception:
            logs.error("Validation with Test Case No: Rank-2 failed")
            browser.save_screenshot(fullpath)
            traceback.print_exc(file=sys.stdout)
            self.fail("Test Case No: Rank-2 failed")
            browser.implicitly_wait(5)
        finally:
            LauncheTender1.closebrowser(browser)

if __name__ == '__main__':
    unittest.main()