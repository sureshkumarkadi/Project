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

class UserProfileinfo():
    def userprofilelink(self,browser):
        userprofile = DataDriver()
        time.sleep(1)
        userprofile_path = userprofile.readfromXML(folder_path+'\Object\SwitchOrganisation.xml','eTender','userprofile')
        time.sleep(1)
        userprofile = browser.find_element_by_link_text(userprofile_path)
        time.sleep(1)
        userprofile.click()
        return browser

    def UserProfilePageUpdate(self,browser):
        userdetailsupdate = DataDriver()

        userdetailsupdateTitle_path = userdetailsupdate.readfromXML(folder_path+'\\Object\\UserProfileObject.xml','eTender','Salutation')
        userdetailsupdateTitle = browser.find_element_by_xpath(userdetailsupdateTitle_path)
        userdetailsupdateTitle.clear()
        userdetailsupdateTitle.click()

        userdetailsupdateTitle_data = userdetailsupdate.readfromXML(folder_path+'\\Data\\UserDetails.xml','eTender','salutation')
        userdetailsupdateTitle.send_keys(userdetailsupdateTitle_data)

        userdetailsupdatefirstname_path = userdetailsupdate.readfromXML(folder_path+'\\Object\\UserProfileObject.xml','eTender','FirstnameTextbox')
        userdetailsupdatefirstname = browser.find_element_by_xpath(userdetailsupdatefirstname_path)
        userdetailsupdatefirstname.clear()
        userdetailsupdatefirstname.click()

        userdetailsupdatefirstname_data = userdetailsupdate.readfromXML(folder_path+'\\Data\\UserDetails.xml','eTender','userfirstname')
        userdetailsupdatefirstname.send_keys(userdetailsupdatefirstname_data)

        userdetailsupdateLastname_path = userdetailsupdate.readfromXML(folder_path+'\\Object\\UserProfileObject.xml','eTender','LastnameTextbox')
        userdetailsupdateLastname = browser.find_element_by_xpath(userdetailsupdateLastname_path)
        userdetailsupdateLastname.clear()
        userdetailsupdateLastname.click()

        userdetailsupdateLastname_data = userdetailsupdate.readfromXML(folder_path+'\\Data\\UserDetails.xml','eTender','userlastname')
        userdetailsupdateLastname.send_keys(userdetailsupdateLastname_data)

        userjobtitleclick_path =userdetailsupdate.readfromXML(folder_path+'\\Object\\UserProfileObject.xml','eTender','Jobtitleclick')
        userjobtitleclick = browser.find_element_by_xpath(userjobtitleclick_path)
        userjobtitleclick.click()
        time.sleep(1)

        jobtitlelist_path =userdetailsupdate.readfromXML(folder_path+'\\Object\\UserProfileObject.xml','eTender','Jobtitlelist')
        jobtitlelist = browser.find_element_by_xpath(jobtitlelist_path)

        jobtitlelist_data = userdetailsupdate.readfromXML(folder_path+'\\Data\\UserDetails.xml','eTender','jobtitle')
        jobtitlelist.send_keys(jobtitlelist_data)
        time.sleep(1)

        jobtitleeselect_path =userdetailsupdate.readfromXML(folder_path+'\\Object\\UserProfileObject.xml','eTender','Jobtitleselect')
        jobtitleeselect = browser.find_element_by_xpath(jobtitleeselect_path)
        jobtitleeselect.click()
        time.sleep(1)

        usermobile_path = userdetailsupdate.readfromXML(folder_path+'\\Object\\UserProfileObject.xml','eTender','usermobile')
        usermobile = browser.find_element_by_xpath(usermobile_path)
        usermobile.clear()

        usermobile_Data = userdetailsupdate.readfromXML(folder_path+'\\Data\\UserDetails.xml','eTender','mobilenumber')
        usermobile.send_keys(usermobile_Data)
        time.sleep(1)

        userphone_path = userdetailsupdate.readfromXML(folder_path+'\\Object\\UserProfileObject.xml','eTender','userphone')
        userphone = browser.find_element_by_xpath(userphone_path)
        userphone.clear()

        userphone_data = userdetailsupdate.readfromXML(folder_path+'\\Data\\UserDetails.xml','eTender','phonenumber')
        userphone.send_keys(userphone_data)
        time.sleep(1)

        userlinkedin_path = userdetailsupdate.readfromXML(folder_path+'\\Object\\UserProfileObject.xml','eTender','userlinkedin')
        userlinkedin = browser.find_element_by_xpath(userlinkedin_path)
        userlinkedin.clear()

        userlinkedin_data = userdetailsupdate.readfromXML(folder_path+'\\Data\\UserDetails.xml','eTender','linkedin')
        userlinkedin.send_keys(userlinkedin_data)
        time.sleep(1)

        userdetailssave_path = userdetailsupdate.readfromXML(folder_path+'\\Object\\UserProfileObject.xml','eTender','submituserdetails')
        userdetailssave = browser.find_element_by_xpath(userdetailssave_path)
        time.sleep(2)
        browser.execute_script("arguments[0].scrollIntoView(true);", userdetailssave)
        time.sleep(2)
        userdetailssave.click()
        time.sleep(2)

        return browser

    def UserProfilePageUpdatebacktoOriginal(self,browser):
        userdetailsupdate3 = DataDriver()

        userdetailsupdatefirstname_path = userdetailsupdate3.readfromXML(folder_path+'\\Object\\UserProfileObject.xml','eTender','FirstnameTextbox')
        userdetailsupdatefirstname = browser.find_element_by_xpath(userdetailsupdatefirstname_path)
        userdetailsupdatefirstname.clear()
        userdetailsupdatefirstname.click()
        time.sleep(1)

        userdetailsupdatefirstname_data = userdetailsupdate3.readfromXML(folder_path+'\\Data\\UserDetails.xml','eTender','userfirstname1')
        userdetailsupdatefirstname.send_keys(userdetailsupdatefirstname_data)
        time.sleep(1)

        userdetailsupdateLastname_path = userdetailsupdate3.readfromXML(folder_path+'\\Object\\UserProfileObject.xml','eTender','LastnameTextbox')
        userdetailsupdateLastname = browser.find_element_by_xpath(userdetailsupdateLastname_path)
        userdetailsupdateLastname.clear()
        userdetailsupdateLastname.click()
        time.sleep(1)

        userdetailsupdateLastname_data = userdetailsupdate3.readfromXML(folder_path+'\\Data\\UserDetails.xml','eTender','userlastname1')
        userdetailsupdateLastname.send_keys(userdetailsupdateLastname_data)
        time.sleep(1)

        userdetailssave_path = userdetailsupdate3.readfromXML(folder_path+'\\Object\\UserProfileObject.xml','eTender','submituserdetails')
        userdetailssave = browser.find_element_by_xpath(userdetailssave_path)
        time.sleep(5)
        browser.execute_script("arguments[0].scrollIntoView(true);", userdetailssave)
        time.sleep(2)
        userdetailssave.click()

        return browser


















