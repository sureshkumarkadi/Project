#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      mathew.jacob
#
# Created:     19/12/2016
# Copyright:   (c) mathew.jacob 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import os
import sys
import time
dir_path = os.path.dirname(os.path.realpath(__file__))
folder_path=os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0,folder_path+"\Syslibrary")
from datadriven import DataDriver
orgLink=DataDriver()
class Projectclass():

    def Openorganization(self,browser):
        p=browser.find_elements_by_xpath(orgLink.readfromXML(folder_path+'\Object\Project.xml','eTender','orgLink'))
        p[0].click()