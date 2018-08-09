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
#sys.path.insert(0,folder_path+"\Estimatorvalue")
sys.path.insert(0,folder_path+"\Env")
from datadriven import DataDriver
import launcheTender
class Tenderdetails():
    def Subcontratorproject(self,browser):
        browser.implicitly_wait(5)
        projects_XML = DataDriver()
        time.sleep(1)
        projects_path = projects_XML.readfromXML(folder_path+'\Object\Object.xml','eTender','projectlist')
        #print projects_path
        time.sleep(1)
        project_link = browser.find_element_by_link_text(projects_path)
        #print project_link
        time.sleep(2)
        project_link.click()
        return browser

    def SubcontratorprojectPtrade(self,browser):
        browser.implicitly_wait(5)
        projects_XML = DataDriver()
        time.sleep(1)
        projects_path = projects_XML.readfromXML(folder_path+'\Object\Object.xml','eTender','projectlistPtrade')
        #print projects_path
        time.sleep(1)
        project_link = browser.find_element_by_link_text(projects_path)
        #print project_link
        time.sleep(2)
        project_link.click()
        return browser

    def Selectpendingtrades(self,browser):
        browser.implicitly_wait(5)
        selectpendingtrades = DataDriver()
        time.sleep(1)
        selectpendingtrades_path = selectpendingtrades.readfromXML(folder_path+'\Object\Project.xml','eTender','selectpendingtrades')
        time.sleep(1)
        selectpendingtrades_checkbox = browser.find_element_by_xpath(selectpendingtrades_path)
        time.sleep(2)
        selectpendingtrades_checkbox.click()
        time.sleep(7)
        return browser

    def verifyColumnsinTradeList(self,browser):
        time.sleep(1)
        browser.implicitly_wait(5)
        return browser

##    def suppliertender(self,browser):
##        time.sleep(1)
##        tenderdetails_XML = DataDriver()
##        list_tenderdetails = []
##        time.sleep(1)
##        tenderdetails_path = tenderdetails_XML.readfromXML(folder_path+'\Object\Object.xml','eTender','tenderdetails')
##        list_tenderdetails = browser.find_elements_by_xpath(tenderdetails_path) #Path fot Tender details list in supplier login
##        time.sleep(1)
##        for tenderdetails in list_tenderdetails:
##         print tenderdetails.text
##        time.sleep(1)
##        list_tenderdetails[0].click()  #Clickon the supplier first Tenderdetails
##        time.sleep(2)
##        return browser

    def suppliertender(self,browser):
        time.sleep(1)
        tenderdetails_XML = DataDriver()
        list_tenderdetails = []
        time.sleep(1)
        tenderdetails_path = tenderdetails_XML.readfromXML(folder_path+'\Object\Object.xml','eTender','tenderdetailsestimator')
        list_tenderdetails = browser.find_elements_by_xpath(tenderdetails_path) #Path fot Tender details list in supplier login
        time.sleep(1)
        list_tenderdetails[3].click()  #Clickon the supplier first Tenderdetails
        time.sleep(2)
        return browser

    def suppliersecondtender(self,browser):
        time.sleep(1)
        tenderdetails_XML = DataDriver()
        list_tenderdetails = []
        time.sleep(1)
        tenderdetails_path = tenderdetails_XML.readfromXML(folder_path+'\Object\Object.xml','eTender','tenderdetailsestimator')
        list_tenderdetails = browser.find_elements_by_xpath(tenderdetails_path) #Path fot Tender details list in supplier login
        time.sleep(1)
        list_tenderdetails[4].click()  #Clickon the supplier second Tenderdetails
        time.sleep(2)
        return browser

    def supplierdetailsfromtender(self,browser):
        time.sleep(1)
        supplierdetailsfromtender_XML = DataDriver()
        #list_tenderdetails = []
        time.sleep(1)
        suppliers_path = supplierdetailsfromtender_XML.readfromXML(folder_path+'\Object\Object.xml','eTender','supplierlist')
        suppliers = browser.find_elements_by_xpath(suppliers_path) #Path fot Tender details list in supplier login
        time.sleep(1)
        suppliers[0].click()  #Clickon the first supplier Icon
        time.sleep(2)
        return browser

    def editmessageinEditor(self,browser):
        time.sleep(1)
        editor_XML = DataDriver()
        sendmessage_path = editor_XML.readfromXML(folder_path+'\Object\Object.xml','eTender','sendmessage')
        time.sleep(1)
        sendmessage_button = browser.find_element_by_xpath(sendmessage_path)
        sendmessage_button.click()
        time.sleep(1)
        noteseditor_path = editor_XML.readfromXML(folder_path+'\Object\Object.xml','eTender','notesinsendmessage')
        time.sleep(1)
        noteseditor = browser.find_element_by_xpath(noteseditor_path)
        noteseditordetails = editor_XML.readfromXML(folder_path+'\Data\Data.xml','eTender','itemdetails')
        time.sleep(1)
        noteseditor.send_keys(noteseditordetails)
        time.sleep(1)
        return browser

    def sendmessagetoEstimator(self,browser):
        sendbutton_XML = DataDriver()
        time.sleep(1)
        sendbutton_path = sendbutton_XML.readfromXML(folder_path+'\Object\Object.xml','eTender','sendbutton')
        time.sleep(1)
        sendbutton = browser.find_element_by_xpath(sendbutton_path)
        sendbutton.click()
        return browser

    def clearmessageineditor(self,browser):
        clearbutton_XML = DataDriver()
        time.sleep(1)
        clearbutton_path = clearbutton_XML.readfromXML(folder_path+'\Object\Object.xml','eTender','clearbutton')
        time.sleep(1)
        clearbutton = browser.find_element_by_xpath(clearbutton_path)
        clearbutton.click()
        return browser

    def backtotenderdetailswindow(self,browser):
        closewindow_XML = DataDriver()
        time.sleep(1)
        backtotenderdetails_path = closewindow_XML.readfromXML(folder_path+'\Object\Object.xml','eTender','backtotenderdetails')
        time.sleep(1)
        backtotenderdetails = browser.find_element_by_xpath(backtotenderdetails_path)
        backtotenderdetails.click()
        return browser

    def unratedItems(self,browser):
        time.sleep(1)
        unratedItems_XML = DataDriver()
        unratedItems_path = unratedItems_XML.readfromXML(folder_path+'\Object\Object.xml','eTender','unrated')
        time.sleep(1)
        unratedItems_button = browser.find_element_by_xpath(unratedItems_path)
        unratedItems_button.click()
        return browser

    def tenderItemslist(self,browser):
        rates_XML = DataDriver()
        rates = []
        rate1 = rates_XML.readfromXML(folder_path+'\Data\Data.xml','eTender','rate1')
        #print rate1
        time.sleep(1)
        rate2 = rates_XML.readfromXML(folder_path+'\Data\Data.xml','eTender','rate2')
        #print rate2
        time.sleep(1)
        rate3 = rates_XML.readfromXML(folder_path+'\Data\Data.xml','eTender','rate3')
        #print rate3
        time.sleep(1)
        browser.implicitly_wait(5)
        rates_path = rates_XML.readfromXML(folder_path+'\Object\Object.xml','eTender','rates')
        rates = browser.find_elements_by_xpath(rates_path)  # Xpath for rate and Columns cells
        counter1 = 0
        time.sleep(1)
        #print(len(rates))
        for counter1 in range(counter1, 6):
            if(counter1 % 2 == 0):
                #print(counter1)
                time.sleep(1)
                actions = webdriver.common.action_chains.ActionChains(browser)
                actions.move_to_element(rates[counter1])
                time.sleep(1)
                actions.double_click(rates[counter1])
                actions.perform()
                try:
                    time.sleep(5)
                    insertrate_path = rates_XML.readfromXML(folder_path+'\Object\Object.xml','eTender','insertrate')
                    #print insertrate_path
                    time.sleep(3)
                    editable_rate = browser.find_element_by_xpath(insertrate_path)  #Inserting rates
                    #print editable_rate
                    time.sleep(2)
                    editable_rate.send_keys(rate1)
                    time.sleep(2)
                    counter1 = counter1 +1
                except:
                    print("Text items/Unpriced items")

        return browser

    def hoverThemousefornoteButton(self,browser):
        browser.implicitly_wait(5)
        global note_hover
        time.sleep(1)
        note_hover = []
        notes = DataDriver()
        time.sleep(1)
        note_path = notes.readfromXML(folder_path+'\Object\Object.xml','eTender','notes')
        note_hover = browser.find_elements_by_xpath(note_path) #Xpath for hover
        time.sleep(3)
        hover = webdriver.common.action_chains.ActionChains(browser)
        hover.move_to_element(note_hover[4])
        time.sleep(1)
        hover.perform()
        return browser

    def dialogueBoxtoAddaNote(self,browser):
        time.sleep(1)
        browser.implicitly_wait(5)
        time.sleep(2)
        note_hover[4].click()
        return browser

    def addingNotes(self,browser,):
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
        savenotes_path = addingnotes.readfromXML(folder_path+'\Object\Object.xml','eTender','savenotes')
        Save_Notes = browser.find_element_by_xpath(savenotes_path) #Save button
        time.sleep(1)
        Save_Notes.click()
        time.sleep(2)
        return browser

    def updatingNotesfortenderplan(self,browser,):
        browser.implicitly_wait(5)
        time.sleep(1)
        updatingnotes = DataDriver()
        addingnotes_path = updatingnotes.readfromXML(folder_path+'\Object\Object.xml','eTender','addingnotes')
        time.sleep(1)
        updating_Notes = browser.find_element_by_xpath(addingnotes_path)#path for adding notes
        time.sleep(1)
        updatenotes = updatingnotes.readfromXML(folder_path+'\Data\Data.xml','eTender','updateenternotes')
        updating_Notes.send_keys(updatenotes)
        time.sleep(1)
        savenotes_path = updatingnotes.readfromXML(folder_path+'\Object\Object.xml','eTender','savenotestenderplan')
        Save_Notes = browser.find_element_by_xpath(savenotes_path) #Save button
        time.sleep(1)
        Save_Notes.click()
        time.sleep(2)
        return browser

    def updatingNotes(self,browser,):
        browser.implicitly_wait(5)
        time.sleep(1)
        updatingnotes = DataDriver()
        addingnotes_path = updatingnotes.readfromXML(folder_path+'\Object\Object.xml','eTender','addingnotes')
        time.sleep(1)
        updating_Notes = browser.find_element_by_xpath(addingnotes_path)#path for adding notes
        time.sleep(1)
        updatenotes = updatingnotes.readfromXML(folder_path+'\Data\Data.xml','eTender','updateenternotes')
        updating_Notes.send_keys(updatenotes)
        time.sleep(1)
        savenotes_path = updatingnotes.readfromXML(folder_path+'\Object\Object.xml','eTender','savenotes')
        Save_Notes = browser.find_element_by_xpath(savenotes_path) #Save button
        time.sleep(1)
        Save_Notes.click()
        time.sleep(2)
        return browser

    def deleteNotes(self,browser):
        browser.implicitly_wait(5)
        enteredNotes = DataDriver()
        time.sleep(1)
        click_notesbubble1 = []
        clicknotesbubble_path = enteredNotes.readfromXML(folder_path+'\Object\Object.xml','eTender','clicknotesbubble')
        click_notesbubble1 = browser.find_elements_by_xpath(clicknotesbubble_path) #Click on Notes bubble
        click_notesbubble1[4].click()
        time.sleep(1)
        enterednotes_path = enteredNotes.readfromXML(folder_path+'\Object\Object.xml','eTender','addingnotes') #finding notes
        find_notes = browser.find_element_by_xpath(enterednotes_path) #Webelement for entered notes
        #print find_notes.text
        time.sleep(1)
        find_notes.send_keys(Keys.CONTROL + "a"); # select the whole text in notes window
        time.sleep(1)
        find_notes.send_keys(Keys.DELETE);# delete selected text in notes window
        time.sleep(1)
        savenotes_path = enteredNotes.readfromXML(folder_path+'\Object\Object.xml','eTender','savenotes')
        Save_Notes = browser.find_element_by_xpath(savenotes_path) #Save button
        time.sleep(1)
        Save_Notes.click()
        return browser

    def Actionslist(self,browser):
        browser.implicitly_wait(2)
        actionslist1 = DataDriver()
        actionslist = []
        time.sleep(1)
        actionslist_path = actionslist1.readfromXML(folder_path+'\Object\Object.xml','eTender','actionslist')
        actionslist = browser.find_elements_by_xpath(actionslist_path) #Clicking Upload my document button
        time.sleep(1)
        actionslist[1].click()
        return browser

    def tenderdocument(self,browser):
        browser.implicitly_wait(2)
        tenderdoc = DataDriver()
        time.sleep(1)
        tenderdoc_path = tenderdoc.readfromXML(folder_path+'\Object\Object.xml','eTender','tendererdocument')
        uploaddoc = browser.find_element_by_xpath(tenderdoc_path) #Clicking Upload my document button
        time.sleep(1)
        uploaddoc.click()
        return browser

    def uploadTendererdocument(self,browser):
        browser.implicitly_wait(2)
        uploaddoc = DataDriver()
        time.sleep(1)
        uploaddoc_path = uploaddoc.readfromXML(folder_path+'\Object\Object.xml','eTender','adddocument')
        for adddocuments in range(0,2):
            time.sleep(5)
            adddocument = browser.find_element_by_xpath(uploaddoc_path) #Clicking Add document
            time.sleep(5)
            adddocument.click()
            time.sleep(5)
            #os.system('E:\AutoIt3\SciTE\Script.exe') #This is AUToIT script for Upload a Document(Note:selenium not supporting uploading a document from windows hence we need to install AUTOIT to upload a document)
            os.system(folder_path+'\Env\FileUpload.exe') #This is AUToIT script for Upload a Document(Note:selenium not supporting uploading a document from windows hence we need to install AUTOIT to upload a document)
            time.sleep(5)
        return browser

    def closedocumentwindow(self,browser):
        closewindow = DataDriver()
        time.sleep(1)
        closewindow_path = closewindow.readfromXML(folder_path+'\Object\Object.xml','eTender','closewindow')
        time.sleep(1)
        close = browser.find_element_by_xpath(closewindow_path) #Clicking on Close button
        time.sleep(1)
        close.click()
        return browser

    def deletedocuments(self,browser):
        browser.implicitly_wait(2)
        deletedoc = DataDriver()
        time.sleep(1)
        deletedoc_path = deletedoc.readfromXML(folder_path+'\Object\Object.xml','eTender','delete')
        for deletedocs in range(0,3):
            delete_link = browser.find_element_by_xpath(deletedoc_path) #Delete option
            delete_link.click()
            time.sleep(1)
            confirmdeletedoc_path = deletedoc.readfromXML(folder_path+'\Object\Object.xml','eTender','deletedoc')
            confirm_delete_link = browser.find_element_by_xpath(confirmdeletedoc_path) #Confirm Delete option
            time.sleep(1)
            confirm_delete_link.click()
            time.sleep(1)
        closewindow_path = deletedoc.readfromXML(folder_path+'\Object\Object.xml','eTender','closewindow')
        time.sleep(1)
        close = browser.find_element_by_xpath(closewindow_path) #Clicking on Close button
        time.sleep(1)
        close.click()
        return browser
        time.sleep(2)

    def estimatorProject(self,browser):
        browser.implicitly_wait(5)
        projects_XML = DataDriver()
        time.sleep(1)
        projects_path = projects_XML.readfromXML(folder_path+'\Object\Object.xml','eTender','projectlist')
        #print projects_path
        time.sleep(3)
        project_link = browser.find_element_by_link_text(projects_path)
        time.sleep(5)
        project_link.click()
        return browser

    def listProjectmenu(self,browser):
        browser.implicitly_wait(5)
        projectslist_XML = DataDriver()
        time.sleep(1)
        projectslist_path = projectslist_XML.readfromXML(folder_path+'\Object\Object.xml','eTender','projectlistmenu')
        time.sleep(3)
        projectmenu_link = browser.find_element_by_link_text(projectslist_path)
        time.sleep(5)
        projectmenu_link.click()
        return browser

    def viewsupplierdetails(self,browser):
        browser.implicitly_wait(5)
        supplierdetails_Pluslink = []
        supplierdetails = DataDriver()
        time.sleep(1)
        supplierdetails_path = supplierdetails.readfromXML(folder_path+'\Object\Object.xml','eTender','Pluslink')
        time.sleep(1)
        supplierdetails_Pluslink = browser.find_element_by_xpath(supplierdetails_path)
        time.sleep(1)
        supplierdetails_Pluslink.click()
        return browser

    def viewsupplierdetailsfortradex(self,browser):
        browser.implicitly_wait(5)
        supplierdetails_Pluslink = []
        supplierdetails = DataDriver()
        time.sleep(1)
        supplierdetails_path = supplierdetails.readfromXML(folder_path+'\Object\Object.xml','eTender','Pluslink')
        time.sleep(1)
        supplierdetails_Pluslink = browser.find_elements_by_xpath(supplierdetails_path)
        time.sleep(1)
        supplierdetails_Pluslink[2].click()
        return browser

    def viewtradexsupplierdetails(self,browser):
        browser.implicitly_wait(5)
        tradex_supplierdetails_Pluslink = []
        supplierdetails = DataDriver()
        time.sleep(1)
        tradex_supplierdetails_path = tradex_supplierdetails_Pluslink.readfromXML(folder_path+'\Object\Object.xml','eTender','Pluslink')
        time.sleep(1)
        tradex_supplierdetails_Pluslink = browser.find_elements_by_xpath(tradex_supplierdetails_path)
        time.sleep(1)
        tradex_supplierdetails_Pluslink[1].click()
        return browser

    def activetendersInestimator(self,browser):
        browser.implicitly_wait(5)
        activetenders = DataDriver()
        time.sleep(1)
        activetenders_path = activetenders.readfromXML(folder_path+'\Object\Object.xml','eTender','activetenders')
        time.sleep(1)
        activestatus = browser.find_element_by_xpath(activetenders_path)
        time.sleep(1)
        activestatus.click()
        return browser

    def opendocumentswindow(self,browser):
        browser.implicitly_wait(5)
        opendocumentswindow = DataDriver()
        time.sleep(1)
        opendocumentswindow_path = opendocumentswindow.readfromXML(folder_path+'\Object\Object.xml','eTender','documentcountEstimator')
        time.sleep(1)
        opendocumentswindow_link = browser.find_element_by_xpath(opendocumentswindow_path)
        time.sleep(1)
        opendocumentswindow_link.click()
        return browser

    def estimatortender(self,browser):
        time.sleep(1)
        tenderdetails_XML = DataDriver()
        list_tenderdetails = []
        time.sleep(1)
        tenderdetails_path = tenderdetails_XML.readfromXML(folder_path+'\Object\Object.xml','eTender','tenderdetailsestimator')
        list_tenderdetails = browser.find_elements_by_xpath(tenderdetails_path) #Path fot Tender details list in supplier login
        time.sleep(1)
        list_tenderdetails[2].click()  #Clickon the supplier first Tenderdetails
        time.sleep(2)
        return browser

    def estimatortender1(self,browser):
        time.sleep(1)
        tenderdetails_XML = DataDriver()
        list_tenderdetails = []
        time.sleep(1)
        tenderdetails_path = tenderdetails_XML.readfromXML(folder_path+'\Object\Object.xml','eTender','tenderdetailsestimator')
        list_tenderdetails = browser.find_elements_by_xpath(tenderdetails_path) #Path fot Tender details list in supplier login
        time.sleep(1)
        list_tenderdetails[3].click()  #Clickon the supplier second Tenderdetails
        time.sleep(2)
        return browser

    def estimatortendertradex(self,browser):
        time.sleep(1)
        tenderdetails_XML = DataDriver()
        list_tenderdetails = []
        time.sleep(1)
        tenderdetails_path = tenderdetails_XML.readfromXML(folder_path+'\Object\Object.xml','eTender','tenderdetailsestimator')
        list_tenderdetails = browser.find_elements_by_xpath(tenderdetails_path) #Path fot Tender details list in supplier login
        time.sleep(1)
        list_tenderdetails[4].click()  #Clickon the supplier third Tenderdetails
        time.sleep(2)
        return browser

    def estimatortender2(self,browser):
        time.sleep(1)
        tenderdetails_XML = DataDriver()
        list_tenderdetails = []
        time.sleep(1)
        tenderdetails_path = tenderdetails_XML.readfromXML(folder_path+'\Object\Object.xml','eTender','tenderdetailsestimator')
        list_tenderdetails = browser.find_elements_by_xpath(tenderdetails_path) #Path fot Tender details list in supplier login
        time.sleep(1)
        list_tenderdetails[5].click()  #Clickon the supplier fourth Tenderdetails
        time.sleep(2)
        return browser

    def estimatortenderAPI(self,browser):
        time.sleep(1)
        tenderdetails_XML = DataDriver()
        list_tenderdetails = []
        time.sleep(2)
        tenderdetails_path = tenderdetails_XML.readfromXML(folder_path+'\Object\Object.xml','eTender','tenderdetailsestimator')
        time.sleep(2)
        list_tenderdetails = browser.find_elements_by_xpath(tenderdetails_path) #Path for Selecting Tender details list
        #print list_tenderdetails
        time.sleep(2)
        list_tenderdetails[0].click()  #Select from dropdown list
        time.sleep(2)

        #input_tenderdetails = []
        time.sleep(2)
        inputtenderdetails_path = tenderdetails_XML.readfromXML(folder_path+'\Object\Object.xml','eTender','inputtenderdetails')
        time.sleep(2)
        input_tenderdetails = browser.find_element_by_xpath(inputtenderdetails_path) #Path input Tender details
        #print input_tenderdetails
        time.sleep(3)
        input_tenderdetails.click()
        time.sleep(1)

        inputtenderdetails_data = tenderdetails_XML.readfromXML(folder_path+'\Data\Data.xml','eTender','details')
        time.sleep(1)
        input_tenderdetails.send_keys(inputtenderdetails_data)
        time.sleep(1)

        time.sleep(1)
        selecttenderdetails_path = tenderdetails_XML.readfromXML(folder_path+'\Object\Object.xml','eTender','selectdetails')
        time.sleep(1)
        select_tenderdetails = browser.find_element_by_xpath(selecttenderdetails_path) #Path for selecting Details from drop down list
        #print select_tenderdetails
        time.sleep(1)
        select_tenderdetails.click()
        time.sleep(1)
        return browser

    def estimatoritemdefault(self,browser):
        time.sleep(1)
        tenderdetails_XML = DataDriver()
        list_tenderdetails = []
        time.sleep(2)
        tenderdetails_path = tenderdetails_XML.readfromXML(folder_path+'\Object\Object.xml','eTender','tenderdetailsestimator')
        time.sleep(2)
        list_tenderdetails = browser.find_elements_by_xpath(tenderdetails_path) #Path for Selecting  Tender plan from list
        #print list_tenderdetails
        time.sleep(2)
        list_tenderdetails[2].click()  #Select from dropdown list
        time.sleep(2)

        input_tenderdetails = []
        time.sleep(2)
        inputtenderdetails_path = tenderdetails_XML.readfromXML(folder_path+'\Object\Object.xml','eTender','inputtenderdetails')
        time.sleep(2)
        input_tenderdetails = browser.find_elements_by_xpath(inputtenderdetails_path) #Path input Details
        #print input_tenderdetails
        time.sleep(2)
        input_tenderdetails[2].click()
        time.sleep(1)

        inputtenderdetails_data = tenderdetails_XML.readfromXML(folder_path+'\Data\Data.xml','eTender','details')
        time.sleep(1)
        input_tenderdetails[2].send_keys(inputtenderdetails_data)
        time.sleep(1)

        time.sleep(1)
        selecttenderdetails_path = tenderdetails_XML.readfromXML(folder_path+'\Object\Object.xml','eTender','selectdetails')
        time.sleep(1)
        select_tenderdetails = browser.find_element_by_xpath(selecttenderdetails_path) #Path for selecting details from drop down list
        #print select_tenderdetails
        time.sleep(1)
        select_tenderdetails.click()
        time.sleep(1)
        return browser

    def estimatortradexsupplier(self,browser):
        time.sleep(1)
        tenderdetails_XML = DataDriver()
        list_tenderdetails = []
        time.sleep(2)
        tenderdetails_path = tenderdetails_XML.readfromXML(folder_path+'\Object\Object.xml','eTender','tradexsupplier')
        time.sleep(2)
        list_tenderdetails = browser.find_elements_by_xpath(tenderdetails_path) #Path for Add Supplier
        time.sleep(2)
        for tenderdetails in list_tenderdetails:
         print (tenderdetails.text)
        time.sleep(3)
        list_tenderdetails[1].click()  #Select Add Supplier from dropdown list
        time.sleep(2)
        return browser

    def entersupplier(self,browser):
        time.sleep(1)
        tradexsupplier_XML = DataDriver()
        list_tradexsupplier = []
        time.sleep(1)
        tradexsupplier_path = tradexsupplier_XML.readfromXML(folder_path+'\Object\Object.xml','eTender','tradexsupplierinput')
        time.sleep(1)
        list_tradexsupplier = browser.find_elements_by_xpath(tradexsupplier_path) #Path for input supplier
        time.sleep(1)
        list_tradexsupplier[0].click()
        time.sleep(1)
        tradexsupplier_data = tradexsupplier_XML.readfromXML(folder_path+'\Data\Tradex.xml','eTender','tradexsupplier')
        time.sleep(1)
        list_tradexsupplier[0].send_keys(tradexsupplier_data) #input supplier
        time.sleep(3)
        return browser

    def closetradexsupplierwindow(self,browser):
        time.sleep(1)
        tradexsupplier_XML = DataDriver()
        list_tradexsupplier = []
        time.sleep(1)
        tradexsupplier_path = tradexsupplier_XML.readfromXML(folder_path+'\Object\Object.xml','eTender','tradexsupplierinput')
        time.sleep(1)
        list_tradexsupplier = browser.find_elements_by_xpath(tradexsupplier_path) #Path for input supplier
        time.sleep(1)
        list_tradexsupplier[0].click()
        time.sleep(1)
        tradexsupplier_data = tradexsupplier_XML.readfromXML(folder_path+'\Data\Tradex.xml','eTender','tradexsupplier')
        time.sleep(1)
        list_tradexsupplier[0].send_keys(tradexsupplier_data) #input supplier
        time.sleep(3)
        return browser

    def estimatorshowvalue(self,browser):
        time.sleep(1)
        estimatorshowvalue_XML = DataDriver()
        list_tenderdetails = []
        time.sleep(1)
        estimatorshowvalue_path = estimatorshowvalue_XML.readfromXML(folder_path+'\Object\Estimatorvalue.xml','eTender','Showvalue')
        estimatorshowvalue = browser.find_element_by_xpath(estimatorshowvalue_path) #Path fot Show value
        time.sleep(1)
        estimatorshowvalue.click()  #Clickon the Show value checkbox
        time.sleep(2)
        return browser

    def selectFilter(self,browser):
        time.sleep(1)
        selectfilter_XML = DataDriver()
        time.sleep(1)
        selectfilter_path = selectfilter_XML.readfromXML(folder_path+'\Object\Estimatorvalue.xml','eTender','selectfilter')
        time.sleep(1)
        selectfilter = browser.find_element_by_xpath(selectfilter_path) #Path fot Show value
        time.sleep(2)
        selectfilter.click()  #Clickon the filter
        time.sleep(2)
        return browser

    def selectpricableitems(self,browser):
        time.sleep(1)
        selectpricableitems_XML = DataDriver()
        list_filteroptions = []
        time.sleep(1)
        selectpricableitems_path = selectpricableitems_XML.readfromXML(folder_path+'\Object\Estimatorvalue.xml','eTender','selectpricable')
        list_filteroptions = browser.find_elements_by_xpath(selectpricableitems_path) #Path fot Show value
        time.sleep(1)
        list_filteroptions[0].click()  #Clickon the filter to select pricable option
        time.sleep(2)
        return browser

    def selectnewbillitems(self,browser):
        time.sleep(1)
        selectnewbillitems_XML = DataDriver()
        list_filteroptions = []
        time.sleep(1)
        selectnewbillitems_path = selectnewbillitems_XML.readfromXML(folder_path+'\Object\Estimatorvalue.xml','eTender','selectpricable')
        list_filteroptions = browser.find_elements_by_xpath(selectnewbillitems_path) #Path fot Show value
        time.sleep(1)
        list_filteroptions[2].click()  #Clickon the filter to select New Bill items option
        time.sleep(2)
        return browser

    def selectdeleteditemsinsupplier(self,browser):
        time.sleep(1)
        selectdeleteditems_XML = DataDriver()
        list_filteroptions = []
        time.sleep(1)
        selectdeleteditems_path = selectdeleteditems_XML.readfromXML(folder_path+'\Object\Estimatorvalue.xml','eTender','selectpricable')
        list_filteroptions = browser.find_elements_by_xpath(selectdeleteditems_path) #Path fot Show value
        time.sleep(1)
        list_filteroptions[4].click()  #Clickon the filter to select Shoe Deleted items option
        time.sleep(2)
        return browser

    def selectdeleteditemsinestimator(self,browser):
        time.sleep(1)
        selectdeleteditems_XML = DataDriver()
        list_filteroptions = []
        time.sleep(1)
        selectdeleteditems_path = selectdeleteditems_XML.readfromXML(folder_path+'\Object\Estimatorvalue.xml','eTender','selectpricable')
        list_filteroptions = browser.find_elements_by_xpath(selectdeleteditems_path) #Path fot Show value
        time.sleep(1)
        list_filteroptions[2].click()  #Clickon the filter to select Shoe Deleted items option
        time.sleep(2)
        return browser

    def selectunpriceditems(self,browser):
        time.sleep(1)
        selectunpriceditems_XML = DataDriver()
        list_filteroptions = []
        time.sleep(1)
        selectunpriceditems_path = selectunpriceditems_XML.readfromXML(folder_path+'\Object\Estimatorvalue.xml','eTender','selectpricable')
        list_filteroptions = browser.find_elements_by_xpath(selectunpriceditems_path) #Path fot Show value
        time.sleep(1)
        list_filteroptions[3].click()  #Clickon the filter to select unpriced items option
        time.sleep(2)
        return browser

    def closefilter(self,browser):
        time.sleep(1)
        closefilter_XML = DataDriver()
        time.sleep(1)
        closefilter_path = closefilter_XML.readfromXML(folder_path+'\Object\Estimatorvalue.xml','eTender','Closefilter')
        closefilter = browser.find_element_by_xpath(closefilter_path) #Path fot closefilter
        time.sleep(1)
        closefilter.click()  #Clickon the closefilter
        time.sleep(2)
        return browser

    def notesinEstimator(self,browser):
        browser.implicitly_wait(5)
        estimatornotes = DataDriver()
        estimatornotes_path = estimatornotes.readfromXML(folder_path+'\Object\Object.xml','eTender','NotesbubbleinEstimatorLogin')
        time.sleep(1)
        click_notesbubble_Estimatorlogin = browser.find_element_by_xpath(estimatornotes_path) #Click on Notes bubble in Estimator Login
        time.sleep(1)
        click_notesbubble_Estimatorlogin.click()
        time.sleep(1)
        return browser

    def tenderstatusinEstimator(self,browser):
        time.sleep(2)
        Pluslink = DataDriver()
        Pluslink_path = Pluslink.readfromXML(folder_path+'\Object\Object.xml','eTender','Pluslink')
        Pluslink = []
        Pluslink = browser.find_elements_by_xpath(Pluslink_path)
        time.sleep(1)
        Pluslink_element = Pluslink[0]
        time.sleep(1)
        Pluslink_element.click()
        time.sleep(2)
        return browser

    def estimatorprojectAPI(self,browser):
        browser.implicitly_wait(5)
        projects_XML = DataDriver()
        time.sleep(2)
        projects_path = projects_XML.readfromXML(folder_path+'\Object\SwitchOrganisation.xml','eTender','newprojectfromAPI')
        time.sleep(1)
        project_link = browser.find_element_by_link_text(projects_path)
        time.sleep(1)
        project_link.click()
        return browser

    def deleteproject(self,browser):
        browser.implicitly_wait(5)
        deleteprojects_XML = DataDriver()
        time.sleep(1)
        deleteprojects_path = deleteprojects_XML.readfromXML(folder_path+'\Object\SwitchOrganisation.xml','eTender','deleteproject')
        time.sleep(2)
        deleteproject_button = browser.find_element_by_xpath(deleteprojects_path)
        time.sleep(2)
        deleteproject_button.click()
        return browser

    def confirmdeleteproject(self,browser):
        browser.implicitly_wait(5)
        confirmdeleteprojects_XML = DataDriver()
        time.sleep(1)
        confirmdeleteprojects_path = confirmdeleteprojects_XML.readfromXML(folder_path+'\Object\SwitchOrganisation.xml','eTender','confirmdeleteproject')
        time.sleep(2)
        confirmdeleteproject_button = browser.find_element_by_xpath(confirmdeleteprojects_path)
        time.sleep(2)
        confirmdeleteproject_button.click()
        return browser

    def userprofilelink(self,browser):
        userprofile = DataDriver()
        time.sleep(1)
        userprofile_path = userprofile.readfromXML(folder_path+'\Object\SwitchOrganisation.xml','eTender','userprofile')
        time.sleep(1)
        userprofile = browser.find_element_by_link_text(userprofile_path)
        time.sleep(1)
        userprofile.click()
        return browser

    def generalsettings(self,browser):
        generalsettings1 = DataDriver()
        time.sleep(1)
        generalsettings_path = generalsettings1.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','generalsettingsmenu')
        time.sleep(1)
        generalsettings = browser.find_element_by_xpath(generalsettings_path)
        time.sleep(1)
        generalsettings.click()
        return browser

    def tenderverifyON(self,browser):
        tenderverifyON1 = DataDriver()
        time.sleep(1)
        tenderverifyON_path = tenderverifyON1.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','tenderverifyON')
        time.sleep(1)
        tenderverifyON = browser.find_element_by_xpath(tenderverifyON_path)
        time.sleep(1)
        tenderverifyON.click()
        return browser

    def tenderverifyOFF(self,browser):
        tenderverifyOFF1 = DataDriver()
        time.sleep(1)
        tenderverifyOFF_path = tenderverifyOFF1.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','tenderverifyOFF')
        time.sleep(1)
        tenderverifyOFF = browser.find_element_by_xpath(tenderverifyOFF_path)
        time.sleep(1)
        tenderverifyOFF.click()
        return browser

    def generalsettingssave(self,browser):
        generalsettingssave1 = DataDriver()
        time.sleep(1)
        generalsettingssave_path = generalsettingssave1.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','generalsettingssave')
        time.sleep(1)
        generalsettingssave = browser.find_element_by_xpath(generalsettingssave_path)
        time.sleep(1)
        generalsettingssave.click()
        return browser

    def clicktenderverifybutton(self,browser):
        tenderverifybutton1 = DataDriver()
        tenderverifybutton = []
        time.sleep(1)
        tenderverifybutton_path = tenderverifybutton1.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','tenderverifybutton')
        time.sleep(1)
        tenderverifybutton = browser.find_elements_by_xpath(tenderverifybutton_path)
        time.sleep(1)
        tenderverifybutton[2].click()
        return browser

    def tenderverifyconfirm(self,browser):
        tenderverifyconfirm1 = DataDriver()
        time.sleep(1)
        tenderverifyconfirm_path = tenderverifyconfirm1.readfromXML(folder_path+'\Object\TenderPage.xml','eTender','tenderverifiedconfirm')
        time.sleep(1)
        tenderverifyconfirm = browser.find_element_by_xpath(tenderverifyconfirm_path)
        time.sleep(1)
        tenderverifyconfirm.click()
        return browser

    def projectdocIcon(self,browser):
        projectdoc1 = DataDriver()
        time.sleep(1)
        projectdoc_path = projectdoc1.readfromXML(folder_path+'\Object\Project.xml','eTender','projectdoc')
        time.sleep(1)
        projectdoc = browser.find_element_by_xpath(projectdoc_path)
        time.sleep(1)
        projectdoc.click()
        return browser

    def addhyperlinkclick(self,browser):
        addhyperlinkclick1 = DataDriver()
        time.sleep(1)
        addhyperlinkclick_path = addhyperlinkclick1.readfromXML(folder_path+'\Object\Project.xml','eTender','hyperlink')
        time.sleep(1)
        addhyperlink = browser.find_element_by_xpath(addhyperlinkclick_path)
        time.sleep(1)
        addhyperlink.click()
        return browser

    def addURLasfile(self,browser):
        browser.implicitly_wait(5)
        note_hover = []
        notes = DataDriver()
        time.sleep(1)
        note_path = notes.readfromXML(folder_path+'\Object\Object.xml','eTender','notes')
        note_hover = browser.find_elements_by_xpath(note_path) #Xpath for hover
        time.sleep(3)
        hover = webdriver.common.action_chains.ActionChains(browser)
        hover.move_to_element(note_hover[4])
        time.sleep(1)
        hover.perform()
        return browser

    def documentasfile(self,browser):
        browser.implicitly_wait(5)
        documentasfile1 = DataDriver()
        time.sleep(1)
        documentname_path = documentasfile1.readfromXML(folder_path+'\Object\Project.xml','eTender','documentnameURLasfile')
        documentname = browser.find_element_by_xpath(documentname_path)

        documentname_data = documentasfile1.readfromXML(folder_path+'\Data\ProjectDetails.xml','eTender','documentnameURLasfile')
        documentname.send_keys(documentname_data)
        time.sleep(1)

        documentaddress_path = documentasfile1.readfromXML(folder_path+'\Object\Project.xml','eTender','documentaddressURLasfile')
        documentaddress = browser.find_element_by_xpath(documentaddress_path)

        documentaddress_data = documentasfile1.readfromXML(folder_path+'\Data\ProjectDetails.xml','eTender','documentaddressURLasfile')
        documentaddress.send_keys(documentaddress_data)

        adddocument_path = documentasfile1.readfromXML(folder_path+'\Object\Project.xml','eTender','addlink')
        adddocument = browser.find_element_by_xpath(adddocument_path)
        adddocument.click()
        time.sleep(3)
        return browser

    def internaldocumentasfile(self,browser):
        browser.implicitly_wait(5)
        internaldocumentasfile1 = DataDriver()
        time.sleep(1)
        internaldocumentname_path = internaldocumentasfile1.readfromXML(folder_path+'\Object\Project.xml','eTender','documentnameURLasfile')
        internaldocumentname = browser.find_element_by_xpath(internaldocumentname_path)

        internaldocumentname_data = internaldocumentasfile1.readfromXML(folder_path+'\Data\ProjectDetails.xml','eTender','internaldocumentnameURLasfile')
        internaldocumentname.send_keys(internaldocumentname_data)
        time.sleep(1)

        internaldocumentaddress_path = internaldocumentasfile1.readfromXML(folder_path+'\Object\Project.xml','eTender','documentaddressURLasfile')
        internaldocumentaddress = browser.find_element_by_xpath(internaldocumentaddress_path)

        internaldocumentaddress_data = internaldocumentasfile1.readfromXML(folder_path+'\Data\ProjectDetails.xml','eTender','internaldocumentaddressURLasfile')
        internaldocumentaddress.send_keys(internaldocumentaddress_data)

        adddocument_path = internaldocumentasfile1.readfromXML(folder_path+'\Object\Project.xml','eTender','addlink')
        adddocument = browser.find_element_by_xpath(adddocument_path)
        adddocument.click()
        time.sleep(3)
        return browser

    def externaldocumentasfile(self,browser):
        browser.implicitly_wait(5)
        externaldocumentasfile1 = DataDriver()
        time.sleep(1)
        externaldocumentname_path = externaldocumentasfile1.readfromXML(folder_path+'\Object\Project.xml','eTender','documentnameURLasfile')
        externaldocumentname = browser.find_element_by_xpath(externaldocumentname_path)

        externaldocumentname_data = externaldocumentasfile1.readfromXML(folder_path+'\Data\ProjectDetails.xml','eTender','externaldocumentnameURLasfile')
        externaldocumentname.send_keys(externaldocumentname_data)
        time.sleep(1)

        externaldocumentaddress_path = externaldocumentasfile1.readfromXML(folder_path+'\Object\Project.xml','eTender','documentaddressURLasfile')
        externaldocumentaddress = browser.find_element_by_xpath(externaldocumentaddress_path)

        externaldocumentaddress_data = externaldocumentasfile1.readfromXML(folder_path+'\Data\ProjectDetails.xml','eTender','externaldocumentaddressURLasfile')
        externaldocumentaddress.send_keys(externaldocumentaddress_data)

        adddocument_path = externaldocumentasfile1.readfromXML(folder_path+'\Object\Project.xml','eTender','addlink')
        adddocument = browser.find_element_by_xpath(adddocument_path)
        adddocument.click()
        time.sleep(3)
        return browser

    def documentClick(self,browser):
        browser.implicitly_wait(5)
        documentclick1 = DataDriver()
        time.sleep(1)
        documentclick_path = documentclick1.readfromXML(folder_path+'\Object\Project.xml','eTender','documentname')
        documentclick = browser.find_element_by_xpath(documentclick_path)
        #documentclick.click()
        time.sleep(3)
        return browser

class SubmitTenderclass():
    def submitTender(self,browser):
          browser.implicitly_wait(5)
          submittender = DataDriver()
          time.sleep(1)
          submittender_path = submittender.readfromXML(folder_path+'\Object\Object.xml','eTender','submittender')
          time.sleep(1)
          submittender_button = browser.find_element_by_xpath(submittender_path) # Click on Submit tender button
          time.sleep(2)
          submittender_button.click()
          return browser

    def confirmTendersubmission(self,browser):
          browser.implicitly_wait(5)
          submittender = DataDriver()
          time.sleep(1)
          confirm_submittender_path = submittender.readfromXML(folder_path+'\Object\Object.xml','eTender','confirmtendersubmission')
          time.sleep(1)
          confirm_submittender = browser.find_element_by_xpath(confirm_submittender_path) # Click on Confirm Submit button
          time.sleep(1)
          confirm_submittender.click()
          return browser

    def priceunrateditems(self,browser):
          browser.implicitly_wait(5)
          priceunrateditems_XML = DataDriver()
          priceunrateditems = []
          time.sleep(1)
          priceunrateditems_path = priceunrateditems_XML.readfromXML(folder_path+'\Object\Object.xml','eTender','priceunrateditems')
          time.sleep(1)
          priceunrateditems = browser.find_elements_by_xpath(priceunrateditems_path) # Select Included option
          time.sleep(1)
          priceunrateditems[0].click()
          return browser

    def applypriceunrateditems(self,browser):
          browser.implicitly_wait(5)
          applypriceunrateditems_XML = DataDriver()
          time.sleep(1)
          applypriceunrateditems_path = applypriceunrateditems_XML.readfromXML(folder_path+'\Object\Object.xml','eTender','applypriceunrateditems')
          time.sleep(1)
          applypriceunrateditems = browser.find_element_by_xpath(applypriceunrateditems_path) # Apply unrated items to the tender
          time.sleep(1)
          applypriceunrateditems.click()
          return browser

    def declineTender(self,browser):
          browser.implicitly_wait(5)
          declinetender = DataDriver()
          declinetender_path = declinetender.readfromXML(folder_path+'\Object\Object.xml','eTender','declinetender')
          declinetender_button = browser.find_element_by_xpath(declinetender_path) # Click on Decline tender button
          time.sleep(2)
          declinetender_button.click()
          time.sleep(1)
          return browser

    def declineTenderSubmission(self,browser):
          browser.implicitly_wait(5)
          declinetender = DataDriver()
          time.sleep(1)
          declinetenderreason_path = declinetender.readfromXML(folder_path+'\Object\Object.xml','eTender','declinetenderreason')
          declinetenderreason_radiobutton = browser.find_element_by_xpath(declinetenderreason_path) # Selecting decline reson
          #print declinetenderreason_radiobutton
          declinetenderreason_radiobutton.click()
          time.sleep(1)
          confirm_declinetender_path = declinetender.readfromXML(folder_path+'\Object\Object.xml','eTender','confirmdecline')
          confirm_declinetender = browser.find_element_by_xpath(confirm_declinetender_path) # Click on Confirm decline button
          time.sleep(1)
          confirm_declinetender.click()
          return browser











