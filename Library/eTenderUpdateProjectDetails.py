#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      suresh.kumar
#
# Created:     24-03-2017
# Copyright:   (c) suresh.kumar 2017
# Licence:     <Causeway>
#-------------------------------------------------------------------------------

import re
import string
import os
import time
import unittest
import sys
import xlrd
import datetime
from datetime import date
from babel import numbers

dir_path = os.path.dirname(os.path.realpath(__file__))
folder_path=os.path.abspath(os.path.join(dir_path, os.pardir))

book = xlrd.open_workbook(folder_path+'\Data\eTender.xls', formatting_info=True)
sheet = book.sheet_by_name('UpdateProjectDetails')

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from launcheTender import LauncheTenderclass
sys.path.insert(0,folder_path+"\Library")
sys.path.insert(0,folder_path+"\Syslibrary")
sys.path.insert(0,folder_path+"\Data")
sys.path.insert(0,folder_path+"\Object")
from datadriven import DataDriver

class updatedetails():

    def createproject(self,browser):
        create_project = DataDriver()

        createproject_path =create_project.readfromXML(folder_path+'\Object\Pairwiserupdateproject.xml','eTender','createproject')
        time.sleep(1)
        createproject = browser.find_element_by_xpath(createproject_path)

        time.sleep(2)
        createproject.click()
        return browser

    def updateproject(self,browser):
        update_project = DataDriver()
        updateproject = []

        updateproject_path =update_project.readfromXML(folder_path+'\Object\Pairwiserupdateproject.xml','eTender','updateproject')
        time.sleep(2)
        updateproject = browser.find_elements_by_xpath(updateproject_path)
        time.sleep(5)
        updateproject[0].click()
        return browser

    def updateprojectdetails(self,browser,projectname,projectreference,projectdescription,projecttype,projectvalue):
        update_projectdetails = DataDriver()

        updateprojectname_path =update_projectdetails.readfromXML(folder_path+'\Object\Pairwiserupdateproject.xml','eTender','ProjectName2')
        updateprojectname = browser.find_element_by_xpath(updateprojectname_path)
        updateprojectname.clear()
        updateprojectname.send_keys(projectname)
        time.sleep(2)

        updateprojectReference_path =update_projectdetails.readfromXML(folder_path+'\Object\Pairwiserupdateproject.xml','eTender','ProjectRef2')
        updateprojectReference = browser.find_element_by_xpath(updateprojectReference_path)
        updateprojectReference.clear()
        updateprojectReference.send_keys(projectreference)

        updateprojectDescription_path =update_projectdetails.readfromXML(folder_path+'\Object\Pairwiserupdateproject.xml','eTender','ProjectDes2')
        time.sleep(1)
        updateprojectDescription = browser.find_element_by_xpath(updateprojectDescription_path)
        updateprojectDescription.clear()
        updateprojectDescription.send_keys(projectdescription)

        projecttypeclick_path =update_projectdetails.readfromXML(folder_path+'\Object\Pairwiserupdateproject.xml','eTender','Projecttypeclick')
        projecttypeclick = browser.find_element_by_xpath(projecttypeclick_path)
        projecttypeclick.click()
        time.sleep(1)

        projecttypelist_path =update_projectdetails.readfromXML(folder_path+'\Object\Pairwiserupdateproject.xml','eTender','Projecttypelist')
        projecttypelist = browser.find_element_by_xpath(projecttypelist_path)
        projecttypelist.send_keys(projecttype)
        time.sleep(1)

        projecttypeselect_path =update_projectdetails.readfromXML(folder_path+'\Object\Pairwiserupdateproject.xml','eTender','Projecttypeselect')
        projecttypeselect = browser.find_element_by_xpath(projecttypeselect_path)
        time.sleep(1)
        projecttypeselect.click()
        time.sleep(1)

        projectcurrencyclick_path =update_projectdetails.readfromXML(folder_path+'\Object\Pairwiserupdateproject.xml','eTender','Projecttypeclick')
        projectcurrencyclick = browser.find_element_by_xpath(projectcurrencyclick_path)
        projectcurrencyclick.click()
        time.sleep(1)

        projectcurrencylist_path =update_projectdetails.readfromXML(folder_path+'\Object\Pairwiserupdateproject.xml','eTender','Projetcurrency')
        projectcurrencylist = browser.find_element_by_xpath(projectcurrencylist_path)

        time.sleep(2)

        projectcurrencylist_data =update_projectdetails.readfromXML(folder_path+'\Data\ProjectDetails.xml','eTender','projectcurrency')

        time.sleep(1)
        projectcurrencylist.send_keys(projectcurrencylist_data)
        time.sleep(1)

        projectcurrencyselect_path =update_projectdetails.readfromXML(folder_path+'\Object\Pairwiserupdateproject.xml','eTender','Projectcurrencyselect')
        projectcurrencyselect = browser.find_element_by_xpath(projectcurrencyselect_path)
        projectcurrencyselect.click()
        time.sleep(1)

        projectappvalue_path =update_projectdetails.readfromXML(folder_path+'\Object\Pairwiserupdateproject.xml','eTender','Projectvalue2')
        projectappvalue = browser.find_element_by_xpath(projectappvalue_path)
        projectappvalue.clear()
        projectappvalue.send_keys(projectvalue)

##        projectlocation_path =update_projectdetails.readfromXML(folder_path+'\Object\Pairwiserupdateproject.xml','eTender','Projectlocation')
##        projectlocation = browser.find_element_by_xpath(projectlocation_path)
##        projectlocation.clear()
##        time.sleep(1)
##        projectlocation.send_keys(projectlocation1)

        return browser

    def updateprojectdetailsstructures(self,browser,projectname,projectreference,projectdescription,projectvalue,projecttype):
        update_projectdetails1 = DataDriver()

        updateprojectname_path =update_projectdetails1.readfromXML(folder_path+'\Object\Pairwiserupdateproject.xml','eTender','ProjectName2')
        updateprojectname = browser.find_element_by_xpath(updateprojectname_path)
        updateprojectname.clear()
        updateprojectname.send_keys(projectname)
        time.sleep(2)

        updateprojectReference_path =update_projectdetails1.readfromXML(folder_path+'\Object\Pairwiserupdateproject.xml','eTender','ProjectRef2')
        updateprojectReference = browser.find_element_by_xpath(updateprojectReference_path)
        updateprojectReference.clear()
        updateprojectReference.send_keys(projectreference)

        updateprojectDescription_path =update_projectdetails1.readfromXML(folder_path+'\Object\Pairwiserupdateproject.xml','eTender','ProjectDes2')
        updateprojectDescription = browser.find_element_by_xpath(updateprojectDescription_path)
        updateprojectDescription.clear()
        updateprojectDescription.send_keys(projectdescription)

        projecttypeclick_path =update_projectdetails1.readfromXML(folder_path+'\Object\Pairwiserupdateproject.xml','eTender','Projecttypeclick')
        projecttypeclick = browser.find_element_by_xpath(projecttypeclick_path)
        projecttypeclick.click()
        time.sleep(1)

        projecttypelist_path =update_projectdetails1.readfromXML(folder_path+'\Object\Pairwiserupdateproject.xml','eTender','Projecttypelist')
        projecttypelist = browser.find_element_by_xpath(projecttypelist_path)
        projecttypelist.send_keys(projecttype)
        time.sleep(1)

        #projecttypeclick = []

        projecttypeclick_path =update_projectdetails1.readfromXML(folder_path+'\Object\Pairwiserupdateproject.xml','eTender','Structures')
        projecttypeclick = browser.find_element_by_xpath(projecttypeclick_path)
        time.sleep(1)
        #projecttypeclick[1].click()
        projecttypeclick.click()
        time.sleep(1)

        projectappvalue_path =update_projectdetails1.readfromXML(folder_path+'\Object\Pairwiserupdateproject.xml','eTender','Projectvalue2')
        projectappvalue = browser.find_element_by_xpath(projectappvalue_path)
        projectappvalue.clear()
        projectappvalue.send_keys(projectvalue)

##        projectlocation_path =update_projectdetails1.readfromXML(folder_path+'\Object\Pairwiserupdateproject.xml','eTender','Projectlocation')
##        projectlocation = browser.find_element_by_xpath(projectlocation_path)
##        projectlocation.clear()
##        time.sleep(1)
##        projectlocation.send_keys(projectlocation1)

        return browser

    def saveprojectdetails(self,browser):
        save_projectdetails = DataDriver()

        saveprojectdetails_path =save_projectdetails.readfromXML(folder_path+'\Object\Pairwiserupdateproject.xml','eTender','Saveproject')
        saveprojectdetails = browser.find_element_by_xpath(saveprojectdetails_path)
        time.sleep(2)
        browser.execute_script("arguments[0].scrollIntoView(true);", saveprojectdetails)
        time.sleep(2)
        saveprojectdetails.click()
        time.sleep(4)
        toastmessage_path =save_projectdetails.readfromXML(folder_path+'\Object\Pairwiserupdateproject.xml','eTender','toastmessageclose')
        time.sleep(2)
        toastmessageclose = browser.find_element_by_xpath(toastmessage_path)
        time.sleep(2)
        toastmessageclose.click()
        time.sleep(2)
        return browser

    def updateprojectdetails1(self,browser):
        update_projectdetails = DataDriver()

        updateprojectdetails_path =update_projectdetails.readfromXML(folder_path+'\Object\Pairwiserupdateproject.xml','eTender','Saveproject')
        updateprojectdetails = browser.find_element_by_xpath(updateprojectdetails_path)
        time.sleep(2)
        browser.execute_script("arguments[0].scrollIntoView(true);", updateprojectdetails)
        time.sleep(2)
        updateprojectdetails.click()
        time.sleep(1)
        return browser


    def deleteproject(self,browser):
        delete_project = DataDriver()

        deleteproject_path =delete_project.readfromXML(folder_path+'\Object\Pairwiserupdateproject.xml','eTender','deleteproject')
        deleteproject = browser.find_element_by_xpath(deleteproject_path)
        time.sleep(2)
        browser.execute_script("arguments[0].scrollIntoView(true);", deleteproject)
        time.sleep(2)
        deleteproject.click()

        confirmdeleteproject_path =delete_project.readfromXML(folder_path+'\Object\Pairwiserupdateproject.xml','eTender','confirmdeleteproject')
        confirmdeleteproject = browser.find_element_by_xpath(confirmdeleteproject_path)
        time.sleep(2)
        confirmdeleteproject.click()
        time.sleep(1)
        return browser

    def updateprojectdetailsbacktooriginal(self,browser,projecttype):
        update_projectdetailstooriginal = DataDriver()

        updateprojectname_path =update_projectdetailstooriginal.readfromXML(folder_path+'\Object\Pairwiserupdateproject.xml','eTender','ProjectName2')
        updateprojectname = browser.find_element_by_xpath(updateprojectname_path)
        updateprojectname.clear()

        updateprojectnamedata =update_projectdetailstooriginal.readfromXML(folder_path+'\Object\Object.xml','eTender','projectlist')
        updateprojectname.send_keys(updateprojectnamedata)
        time.sleep(2)

        updateprojectReference_path =update_projectdetailstooriginal.readfromXML(folder_path+'\Object\Pairwiserupdateproject.xml','eTender','ProjectRef2')
        updateprojectReference = browser.find_element_by_xpath(updateprojectReference_path)
        updateprojectReference.clear()

        updateprojectRefdata =update_projectdetailstooriginal.readfromXML(folder_path+'\Object\Object.xml','eTender','projectlist')
        updateprojectReference.send_keys(updateprojectRefdata)
        time.sleep(2)

        projecttypeclick_path =update_projectdetailstooriginal.readfromXML(folder_path+'\Object\Pairwiserupdateproject.xml','eTender','Projecttypeclick')
        projecttypeclick = browser.find_element_by_xpath(projecttypeclick_path)
        projecttypeclick.click()
        time.sleep(1)

        projecttypelist_path =update_projectdetailstooriginal.readfromXML(folder_path+'\Object\Pairwiserupdateproject.xml','eTender','Projecttypelist')
        projecttypelist = browser.find_element_by_xpath(projecttypelist_path)
        projecttypelist.send_keys(projecttype)
        time.sleep(1)

        projecttypeselect_path =update_projectdetailstooriginal.readfromXML(folder_path+'\Object\Pairwiserupdateproject.xml','eTender','Projecttypeselect')
        projecttypeselect = browser.find_element_by_xpath(projecttypeselect_path)
        projecttypeselect.click()
        time.sleep(1)

        projectcurrencyclick_path =update_projectdetailstooriginal.readfromXML(folder_path+'\Object\Pairwiserupdateproject.xml','eTender','Projecttypeclick')
        projectcurrencyclick = browser.find_element_by_xpath(projectcurrencyclick_path)
        projectcurrencyclick.click()
        time.sleep(1)

        projectcurrencylist_path =update_projectdetailstooriginal.readfromXML(folder_path+'\Object\Pairwiserupdateproject.xml','eTender','Projetcurrency')
        projectcurrencylist = browser.find_element_by_xpath(projectcurrencylist_path)

        projectcurrencylist_data =update_projectdetailstooriginal.readfromXML(folder_path+'\Data\ProjectDetails.xml','eTender','projectcurrency')
        projectcurrencylist.send_keys(projectcurrencylist_data)
        time.sleep(1)

        projectcurrencyselect_path =update_projectdetailstooriginal.readfromXML(folder_path+'\Object\Pairwiserupdateproject.xml','eTender','Projectcurrencyselect')
        projectcurrencyselect = browser.find_element_by_xpath(projectcurrencyselect_path)
        time.sleep(2)
        projectcurrencyselect.click()
        time.sleep(1)
        return browser

    def projectstartdate(self,browser):
        startdate_projectdetails = DataDriver()

        startdate_path =startdate_projectdetails.readfromXML(folder_path+'\Object\Pairwiserupdateproject.xml','eTender','Projectstartdate')
        startdate = browser.find_element_by_xpath(startdate_path)
        startdate.click()
        time.sleep(1)
        startdatepicker = []

        weekenddate = datetime.date.today().weekday()
        if weekenddate>=5:
            startdatepicker_path = startdate_projectdetails.readfromXML(folder_path+'\Object\Pairwiserupdateproject.xml','eTender','startdatepickerweekend')
            startdatepicker = browser.find_elements_by_xpath(startdatepicker_path)
            startdatepicker[0].click()

        else:
            startdatepicker_path = startdate_projectdetails.readfromXML(folder_path+'\Object\Pairwiserupdateproject.xml','eTender','startdatepicker')
            startdatepicker = browser.find_elements_by_xpath(startdatepicker_path)
            startdatepicker[0].click()

        time.sleep(1)
        return browser

    def projectduedate(self,browser):
        duedate_projectdetails = DataDriver()

        duedate_path =duedate_projectdetails.readfromXML(folder_path+'\Object\Pairwiserupdateproject.xml','eTender','Projectduedate')
        duedate = browser.find_element_by_xpath(duedate_path)
        duedate.click()
        time.sleep(1)

        for duedatenextdate in range(0,3):
            duedatenext = []
            duedatenext_path =duedate_projectdetails.readfromXML(folder_path+'\Object\Pairwiserupdateproject.xml','eTender','duedatepickernext')
            duedatenext = browser.find_elements_by_xpath(duedatenext_path)
            time.sleep(1)
            duedatenext[0].click()
            time.sleep(2)

        duedatepicker = []

        duedatepicker_path =duedate_projectdetails.readfromXML(folder_path+'\Object\Pairwiserupdateproject.xml','eTender','duedatepicker')
        duedatepicker = browser.find_elements_by_xpath(duedatepicker_path)
        time.sleep(1)
        duedatepicker[0].click()
        time.sleep(2)

        return browser

    def projectduedateprevious(self,browser):
        duedateprevious_projectdetails = DataDriver()

        duedate_path =duedateprevious_projectdetails.readfromXML(folder_path+'\Object\Pairwiserupdateproject.xml','eTender','Projectduedate')
        duedate = browser.find_element_by_xpath(duedate_path)
        duedate.click()
        time.sleep(1)

        for duedatepreviousdate in range(0,1):
            duedateprevious = []
            duedateprevious_path =duedateprevious_projectdetails.readfromXML(folder_path+'\Object\Pairwiserupdateproject.xml','eTender','duedatepickerprevious')
            duedateprevious = browser.find_elements_by_xpath(duedateprevious_path)
            time.sleep(1)
            duedateprevious[0].click()
            time.sleep(2)

        duedatepicker = []

        duedatepicker_path =duedateprevious_projectdetails.readfromXML(folder_path+'\Object\Pairwiserupdateproject.xml','eTender','duedatepicker')
        duedatepicker = browser.find_elements_by_xpath(duedatepicker_path)
        time.sleep(1)
        duedatepicker[0].click()
        time.sleep(2)

        return browser

    def projectdetailsupdate(self,browser):
        update_projectdetails1 = DataDriver()

        updateprojectname_path =update_projectdetails1.readfromXML(folder_path+'\Object\Pairwiserupdateproject.xml','eTender','ProjectName2')
        updateprojectname = browser.find_element_by_xpath(updateprojectname_path)
        updateprojectname.clear()

        updateprojectname_data =update_projectdetails1.readfromXML(folder_path+'\Data\ProjectDetails.xml','eTender','updateprojectname')
        updateprojectname.send_keys(updateprojectname_data)
        time.sleep(2)

        updateprojectReference_path =update_projectdetails1.readfromXML(folder_path+'\Object\Pairwiserupdateproject.xml','eTender','ProjectRef2')
        updateprojectReference = browser.find_element_by_xpath(updateprojectReference_path)
        updateprojectReference.clear()

        updateprojectRef_data =update_projectdetails1.readfromXML(folder_path+'\Data\ProjectDetails.xml','eTender','updateprojectRef')
        updateprojectReference.send_keys(updateprojectRef_data)
        time.sleep(2)

        updateprojectappvalue_path =update_projectdetails1.readfromXML(folder_path+'\Object\Pairwiserupdateproject.xml','eTender','Projectvalue2')
        updateprojectappvalue = browser.find_element_by_xpath(updateprojectappvalue_path)
        updateprojectappvalue.clear()

        updateprojectappvalue_data =update_projectdetails1.readfromXML(folder_path+'\Data\ProjectDetails.xml','eTender','updateprojectvalue')
        updateprojectappvalue.send_keys(updateprojectappvalue_data)
        time.sleep(2)

        return browser

    def projectcurrency(self):
        project_currency = DataDriver()

        projectcurrency_value =project_currency.readfromXML(folder_path+'\Data\ProjectDetails.xml','eTender','updateprojectvalue')
        projectcurrency_code =project_currency.readfromXML(folder_path+'\Data\ProjectDetails.xml','eTender','projectcurrencycode')

        value = numbers.format_currency(projectcurrency_value,projectcurrency_code,locale='en')
        return value

    def projectdetails(self,browser):
        project_details = DataDriver()

        projectdetails = []

        projectdetails_path =project_details.readfromXML(folder_path+'\Object\Project.xml','eTender','projectvaluelabel')
        projectdetails=browser.find_elements_by_xpath(projectdetails_path)
        for projectdetails1 in projectdetails.items():
            print (projectdetails1.text)
        #print projectdetails[0].items
        #prj1 = projectdetails[0].items
        #return prj1
##        print projectdetails[1]
##        print projectdetails[2]
##        print projectdetails[3]
##        print projectdetails[4]
        return browser

    def projectdetailscurrency(self,browser,projecttype,projectcurrency,projectvalue):
        update_projectdetails = DataDriver()

        projecttypeclick_path =update_projectdetails.readfromXML(folder_path+'\Object\Pairwiserupdateproject.xml','eTender','Projecttypeclick')
        projecttypeclick = browser.find_element_by_xpath(projecttypeclick_path)
        projecttypeclick.click()
        time.sleep(1)

        projecttypelist_path =update_projectdetails.readfromXML(folder_path+'\Object\Pairwiserupdateproject.xml','eTender','Projecttypelist')
        projecttypelist = browser.find_element_by_xpath(projecttypelist_path)
        projecttypelist.send_keys(projecttype)
        time.sleep(1)

        projecttypeselect_path =update_projectdetails.readfromXML(folder_path+'\Object\Pairwiserupdateproject.xml','eTender','Projecttypeselect')
        projecttypeselect = browser.find_element_by_xpath(projecttypeselect_path)
        projecttypeselect.click()
        time.sleep(1)

        projectcurrencyclick_path =update_projectdetails.readfromXML(folder_path+'\Object\Pairwiserupdateproject.xml','eTender','Projecttypeclick')
        projectcurrencyclick = browser.find_element_by_xpath(projectcurrencyclick_path)
        projectcurrencyclick.click()
        time.sleep(1)

        projectcurrencylist_path =update_projectdetails.readfromXML(folder_path+'\Object\Pairwiserupdateproject.xml','eTender','Projetcurrency')
        projectcurrencylist = browser.find_element_by_xpath(projectcurrencylist_path)

        projectcurrencylist.send_keys(projectcurrency)
        time.sleep(1)

        projectcurrencyselect_path =update_projectdetails.readfromXML(folder_path+'\Object\Pairwiserupdateproject.xml','eTender','Projectcurrencyselect')
        projectcurrencyselect = browser.find_element_by_xpath(projectcurrencyselect_path)
        projectcurrencyselect.click()
        time.sleep(1)

        projectappvalue_path =update_projectdetails.readfromXML(folder_path+'\Object\Pairwiserupdateproject.xml','eTender','Projectvalue2')
        projectappvalue = browser.find_element_by_xpath(projectappvalue_path)
        projectappvalue.clear()
        time.sleep(1)
        projectappvalue.send_keys(projectvalue)

        return browser

    def projectdetailscurrencydollar(self,browser,projecttype):
        update_projectdetails = DataDriver()

        projecttypeclick_path =update_projectdetails.readfromXML(folder_path+'\Object\Pairwiserupdateproject.xml','eTender','Projecttypeclick')
        projecttypeclick = browser.find_element_by_xpath(projecttypeclick_path)
        projecttypeclick.click()
        time.sleep(1)

        projecttypelist_path =update_projectdetails.readfromXML(folder_path+'\Object\Pairwiserupdateproject.xml','eTender','Projecttypelist')
        projecttypelist = browser.find_element_by_xpath(projecttypelist_path)
        projecttypelist.send_keys(projecttype)
        time.sleep(1)

        projecttypeselect_path =update_projectdetails.readfromXML(folder_path+'\Object\Pairwiserupdateproject.xml','eTender','Projecttypeselect')
        projecttypeselect = browser.find_element_by_xpath(projecttypeselect_path)
        projecttypeselect.click()
        time.sleep(1)

        projectcurrencyclick_path =update_projectdetails.readfromXML(folder_path+'\Object\Pairwiserupdateproject.xml','eTender','Projecttypeclick')
        projectcurrencyclick = browser.find_element_by_xpath(projectcurrencyclick_path)
        projectcurrencyclick.click()
        time.sleep(1)

        projectcurrencylist_path =update_projectdetails.readfromXML(folder_path+'\Object\Pairwiserupdateproject.xml','eTender','Projetcurrency')
        projectcurrencylist = browser.find_element_by_xpath(projectcurrencylist_path)

        projectcurrencylist_data =update_projectdetails.readfromXML(folder_path+'\Data\ProjectDetails.xml','eTender','projectcurrencyUS')
        projectcurrencylist.send_keys(projectcurrencylist_data)
        time.sleep(1)

        projectcurrencyselect_path =update_projectdetails.readfromXML(folder_path+'\Object\Pairwiserupdateproject.xml','eTender','Projectcurrencyselect')
        projectcurrencyselect = browser.find_element_by_xpath(projectcurrencyselect_path)
        projectcurrencyselect.click()
        time.sleep(1)

        return browser





