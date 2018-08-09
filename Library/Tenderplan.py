#-------------------------------------------------------------------------------
# Name:        LauncheTender
# Purpose:
#
# Author:      suresh.kumar
#
# Created:     12-07-2017
# Copyright:   (c) suresh.kumar 2017
# Licence:     <Causeway licence>
#-------------------------------------------------------------------------------
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time
import unittest
import sys
import os
import datetime
from datetime import timedelta
from datetime import datetime
dir_path = os.path.dirname(os.path.realpath(__file__))
folder_path=os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0,folder_path+"\Library")
sys.path.insert(0,folder_path+"\Syslibrary")
sys.path.insert(0,folder_path+"\Data")
sys.path.insert(0,folder_path+"\Object")
sys.path.insert(0,folder_path+"\Object")
sys.path.insert(0,folder_path+"\Env")
from datadriven import DataDriver
import launcheTender
class Tenderplans():
    def plantemplatemenu(self,browser):
        browser.implicitly_wait(5)
        template = DataDriver()
        time.sleep(1)
        tenderplantemplate_path = template.readfromXML(folder_path+'\Object\TenderplanObjects.xml','eTender','plantemplatelink')
        time.sleep(1)
        tenderplantemplate_link = browser.find_element_by_xpath(tenderplantemplate_path)
        time.sleep(1)
        tenderplantemplate_link.click()
        return browser

    def plantemplatebutton(self,browser):
        time.sleep(1)
        templatebutton = DataDriver()
        time.sleep(2)
        templatebutton_path = templatebutton.readfromXML(folder_path+'\Object\TenderplanObjects.xml','eTender','createtemplatebutton')
        time.sleep(2)
        templatebutton = browser.find_element_by_xpath(templatebutton_path) #Path Create template button
        time.sleep(2)
        templatebutton.click()  #Click Create template button
        return browser

    def plantemplatecreation(self,browser):
        time.sleep(1)
        templatecreation = DataDriver()
        time.sleep(1)
        templatename_path = templatecreation.readfromXML(folder_path+'\Object\TenderplanObjects.xml','eTender','templatename')
        time.sleep(1)
        templatename = browser.find_element_by_xpath(templatename_path) #Path for input template name
        time.sleep(1)

        templatename_data = templatecreation.readfromXML(folder_path+'\Data\TenderplanData.xml','eTender','templatename')
        time.sleep(1)
        templatename.send_keys(templatename_data)
        time.sleep(1)

        templatedescription_path = templatecreation.readfromXML(folder_path+'\Object\TenderplanObjects.xml','eTender','templatedescription')
        time.sleep(1)
        templatedescription = browser.find_element_by_xpath(templatedescription_path) #Path for input template description
        time.sleep(1)

        templatedescription_data = templatecreation.readfromXML(folder_path+'\Data\TenderplanData.xml','eTender','templatedescription')
        time.sleep(1)
        templatedescription.send_keys(templatedescription_data)
        time.sleep(1)
        return browser

    def templatedetialsupdation(self,browser):
        time.sleep(1)
        templatedetailsupdate = DataDriver()
        time.sleep(1)
        templatenameupdate_path = templatedetailsupdate.readfromXML(folder_path+'\Object\TenderplanObjects.xml','eTender','templatename')
        time.sleep(1)
        templatenameupdate = browser.find_element_by_xpath(templatenameupdate_path) #Path for update template name
        time.sleep(1)
        templatenameupdate.clear()

        templatenameupdate_data = templatedetailsupdate.readfromXML(folder_path+'\Data\TenderplanData.xml','eTender','templatenameupdate')
        time.sleep(1)
        templatenameupdate.send_keys(templatenameupdate_data)
        time.sleep(1)

        templatedescriptionupdate_path = templatedetailsupdate.readfromXML(folder_path+'\Object\TenderplanObjects.xml','eTender','templatedescription')
        time.sleep(1)
        templatedescriptionupdate = browser.find_element_by_xpath(templatedescriptionupdate_path) #Path for update template description
        time.sleep(1)
        templatedescriptionupdate.clear()

        templatedescriptionupdate_data = templatedetailsupdate.readfromXML(folder_path+'\Data\TenderplanData.xml','eTender','templatedescriptionupdate')
        time.sleep(1)
        templatedescriptionupdate.send_keys(templatedescriptionupdate_data)
        time.sleep(1)
        return browser

    def plantemplatesave(self,browser):
        time.sleep(1)
        templatesave1 = DataDriver()
        templatesave_path = templatesave1.readfromXML(folder_path+'\Object\TenderplanObjects.xml','eTender','templateplansave')
        time.sleep(1)
        templatesave = browser.find_element_by_xpath(templatesave_path)
        time.sleep(1)
        templatesave.click() #template save
        time.sleep(1)
        return browser

    def plantemplateupdate(self,browser):
        time.sleep(1)
        templateupdate1 = DataDriver()
        templateupdate_path = templateupdate1.readfromXML(folder_path+'\Object\TenderplanObjects.xml','eTender','templateplanupdate')
        time.sleep(1)
        templateupdate = browser.find_element_by_xpath(templateupdate_path)
        time.sleep(1)
        templateupdate.click() #template update
        time.sleep(1)
        return browser

    def plantemplateupdation(self,browser):
        time.sleep(1)
        templateupdation = DataDriver()
        templateupdation_path = templateupdation.readfromXML(folder_path+'\Object\TenderplanObjects.xml','eTender','templateedition')
        templateupdation = browser.find_element_by_xpath(templateupdation_path)
        time.sleep(1)
        templateupdation.click() #template updation
        time.sleep(1)
        return browser

    def plantemplateupdateduration(self,browser):
        time.sleep(1)
        templateduration1 = DataDriver()
        templateduration = []
        templateduration1_path = templateduration1.readfromXML(folder_path+'\Object\TenderplanObjects.xml','eTender','templateduration')
        templateduration = browser.find_elements_by_xpath(templateduration1_path)
        time.sleep(1)
        #print len(templateduration)
        counter1 = 0
        #for counter1 in range(counter1,len(templateduration)):
        for counter1 in range(counter1,7):
                try:
                    templateduration_path = templateduration1.readfromXML(folder_path+'\Object\TenderplanObjects.xml','eTender','templateduration')
                    templateduration = browser.find_elements_by_xpath(templateduration_path)

                    templateduration_data = templateduration1.readfromXML(folder_path+'\Data\TenderplanData.xml','eTender','Stag1')
                    templateduration[counter1].clear()
                    time.sleep(1)
                    templateduration[counter1].send_keys(templateduration_data)
                    counter1 = counter1 + 1
                    time.sleep(2)
                except:
                    print("not entered")
        return browser

    def plantemplateselection(self,browser):
        time.sleep(1)
        templateselection1 = DataDriver()
        templateselection = []
        templateselection_path = templateselection1.readfromXML(folder_path+'\Object\TenderplanObjects.xml','eTender','templateplanselection')
        templateselection = browser.find_elements_by_xpath(templateselection_path)
        time.sleep(1)
        templateselection[1].click() #template selection
        time.sleep(1)
        return browser

    def plantemplateselectionfromlist(self,browser):
        time.sleep(1)
        templateselection1 = DataDriver()
        templateselection = []
        templateselection_path = templateselection1.readfromXML(folder_path+'\Object\TenderplanObjects.xml','eTender','tenderplantender')
        templateselection = browser.find_elements_by_xpath(templateselection_path)
        #print templateselection
        time.sleep(7)
        templateselection[2].click() #template selection
        time.sleep(1)
        return browser

    def tendereselection(self,browser):
        time.sleep(1)
        tendereselection1 = DataDriver()
        tendereselection = []
        tendereselection_path = tendereselection1.readfromXML(folder_path+'\Object\TenderplanObjects.xml','eTender','templateplanselection')
        tendereselection = browser.find_elements_by_xpath(tendereselection_path)
        time.sleep(1)
        tendereselection[2].click() #tender selection
        time.sleep(1)
        return browser

    def autofillselect(self,browser):
        time.sleep(1)
        selectautofill1 = DataDriver()
        selectautofil_path = selectautofill1.readfromXML(folder_path+'\Object\TenderplanObjects.xml','eTender','selectautofill')
        selectautofil = browser.find_element_by_xpath(selectautofil_path)
        time.sleep(1)
        selectautofil.click() #select autofill button
        time.sleep(1)
        return browser

    def datepickerselectforautofill(self,browser):
        time.sleep(1)
        datepickerselect1 = DataDriver()
        #datepickerselect = []
        datepickerselect_path = datepickerselect1.readfromXML(folder_path+'\Object\TenderplanObjects.xml','eTender','datepickerselect')
        datepickerselect = browser.find_element_by_xpath(datepickerselect_path)
        time.sleep(2)
        datepickerselect.click() #date picker click
        time.sleep(1)
        return browser

##    def selectstartdateasforecast(self,browser):
##        time.sleep(1)
##        datepickerselect1 = DataDriver()
##        dateselect1 = []
##        todaysdate = datetime.today().strftime('%d-%b-%Y')
##        print todaysdate
##        time.sleep(2)
##        if todaysdate == '12-Nov-2017':
##            dateselect_path = datepickerselect1.readfromXML(folder_path+'\Object\TenderplanObjects.xml','eTender','dateselect')
##            dateselect = browser.find_element_by_xpath(dateselect_path)
##            time.sleep(1)
##            dateselect.click() #forecast date select
##            time.sleep(1)
##        else:
##            dateselect1_path = datepickerselect1.readfromXML(folder_path+'\Object\TenderplanObjects.xml','eTender','dateselect1')
##            dateselect1 = browser.find_elements_by_xpath(dateselect1_path)
##            time.sleep(1)
##            dateselect1[11].click() #forecast date select
##            time.sleep(1)
##        return browser

    def selectstartdateasforecast(self,browser):
        time.sleep(1)
        datepickerselect1 = DataDriver()
        #dateselect1 = []
        #todaysdate = datetime.today().strftime('%d-%b-%Y')
        #print todaysdate
        time.sleep(2)

        dateselect_path = datepickerselect1.readfromXML(folder_path+'\Object\TenderplanObjects.xml','eTender','dateselect')
        dateselect = browser.find_element_by_xpath(dateselect_path)
        time.sleep(1)
        dateselect.click() #forecast date select
        return browser

    def selectduedateasforecast(self,browser):
        time.sleep(1)
        datepickerselect1 = DataDriver()
        dateselect1 = []
        todaysdate = datetime.today().strftime('%d-%b-%Y')
        #print todaysdate
        time.sleep(1)
        if todaysdate == '28-July-2018':
            dateselect_path = datepickerselect1.readfromXML(folder_path+'\Object\TenderplanObjects.xml','eTender','dateselect')
            dateselect = browser.find_element_by_xpath(dateselect_path)
            time.sleep(1)
            dateselect.click() #forecast date select
            time.sleep(1)
        else:
            dateselect1_path = datepickerselect1.readfromXML(folder_path+'\Object\TenderplanObjects.xml','eTender','dateselect1')
            dateselect1 = browser.find_elements_by_xpath(dateselect1_path)
            time.sleep(1)
            dateselect1[26].click() #forecast date select
            time.sleep(1)
        return browser



    def selectforecastenddateradiobutton(self,browser):
        time.sleep(1)
        radiobutton1 = DataDriver()
        radiobutton = []
        radiobutton_path = radiobutton1.readfromXML(folder_path+'\Object\TenderplanObjects.xml','eTender','radiobutton')
        radiobutton = browser.find_elements_by_xpath(radiobutton_path)
        time.sleep(1)
        radiobutton[1].click()
        return browser

    def forecastdatesave(self,browser):
        time.sleep(1)
        savedetails1 = DataDriver()
        savedetails = []
        savedetails_path = savedetails1.readfromXML(folder_path+'\Object\TenderplanObjects.xml','eTender','savedetails')
        savedetails = browser.find_elements_by_xpath(savedetails_path)
        time.sleep(1)
        savedetails[2].click()
        return browser

    def templateclose(self,browser):
        time.sleep(1)
        templateclose1 = DataDriver()
        templateclose = []
        templateclose_path = templateclose1.readfromXML(folder_path+'\Object\TenderplanObjects.xml','eTender','templateclose')
        templateclose = browser.find_element_by_xpath(templateclose_path)
        templateclose.click()
        return browser

    def plantemplatedelete(self,browser):
        time.sleep(1)
        templatedelete = DataDriver()
        templatedelete_path = templatedelete.readfromXML(folder_path+'\Object\TenderplanObjects.xml','eTender','templateplandelete')

        templatedelete = browser.find_element_by_xpath(templatedelete_path)
        time.sleep(3)
        templatedelete.click() #template delete
        time.sleep(3)

        templatedeleteconfirm = []
        templatedelete1 = DataDriver()

        templatedeleteconfirm_path = templatedelete1.readfromXML(folder_path+'\Object\TenderplanObjects.xml','eTender','templateplandelete')
        templatedeleteconfirm = browser.find_elements_by_xpath(templatedeleteconfirm_path)
        time.sleep(3)
        templatedeleteconfirm[1].click() #template delete confirm
        time.sleep(5)
        return browser

    def plantemplatecreationwithstages(self,browser):
        time.sleep(1)
        templatecreationstages = DataDriver()
        time.sleep(1)
        templatecreationstages_path = templatecreationstages.readfromXML(folder_path+'\Object\TenderplanObjects.xml','eTender','templatecreationaddstage')
        time.sleep(1)
        templatecreationstages = browser.find_element_by_id(templatecreationstages_path) #Path for add/Remove stages
        time.sleep(1)
        templatecreationstages.click()
        time.sleep(3)
        templatecreationstages1 = DataDriver()
        selectstages_path = templatecreationstages1.readfromXML(folder_path+'\Object\TenderplanObjects.xml','eTender','selectstages1')
        time.sleep(1)
        selectstages = browser.find_elements_by_xpath(selectstages_path) #Path for select stages
        time.sleep(1)
        #selectstages.click()
        counter = 0
        for test in range(counter,7):
            selectstages[counter].click()  #Select specific stages
            time.sleep(1)
            counter = counter + 1
        time.sleep(2)
        updatestages_path = templatecreationstages1.readfromXML(folder_path+'\Object\TenderplanObjects.xml','eTender','savestages')
        time.sleep(1)
        updatestages = browser.find_element_by_id(updatestages_path) #Path for update stages
        time.sleep(1)
        updatestages.click()
        time.sleep(1)
        return browser

    def estimatortenderpalntender(self,browser):
        time.sleep(1)
        tenderplan_tender = DataDriver()
        tenderplantender = []
        time.sleep(1)
        tenderplantender_path = tenderplan_tender.readfromXML(folder_path+'\Object\TenderplanObjects.xml','eTender','tenderplan')
        time.sleep(1)
        #tenderplantender = browser.find_elements_by_xpath(tenderplantender_path) #Path for Tender details list
        tenderplantender = browser.find_element_by_xpath(tenderplantender_path) #Path for Tender details list
        time.sleep(3)
        #tenderplantender[2].click()
        tenderplantender.click()
        return browser

    def estimatortenderplan(self,browser):
        time.sleep(1)
        tenderplan_XML = DataDriver()
        time.sleep(1)
        listtenderplan_path = tenderplan_XML.readfromXML(folder_path+'\Object\TenderplanObjects.xml','eTender','selecttenderplan')
        list_tenderplan = browser.find_element_by_xpath(listtenderplan_path)
        time.sleep(1)
        list_tenderplan.click()  #Click on Select plan template
        time.sleep(2)
        return browser

    def plantemplateselect(self,browser):
        time.sleep(1)
        plantemplateselect1 = DataDriver()
        time.sleep(1)
        plantemplateselect_path = plantemplateselect1.readfromXML(folder_path+'\Object\TenderplanObjects.xml','eTender','plantemplateselect')
        time.sleep(1)
        plantemplateselect = browser.find_element_by_xpath(plantemplateselect_path) #plantemplateselect
        time.sleep(1)
        plantemplateselect.click()
        return browser

    def tenderplansave(self,browser):
        time.sleep(1)
        tenderplansave1 = DataDriver()
        tenderplansave2 = []
        time.sleep(1)
        tenderplansave_path = tenderplansave1.readfromXML(folder_path+'\Object\TenderplanObjects.xml','eTender','savedetails')
        time.sleep(1)
        tenderplansave2 = browser.find_elements_by_xpath(tenderplansave_path) #plantemplateselect
        time.sleep(1)
        tenderplansave2[1].click()
        return browser

    def TenderDeletion(self,browser):
        orgLink=DataDriver()
        time.sleep(1)
        p=browser.find_elements_by_xpath(orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','TenderCheckbox'))
        time.sleep(1)
        p[3].click()
        time.sleep(1)
        delete_path = orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','DeleteBtn')
        time.sleep(1)
        delete = browser.find_element_by_xpath(delete_path)
        time.sleep(2)
        delete.click()
        time.sleep(1)
        confirmdelete_path = orgLink.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','YesBtn')
        confirmdelete = browser.find_element_by_xpath(confirmdelete_path)
        time.sleep(1)
        confirmdelete.click()
        return browser

    def stagactualdate(self,browser):
        stagactualdate1 = DataDriver()

        stagactualdate_path =stagactualdate1.readfromXML(folder_path+'\Object\TenderplanObjects.xml','eTender','actualdateclick')
        stagactualdate = browser.find_element_by_xpath(stagactualdate_path)
        time.sleep(1)
        stagactualdate.click()
        time.sleep(1)

        #stagactualdateselect1 = []

        stagactualdateselect_path =stagactualdate1.readfromXML(folder_path+'\Object\TenderplanObjects.xml','eTender','actualdateselect')
        stagactualdateselect = browser.find_element_by_xpath(stagactualdateselect_path)
        #stagactualdateselect[0].click()
        time.sleep(1)
        stagactualdateselect.click()
        time.sleep(1)

        stagactualdateselectconfirm_path =stagactualdate1.readfromXML(folder_path+'\Object\TenderplanObjects.xml','eTender','actualdateselectconfirm')
        stagactualdateselectconfirm = browser.find_element_by_xpath(stagactualdateselectconfirm_path)
        time.sleep(1)
        stagactualdateselectconfirm.click()
        return browser

    def stagereorder(self,browser):
        time.sleep(1)
        stagesreorder1 = DataDriver()
        time.sleep(1)
        stagesreorder = []
        stagesreorder_path = stagesreorder1.readfromXML(folder_path+'\Object\TenderplanObjects.xml','eTender','stagesorder')
        time.sleep(1)
        stagesreorder = browser.find_elements_by_xpath(stagesreorder_path) #Stages reorder
        #print stagesreorder[2].location
        time.sleep(1)

        #print stagesreorder[1].location
        time.sleep(1)
        actions = webdriver.common.action_chains.ActionChains(browser)
        time.sleep(3)
##        actions.click_and_hold(stagesreorder[2]).perform()
##        time.sleep(1)
        ##actions.drag_and_drop_by_offset(stagesreorder[2],stagesreorder[1])
        actions.drag_and_drop_by_offset(stagesreorder[2],500,308)
        time.sleep(3)
        actions.perform()
        time.sleep(1)
##        actions.click_and_hold(stagesreorder[2])
##        time.sleep(1)
##        #actions.perform()
##        actions.release(stagesreorder[1])
##        time.sleep(1)
##        actions.perform()
        return browser

    def gettodaydate(self):
        #todaydate = datetime.datetime.now().strftime('%d-%b-%Y')
        todaydate = datetime.now().strftime('%d-%b-%Y')
        #print todaydate
        todaydate1 = str(todaydate)
        todaydate2 = todaydate1.strip()
        #print todaydate2
        return todaydate2
        time.sleep(1)

    def plantemplateplanneddates(self,browser):
        time.sleep(1)
        templateplanneddate1 = DataDriver()
        templateplanneddate = []
        templateplanneddate_path = templateplanneddate1.readfromXML(folder_path+'\Object\TenderplanObjects.xml','eTender','templateplanneddate')
        templateplanneddate = browser.find_elements_by_xpath(templateplanneddate_path)
        time.sleep(1)
        #print len(templateplanneddate)
        duration = 10
        dateafter10days = []
        for planneddays in range(0,len(templateplanneddate)):
            try:
                add10days = datetime.now()+ timedelta(days=duration)
                dateafter10days.append(add10days.strftime('%d-%b-%Y'))
                duration = duration + 10
            except:
                print("planned dates are wrong")

        print (dateafter10days)
        return dateafter10days

    def plantemplatestartdateasforecastdate(self,browser):
        time.sleep(1)
        templateforecastdate1 = DataDriver()
        templateforecastdate = []
        templateforecastdate_path = templateforecastdate1.readfromXML(folder_path+'\Object\TenderplanObjects.xml','eTender','templateforecastdate')
        templateforecastdate = browser.find_elements_by_id(templateforecastdate_path)
        time.sleep(1)
        #print len(templateforecastdate)
        date = datetime.now().strftime('%d-%b-%Y')
        #print date
        #date = '16-Nov-2017'
        #t = datetime.datetime.strptime(date, '%d-%m-%Y')
        startdate = datetime.strptime(date, '%d-%b-%Y')
        #startdate = t.strftime('%d-%b-%Y')
        #print startdate
        duration = 10
        dateafter10days = []
        for planneddays in range(0,len(templateforecastdate)):
            try:
                add10days = startdate + timedelta(days=duration)
                dateafter10days.append(add10days.strftime('%d-%b-%Y'))
                duration = duration + 10
            except:
                print("forecast dates are wrong")

        print (dateafter10days)
        return dateafter10days

    def plantemplateduedateasforecastdate(self,browser):
        time.sleep(1)
        templateforecastdate1 = DataDriver()
        templateforecastdate = []
        templateforecastdate_path = templateforecastdate1.readfromXML(folder_path+'\Object\TenderplanObjects.xml','eTender','templateforecastdate')
        templateforecastdate = browser.find_elements_by_id(templateforecastdate_path)
        time.sleep(1)
        #print len(templateforecastdate)
        date = '28-July-2018'
        #t = datetime.datetime.strptime(date, '%d-%m-%Y')
        startdate = datetime.strptime(date, '%d-%b-%Y')
        #startdate = t.strftime('%d-%b-%Y')
        #print startdate
        duration = 10
        dateafter10days = []
        for planneddays in range(0,len(templateforecastdate)):
            try:
                add10days = startdate - timedelta(days=duration)
                dateafter10days.append(add10days.strftime('%d-%b-%Y'))
                duration = duration + 10
            except:
                print("forecast dates are wrong")

        #print dateafter10days
        return dateafter10days

    def plantemplateforecastdates(self,browser):
        time.sleep(1)
        templateforecastdate1 = DataDriver()
        templateforecastdate = []
        templateforecastdate_path = templateforecastdate1.readfromXML(folder_path+'\Object\TenderplanObjects.xml','eTender','templateforecastdate')
        templateforecastdate = browser.find_elements_by_id(templateforecastdate_path)
        time.sleep(1)
        #print len(templateforecastdate)
        duration = 10
        dateafter10days = []
        for forecastdays in range(0,len(templateforecastdate)):
            try:
                add10days = datetime.now()+ timedelta(days=duration)
                dateafter10days.append(add10days.strftime('%d-%b-%Y'))
                duration = duration + 10
            except:
                print("forecast dates are wrong")

        print (dateafter10days)
        return dateafter10days

    def stagdelete(self,browser):
        stagdelete1 = DataDriver()
        stagselect = []

        stagselect_path =stagdelete1.readfromXML(folder_path+'\Object\TenderplanObjects.xml','eTender','stagselection')
        stagselect = browser.find_elements_by_xpath(stagselect_path)
        time.sleep(1)
        stagselect[7].click()
        time.sleep(1)

        stagdelete_path =stagdelete1.readfromXML(folder_path+'\Object\TenderplanObjects.xml','eTender','stagdelete')
        stagdelete2 = browser.find_element_by_xpath(stagdelete_path)
        time.sleep(1)
        stagdelete2.click()
        time.sleep(1)

        stagdeleteconfirm_path =stagdelete1.readfromXML(folder_path+'\Object\TenderplanObjects.xml','eTender','stagdeleteconfirm')
        stagdeleteconfirm = browser.find_element_by_xpath(stagdeleteconfirm_path)
        time.sleep(1)
        stagdeleteconfirm.click()
        return browser

    def stagaddition(self,browser):
        stagaddition1 = DataDriver()

        stagaddition_path =stagaddition1.readfromXML(folder_path+'\Object\TenderplanObjects.xml','eTender','stagadd')
        stagaddition2 = browser.find_element_by_xpath(stagaddition_path)
        time.sleep(1)
        stagaddition2.click()
        time.sleep(1)

        stagselection = []

        stagselection_path =stagaddition1.readfromXML(folder_path+'\Object\TenderplanObjects.xml','eTender','stagselect')
        stagselection = browser.find_elements_by_xpath(stagselection_path)
        time.sleep(1)
        stagselection[0].click()
        time.sleep(1)

        stagselectionconfirm_path =stagaddition1.readfromXML(folder_path+'\Object\TenderplanObjects.xml','eTender','stagselectconfirm')
        stagselectionconfirm = browser.find_element_by_id(stagselectionconfirm_path)
        time.sleep(1)
        stagselectionconfirm.click()
        return browser

    def stagdurationupdate(self,browser):
        stagdurationupdate1 = DataDriver()
        stagdurationupdate2 = []

        stagdurationupdate2_path =stagdurationupdate1.readfromXML(folder_path+'\Object\TenderplanObjects.xml','eTender','durationupdate')
        stagdurationupdate2 = browser.find_elements_by_xpath(stagdurationupdate2_path)
        time.sleep(1)
        stagdurationupdate2[6].clear()
        time.sleep(1)
        stagdurationupdate2[6].click()
        time.sleep(1)

        stagdurationupdate2_data =stagdurationupdate1.readfromXML(folder_path+'\Data\TenderplanData.xml','eTender','durationupdate')
        stagdurationupdate2[6].send_keys(stagdurationupdate2_data)
        return browser

    def notesfortenderplan(self,browser):
        notesfortenderplan1 = DataDriver()

        notesfortenderplan_path =notesfortenderplan1.readfromXML(folder_path+'\Object\TenderplanObjects.xml','eTender','notesfortenderplan') #Click on Notes
        notesfortenderplan2 = browser.find_element_by_xpath(notesfortenderplan_path)
        time.sleep(1)
        notesfortenderplan2.click()
        return browser

    def addingNotesfortenderplan(self,browser,):
        browser.implicitly_wait(5)
        time.sleep(1)
        addingnotes = DataDriver()
        addingnotes_path = addingnotes.readfromXML(folder_path+'\Object\Object.xml','eTender','addingnotes')
        time.sleep(2)
        Adding_Notes = browser.find_element_by_xpath(addingnotes_path)#path for adding notes
        time.sleep(2)
        Enternotes = addingnotes.readfromXML(folder_path+'\Data\Data.xml','eTender','enternotes')
        Adding_Notes.send_keys(Enternotes)
        time.sleep(1)
        savenotes_path = addingnotes.readfromXML(folder_path+'\Object\TenderplanObjects.xml','eTender','notesfortenderplan1')
        Save_Notes = browser.find_element_by_xpath(savenotes_path) #Save button
        time.sleep(1)
        Save_Notes.click()
        #print"savenotes"
        time.sleep(2)
        return browser

    def deletenotesfortenderplan(self,browser):
        deletenotesfortenderplan1 = DataDriver()

        deletenotesfortenderplan_path = deletenotesfortenderplan1.readfromXML(folder_path+'\Object\Object.xml','eTender','addingnotes') #clear/delete notes for Tender Plan
        deletenotesfortenderplan2 = browser.find_element_by_xpath(deletenotesfortenderplan_path)
        time.sleep(1)

        deletenotesfortenderplan2.send_keys(Keys.CONTROL + "a"); # select the whole text in notes window
        time.sleep(1)
        deletenotesfortenderplan2.send_keys(Keys.DELETE);# delete selected text in notes window
        return browser

    def notesfortenderplansave(self,browser):
        notesfortenderplansave1 = DataDriver()

        notesfortenderplansave_path = notesfortenderplansave1.readfromXML(folder_path+'\Object\TenderplanObjects.xml','eTender','notessave') #Notes save for Tender Plan
        notesfortenderplansave2 = browser.find_element_by_xpath(notesfortenderplansave_path)
        time.sleep(1)
        notesfortenderplansave2.click()
        return browser

    def notesforfirststag(self,browser):
        notesforfirststag1 = DataDriver()
        notesforfirststag2 = []

        notesforfirststag_path =notesforfirststag1.readfromXML(folder_path+'\Object\TenderplanObjects.xml','eTender','notesforstag') #Click on Notes
        notesforfirststag2 = browser.find_elements_by_xpath(notesforfirststag_path)
        time.sleep(1)
        notesforfirststag2[0].click()
        return browser

    def notesforstagsave(self,browser):
        notesforstagsave1 = DataDriver()

        notesforstagsave_path = notesforstagsave1.readfromXML(folder_path+'\Object\TenderplanObjects.xml','eTender','notessaveforstag') #Notes save for Stag
        notesforstagsave2 = browser.find_element_by_xpath(notesforstagsave_path)
        time.sleep(1)
        notesforstagsave2.click()
        return browser

    def deletenotesforstag(self,browser):
        deletenotesforstag1 = DataDriver()

        deletenotesforstag_path = deletenotesforstag1.readfromXML(folder_path+'\Object\Object.xml','eTender','addingnotes') #clear/delete notes for stag
        deletenotesforstag2 = browser.find_element_by_xpath(deletenotesforstag_path)
        time.sleep(1)

        deletenotesforstag2.send_keys(Keys.CONTROL + "a"); # select the whole text in notes window
        time.sleep(1)
        deletenotesforstag2.send_keys(Keys.DELETE);# delete selected text in notes window
        return browser

    def resetplanned(self,browser):
        resetplanned1 = DataDriver()

        resetplanned_path =resetplanned1.readfromXML(folder_path+'\Object\TenderplanObjects.xml','eTender','resetplanned')
        resetplanned2 = browser.find_element_by_xpath(resetplanned_path)
        time.sleep(1)
        resetplanned2.click()
        time.sleep(1)

        resetplannedconfirm_path =resetplanned1.readfromXML(folder_path+'\Object\TenderplanObjects.xml','eTender','resetplannedconfirm')
        resetplannedconfirm = browser.find_element_by_xpath(resetplannedconfirm_path)
        time.sleep(1)
        resetplannedconfirm.click()
        time.sleep(1)
        return browser

    def stagforecastdate(self,browser):
        stagforecastdate1 = DataDriver()
        stagforecastdate = []

        stagforecastdate_path =stagforecastdate1.readfromXML(folder_path+'\Object\TenderplanObjects.xml','eTender','actualdateclick')
        stagforecastdate = browser.find_elements_by_xpath(stagforecastdate_path)
        time.sleep(1)
        stagactualdate[1].click()
        time.sleep(1)

        #stagactualdateselect1 = []

        stagactualdateselect_path =stagactualdate1.readfromXML(folder_path+'\Object\TenderplanObjects.xml','eTender','actualdateselect')
        stagactualdateselect = browser.find_element_by_xpath(stagactualdateselect_path)
        #stagactualdateselect[0].click()
        time.sleep(1)
        stagactualdateselect.click()
        time.sleep(1)

        stagactualdateselectconfirm_path =stagactualdate1.readfromXML(folder_path+'\Object\TenderplanObjects.xml','eTender','actualdateselectconfirm')
        stagactualdateselectconfirm = browser.find_element_by_xpath(stagactualdateselectconfirm_path)
        time.sleep(1)
        stagactualdateselectconfirm.click()
        return browser















