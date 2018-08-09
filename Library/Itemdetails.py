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

class ItemDetails():
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
        inputtenderdetails_path = tenderdetails_XML.readfromXML(folder_path+'\Object\Object.xml','eTender','inputtenderdetails')
        time.sleep(1)
        input_tenderdetails = browser.find_elements_by_xpath(inputtenderdetails_path) #Path input Details
        #print input_tenderdetails
        time.sleep(1)
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

    def localtender(self,browser):
        time.sleep(1)
        tenderdetails_XML = DataDriver()
        list_tenderdetails = []
        time.sleep(1)
        tenderdetails_path = tenderdetails_XML.readfromXML(folder_path+'\Object\Object.xml','eTender','tenderdetailsestimator')
        list_tenderdetails = browser.find_elements_by_xpath(tenderdetails_path) #Path fot Tender details list in supplier login
        time.sleep(1)
        list_tenderdetails[4].click()  #Clickon the supplier first Tenderdetails
        time.sleep(2)
        return browser

    def edititems(self,browser):
        time.sleep(1)
        edititems1 = DataDriver()
        time.sleep(2)
        edititems_path = edititems1.readfromXML(folder_path+'\Object\Itemsobject.xml','eTender','edititem')
        time.sleep(2)
        edititems = browser.find_element_by_xpath(edititems_path) #Path for clicking Edit tender items button
        time.sleep(2)
        edititems.click()  #Click on Edit tender items button
        time.sleep(2)
        return browser

    def additemclick(self,browser):
        time.sleep(1)
        additemclick1 = DataDriver()
        time.sleep(2)
        additemclick_path = additemclick1.readfromXML(folder_path+'\Object\Itemsobject.xml','eTender','additemclick')
        time.sleep(2)
        additemclick = browser.find_element_by_xpath(additemclick_path) #Path for clicking add items button
        time.sleep(2)
        additemclick.click()  #Click on add items button
        time.sleep(2)
        return browser

    def additem(self,browser):
        time.sleep(1)
        additem1 = DataDriver()
        additem = []
        time.sleep(1)
        additem_path = additem1.readfromXML(folder_path+'\Object\Itemsobject.xml','eTender','additem')
        time.sleep(1)
        additem = browser.find_elements_by_xpath(additem_path) #Path for entering item details
        time.sleep(1)
        counter = 0
        for items in range(counter,5):
            additemdetails = ActionChains(browser)
            additemdetails.move_to_element(additem[counter])
            additemdetails.double_click(additem[counter]) #double Click to add items
            time.sleep(1)
            additemdetails.perform()
            time.sleep(1)
            if counter == 0:
                additeminput_path = additem1.readfromXML(folder_path+'\Object\Itemsobject.xml','eTender','additeminput')
                time.sleep(1)
                additeminput = browser.find_element_by_xpath(additeminput_path) #Path for entering item details

                itemRef = additem1.readfromXML(folder_path+'\Data\Itemsdata.xml','eTender','itemref')
                time.sleep(1)
                additeminput.send_keys(itemRef)

            elif counter == 1:

                additeminput_path = additem1.readfromXML(folder_path+'\Object\Itemsobject.xml','eTender','additeminput')
                time.sleep(1)
                additeminput = browser.find_element_by_xpath(additeminput_path) #Path for entering item details

                itemdescription = additem1.readfromXML(folder_path+'\Data\Itemsdata.xml','eTender','itemdescription')
                time.sleep(1)
                additeminput.send_keys(itemdescription)

            elif counter == 2:

                additeminput_path = additem1.readfromXML(folder_path+'\Object\Itemsobject.xml','eTender','additeminput')
                time.sleep(1)
                additeminput = browser.find_element_by_xpath(additeminput_path) #Path for entering item details

                itemqty = additem1.readfromXML(folder_path+'\Data\Itemsdata.xml','eTender','itemqty')
                time.sleep(1)
                additeminput.send_keys(itemqty)

            elif counter == 3:

                additeminput_path = additem1.readfromXML(folder_path+'\Object\Itemsobject.xml','eTender','additeminput')
                time.sleep(1)
                additeminput = browser.find_element_by_xpath(additeminput_path) #Path for entering item details

                itemunit = additem1.readfromXML(folder_path+'\Data\Itemsdata.xml','eTender','itemunit')
                time.sleep(1)
                additeminput.send_keys(itemunit)

            elif counter == 4:

                additeminput_path = additem1.readfromXML(folder_path+'\Object\Itemsobject.xml','eTender','additeminput')
                time.sleep(1)
                additeminput = browser.find_element_by_xpath(additeminput_path) #Path for entering item details

                itemrate = additem1.readfromXML(folder_path+'\Data\Itemsdata.xml','eTender','itemrate')
                time.sleep(1)
                additeminput.send_keys(itemrate)
            counter = counter + 1
            time.sleep(2)
        return browser

    def additemsave(self,browser):
        time.sleep(1)
        additemsave1 = DataDriver()
        time.sleep(1)
        additemsave_path = additemsave1.readfromXML(folder_path+'\Object\Itemsobject.xml','eTender','additemsave')
        additemsave = browser.find_element_by_xpath(additemsave_path) #Path for entering item details
        time.sleep(1)
        additemsave.click()
        return browser

    def selectitem(self,browser):
        time.sleep(1)
        selectitem1 = DataDriver()
        selectitem = []
        time.sleep(1)
        selectitem_path = selectitem1.readfromXML(folder_path+'\Object\Itemsobject.xml','eTender','selectitem')
        selectitem = browser.find_elements_by_xpath(selectitem_path) #Path for entering item details
        time.sleep(1)
        selectitem[0].click()
        return browser

    def deleteitem(self,browser):
        time.sleep(1)
        deleteitem1 = DataDriver()
        time.sleep(1)
        deleteitem_path = deleteitem1.readfromXML(folder_path+'\Object\Itemsobject.xml','eTender','deleteitem')
        deleteitem = browser.find_element_by_xpath(deleteitem_path) #Path for entering item details
        time.sleep(1)
        deleteitem.click()

        deleteitemconfirm_path = deleteitem1.readfromXML(folder_path+'\Object\Itemsobject.xml','eTender','confirmdeleteitem')
        deleteitemconfirm = browser.find_element_by_xpath(deleteitemconfirm_path) #Path for entering item details
        time.sleep(1)
        deleteitemconfirm.click()
        return browser

    def tenderlink(self,browser):
        time.sleep(1)
        tenderlink = []
        tenderlink1 = DataDriver()
        time.sleep(1)
        tenderlink_path = tenderlink1.readfromXML(folder_path+'\Object\Itemsobject.xml','eTender','tenderlink')
        tenderlink = browser.find_elements_by_xpath(tenderlink_path) #Path for tenderlink
        time.sleep(1)
        tenderlink[1].click()
        return browser

    def tenderproject(self,browser):
        time.sleep(1)
        tenderproject = []
        tenderproject1 = DataDriver()
        time.sleep(1)
        tenderproject_path = tenderproject1.readfromXML(folder_path+'\Object\Itemsobject.xml','eTender','tenderlink')
        tenderproject = browser.find_elements_by_xpath(tenderproject_path) #Path for tenderlink
        time.sleep(1)
        tenderproject[0].click()
        return browser

    def updateitem(self,browser):
        time.sleep(1)
        additem1 = DataDriver()
        additem = []
        time.sleep(1)
        additem_path = additem1.readfromXML(folder_path+'\Object\Itemsobject.xml','eTender','additem')
        time.sleep(1)
        additem = browser.find_elements_by_xpath(additem_path) #Path for entering item details
        time.sleep(1)
        counter = 0
        for items in range(counter,5):
            additemdetails = ActionChains(browser)
            additemdetails.move_to_element(additem[counter])
            additemdetails.double_click(additem[counter]) #double Click to add items
            time.sleep(1)
            additemdetails.perform()
            time.sleep(1)
            if counter == 0:
                additeminput_path = additem1.readfromXML(folder_path+'\Object\Itemsobject.xml','eTender','additeminput')
                time.sleep(1)
                additeminput = browser.find_element_by_xpath(additeminput_path) #Path for entering item details
                additeminput.clear()

                itemRef = additem1.readfromXML(folder_path+'\Data\Itemsdata.xml','eTender','itemrefupdate')
                time.sleep(1)
                additeminput.send_keys(itemRef)

            elif counter == 1:

                additeminput_path = additem1.readfromXML(folder_path+'\Object\Itemsobject.xml','eTender','additeminput')
                time.sleep(1)
                additeminput = browser.find_element_by_xpath(additeminput_path) #Path for entering item details
                additeminput.clear()

                itemdescription = additem1.readfromXML(folder_path+'\Data\Itemsdata.xml','eTender','itemdescriptionupdate')
                time.sleep(1)
                additeminput.send_keys(itemdescription)

            elif counter == 2:

                additeminput_path = additem1.readfromXML(folder_path+'\Object\Itemsobject.xml','eTender','additeminput')
                time.sleep(1)
                additeminput = browser.find_element_by_xpath(additeminput_path) #Path for entering item details
                additeminput.clear()

                itemqty = additem1.readfromXML(folder_path+'\Data\Itemsdata.xml','eTender','itemqtyupdate')
                time.sleep(1)
                additeminput.send_keys(itemqty)

            elif counter == 3:

                additeminput_path = additem1.readfromXML(folder_path+'\Object\Itemsobject.xml','eTender','additeminput')
                time.sleep(1)
                additeminput = browser.find_element_by_xpath(additeminput_path) #Path for entering item details
                additeminput.clear()

                itemunit = additem1.readfromXML(folder_path+'\Data\Itemsdata.xml','eTender','itemunitupdate')
                time.sleep(1)
                additeminput.send_keys(itemunit)

            elif counter == 4:

                additeminput_path = additem1.readfromXML(folder_path+'\Object\Itemsobject.xml','eTender','additeminput')
                time.sleep(1)
                additeminput = browser.find_element_by_xpath(additeminput_path) #Path for entering item details
                additeminput.clear()

                itemrate = additem1.readfromXML(folder_path+'\Data\Itemsdata.xml','eTender','itemrateupdate')
                time.sleep(1)
                additeminput.send_keys(itemrate)
            counter = counter + 1
            time.sleep(2)
        return browser

    def importlink(self,browser):
        time.sleep(1)
        importlink1 = DataDriver()
        time.sleep(1)
        importlink_path = importlink1.readfromXML(folder_path+'\Object\Itemsobject.xml','eTender','importlink')
        importlink = browser.find_element_by_xpath(importlink_path) #Path for import link
        time.sleep(1)
        importlink.click()
        return browser

    def importitems(self,browser):
        time.sleep(3)
        os.system(folder_path+'\Env\Importitems.exe') #This is AUToIT script for Upload a Document(Note:selenium not supporting uploading a document from windows hence we need to install AUTOIT to upload a document)
        time.sleep(4)
        importitems1 = DataDriver()
        importitemsconfirm_path = importitems1.readfromXML(folder_path+'\Object\Itemsobject.xml','eTender','importitems')
        importitemsconfirm = browser.find_element_by_xpath(importitemsconfirm_path) #path for confirm Import
        time.sleep(1)
        importitemsconfirm.click()
        time.sleep(3)
        return browser

    def moreactions(self,browser):
        time.sleep(2)
        moreactions1 = DataDriver()
        moreactions = []
        moreactions_path = moreactions1.readfromXML(folder_path+'\Object\Itemsobject.xml','eTender','actions')
        moreactions = browser.find_elements_by_xpath(moreactions_path) #path for actions button
        time.sleep(1)
        moreactions[1].click()
        time.sleep(2)
        return browser

    def invitecolleague(self,browser):
        time.sleep(2)
        invitecolleague1 = DataDriver()
        invitecolleague_path = invitecolleague1.readfromXML(folder_path+'\Object\Itemsobject.xml','eTender','invitecolleague')
        invitecolleague = browser.find_element_by_xpath(invitecolleague_path)
        time.sleep(1)
        invitecolleague.click()
        time.sleep(2)
        return browser

    def invitecolleaguenotinthelist(self,browser):
        time.sleep(2)
        invitecolleaguenotinthelist1 = DataDriver()
        invitecolleaguenotinthelist_path = invitecolleaguenotinthelist1.readfromXML(folder_path+'\Object\Itemsobject.xml','eTender','emailinvite')
        invitecolleaguenotinthelist = browser.find_element_by_xpath(invitecolleaguenotinthelist_path)
        time.sleep(1)
        invitecolleaguenotinthelist.click()
        time.sleep(2)
        return browser

    def emailnotinthelist(self,browser):
        emailnotinthelist1 = DataDriver()
        emailnotinthelist_path = emailnotinthelist1.readfromXML(folder_path+'\Object\Itemsobject.xml','eTender','emailnotinthelist')
        emailnotinthelist = browser.find_element_by_xpath(emailnotinthelist_path) #path for new email
        time.sleep(2)

        emailnotinthelist_data = emailnotinthelist1.readfromXML(folder_path+'\Data\Itemsdata.xml','eTender','emailnotinthelist')
        emailnotinthelist.send_keys(emailnotinthelist_data)
        time.sleep(1)

        Invitebutton_path = emailnotinthelist1.readfromXML(folder_path+'\Object\Itemsobject.xml','eTender','Invitebutton')
        Invitebutton = browser.find_element_by_xpath(Invitebutton_path) #path for new email
        Invitebutton.click()
        time.sleep(1)

        closewindow_path = emailnotinthelist1.readfromXML(folder_path+'\Object\Itemsobject.xml','eTender','close')
        closewindow = browser.find_element_by_xpath(closewindow_path) #path for new email
        time.sleep(1)
        closewindow.click()
        time.sleep(1)
        return browser

    def invitecolleagueSearch(self,browser):
        invitecolleaguesearch1 = DataDriver()
        invitecolleaguesearch = []
        invitecolleaguesearch_path = invitecolleaguesearch1.readfromXML(folder_path+'\Object\Itemsobject.xml','eTender','invitecolleaguesearch')
        invitecolleaguesearch = browser.find_elements_by_xpath(invitecolleaguesearch_path) #path for search
        time.sleep(2)

        emailsearch_data = invitecolleaguesearch1.readfromXML(folder_path+'\Data\Itemsdata.xml','eTender','emailsearch')
        invitecolleaguesearch[2].send_keys(emailsearch_data)
        time.sleep(1)
        return browser




