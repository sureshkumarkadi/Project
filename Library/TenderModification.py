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
    def TenderCreation(self,browser):
        time.sleep(2)
        browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','CreateTbtn')).click()
        fakeValue = Factory.create()
        Tendervalue=fakeValue.name()
        Tenderstring=str(Tendervalue)
        time.sleep(2)
        browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','TenderName')).send_keys(Tenderstring)
        browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','TenderReference')).send_keys(Tenderstring)
        browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','TenderDescription')).send_keys(Tenderstring)
        TenderType=orgLink.readfromXML(folder_path+'\Data\TenderData.xml','eTender','TradeType')
        browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','TenderType')).click()
        time.sleep(2)
        browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','TradeItem')).click()
        time.sleep(2)
        browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','startdate')).click()
        time.sleep(2)
        weekenddate = datetime.date.today().weekday()
        if weekenddate>=5:
            swbutton=browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','SSdateweekend'))
            browser.execute_script("arguments[0].scrollIntoView(true);", swbutton)
            swbutton.click()
        else:
            ssbutton=browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','SSdate'))
            browser.execute_script("arguments[0].scrollIntoView(true);", ssbutton)
            ssbutton.click()
        time.sleep(2)
        ddbutton=browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','enddate'))
        browser.execute_script("arguments[0].scrollIntoView(true);", ddbutton)
        ddbutton.click()
        time.sleep(2)
        Arrow=browser.find_elements_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','RightArrow'))
        Arrow[0].click()
        time.sleep(5)
        browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','DDdate')).click()
##        stime=datetime.datetime.now()
##        sftime=stime.strftime('%d-%b-%Y')
##        endtime=stime+datetime.timedelta(days=10)
##        endftime=endtime.strftime('%d-%b-%Y')
##        browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','TenderStartDate')).send_keys(sftime)
##        browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','TenderDueDate')).send_keys(endftime)
        sbutton=browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','SaveBtn'))
        browser.execute_script("arguments[0].scrollIntoView(true);", sbutton)
        time.sleep(2)
        sbutton.click()
        time.sleep(3)
        browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','CloseBtn')).click()
        return Tenderstring
    def TenderCreationwithProjectDate(self,browser):
        time.sleep(2)
        browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','CreateTbtn')).click()
        fakeValue = Factory.create()
        Tendervalue=fakeValue.name()
        Tenderstring=str(Tendervalue)
        browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','TenderName')).send_keys(Tenderstring)
        browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','TenderReference')).send_keys(Tenderstring)
        browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','TenderDescription')).send_keys(Tenderstring)
        TenderType=orgLink.readfromXML(folder_path+'\Data\TenderData.xml','eTender','TradeType')
        browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','TenderType')).click()
        time.sleep(2)
        browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','TradeItem')).click()
        time.sleep(2)
        browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','startdate')).click()
        time.sleep(2)
        weekenddate = datetime.date.today().weekday()
        if weekenddate>=5:
            swbutton=browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','SSdateweekend'))
            browser.execute_script("arguments[0].scrollIntoView(true);", swbutton)
            swbutton.click()
        else:
            ssbutton=browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','SSdate'))
            browser.execute_script("arguments[0].scrollIntoView(true);", ssbutton)
            ssbutton.click()
        time.sleep(2)
        ddbutton=browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','enddate'))
        browser.execute_script("arguments[0].scrollIntoView(true);", ddbutton)
        ddbutton.click()
        time.sleep(2)
        newscount=4
        Arrow=browser.find_elements_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','RightArrow'))
        browser.execute_script("arguments[0].scrollIntoView(true);", Arrow[newscount])
        Arrow[newscount].click()
        #scount=len(browser.find_elements_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','DDdateTender')))
        dddate=browser.find_elements_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','DDdateTender'))
        browser.execute_script("arguments[0].scrollIntoView(true);", dddate[3])
        dddate[3].click()
        sbutton=browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','SaveBtn'))
        browser.execute_script("arguments[0].scrollIntoView(true);", sbutton)
        time.sleep(2)
        sbutton.click()
        time.sleep(3)
        browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','CloseBtn')).click()
        return Tenderstring
    def TenderCreationwithStartDate(self,browser,value):
        global startdate
        global duedate
        time.sleep(2)
        browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','CreateTbtn')).click()
        fakeValue = Factory.create()
        Tendervalue=fakeValue.name()
        Tenderstring=str(Tendervalue)
        browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','TenderName')).send_keys(Tenderstring)
        browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','TenderReference')).send_keys(Tenderstring)
        browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','TenderDescription')).send_keys(Tenderstring)
        TenderType=orgLink.readfromXML(folder_path+'\Data\TenderData.xml','eTender','TradeType')
        browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','TenderType')).click()
        time.sleep(2)
        browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','TradeItem')).click()
        time.sleep(2)
        browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','startdate')).click()
        time.sleep(2)
        weekenddate = datetime.date.today().weekday()
        if weekenddate>=5:
            swbutton=browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','SSdateweekend'))
            browser.execute_script("arguments[0].scrollIntoView(true);", swbutton)
            swbutton.click()
        else:
            ssbutton=browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','SSdate'))
            browser.execute_script("arguments[0].scrollIntoView(true);", ssbutton)
            ssbutton.click()
        time.sleep(2)
        ddbutton=browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','enddate'))
        browser.execute_script("arguments[0].scrollIntoView(true);", ddbutton)
        time.sleep(2)
        ddbutton.click()
        browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','RightArrow')).click()
        browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','DDdate')).click()
        time.sleep(2)
        self.startdate=browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','StartdateText')).get_attribute('value')
        self.duedate=browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','DueDateText')).get_attribute('value')
        p=browser.find_elements_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','ForeStartButton'))
        p[value].click()
        sbutton=browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','SaveBtn'))
        browser.execute_script("arguments[0].scrollIntoView(true);", sbutton)
        time.sleep(2)
        sbutton.click()
        time.sleep(3)
        browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','CloseBtn')).click()
        return Tenderstring

    def TenderCreationforstartdate(self,browser):
        time.sleep(2)
        browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','CreateTbtn')).click()
        fakeValue = Factory.create()
        Tendervalue=fakeValue.name()
        Tenderstring=str(Tendervalue)
        browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','TenderName')).send_keys(Tenderstring)
        browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','TenderReference')).send_keys(Tenderstring)
        browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','TenderDescription')).send_keys(Tenderstring)
        TenderType=orgLink.readfromXML(folder_path+'\Data\TenderData.xml','eTender','TradeType')
        browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','TenderType')).click()
        time.sleep(2)
        browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','TradeItem')).click()
        time.sleep(2)
        browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','startdate')).click()
        time.sleep(2)
        weekenddate = datetime.date.today().weekday()
        if weekenddate>=5:
            browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','startdateforecastasweekdate')).click()
        else:
            browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','startdateforecast')).click()

        startdate_path = orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','startdateforecastselection')
        startdate = browser.find_element_by_xpath(startdate_path)

        ddbutton=browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','enddate'))
        browser.execute_script("arguments[0].scrollIntoView(true);", ddbutton)
        time.sleep(2)
        ddbutton.click()
        browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','RightArrow')).click()
        browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','DDdate')).click()
        forecastdate = []
        forecastdate_path = orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','startdateforecastselection')
        forecastdate = browser.find_elements_by_xpath(forecastdate_path)
        forecastdate[0].click()
        time.sleep(1)
        sbutton=browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','SaveBtn'))
        browser.execute_script("arguments[0].scrollIntoView(true);", sbutton)
        time.sleep(2)
        sbutton.click()
        time.sleep(3)
        browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','CloseBtn')).click()
        return Tenderstring



    def TenderCreationforduedate(self,browser):
        time.sleep(2)
        browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','CreateTbtn')).click()
        fakeValue = Factory.create()
        Tendervalue=fakeValue.name()
        Tenderstring=str(Tendervalue)
        browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','TenderName')).send_keys(Tenderstring)
        browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','TenderReference')).send_keys(Tenderstring)
        browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','TenderDescription')).send_keys(Tenderstring)
        TenderType=orgLink.readfromXML(folder_path+'\Data\TenderData.xml','eTender','TradeType')
        browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','TenderType')).click()
        time.sleep(2)
        browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','TradeItem')).click()
        time.sleep(2)
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
        ddbutton.click()
        time.sleep(1)
        browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','duedateforecast')).click()
        forecastdate = []
        forecastdate_path = orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','startdateforecastselection')
        forecastdate = browser.find_elements_by_xpath(forecastdate_path)
        forecastdate[1].click()

        sbutton=browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','SaveBtn'))
        browser.execute_script("arguments[0].scrollIntoView(true);", sbutton)
        time.sleep(2)
        sbutton.click()
        time.sleep(3)
        browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','CloseBtn')).click()
        return Tenderstring

    def ProjectCreation(self,browser):
        time.sleep(2)
        fake = Factory.create()
        fakevalue=fake.name()
        PString=str(fakevalue)
        browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','CreateProject')).click()
        browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','ProjectName')).send_keys(PString)
        browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','ProjReference')).send_keys(PString)
        time.sleep(2)
        sbutton=browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','SaveBtn'))
        browser.execute_script("arguments[0].scrollIntoView(true);", sbutton)
        time.sleep(2)
        sbutton.click()
        time.sleep(2)
        return PString
    def ProjectCreationWithdate(self,browser):
        time.sleep(2)
        fake = Factory.create()
        fakevalue=fake.name()
        PString=str(fakevalue)
        browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','CreateProject')).click()
        browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','ProjectName')).send_keys(PString)
        browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','ProjReference')).send_keys(PString)
        time.sleep(2)
        browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','startdate')).click()
        time.sleep(2)
        weekenddate = datetime.date.today().weekday()
        if weekenddate>=5:
            browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','SSdateweekend')).click()
        else:
            browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','startdateforecast')).click()
        ddbutton=browser.find_element_by_id(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','DueDatePro'))
        browser.execute_script("arguments[0].scrollIntoView(true);", ddbutton)
        time.sleep(2)
        ddbutton.click()
        time.sleep(2)
        browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','RightArrowDuedate')).click()
        browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','DDdate')).click()
        time.sleep(2)
        sbutton=browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','SaveBtn'))
        browser.execute_script("arguments[0].scrollIntoView(true);", sbutton)
        time.sleep(2)
        sbutton.click()
        time.sleep(2)
        return PString

    def TenderDeletion(self,browser,tenderName):
        time.sleep(3)
        p=browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','tenderSearch'))
        p.send_keys(tenderName)
        time.sleep(2)
        browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','updateTender')).click()
        time.sleep(2)
        Deletebutton=browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','DeleteBtn'))
        browser.execute_script("arguments[0].scrollIntoView(true);", Deletebutton)
        time.sleep(2)
        Deletebutton.click()
        browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','YesBtn')).click()
        time.sleep(1)
        p1=browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','tenderSearch'))
        p1.send_keys(tenderName)
    def OpenProject(self,ProjName,browser):
        browser.find_element_by_link_text(ProjName).click()

    def OpenProjectList(browser,self):
        browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\Object.xml','eTender','projectlistmenu')).click()

    def TenderUpdation(self,TenderName,browser):
        UpTenderName=TenderName+'new'
        p=browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','tenderSearch'))
        p.send_keys(TenderName)
        time.sleep(2)
        browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','updateTender')).click()
        time.sleep(2)
        browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','TenderName')).clear()
        browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','TenderName')).send_keys(UpTenderName)
        browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','TenderReference')).clear()
        browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','TenderReference')).send_keys(UpTenderName)
        time.sleep(2)
        stime=datetime.datetime.now()
        sftime=stime.strftime('%d-%b-%Y')
        endtime=stime+datetime.timedelta(days=10)
        endftime=endtime.strftime('%d-%b-%Y')
        browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','TenderStartDate')).send_keys(sftime)
        browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','TenderDueDate')).send_keys(endftime)
        time.sleep(2)
        ubutton=browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','UpdateBtn'))
        browser.execute_script("arguments[0].scrollIntoView(true);", ubutton)
        time.sleep(2)
        ubutton.click()
        return UpTenderName

    #Function for Back to tenderlist
    def BacktoTenderList(self,browser,TenderName):
        p=browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','tenderSearch'))
        p.send_keys(TenderName)
        time.sleep(2)
        browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','updateTender')).click()
        time.sleep(2)
        backbutton=browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','BackToList'))
        browser.execute_script("arguments[0].scrollIntoView(true);", backbutton)
        time.sleep(2)
        backbutton.click()

    #Function for resetting tender
    def ResetTender(self,browser,TenderName):
        NewTenderName=TenderName+'new'
        p=browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','tenderSearch'))
        p.send_keys(TenderName)
        time.sleep(2)
        browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','updateTender')).click()
        time.sleep(2)
        browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','TenderName')).clear()
        browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','TenderName')).send_keys(NewTenderName)
        time.sleep(2)
        browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','TenderReference')).clear()
        browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','TenderReference')).send_keys(NewTenderName)
        time.sleep(2)
        rbutton=browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','ResetBtn'))
        browser.execute_script("arguments[0].scrollIntoView(true);", rbutton)
        time.sleep(2)
        rbutton.click()
        time.sleep(3)
        TenderNameText=browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','TenderName')).get_attribute('value')
        TenderRefText=browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','TenderReference')).get_attribute('value')
        assert(TenderName==TenderNameText)
        assert(TenderName==TenderRefText)

    def OpenLookup(self,browser):
        #browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','SupplierBtn')).click()
        browser.find_element_by_link_text(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','SupplierBtn')).click()
        time.sleep(2)
        browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','AddSupplierBtn')).click()

    def OpenTenderPlan(self,browser):
        browser.find_element_by_link_text(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','PlanBtn')).click()

    def SearchTender(self,TenderValue,browser):
        browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','TenderSearchBox')).clear()
        browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','TenderSearchBox')).send_keys(TenderValue)

    def OpenDetails(self,browser,TenderName):
        browser.find_element_by_link_text(TenderName).click()












































