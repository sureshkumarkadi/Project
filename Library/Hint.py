#-------------------------------------------------------------------------------
# Name:        User Registration
# Purpose:
#
# Author:      suresh.kumar
#
# Created:     04-10-2016
# Copyright:   (c) causeway Technologies 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from launcheTender import LauncheTenderclass
import time
import unittest
import sys
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
folder_path=os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0,folder_path+"\Library")
sys.path.insert(0,folder_path+"\Syslibrary")
sys.path.insert(0,folder_path+"\Data")
sys.path.insert(0,folder_path+"\Object")
from datadriven import DataDriver

hints = DataDriver()

class HintInteract():
    def stagesmenu(self,browser):
        time.sleep(1)
        stages = browser.find_element_by_link_text(hints.readfromXML(folder_path+'\Object\Hint.xml','eTender','stagesmenu'))
        stages.click()
        time.sleep(1)
        return browser

    def hintDone(self,browser):
        hintdone = browser.find_element_by_xpath(hints.readfromXML(folder_path+'\Object\Hint.xml','eTender','hintbutton'))
        hintdone.click()
        time.sleep(1)
        return browser

    def systemfiledsmenu(self,browser):
        time.sleep(1)
        systemfieldsmenu = browser.find_element_by_link_text(hints.readfromXML(folder_path+'\Object\Hint.xml','eTender','systemfieldsmenu'))
        systemfieldsmenu.click()
        time.sleep(1)
        return browser

    def systemcurrencymenu(self,browser):
        time.sleep(1)
        systemCurrencymenu = browser.find_element_by_link_text(hints.readfromXML(folder_path+'\Object\Hint.xml','eTender','systemcurrencymenu'))
        systemCurrencymenu.click()
        time.sleep(1)
        return browser

    def statisticsmenu(self,browser):
        time.sleep(1)
        statisticsMenu1 = browser.find_element_by_link_text(hints.readfromXML(folder_path+'\Object\Hint.xml','eTender','statisticsmenu'))
        time.sleep(1)
        statisticsMenu1.click()
        time.sleep(1)
        return browser

    def nexthint(self,browser):
        time.sleep(1)
        hintbutton = browser.find_element_by_xpath(hints.readfromXML(folder_path+'\Object\Hint.xml','eTender','hintbutton'))
        hintbutton.click()
        time.sleep(1)
        return browser

    def showhints(self,browser):
        time.sleep(1)
        showHints = browser.find_elements_by_xpath(hints.readfromXML(folder_path+'\Object\Hint.xml','eTender','showhints'))
        time.sleep(1)
        showHints[1].click()
        time.sleep(1)
        return browser

    def projectlistmenu(self,browser):
        time.sleep(1)
        projectlist = browser.find_element_by_link_text(hints.readfromXML(folder_path+'\Object\Object.xml','eTender','projectlistmenu'))
        time.sleep(1)
        projectlist.click()
        time.sleep(1)
        return browser

    def projectlistclick(self,browser):
        time.sleep(1)
        projectlist1 = browser.find_elements_by_xpath(hints.readfromXML(folder_path+'\Object\Hint.xml','eTender','projectlist'))
        time.sleep(1)
        projectlist1[0].click()
        time.sleep(1)
        return browser