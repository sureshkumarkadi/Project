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

import unittest
import sys
from selenium.webdriver.support.ui import WebDriverWait
sys.path.insert(0,'E:\PythonScripts\Library')
class LoginnewAction(unittest.TestCase):
    def test_SubcontractorlogineTender(self):
            launcheTender1 = LauncheTenderclass()
            #browser=launcheTender1.launchetender()
            browser = launcheTender1.subcontractorValidlogin()
            browser.implicitly_wait(5)
            #launcheTender1.subcontractorValidlogin()
            organisation = browser.find_element_by_link_text('GSE Civil Engineering Ltd')
            organisation1  = organisation.text
            self.assertEqual(organisation1,'GSE Civil Engineering Ltd')
