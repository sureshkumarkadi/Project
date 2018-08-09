#-------------------------------------------------------------------------------
# Name:        SubmitTender
# Purpose:
#
# Author:      suresh.kumar
#
# Created:     04-05-2016
# Copyright:   (c) suresh.kumar 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
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
#import LauncheTender
import unittest

global browser
#Test case Number = 100034
class SubmitTenderclass():
      def SubmitTender(self):
          #browser=LauncheTender.browser
          browser.implicitly_wait(5)
          elems = browser.find_elements_by_xpath("//div//button[@ng-click='submitTender()']") # Click on Submit tender button
          for elem in elems:
              elem.click()
              break

#Validating whether xpath exists for ConfirmSubmit,If exists pass else fail

          browser.implicitly_wait(5)
          tCase = "100034"
          eResults = "Confirm TenderSubmission"
          aResults = "Confirm TenderSubmission"

          elem = browser.find_element_by_xpath("//div//button[@ng-click='confirmSubmitTender()']") #Verifying Webelement for Confirm Submit button

          if elem.is_displayed():
        #elem.click()
            rStatus = "PASS"
          else:
            rStatus = "FAIL"
          report = htmlreportclass()
          report.resultHtmlPageBody(tCase,eResults,aResults,rStatus)
          print(rStatus)

#End of Validating

#Test case Number = 100035
      def ConfirmTenderSubmission(self,browser):
          browser.implicitly_wait(5)
          elems = browser.find_elements_by_xpath("//div//button[@ng-click='confirmSubmitTender()']") # Click on Confirm Submit button
          for elem in elems:
              elem.click()
              break

#Validating whether xpath exists for Project,If exists pass else fail

          browser.implicitly_wait(5)
          tCase = "100035"
          eResults = "Tender Submitted"
          aResults = "Tender Submitted"

          elem = browser.find_element_by_xpath("//div//li[@ng-show='projectName']//a[@class='ng-binding']") #Verifying Webelement for Projectname

          if elem.is_displayed():
        #elem.click()
            rStatus = "PASS"
          else:
            rStatus = "FAIL"
          report = htmlreportclass()
          report.resultHtmlPageBody(tCase,eResults,aResults,rStatus)
          print(rStatus)

#End of Validating

#Test case Number = 100036
class declineTenderclass():
      def declineTenderConfirm(self,browser):
          browser.implicitly_wait(5)
          elems = browser.find_elements_by_xpath("//div//button[@ng-click='declineTender()']") # Click on decline tender button
          for elem in elems:
              elem.click()
              break

#Validating whether xpath exists for Confirmdecline,If exists pass else fail

          browser.implicitly_wait(5)
          tCase = "100036"
          eResults = "Confirm Tenderdecline"
          aResults = "Confirm Tenderdecline"

          decline_button = browser.find_element_by_xpath("//div//button[@ng-click='confirmDeclineTender()']") #Verifying Webelement for Confirm decline button
          cancel_button = browser.find_element_by_xpath("//div//button[@ng-click='cancel()']") #Verifying Webelement for cancel button

          if decline_button.is_displayed() and cancel_button.is_displayed():
                rStatus = "PASS"
          else:
                rStatus = "FAIL"
          report = htmlreportclass()
          report.resultHtmlPageBody(tCase,eResults,aResults,rStatus)
          print(rStatus)

#End of Validating

#Test case Number = 100037
      def declineTenderSubmission(self,browser):
          browser.implicitly_wait(5)
          decline_button = browser.find_element_by_xpath("//div//button[@ng-click='confirmDeclineTender()']") #Click on decline button
          decline_button.click()

#Validating whether xpath exists for Project,If exists pass else fail

          browser.implicitly_wait(5)
          tCase = "100037"
          eResults = "Tender declined"
          aResults = "Tender declined"

          tenderdeclined_notification = browser.find_element_by_xpath("//div[@class='toast-message']//div[@class='col-md-11 ng-binding ng-scope']"); #xpath for tender declined notification

          if tenderdeclined_notification.is_displayed():
            rStatus = "PASS"
          else:
            rStatus = "FAIL"
          report = htmlreportclass()
          report.resultHtmlPageBody(tCase,eResults,aResults,rStatus)
          print(rStatus)

#End of Validating


