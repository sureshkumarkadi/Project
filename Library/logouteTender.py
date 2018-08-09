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
import sys
import time
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
folder_path=os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0,folder_path+"\Library")
sys.path.insert(0,folder_path+"\Syslibrary")
sys.path.insert(0,folder_path+"\Data")
sys.path.insert(0,folder_path+"\Object")
from datadriven import DataDriver
import launcheTender


class Userprofilemenu():
     def logout_eTender(self,browser):
          browser.implicitly_wait(5)
          time.sleep(1)
          logout_XML = DataDriver()
          time.sleep(3)
          userprofile_path =logout_XML.readfromXML(folder_path+'\Object\Object.xml','eTender','userprofile')
          userprofile_menu = browser.find_element_by_xpath(userprofile_path) #Click on User profile menu on top right Corner
          userprofile_menu.click()
          time.sleep(3)
          logout_path = logout_XML.readfromXML(folder_path+'\Object\Object.xml','eTender','logout')
          logouteTender = browser.find_element_by_link_text(logout_path) #Select option Logout
          logouteTender.click()
          time.sleep(1)
          return browser

     def changePassword(self,browser):
          time.sleep(2)
          changepassword = DataDriver()
          time.sleep(1)
          userprofile_path =changepassword.readfromXML(folder_path+'\Object\Object.xml','eTender','userprofile')
          time.sleep(1)
          userprofile_menu = browser.find_element_by_xpath(userprofile_path) #Click on User profile menu on top right Corner
          userprofile_menu.click()
          time.sleep(1)
          browser.implicitly_wait(5)
          changepassword_path =changepassword.readfromXML(folder_path+'\Object\Object.xml','eTender','changepassword')
          changepassword = browser.find_element_by_link_text(changepassword_path)
          time.sleep(1)
          changepassword.click()
          time.sleep(3)
          return browser

     def changePasswordForm(self,browser):
          time.sleep(2)
          changepasswordform = DataDriver()
          time.sleep(1)
          currentpassword_path =changepasswordform.readfromXML(folder_path+'\Object\Object.xml','eTender','currentpassword')
          currentpassword = browser.find_element_by_xpath(currentpassword_path)#Current password
          time.sleep(1)
          currentpassword_data =changepasswordform.readfromXML(folder_path+'\Data\Data.xml','eTender','Subpassword')
          currentpassword.send_keys(currentpassword_data)
          time.sleep(1)

          newpassword_path =changepasswordform.readfromXML(folder_path+'\Object\Object.xml','eTender','newpassword')
          newpassword = browser.find_element_by_xpath(newpassword_path);#New password
          time.sleep(1)
          newpassword_data =changepasswordform.readfromXML(folder_path+'\Data\Data.xml','eTender','Changedpassword')
          newpassword.send_keys(newpassword_data)
          time.sleep(1)

          confirmnewpassword_path =changepasswordform.readfromXML(folder_path+'\Object\Object.xml','eTender','confirmnewpassword')
          confirmnewpassword = browser.find_element_by_xpath(confirmnewpassword_path);#Confirm new password
          time.sleep(1)
          confirmnewpassword_data =changepasswordform.readfromXML(folder_path+'\Data\Data.xml','eTender','Changedpassword')
          confirmnewpassword.send_keys(confirmnewpassword_data)
          time.sleep(1)

          changepasswordbutton_path =changepasswordform.readfromXML(folder_path+'\Object\Object.xml','eTender','changegpasswordbutton')
          changepasswordbutton = browser.find_element_by_xpath(changepasswordbutton_path);#Click on Change password button
          time.sleep(1)
          changepasswordbutton.click()
          time.sleep(7)
          return browser

     def subcontractorloginwithchangedpassword(self,browser):
          browser.implicitly_wait(5)
          login=DataDriver()

          login_id=login.readfromXML(folder_path+'\Object\Object.xml','eTender','LoginName')
          #print login_id
          login_id1 = browser.find_element_by_id(login_id)
          time.sleep(1)

          username_id=login.readfromXML(folder_path+'\Data\Data.xml','eTender','Subusername')
          #print username_id
          login_id1.send_keys(username_id)
          time.sleep(1)

          password_id=login.readfromXML(folder_path+'\Object\Object.xml','eTender','password')
          #print password_id
          password_id1 = browser.find_element_by_id(password_id)
          time.sleep(1)

          password=login.readfromXML(folder_path+'\Data\Data.xml','eTender','Changedpassword')
          #print password
          password_id1.send_keys(password)
          time.sleep(1)

          submitButton_id=login.readfromXML(folder_path+'\Object\Object.xml','eTender','submitButton')
          #print submitButton_id
          submitButton = browser.find_element_by_id(submitButton_id)
          submitButton.click()
          time.sleep(1)
          return browser

     def changepasswordbacktoOriginal(self,browser):
          browser.implicitly_wait(5)
          self.changePassword(browser)
          time.sleep(2)
          changepasswordbacktooriginal = DataDriver()
          currentpassword_path =changepasswordbacktooriginal.readfromXML(folder_path+'\Object\Object.xml','eTender','currentpassword')
          time.sleep(1)
          currentpassword = browser.find_element_by_xpath(currentpassword_path)#Current password
          time.sleep(1)
          currentpassword_data =changepasswordbacktooriginal.readfromXML(folder_path+'\Data\Data.xml','eTender','Changedpassword')
          currentpassword.send_keys(currentpassword_data)

          newpassword_path =changepasswordbacktooriginal.readfromXML(folder_path+'\Object\Object.xml','eTender','newpassword')
          newpassword = browser.find_element_by_xpath(newpassword_path);#New password
          time.sleep(1)
          newpassword_data =changepasswordbacktooriginal.readfromXML(folder_path+'\Data\Data.xml','eTender','Subpassword')
          newpassword.send_keys(newpassword_data)
          time.sleep(1)

          confirmnewpassword_path =changepasswordbacktooriginal.readfromXML(folder_path+'\Object\Object.xml','eTender','confirmnewpassword')
          confirmnewpassword = browser.find_element_by_xpath(confirmnewpassword_path);#Confirm new password
          time.sleep(1)
          confirmnewpassword_data =changepasswordbacktooriginal.readfromXML(folder_path+'\Data\Data.xml','eTender','Subpassword')
          confirmnewpassword.send_keys(confirmnewpassword_data)

          changepasswordbutton_path =changepasswordbacktooriginal.readfromXML(folder_path+'\Object\Object.xml','eTender','changegpasswordbutton')
          changepasswordbutton = browser.find_element_by_xpath(changepasswordbutton_path);#Click on Change password button
          time.sleep(1)
          changepasswordbutton.click()
          time.sleep(7)
          return browser

    #Calling Methods
        #for num in range(1,2):
            #launcheTender()
            #logineTender()