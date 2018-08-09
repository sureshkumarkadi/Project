#-------------------------------------------------------------------------------
# Name:        LauncheTender
# Purpose:
#
# Author:      suresh.kumar
#
# Created:     29-04-2016
# Copyright:   (c) suresh.kumar 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
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

class LauncheTenderclass():
    def openURL(self,browser):
                #browser.implicitly_wait(5)
                url=DataDriver()
                Environ=url.readfromXML(folder_path+'\Env\Setup.xml','eTender','env')
                print (Environ)
                if Environ.lower()=='StageURL'.lower():
                    etenderURL=url.readfromXML(folder_path+'\Env\Setup.xml','eTender','StageURL')
                elif Environ.lower()=='PreStageURL'.lower():
                    etenderURL=url.readfromXML(folder_path+'\Env\Setup.xml','eTender','PreStageURL')
                elif Environ.lower()=='MasterURL'.lower():
                    etenderURL=url.readfromXML(folder_path+'\Env\Setup.xml','eTender','MasterURL')
                browser.get(etenderURL)
                time.sleep(2)
                browser.maximize_window()
                time.sleep(1)
                assert browser.title == 'Causeway eTender'
                return browser

    def closebrowser(self,browser):
               time.sleep(1)
               browser.close()
               return browser

    def subcontractorValidlogin(self,browser):
              browser.implicitly_wait(5)
              login=DataDriver()
              login_id=login.readfromXML(folder_path+'\Object\Object.xml','eTender','LoginName')
              login_id1 = browser.find_element_by_id(login_id)
              time.sleep(1)
              username_id=login.readfromXML(folder_path+'\Data\Data.xml','eTender','Subusername')
              login_id1.clear()
              login_id1.send_keys(username_id)
              time.sleep(1)
              password_id=login.readfromXML(folder_path+'\Object\Object.xml','eTender','password')
              password_id1 = browser.find_element_by_id(password_id)
              time.sleep(1)
              password=login.readfromXML(folder_path+'\Data\Data.xml','eTender','Subpassword')
              password_id1.clear()
              password_id1.send_keys(password)
              time.sleep(1)
              submitButton_id=login.readfromXML(folder_path+'\Object\Object.xml','eTender','submitButton')
              print (submitButton_id)
              time.sleep(1)
              submitButton = browser.find_element_by_id(submitButton_id)
              submitButton.click()
              return browser

    def subcontractorloginPendingtrades(self,browser):
              browser.implicitly_wait(5)
              login=DataDriver()
              login_id=login.readfromXML(folder_path+'\Object\Object.xml','eTender','LoginName')
              login_id1 = browser.find_element_by_id(login_id)
              time.sleep(1)
              username_id=login.readfromXML(folder_path+'\Data\Data.xml','eTender','SubusernamePtrades')
              login_id1.clear()
              login_id1.send_keys(username_id)
              time.sleep(1)
              password_id=login.readfromXML(folder_path+'\Object\Object.xml','eTender','password')
              password_id1 = browser.find_element_by_id(password_id)
              time.sleep(1)
              password=login.readfromXML(folder_path+'\Data\Data.xml','eTender','SubpasswordPtrade')
              password_id1.clear()
              password_id1.send_keys(password)
              time.sleep(1)
              submitButton_id=login.readfromXML(folder_path+'\Object\Object.xml','eTender','submitButton')
              print (submitButton_id)
              time.sleep(1)
              submitButton = browser.find_element_by_id(submitButton_id)
              submitButton.click()
              return browser

    def estimatorValidlogin(self,browser):
              browser.implicitly_wait(5)
              login=DataDriver()
              time.sleep(1)
              login_id=login.readfromXML(folder_path+'\Object\Object.xml','eTender','LoginName')
              login_id1 = browser.find_element_by_id(login_id)
              time.sleep(1)
              username_id=login.readfromXML(folder_path+'\Data\Data.xml','eTender','Estusername')
              login_id1.send_keys(username_id)
              time.sleep(1)
              password_id=login.readfromXML(folder_path+'\Object\Object.xml','eTender','password')
              password_id1 = browser.find_element_by_id(password_id)
              time.sleep(1)
              password=login.readfromXML(folder_path+'\Data\Data.xml','eTender','Estpassword')
              password_id1.send_keys(password)
              time.sleep(1)
              submitButton_id=login.readfromXML(folder_path+'\Object\Object.xml','eTender','submitButton')
              submitButton = browser.find_element_by_id(submitButton_id)
              time.sleep(1)
              submitButton.click()
              return browser

    def estimatorValidlogin1(self,browser):
              browser.implicitly_wait(5)
              login=DataDriver()
              time.sleep(1)
              login_id=login.readfromXML(folder_path+'\Object\Object.xml','eTender','LoginName')
              login_id1 = browser.find_element_by_id(login_id)
              time.sleep(1)
              username_id=login.readfromXML(folder_path+'\Data\Data.xml','eTender','Estusername1')
              login_id1.send_keys(username_id)
              time.sleep(1)
              password_id=login.readfromXML(folder_path+'\Object\Object.xml','eTender','password')
              password_id1 = browser.find_element_by_id(password_id)
              time.sleep(1)
              password=login.readfromXML(folder_path+'\Data\Data.xml','eTender','Estpassword1')
              password_id1.send_keys(password)
              time.sleep(1)
              submitButton_id=login.readfromXML(folder_path+'\Object\Object.xml','eTender','submitButton')
              submitButton = browser.find_element_by_id(submitButton_id)
              time.sleep(1)
              submitButton.click()
              return browser

    def estimatorinvalidpassword(self,browser):
              browser.implicitly_wait(5)
              login=DataDriver()
              time.sleep(1)
              login_id=login.readfromXML(folder_path+'\Object\Object.xml','eTender','LoginName')
              login_id1 = browser.find_element_by_id(login_id)
              time.sleep(1)
              login_id1.clear()
              time.sleep(1)
              username_id=login.readfromXML(folder_path+'\Data\Data.xml','eTender','Estusername1')
              login_id1.send_keys(username_id)
              time.sleep(1)
              password_id=login.readfromXML(folder_path+'\Object\Object.xml','eTender','password')
              password_id1 = browser.find_element_by_id(password_id)
              time.sleep(1)
              password_id1.clear()
              time.sleep(1)
              password=login.readfromXML(folder_path+'\Data\Data.xml','eTender','Estwrongpassword')
              password_id1.send_keys(password)
              time.sleep(1)
              submitButton_id=login.readfromXML(folder_path+'\Object\Object.xml','eTender','submitButton')
              submitButton = browser.find_element_by_id(submitButton_id)
              time.sleep(1)
              submitButton.click()
              return browser

    def estimatorinvalidusername(self,browser):
              browser.implicitly_wait(5)
              login=DataDriver()
              time.sleep(1)
              login_id=login.readfromXML(folder_path+'\Object\Object.xml','eTender','LoginName')
              login_id1 = browser.find_element_by_id(login_id)
              time.sleep(1)
              login_id1.clear()
              time.sleep(1)
              username_id=login.readfromXML(folder_path+'\Data\Data.xml','eTender','Estwrongusername')
              login_id1.send_keys(username_id)
              time.sleep(1)
              password_id=login.readfromXML(folder_path+'\Object\Object.xml','eTender','password')
              password_id1 = browser.find_element_by_id(password_id)
              time.sleep(1)
              password_id1.clear()
              time.sleep(1)
              password=login.readfromXML(folder_path+'\Data\Data.xml','eTender','Estpassword1')
              password_id1.send_keys(password)
              time.sleep(1)
              submitButton_id=login.readfromXML(folder_path+'\Object\Object.xml','eTender','submitButton')
              submitButton = browser.find_element_by_id(submitButton_id)
              time.sleep(1)
              submitButton.click()
              return browser

    def superAdminValidlogin(self,browser):
              browser.implicitly_wait(5)
              login=DataDriver()

              login_id=login.readfromXML(folder_path+'\Object\Object.xml','eTender','LoginName')
              login_id1 = browser.find_element_by_id(login_id)

              username_id=login.readfromXML(folder_path+'\Data\Data.xml','eTender','Superadminusername')
              login_id1.send_keys(username_id)

              password_id=login.readfromXML(folder_path+'\Object\Object.xml','eTender','password')
              password_id1 = browser.find_element_by_id(password_id)

              password=login.readfromXML(folder_path+'\Data\Data.xml','eTender','Superadminpassword')
              password_id1.send_keys(password)

              submitButton_id=login.readfromXML(folder_path+'\Object\Object.xml','eTender','submitButton')
              submitButton = browser.find_element_by_id(submitButton_id)
              submitButton.click()
              return browser

    def list_Organisation(self,browser):
            browser.implicitly_wait(5)
            Tenderacceptance = []
            Tenderacceptance_XML=DataDriver()
            Tenderacceptance_path=Tenderacceptance_XML.readfromXML(folder_path+'\Data\Data.xml','eTender','Tenderacceptance')
            time.sleep(3)
            print (Tenderacceptance_path)
            Tenderacceptance = browser.find_element_by_link_text(Tenderacceptance_path) # Select Tender acceptance from lefthand side menu
            time.sleep(2)
            Tenderacceptance.click()
            time.sleep(2)
            organisation = []
            organisation_path=Tenderacceptance_XML.readfromXML(folder_path+'\Object\Object.xml','eTender','organisation')
            time.sleep(2)
            organisation = browser.find_elements_by_xpath(organisation_path) # Select Organisation from lefthand side menu
            organisation[0].click()
            time.sleep(2)
            return browser

    def verifyorganisationdetails(self,browser):

            time.sleep(1)
            return browser

    def list_project(self,browser):
            browser.implicitly_wait(5)
            time.sleep(1)
            organisations_XML = DataDriver()
            organisation_path = organisations_XML.readfromXML(folder_path+'\Object\Object.xml','eTender','project')
            time.sleep(1)
            organisation = browser.find_element_by_link_text(organisation_path) #Click on Organisation
            time.sleep(2)
            organisation.click()
            time.sleep(1)
            return browser

    def switchOrganisation(self,browser):
        browser.implicitly_wait(5)
        time.sleep(1)
        switchOrganisation = DataDriver()
        time.sleep(3)
        switchOrganisation_path = switchOrganisation.readfromXML(folder_path+'\Object\SwitchOrganisation.xml','eTender','switchOrganisation')
        time.sleep(2)
        switchOrganisation_link = browser.find_element_by_link_text(switchOrganisation_path) # Select switchOrganisation
        time.sleep(2)
        switchOrganisation_link.click()
        return browser

    def selectfirstOrganisation(self,browser):
        browser.implicitly_wait(5)
        time.sleep(2)
        selectOrganisation = DataDriver()
        #selectOrganisation_link = []
        time.sleep(3)
        selectOrganisation_path = selectOrganisation.readfromXML(folder_path+'\Object\SwitchOrganisation.xml','eTender','selectDMOrganisation')
        time.sleep(2)
        selectOrganisation_link = browser.find_element_by_xpath(selectOrganisation_path) # Select first organisation
        time.sleep(2)
        selectOrganisation_link.click()
        return browser

    def selectfirstOrganisationPtrades(self,browser):
        browser.implicitly_wait(5)
        time.sleep(2)
        selectOrganisation = DataDriver()
        #selectOrganisation_link = []
        time.sleep(3)
        selectOrganisation_path = selectOrganisation.readfromXML(folder_path+'\Object\SwitchOrganisation.xml','eTender','selectDMOrganisationPtrade')
        time.sleep(2)
        selectOrganisation_link = browser.find_element_by_xpath(selectOrganisation_path) # Select first organisation
        time.sleep(2)
        selectOrganisation_link.click()
        return browser

    def selectsecondOrganisation(self,browser):
        browser.implicitly_wait(5)
        time.sleep(2)
        selectOrganisation = DataDriver()
        #selectOrganisation_link = []
        time.sleep(3)
        selectOrganisation_path = selectOrganisation.readfromXML(folder_path+'\Object\SwitchOrganisation.xml','eTender','selectGSEOrganisation')
        time.sleep(2)
        selectOrganisation_link = browser.find_element_by_xpath(selectOrganisation_path) # Select second organisation
        time.sleep(2)
        selectOrganisation_link.click()
        return browser

##    def Subcontratorproject(self,browser):
##            #browser = launcheTender.browser
##            browser.implicitly_wait(5)
##            projects_XML = DataDriver()
##            projects_path = projects_XML.readfromXML(folder_path+'\Object\Object.xml','eTender','projectlist')
##            print projects_path
##            project_link = browser.find_element_by_link_text(projects_path)
##            #print(project_link)
##            time.sleep(1)
##            project_link.click()
##            return browser

class Quicklyaccessingtendersclass():
    def tenderQuickAccess(self,browser):
        browser.implicitly_wait(5)
        time.sleep(1)
        quickaccess = DataDriver()
        time.sleep(3)
        quickaccess_path = quickaccess.readfromXML(folder_path+'\Data\Data.xml','eTender','tenderquickaccess')
        time.sleep(2)
        quickaccess_lists = browser.find_element_by_link_text(quickaccess_path) # Select Tender quick access
        time.sleep(2)
        print (quickaccess_lists.text)
        time.sleep(1)
        quickaccess_lists.click()
        return browser

    def tenderQuickItemAccess(self,browser):
        browser.implicitly_wait(3)
        quickaccess = DataDriver()
        time.sleep(1)
        element2 = []
        element2 = browser.find_elements_by_xpath("//h4//a[@class='ng-binding']") # Click "A - Preliminaries - A1303 - Temp Proppin" tender
        time.sleep(1)
        element2[0].click()
