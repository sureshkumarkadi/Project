#-------------------------------------------------------------------------------
# Name:         TenderModification
#
# Purpose:      Liberary functions for tender modification
#
# Author:       mathew.jacob
#
# Created:      19/05/2017
#
# Copyright:    (c) Causeway Technologies 2017
#-------------------------------------------------------------------------------
import os
import sys
import time
import datetime
from faker import Factory
dir_path = os.path.dirname(os.path.realpath(__file__))
folder_path=os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0,folder_path+"\Syslibrary")
from datadriven import DataDriver
from selenium.webdriver.support.ui import Select
orgLink=DataDriver()
from logdriver import logvalue
logs=logvalue.logger

class TenderClass():
    def TenderCreation(self,browser,tendername,tenderreference,tenderdescription,tendertype):
        time.sleep(2)
        browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','CreateTbtn')).click()

        tendername_path =orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','TenderName')
        tendername1 = browser.find_element_by_xpath(tendername_path)
        tendername1.send_keys(tendername)
        time.sleep(2)

        tenderReference_path =orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','TenderReference')
        tenderReference1 = browser.find_element_by_xpath(tenderReference_path)
        tenderReference1.send_keys(tenderreference)

        tenderDescription_path =orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','TenderDescription')
        time.sleep(1)
        tenderDescription1 = browser.find_element_by_xpath(tenderDescription_path)
        tenderDescription1.send_keys(tenderdescription)

        tendertypeclick_path =orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','TenderType')
        tendertypeclick = browser.find_element_by_xpath(tendertypeclick_path)
        tendertypeclick.click()
        time.sleep(1)

        tendertypelist_path =orgLink.readfromXML(folder_path+'\Object\Pairwiserupdateproject.xml','eTender','Projecttypelist')
        tendertypelist = browser.find_element_by_xpath(tendertypelist_path)
        tendertypelist.send_keys(tendertype)
        time.sleep(1)

        tendertypeselect_path =orgLink.readfromXML(folder_path+'\Object\Pairwiserupdateproject.xml','eTender','Tendertypeselect')
        tendertypeselect = browser.find_element_by_xpath(tendertypeselect_path)
        tendertypeselect.click()
        time.sleep(1)

        browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','startdate')).click()
        time.sleep(2)
        weekenddate = datetime.date.today().weekday()
        if weekenddate>=5:
            browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','SSdateweekend')).click()
        else:
            browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','startdateforecast')).click()

        startdate_path = orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','startdateforecastselection')
        startdate = browser.find_element_by_xpath(startdate_path)

        ddbutton=browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','enddate'))
        browser.execute_script("arguments[0].scrollIntoView(true);", ddbutton)
        time.sleep(2)
        ddbutton.click() # click on calender
        time.sleep(1)
        browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','duedateforecast')).click() # select date
        time.sleep(1)

        sbutton=browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','SaveBtn'))
        browser.execute_script("arguments[0].scrollIntoView(true);", sbutton)
        time.sleep(2)
        sbutton.click()
        time.sleep(3)

        return browser

    def Backtotradelist(self,browser):
        time.sleep(1)
        backtotradelist_path = orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','tradelist')
        backtotradelist = browser.find_element_by_xpath(backtotradelist_path)
        time.sleep(1)
        backtotradelist.click()
        return browser

    def TenderDeletion(self,browser):
        time.sleep(1)
        p = []
        p=browser.find_elements_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','TenderCheckbox'))
        time.sleep(1)
        counter = 3
        for tenderdeletion in range(counter,len(p)):
            time.sleep(2)
            p=browser.find_elements_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','TenderCheckbox'))
            counter = 3
            time.sleep(1)
            p[counter].click()
            time.sleep(1)
            delete_path = orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','DeleteBtn')
            time.sleep(1)
            delete = browser.find_element_by_xpath(delete_path)
            time.sleep(1)
            delete.click()
            time.sleep(1)
            confirmdelete_path = orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','YesBtn')
            confirmdelete = browser.find_element_by_xpath(confirmdelete_path)
            time.sleep(1)
            confirmdelete.click()
        return browser