#-------------------------------------------------------------------------------
# Name:         OrganizationFunction
#
# Purpose:      Liberary fucntions for Organization menu
#
# Author:       mathew.jacob
#
# Created:      19/09/2016
# Copyright:    (c) Causeway Technologies 2016
#-------------------------------------------------------------------------------
import os
import sys
import time
dir_path = os.path.dirname(os.path.realpath(__file__))
folder_path=os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0,folder_path+"\Syslibrary")
from datadriven import DataDriver
orgLink=DataDriver()
class Organizationclass():

    def OpenaddUser(self,browser):
        time.sleep(2)
        browser.find_element_by_link_text(orgLink.readfromXML(folder_path+'\Object\Object.xml','eTender','addUserLink')).click()

    def AddUserOrganization(self,browser):
        addusertoOrg=orgLink.readfromXML(folder_path+'\Object\Object.xml','eTender','adduserOrganisation')
        usercount =browser.find_elements_by_xpath(orgLink.readfromXML(folder_path+'\Object\Object.xml','eTender','UserCount'))
        count=len(usercount)
        count=count+1
        browser.find_element_by_xpath(addusertoOrg).click()
        time.sleep(4)
        p=browser.find_elements_by_xpath(orgLink.readfromXML(folder_path+'\Object\Object.xml','eTender','emailSearchbox'))
        time.sleep(2)
        p[3].send_keys(orgLink.readfromXML(folder_path+'\Data\Data.xml','eTender','userSaveEmail'))
        time.sleep(5)
        Checkbox1= browser.find_elements_by_xpath(orgLink.readfromXML(folder_path+'\Object\Object.xml','eTender','adduserCheckbox'))
        Checkbox1[count].click()
        browser.find_element_by_id(orgLink.readfromXML(folder_path+'\Object\Object.xml','eTender','adduserSavebutton')).click()
        time.sleep(5)
        return browser

    def RemoveUserOrganization(self,browser):
        p1=browser.find_elements_by_xpath(orgLink.readfromXML(folder_path+'\Object\Object.xml','eTender','emailSearchbox'))
        p1[1].send_keys(orgLink.readfromXML(folder_path+'\Data\Data.xml','eTender','userSaveEmail'))
        time.sleep(5)
        browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\Object.xml','eTender','adduserCheckbox')).click()
        time.sleep(2)
        browser.find_element_by_id(orgLink.readfromXML(folder_path+'\Object\Object.xml','eTender','removeButton')).click()
        time.sleep(3)
        browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\Object.xml','eTender','yesButton')).click()
        time.sleep(3)

    def OpenUserRole(self,browser):
        browser.find_element_by_link_text(orgLink.readfromXML(folder_path+'\Object\Object.xml','eTender','userRoleLink')).click()

    def AddUserOrganizationCancel(self,browser):
        addusertoOrg=orgLink.readfromXML(folder_path+'\Object\Object.xml','eTender','adduserOrganisation')
        usercount =browser.find_elements_by_xpath("//div[@class='ui-grid-selection-row-header-buttons ui-grid-icon-ok ng-scope']")
        count1=len(usercount)
        count1=count1+1
        browser.find_element_by_xpath(addusertoOrg).click()
        time.sleep(5)
        p=browser.find_elements_by_xpath(orgLink.readfromXML(folder_path+'\Object\Object.xml','eTender','emailSearchbox'))
        p[3].send_keys(orgLink.readfromXML(folder_path+'\Data\Data.xml','eTender','userSaveEmail'))
        time.sleep(5)
        Checkbox1= browser.find_elements_by_xpath(orgLink.readfromXML(folder_path+'\Object\Object.xml','eTender','adduserCheckbox'))
        Checkbox1[count1].click()
        browser.find_element_by_xpath(orgLink.readfromXML(folder_path+'\Object\Object.xml','eTender','CancelAddUser')).click()

    def OpenProfilePage(self,browser):
        browser.find_element_by_link_text(orgLink.readfromXML(folder_path+'\Object\Object.xml','eTender','profileLink')).click()

    def OpenUserProfilePage(self,browser):
        browser.find_element_by_link_text(orgLink.readfromXML(folder_path+'\\Object\\UserProfileObject.xml','eTender','userProfileLink')).click()

    def Userslist(self,browser):
        userslist = []
        userslist = browser.find_elements_by_xpath(orgLink.readfromXML(folder_path+'\\Object\\UserProfileObject.xml','eTender','userslist'))
        email1 = userslist[1].text
        parenthesis = "({})"
        user1 = parenthesis.format(email1)
        email2 = userslist[4].text
        parenthesis = "({})"
        user2 = parenthesis.format(email2)
        firstuser = userslist[0].text +  user1
        seconduser = userslist[3].text + user2
        return firstuser,seconduser








