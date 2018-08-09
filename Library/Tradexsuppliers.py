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
sys.path.insert(0,folder_path+"\Env")
from datadriven import DataDriver
import launcheTender
class Tradexsupplier():
    def viewtradexsupplierdetails(self,browser):
        browser.implicitly_wait(5)
        #tradex_supplierdetails_Pluslink = []
        Pluslink1 = DataDriver()
        time.sleep(1)
        tradex_supplierdetails_path = Pluslink1.readfromXML(folder_path+'\Object\Tradex.xml','eTender','Pluslink')
        time.sleep(1)
        tradex_supplierdetails_Pluslink = browser.find_element_by_xpath(tradex_supplierdetails_path)
        time.sleep(1)
        tradex_supplierdetails_Pluslink.click()
        return browser

    def estimatortradexsupplier(self,browser):
        time.sleep(1)
        tenderdetails_XML = DataDriver()
        list_tenderdetails = []
        time.sleep(1)
        tenderdetails_path = tenderdetails_XML.readfromXML(folder_path+'\Object\Tradex.xml','eTender','suppliericon')
        list_tenderdetails = browser.find_elements_by_xpath(tenderdetails_path)
        time.sleep(1)
        list_tenderdetails[2].click()  #Clickon the Add supplier Icon
        time.sleep(2)
        return browser

    def estimatortradexaddsupplier(self,browser):
        time.sleep(1)
        addsupplier_XML = DataDriver()
        time.sleep(1)
        addsupplier_path = addsupplier_XML.readfromXML(folder_path+'\Object\Tradex.xml','eTender','addsupplierbutton')
        addsupplier = browser.find_element_by_xpath(addsupplier_path)
        time.sleep(1)
        addsupplier.click()  #Clickon the Add supplier button to add suppliers
        time.sleep(2)
        return browser

    def entersupplier(self,browser):
        time.sleep(1)
        tradexsupplier_XML = DataDriver()
        list_tradexsupplier = []
        time.sleep(1)
        tradexsupplier_path = tradexsupplier_XML.readfromXML(folder_path+'\Object\Tradex.xml','eTender','tradexsupplierinput')
        time.sleep(1)
        list_tradexsupplier = browser.find_elements_by_xpath(tradexsupplier_path) #Path for input supplier
        time.sleep(1)
        list_tradexsupplier[2].click()
        time.sleep(1)
        tradexsupplier_data = tradexsupplier_XML.readfromXML(folder_path+'\Data\Tradex.xml','eTender','tradexsupplier')
        time.sleep(1)
        list_tradexsupplier[2].send_keys(tradexsupplier_data) #input supplier
        time.sleep(5)
        return browser

    def entersupplierfortradexstatus(self,browser):
        time.sleep(1)
        tradexsupplier_XML = DataDriver()
        list_tradexsupplier = []
        time.sleep(1)
        tradexsupplier_path = tradexsupplier_XML.readfromXML(folder_path+'\Object\Tradex.xml','eTender','tradexsupplierinput')
        time.sleep(1)
        list_tradexsupplier = browser.find_elements_by_xpath(tradexsupplier_path) #Path for input supplier
        time.sleep(1)
        list_tradexsupplier[2].click()
        time.sleep(1)
        tradexsupplier_data = tradexsupplier_XML.readfromXML(folder_path+'\Data\Tradex.xml','eTender','tradexstatus')
        time.sleep(1)
        list_tradexsupplier[2].send_keys(tradexsupplier_data) #input supplier
        time.sleep(5)
        return browser

    def closetradexsupplierwindow(self,browser):
        time.sleep(1)
        closetradexsupplierwindow_XML = DataDriver()
        time.sleep(1)
        closetradexsupplierwindow_path = closetradexsupplierwindow_XML.readfromXML(folder_path+'\Object\Tradex.xml','eTender','tradexsupplierwindowclose')
        time.sleep(1)
        closetradexsupplierwindow1 = browser.find_element_by_xpath(closetradexsupplierwindow_path) #Path for input supplier
        time.sleep(1)
        closetradexsupplierwindow1.click()
        return browser

    def closetradexuserwindow(self,browser):
        time.sleep(1)
        closetradexuserwindow_XML = DataDriver()
        time.sleep(1)
        closetradexuserwindow_path = closetradexuserwindow_XML.readfromXML(folder_path+'\Object\Tradex.xml','eTender','closetradexuserwindow')
        time.sleep(1)
        closetradexuserwindow1 = browser.find_element_by_xpath(closetradexuserwindow_path) #Path for input supplier
        time.sleep(1)
        closetradexuserwindow1.click()
        return browser

    def selectsuppliercontact(self,browser):
        browser.implicitly_wait(5)
        selectsuppliercontact_list = []
        selectsuppliercontact_XML = DataDriver()
        time.sleep(1)
        selectsuppliercontact_path = selectsuppliercontact_XML.readfromXML(folder_path+'\Object\Tradex.xml','eTender','adduserCheckbox')
        time.sleep(1)
        selectsuppliercontact_list = browser.find_elements_by_xpath(selectsuppliercontact_path) #Select supplier contact
        time.sleep(1)
        selectsuppliercontact_list[1].click()
        time.sleep(1)
        addtoinvite_path = selectsuppliercontact_XML.readfromXML(folder_path+'\Object\Tradex.xml','eTender','addtoinvite')
        time.sleep(1)
        addtoinvite = browser.find_element_by_xpath(addtoinvite_path) #Select supplier contact
        time.sleep(1)
        addtoinvite.click()
        return browser

    def deletesuppliercontact(self,browser):
        time.sleep(1)
        deletesuppliercontact_list = []
        deletesuppliercontact_XML = DataDriver()
        time.sleep(1)
        deletesuppliercontact_path = deletesuppliercontact_XML.readfromXML(folder_path+'\Object\Tradex.xml','eTender','deletesuppliercontact')
        time.sleep(1)
        deletesuppliercontact_list = browser.find_element_by_xpath(deletesuppliercontact_path) #delete supplier contact
        time.sleep(1)
        deletesuppliercontact_list.click()
        confirmdeletesuppliercontact_path = deletesuppliercontact_XML.readfromXML(folder_path+'\Object\Tradex.xml','eTender','confirmdeletesuppliercontact')
        time.sleep(1)
        confirmdeletesuppliercontact_list = browser.find_element_by_xpath(confirmdeletesuppliercontact_path) #confirm delete supplier contact
        time.sleep(1)
        confirmdeletesuppliercontact_list.click()
        return browser

    def sendenquirytosupplier(self,browser):
        time.sleep(1)
        sendenquirytosupplier_XML = DataDriver()
        time.sleep(1)
        sendenquirytosupplier_path = sendenquirytosupplier_XML.readfromXML(folder_path+'\Object\Tradex.xml','eTender','sendenquirytosuppliercontact')
        time.sleep(1)
        sendenquirytosupplier_list = browser.find_element_by_xpath(sendenquirytosupplier_path) #Send enquiry to supplier contact
        time.sleep(1)
        sendenquirytosupplier_list.click()
        return browser

    def supplierinvite(self,browser):
        time.sleep(1)
        tradexsupplier_XML = DataDriver()
        list_tradexsupplier = []
        time.sleep(1)
        tradexsupplier_path = tradexsupplier_XML.readfromXML(folder_path+'\Object\Tradex.xml','eTender','tradexsupplierinput')
        time.sleep(1)
        list_tradexsupplier = browser.find_elements_by_xpath(tradexsupplier_path) #Path for input supplier
        time.sleep(2)
        list_tradexsupplier[2].click()
        time.sleep(1)
        tradexsupplier_data = tradexsupplier_XML.readfromXML(folder_path+'\Data\Tradex.xml','eTender','supplier')
        time.sleep(1)
        list_tradexsupplier[2].send_keys(tradexsupplier_data) #input supplier
        return browser

    def addnewsupplier(self,browser):
        tradexsupplier_XML = DataDriver()
        time.sleep(3)
        newsupplierinvite_path = tradexsupplier_XML.readfromXML(folder_path+'\Object\Tradex.xml','eTender','supplierinvite')
        time.sleep(1)
        newsupplierinvite = browser.find_element_by_xpath(newsupplierinvite_path) #Path for selecting supplier invite
        time.sleep(1)
        newsupplierinvite.click() # click on supplier invite link
        time.sleep(1)
        return browser

    def enternewsupplierdetails(self,browser):
        tradexsupplier_XML = DataDriver()
        newsuppliername_path = tradexsupplier_XML.readfromXML(folder_path+'\Object\Tradex.xml','eTender','newsuppliername')
        time.sleep(1)
        newsuppliername = browser.find_element_by_xpath(newsuppliername_path)
        time.sleep(1)
        newsuppliername_data = tradexsupplier_XML.readfromXML(folder_path+'\Data\Tradex.xml','eTender','newsuppliername')
        time.sleep(1)
        newsuppliername.send_keys(newsuppliername_data) # input supplier name
        time.sleep(1)
        newsupplieremail_path = tradexsupplier_XML.readfromXML(folder_path+'\Object\Tradex.xml','eTender','newsupplieremail')
        time.sleep(1)
        newsupplieremail = browser.find_element_by_xpath(newsupplieremail_path)
        time.sleep(1)
        newsupplieremail_data = tradexsupplier_XML.readfromXML(folder_path+'\Data\Tradex.xml','eTender','newsupplieremail')
        time.sleep(1)
        newsupplieremail.send_keys(newsupplieremail_data) # input supplier email
        time.sleep(1)

        addsupplier_path = tradexsupplier_XML.readfromXML(folder_path+'\Object\Tradex.xml','eTender','newsupplieradd')
        time.sleep(1)
        addsupplier = browser.find_element_by_xpath(addsupplier_path)
        time.sleep(1)
        addsupplier.click() # Click on add supplier button
        return browser

    def addnewtradexuser(self,browser):
        tradexsupplier_XML = DataDriver()
        time.sleep(3)
        newuserinvite_path = tradexsupplier_XML.readfromXML(folder_path+'\Object\Tradex.xml','eTender','userinvite')
        time.sleep(1)
        newuserinvite = browser.find_element_by_xpath(newuserinvite_path) #Path for selecting user invite
        time.sleep(1)
        newuserinvite.click() # click on user invite link
        time.sleep(1)
        newusername_path = tradexsupplier_XML.readfromXML(folder_path+'\Object\Tradex.xml','eTender','newusername')
        time.sleep(1)
        newusername = browser.find_element_by_xpath(newusername_path)
        time.sleep(1)
        newusername_data = tradexsupplier_XML.readfromXML(folder_path+'\Data\Tradex.xml','eTender','newusername')
        time.sleep(1)
        newusername.send_keys(newusername_data) # input user name
        time.sleep(1)
        newuseremail_path = tradexsupplier_XML.readfromXML(folder_path+'\Object\Tradex.xml','eTender','newuseremail')
        time.sleep(1)
        newuseremail = browser.find_element_by_xpath(newuseremail_path)
        time.sleep(1)
        newuseremail_data = tradexsupplier_XML.readfromXML(folder_path+'\Data\Tradex.xml','eTender','newuseremail')
        time.sleep(1)
        newuseremail.send_keys(newuseremail_data) # input user email
        time.sleep(1)

        adduser_path = tradexsupplier_XML.readfromXML(folder_path+'\Object\Tradex.xml','eTender','newuseradd')
        time.sleep(1)
        adduser = browser.find_element_by_xpath(adduser_path)
        time.sleep(1)
        adduser.click() # Click on add user button
        return browser

ranksupplier1 = DataDriver()

class Ranksupplier():
    def ranksupplier(self,browser):
        ranksupplierlink_path = ranksupplier1.readfromXML(folder_path+'\Object\Tradex.xml','eTender','ranksupplierlink')
        time.sleep(1)
        ranksupplierlink = browser.find_element_by_xpath(ranksupplierlink_path)
        time.sleep(1)
        ranksupplierlink.click()
        return browser

    def ranksupplieractivestate(self,browser):
        ranking_path = ranksupplier1.readfromXML(folder_path+'\Object\Tradex.xml','eTender','rankingoff')
        time.sleep(1)
        ranking = browser.find_element_by_xpath(ranking_path)
        time.sleep(1)
        ranking.click()
        return browser