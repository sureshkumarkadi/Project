#-------------------------------------------------------------------------------
# Name:         AdminEstimator.py
#
# Purpose:      Library functions for Admin menu
#
# Author:       mathew.jacob
#
# Created:      19/09/2016
# Copyright:    (c) Causeway Technologies 2016
#-------------------------------------------------------------------------------
import os
import sys
import time
dir_path = os.path.dirname(os.path.realpath(__file__))
folder_path=os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0,folder_path+"\Syslibrary")
from datadriven import DataDriver
orgLink=DataDriver()
from faker import Factory
class Adminclass():

    def OpenNotificationRecipients(self,browser):
        time.sleep(2)
        browser.find_element_by_link_text(orgLink.readfromXML(folder_path+'\Object\AdminEstimator.xml','eTender','NotificationLink')).click()

    def OpenTags(self,browser):
        time.sleep(2)
        browser.find_element_by_link_text(orgLink.readfromXML(folder_path+'\Object\AdminEstimator.xml','eTender','tags')).click()

    def TagCreation(self,browser,tagname):
        time.sleep(2)
        browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\AdminEstimator.xml','eTender','TagInputBox')).send_keys(tagname)
        browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\AdminEstimator.xml','eTender','TagButton')).click()

    def TagDeletion(self,browser,tagname):
        browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\AdminEstimator.xml','eTender','TagSearchBox')).send_keys(tagname)
        time.sleep(2)
        browser.find_element_by_link_text(orgLink.readfromXML(folder_path+'\Object\AdminEstimator.xml','eTender','TagDelete')).click()
        time.sleep(2)
        browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\AdminEstimator.xml','eTender','DeleteButton')).click()

    def OpenTaskScheduler(self,browser):
        time.sleep(4)
        browser.find_element_by_link_text(orgLink.readfromXML(folder_path+'\Object\AdminEstimator.xml','eTender','TaskScheduler')).click()

    def NotificationMessages(self,browser):
        time.sleep(3)
        browser.find_element_by_link_text(orgLink.readfromXML(folder_path+'\Object\AdminEstimator.xml','eTender','NotificationMessageLink')).click()

    def EmailSetup(self,browser):
        browser.find_element_by_link_text(orgLink.readfromXML(folder_path+'\Object\AdminEstimator.xml','eTender','EmailSetup')).click()

    def GeneralSettings(self,browser):
        browser.find_element_by_link_text(orgLink.readfromXML(folder_path+'\Object\AdminEstimator.xml','eTender','GeneralSettings')).click()















