#-------------------------------------------------------------------------------
# Name:        Organisation Profile
# Purpose:
#
# Author:      suresh.kumar
#
# Created:     18-04-2017
# Copyright:   (c) causeway Technologies 2017
# Licence:     <causeway licence>
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

class OrganisationProfile():
    def OpenOrganisationProfilePage(self,browser):
        openorganisation = DataDriver()
        organisationprofile_path = openorganisation.readfromXML(folder_path+'\Object\OrgProfileObject.xml','eTender','orgProfileLink')
        organisationprofile = browser.find_element_by_link_text(organisationprofile_path)
        organisationprofile.click()
        return browser

    def OrganisationProfilePageUpdate(self,browser):
        organisationdetailsupdate = DataDriver()

        organisationdetailsupdatename_path = organisationdetailsupdate.readfromXML(folder_path+'\Object\OrgProfileObject.xml','eTender','orgName1')
        organisationdetailsupdatename = browser.find_element_by_xpath(organisationdetailsupdatename_path)
        organisationdetailsupdatename.clear()
        organisationdetailsupdatename.click()

        organisationdetailsupdatename_data = organisationdetailsupdate.readfromXML(folder_path+'\Data\OrganisationDetails.xml','eTender','orgname')
        organisationdetailsupdatename.send_keys(organisationdetailsupdatename_data)

        organisationdetailsupdatephone_path = organisationdetailsupdate.readfromXML(folder_path+'\Object\OrgProfileObject.xml','eTender','orgPhone1')
        organisationdetailsupdatephone = browser.find_element_by_xpath(organisationdetailsupdatephone_path)
        organisationdetailsupdatephone.clear()
        organisationdetailsupdatephone.click()

        organisationdetailsupdatephone_data = organisationdetailsupdate.readfromXML(folder_path+'\Data\OrganisationDetails.xml','eTender','orgphone')
        organisationdetailsupdatephone.send_keys(organisationdetailsupdatephone_data)

        organisationdetailsupdatewebsite_path = organisationdetailsupdate.readfromXML(folder_path+'\Object\OrgProfileObject.xml','eTender','organisationWebsite1')
        organisationdetailsupdate2 = browser.find_element_by_xpath(organisationdetailsupdatewebsite_path)
        organisationdetailsupdate2.clear()

        organisationdetailsupdatewebsite_data = organisationdetailsupdate.readfromXML(folder_path+'\Data\OrganisationDetails.xml','eTender','orgwebsite')
        organisationdetailsupdate2.send_keys(organisationdetailsupdatewebsite_data)
        time.sleep(1)

        organisationdetailsupdateEmail_path = organisationdetailsupdate.readfromXML(folder_path+'\Object\OrgProfileObject.xml','eTender','organisationEmail1')
        organisationdetailsupdateEmail = browser.find_element_by_xpath(organisationdetailsupdateEmail_path)
        organisationdetailsupdateEmail.clear()

        organisationdetailsupdateEmail_data = organisationdetailsupdate.readfromXML(folder_path+'\Data\OrganisationDetails.xml','eTender','orgEmail')
        organisationdetailsupdateEmail.send_keys(organisationdetailsupdateEmail_data)
        time.sleep(1)

##        organisationdetailsupdateImage_path = organisationdetailsupdate.readfromXML(folder_path+'\Object\OrgProfileObject.xml','eTender','OrgImage')
##        organisationdetailsupdateImage = browser.find_element_by_xpath(organisationdetailsupdateImage_path)
##        organisationdetailsupdateImage.click()
##        time.sleep(3)
##        os.system(folder_path+'\Env\OrgImageUpload.exe') #This is AUToIT script for Upload a Document(Note:selenium not supporting uploading a document from windows hence we need to install AUTOIT to upload a document)
##        time.sleep(3)

        organisationdetailsupdate_path = organisationdetailsupdate.readfromXML(folder_path+'\Object\OrgProfileObject.xml','eTender','organisatioupdate')
        organisationdetailsupdate = browser.find_element_by_xpath(organisationdetailsupdate_path)
        organisationdetailsupdate.click()
        time.sleep(2)
        return browser

    def OrganisationProfilePageUpdatetoOriginal(self,browser):
        organisationdetailsupdate3 = DataDriver()

        Adduser_path = organisationdetailsupdate3.readfromXML(folder_path+'\Object\OrgProfileObject.xml','eTender','AdduserLink')
        Adduser = browser.find_element_by_link_text(Adduser_path)
        Adduser.click()
        time.sleep(2)
        self.OpenOrganisationProfilePage(browser)
        time.sleep(1)

        organisationdetailsupdatenameoriginal_path = organisationdetailsupdate3.readfromXML(folder_path+'\Object\OrgProfileObject.xml','eTender','orgName')
        organisationdetailsupdatenameoriginal = browser.find_element_by_xpath(organisationdetailsupdatenameoriginal_path)
        organisationdetailsupdatenameoriginal.clear()
        time.sleep(1)
        organisationdetailsupdatenameoriginal.click()

        organisationdetailsupdatenameoriginal_data = organisationdetailsupdate3.readfromXML(folder_path+'\Data\OrganisationDetails.xml','eTender','orgnameOriginal')
        organisationdetailsupdatenameoriginal.send_keys(organisationdetailsupdatenameoriginal_data)

        organisationdetailsupdate_path = organisationdetailsupdate3.readfromXML(folder_path+'\Object\OrgProfileObject.xml','eTender','organisatioupdate')
        organisationdetailsupdate = browser.find_element_by_xpath(organisationdetailsupdate_path)
        organisationdetailsupdate.click()
        time.sleep(1)
        return browser


















