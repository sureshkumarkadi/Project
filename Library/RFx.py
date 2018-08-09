#-------------------------------------------------------------------------------
# Name:        User Registration
# Purpose:
#
# Author:      suresh.kumar
#
# Created:     05-05-2018
# Copyright:   (c) causeway Technologies 2018
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
sys.path.insert(0,folder_path+"\Env")
from datadriven import DataDriver

rfx = DataDriver()

class RFxQuestionnaire():
    def RFxQuestionsTab(self,browser):
        time.sleep(1)
        RFxTab = browser.find_element_by_xpath(rfx.readfromXML(folder_path+'\Object\TenderplanObjects.xml','eTender','rfi'))
        time.sleep(1)
        RFxTab.click()
        time.sleep(1)
        return browser

    def RFxQuestionsTabinsupplier(self,browser):
        time.sleep(1)
        RFxTab = browser.find_element_by_xpath(rfx.readfromXML(folder_path+'\Object\TenderplanObjects.xml','eTender','rfi'))
        time.sleep(1)
        RFxTab.click()
        time.sleep(1)
        return browser

    def RFxAddQuestions(self,browser):
        time.sleep(1)
        RFxaddquestion = browser.find_element_by_xpath(rfx.readfromXML(folder_path+'\Object\RFx.xml','eTender','addquestion'))
        time.sleep(1)
        RFxaddquestion.click()
        time.sleep(1)
        return browser

    def RFxTextresponse(self,browser):
        RFxtextresponse = browser.find_element_by_xpath(rfx.readfromXML(folder_path+'\Object\RFx.xml','eTender','enterquestion'))
        time.sleep(1)
        RFxtextresponse_Data = rfx.readfromXML(folder_path+'\Data\RFx.xml','eTender','question1')
        time.sleep(1)
        RFxtextresponse.send_keys(RFxtextresponse_Data)
        time.sleep(1)
        return browser

    def RFxTextresponseanswer(self,browser):
        RFxTextresponseanswer = browser.find_element_by_xpath(rfx.readfromXML(folder_path+'\Object\RFx.xml','eTender','answertextresponse'))
        time.sleep(1)
        RFxTextresponseanswer_Data = rfx.readfromXML(folder_path+'\Data\RFx.xml','eTender','answer1')
        time.sleep(1)
        RFxTextresponseanswer.send_keys(RFxTextresponseanswer_Data)
        time.sleep(1)
        return browser

    def RFxMultiplechoice(self,browser):
        RFxMultiplechoice = browser.find_elements_by_xpath(rfx.readfromXML(folder_path+'\Object\RFx.xml','eTender','enterquestion'))
        time.sleep(1)
        RFxMultiplechoice_Data = rfx.readfromXML(folder_path+'\Data\RFx.xml','eTender','question2')
        time.sleep(1)
        RFxMultiplechoice[1].send_keys(RFxMultiplechoice_Data)
        time.sleep(1)
        return browser

    def RFxCheckbox(self,browser):
        RFxCheckbox = browser.find_elements_by_xpath(rfx.readfromXML(folder_path+'\Object\RFx.xml','eTender','enterquestion'))
        time.sleep(1)
        RFxCheckbox_Data = rfx.readfromXML(folder_path+'\Data\RFx.xml','eTender','question3')
        time.sleep(1)
        RFxCheckbox[2].send_keys(RFxCheckbox_Data)
        time.sleep(1)
        return browser

    def RFxFileupload(self,browser):
        RFxFileupload = browser.find_elements_by_xpath(rfx.readfromXML(folder_path+'\Object\RFx.xml','eTender','enterquestion'))
        time.sleep(1)
        RFxFileupload_Data = rfx.readfromXML(folder_path+'\Data\RFx.xml','eTender','question4')
        time.sleep(1)
        RFxFileupload[3].send_keys(RFxFileupload_Data)
        time.sleep(1)
        return browser

    def SaveRFxquestions(self,browser):
        time.sleep(1)
        saveRFxquestions = browser.find_element_by_xpath(rfx.readfromXML(folder_path+'\Object\RFx.xml','eTender','saverfxquestions'))
        saveRFxquestions.click()
        time.sleep(1)
        return browser

    def SubmitRFxanswers(self,browser):
        time.sleep(1)
        submitRFxanswers = browser.find_element_by_xpath(rfx.readfromXML(folder_path+'\Object\RFx.xml','eTender','saveanswers'))
        submitRFxanswers.click()
        time.sleep(1)
        return browser

    def DraftRFxanswers(self,browser):
        draftRFxanswers = browser.find_element_by_xpath(rfx.readfromXML(folder_path+'\Object\RFx.xml','eTender','draftRFxanswers'))
        draftRFxanswers.click()
        time.sleep(1)
        return browser

    def selectdropdown(self,browser):
        selectDropdown = browser.find_element_by_xpath(rfx.readfromXML(folder_path+'\Object\RFx.xml','eTender','selectdropdown'))
        time.sleep(1)
        selectDropdown.click()
        return browser

    def selecttextresponse(self,browser):
        selectTextresponse = browser.find_element_by_xpath(rfx.readfromXML(folder_path+'\Object\RFx.xml','eTender','selecttextresponse'))
        time.sleep(1)
        selectTextresponse.click()
        return browser

    def selectMultiplechoice(self,browser):
        selectmultiplechoice = browser.find_element_by_xpath(rfx.readfromXML(folder_path+'\Object\RFx.xml','eTender','selectmultiplechoice'))
        time.sleep(1)
        selectmultiplechoice.click()
        return browser

    def selectCheckbox(self,browser):
        selectcheckbox = browser.find_element_by_xpath(rfx.readfromXML(folder_path+'\Object\RFx.xml','eTender','selectcheckbox'))
        time.sleep(1)
        selectcheckbox.click()
        return browser

    def selectFileupload(self,browser):
        selectfileupload = browser.find_element_by_xpath(rfx.readfromXML(folder_path+'\Object\RFx.xml','eTender','selectfile'))
        time.sleep(1)
        selectfileupload.click()
        return browser

    def selectoptiontemplatedropdown(self,browser):
        optiontemplateDropdown = browser.find_element_by_xpath(rfx.readfromXML(folder_path+'\Object\RFx.xml','eTender','selectoptiontemplate'))
        time.sleep(1)
        optiontemplateDropdown.click()
        return browser

    def optiontemplatechoice(self,browser):
        optiontemplatechoice = browser.find_element_by_xpath(rfx.readfromXML(folder_path+'\Object\RFx.xml','eTender','optiontemplatechoice'))
        time.sleep(1)
        optiontemplatechoice.click()
        return browser

    def uploadFile(self,browser):
        uploadfileclick = browser.find_element_by_xpath(rfx.readfromXML(folder_path+'\Object\RFx.xml','eTender','uploadfileclick'))
        time.sleep(1)
        uploadfileclick.click()
        time.sleep(3)
        os.system(folder_path+'\Env\Importitems.exe') #This is AUToIT script for Upload a Document(Note:selenium not supporting uploading a document from windows hence we need to install AUTOIT to upload a document)
        return browser

    def deleteQuestions(self,browser):
        deletequestions = browser.find_element_by_xpath(rfx.readfromXML(folder_path+'\Object\RFx.xml','eTender','deletequestions'))
        time.sleep(1)
        deletequestions.click()
        return browser

    def textresponserequired(self,browser):
        textresponserequired = browser.find_element_by_xpath(rfx.readfromXML(folder_path+'\Object\RFx.xml','eTender','textresponserequired'))
        time.sleep(1)
        textresponserequired.click()
        return browser

