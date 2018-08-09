#-------------------------------------------------------------------------------
# Name:        User Registration
# Purpose:
#
# Author:      suresh.kumar
#
# Created:     04-10-2016
# Copyright:   (c) causeway Technologies 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from launcheTender import LauncheTenderclass
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

class RegistrationineT():
    def register(self,browser):
        browser.implicitly_wait(2)
        register = DataDriver()
        register_path = register.readfromXML(folder_path+'\Object\Object.xml','eTender','register')
        register_link = browser.find_element_by_link_text(register_path)
        register_link.click()
        time.sleep(1)
        return browser

    def selectsupplierRole(self,browser):
        browser.implicitly_wait(2)
        register = DataDriver()
        selectrole_button = []
        selectrole_path = register.readfromXML(folder_path+'\Object\Object.xml','eTender','contractorrole')
        selectrole_button = browser.find_elements_by_xpath(selectrole_path)
        selectrole_button[1].click()
        time.sleep(2)
        return browser

    def selectmaincontractorRole(self,browser):
        browser.implicitly_wait(2)
        register = DataDriver()
        selectrole_button = []
        selectrole_path = register.readfromXML(folder_path+'\Object\Object.xml','eTender','contractorrole')
        selectrole_button = browser.find_elements_by_xpath(selectrole_path)
        selectrole_button[0].click()
        time.sleep(1)
        return browser

    def selectestimatorRole(self,browser):
        browser.implicitly_wait(2)
        estimatorrole_radiobutton = []
        register = DataDriver()
        estimatorrole_path = register.readfromXML(folder_path+'\Object\Object.xml','eTender','estimator-select')
        estimatorrole_radiobutton = browser.find_elements_by_xpath(estimatorrole_path)
        estimatorrole_radiobutton[0].click()
        time.sleep(1)
        return browser

    def selectestimatoradminRole(self,browser):
        browser.implicitly_wait(2)
        estimatorrole_radiobutton = []
        register = DataDriver()
        estimatorrole_path = register.readfromXML(folder_path+'\Object\Object.xml','eTender','estimator-select')
        estimatorrole_radiobutton = browser.find_elements_by_xpath(estimatorrole_path)
        estimatorrole_radiobutton[1].click()
        time.sleep(1)
        return browser

    def registrationForm(self,browser):
        browser.implicitly_wait(2)
        time.sleep(1)
        supplier_register = DataDriver()
        supplier_register_email_path =supplier_register.readfromXML(folder_path+'\Object\Object.xml','eTender','supplier-email')
        supplier_register_email = browser.find_element_by_xpath(supplier_register_email_path)
        time.sleep(1)
        supplier_register_email_data = supplier_register.readfromXML(folder_path+'\Data\Data.xml','eTender','supplier-email1')
        supplier_register_email.send_keys(supplier_register_email_data)
        time.sleep(1)
        supplier_register_password_path =supplier_register.readfromXML(folder_path+'\Object\Object.xml','eTender','supplier-password')
        supplier_register_password = browser.find_element_by_xpath(supplier_register_password_path)
        supplier_register_password_data =supplier_register.readfromXML(folder_path+'\Data\Data.xml','eTender','supplier-password1')
        supplier_register_password.send_keys(supplier_register_password_data)
        time.sleep(1)

        supplier_register_confirmpassword_path =supplier_register.readfromXML(folder_path+'\Object\Object.xml','eTender','supplier-confirmpassword')
        supplier_register_confirmpassword = browser.find_element_by_xpath(supplier_register_confirmpassword_path)

        supplier_register_confirmpassword_data =supplier_register.readfromXML(folder_path+'\Data\Data.xml','eTender','supplier-confirmpassword1')

        supplier_register_confirmpassword.send_keys(supplier_register_confirmpassword_data)
        time.sleep(1)

        supplier_register_firstname_path =supplier_register.readfromXML(folder_path+'\Object\Object.xml','eTender','supplier-firstname')
        supplier_register_firstname = browser.find_element_by_xpath(supplier_register_firstname_path)

        supplier_register_firstname_data =supplier_register.readfromXML(folder_path+'\Data\Data.xml','eTender','supplier-firstname')
        supplier_register_firstname.send_keys(supplier_register_firstname_data)
        time.sleep(1)

        supplier_register_lastname_path =supplier_register.readfromXML(folder_path+'\Object\Object.xml','eTender','supplier-lastname')
        supplier_register_lastname = browser.find_element_by_xpath(supplier_register_lastname_path)

        supplier_register_lastname_data =supplier_register.readfromXML(folder_path+'\Data\Data.xml','eTender','supplier-lastname')

        supplier_register_lastname.send_keys(supplier_register_lastname_data)
        time.sleep(1)

        supplier_register_mobile_path =supplier_register.readfromXML(folder_path+'\Object\Object.xml','eTender','supplier-mobile')
        supplier_register_mobile = browser.find_element_by_xpath(supplier_register_mobile_path)

        supplier_register_mobile_data =supplier_register.readfromXML(folder_path+'\Data\Data.xml','eTender','supplier-mobile')

        supplier_register_mobile.send_keys(supplier_register_mobile_data)
        time.sleep(1)

        supplier_register_phone_path =supplier_register.readfromXML(folder_path+'\Object\Object.xml','eTender','supplier-phone')
        supplier_register_phone = browser.find_element_by_xpath(supplier_register_phone_path)

        supplier_register_phone_data =supplier_register.readfromXML(folder_path+'\Data\Data.xml','eTender','supplier-phone')

        supplier_register_phone.send_keys(supplier_register_phone_data)
        time.sleep(1)

        supplier_register_Nextbutton_path =supplier_register.readfromXML(folder_path+'\Object\Object.xml','eTender','Nextbutton')
        supplier_register_Nextbutton = browser.find_element_by_xpath(supplier_register_Nextbutton_path)

        supplier_register_Nextbutton.click()
        time.sleep(5)
        return browser

    def organisationselect(self,browser):
        organisation_select = DataDriver()
        time.sleep(1)
        dropdownselect_organisation_path = organisation_select.readfromXML(folder_path+'\Object\Object.xml','eTender','organisation-dropdownselect')
        time.sleep(1)
        dropdownselect_organisation = browser.find_element_by_xpath(dropdownselect_organisation_path)
        time.sleep(2)
        dropdownselect_organisation.click()
        time.sleep(2)

        enter_organisation_path = organisation_select.readfromXML(folder_path+'\Object\Object.xml','eTender','organisation-enter')
        enter_organisation = browser.find_element_by_xpath(enter_organisation_path)
        time.sleep(1)

        select_organisation_datapath = organisation_select.readfromXML(folder_path+'\Data\Data.xml','eTender','supplier-company')
        time.sleep(1)
        enter_organisation.send_keys(select_organisation_datapath)
        time.sleep(1)

        #enter_organisation.send_keys(u'\ue007')
        select_organisation_path = organisation_select.readfromXML(folder_path+'\Object\Object.xml','eTender','organisation-select')
        time.sleep(2)
        select_organisation = browser.find_element_by_xpath(select_organisation_path)
        time.sleep(2)
        select_organisation.click()
        time.sleep(2)
        return browser

    def organisationselectLOAD(self,browser):
        organisation_select = DataDriver()
        time.sleep(1)
        dropdownselect_organisation_path = organisation_select.readfromXML(folder_path+'\Object\Object.xml','eTender','organisation-dropdownselect')
        time.sleep(1)
        dropdownselect_organisation = browser.find_element_by_xpath(dropdownselect_organisation_path)
        time.sleep(2)
        dropdownselect_organisation.click()
        time.sleep(2)

        enter_organisation_path = organisation_select.readfromXML(folder_path+'\Object\Object.xml','eTender','organisation-enter')
        enter_organisation = browser.find_element_by_xpath(enter_organisation_path)
        time.sleep(1)

        select_organisation_datapath = organisation_select.readfromXML(folder_path+'\Data\Data.xml','eTender','supplier-companyLOAD')
        time.sleep(1)
        enter_organisation.send_keys(select_organisation_datapath)
        time.sleep(2)

        #enter_organisation.send_keys(u'\ue007')
        select_organisation_path = organisation_select.readfromXML(folder_path+'\Object\Object.xml','eTender','organisation-select')
        time.sleep(2)
        select_organisation = browser.find_element_by_xpath(select_organisation_path)
        time.sleep(2)
        select_organisation.click()
        time.sleep(2)
        return browser

    def organisationcreate(self,browser):
        supplier_register = DataDriver()
        time.sleep(1)
        supplier_organisationcreate_path =supplier_register.readfromXML(folder_path+'\Object\Object.xml','eTender','organisation-create')
        time.sleep(1)

        supplier_organisationcreate = browser.find_element_by_xpath(supplier_organisationcreate_path)
        time.sleep(3)
        #print supplier_organisationcreate.text
        supplier_organisationcreate.click()
        time.sleep(4)

        #supplier_company = []
        supplier_company_path = supplier_register.readfromXML(folder_path+'\Object\Object.xml','eTender','supplier-company')
        supplier_company = browser.find_element_by_xpath(supplier_company_path)
        time.sleep(1)

        supplier_company_data =supplier_register.readfromXML(folder_path+'\Data\Data.xml','eTender','supplier-company')

        supplier_company.send_keys(supplier_company_data)
        time.sleep(1)

        organisation_phone_path = supplier_register.readfromXML(folder_path+'\Object\Object.xml','eTender','organisation-phone')
        organisation_phone = browser.find_element_by_xpath(organisation_phone_path)
        time.sleep(1)

        organisation_phone_data =supplier_register.readfromXML(folder_path+'\Data\Data.xml','eTender','organisation-phone')

        organisation_phone.send_keys(organisation_phone_data)
        time.sleep(1)

        organisation_email_path = supplier_register.readfromXML(folder_path+'\Object\Object.xml','eTender','organisation-email')
        organisation_email = browser.find_element_by_xpath(organisation_email_path)
        time.sleep(1)

        organisation_email_data =supplier_register.readfromXML(folder_path+'\Data\Data.xml','eTender','organisation-email')

        organisation_email.send_keys(organisation_email_data)
        time.sleep(1)

        organisation_website_path = supplier_register.readfromXML(folder_path+'\Object\Object.xml','eTender','organisation-website')
        organisation_website = browser.find_element_by_xpath(organisation_website_path)
        time.sleep(1)

        organisation_website_data =supplier_register.readfromXML(folder_path+'\Data\Data.xml','eTender','organisation-website')

        organisation_website.send_keys(organisation_website_data)
        time.sleep(1)

        organisation_address_path = supplier_register.readfromXML(folder_path+'\Object\Object.xml','eTender','organisation-address')
        organisation_address = browser.find_element_by_xpath(organisation_address_path)
        time.sleep(1)

        organisation_address_data =supplier_register.readfromXML(folder_path+'\Data\Data.xml','eTender','organisation-address')
        organisation_address.send_keys(organisation_address_data)
        time.sleep(1)

        organisation_county_path = supplier_register.readfromXML(folder_path+'\Object\Object.xml','eTender','organisation-county')
        organisation_county = browser.find_element_by_xpath(organisation_county_path)
        time.sleep(1)

        organisation_county_data =supplier_register.readfromXML(folder_path+'\Data\Data.xml','eTender','organisation-county')

        organisation_county.send_keys(organisation_county_data)
        time.sleep(1)

        organisation_country_path = supplier_register.readfromXML(folder_path+'\Object\Object.xml','eTender','organisation-country')
        organisation_country = browser.find_element_by_xpath(organisation_country_path)
        time.sleep(1)

        organisation_country_data =supplier_register.readfromXML(folder_path+'\Data\Data.xml','eTender','organisation-country')

        organisation_country.send_keys(organisation_country_data)
        time.sleep(1)

        organisation_postalcode_path = supplier_register.readfromXML(folder_path+'\Object\Object.xml','eTender','organisation-postalcode')
        organisation_postalcode = browser.find_element_by_xpath(organisation_postalcode_path)
        time.sleep(1)

        organisation_postalcode_data =supplier_register.readfromXML(folder_path+'\Data\Data.xml','eTender','organisation-postalcode')

        organisation_postalcode.send_keys(organisation_postalcode_data)
        time.sleep(1)

        return browser

    def organisationLocation(self,browser):
        organisation_location = DataDriver()

        organisation_location_path = organisation_location.readfromXML(folder_path+'\Object\Object.xml','eTender','organisation-location')
        organisation_location = browser.find_element_by_xpath(organisation_location_path)
        time.sleep(1)

        organisation_location_data =supplier_register.readfromXML(folder_path+'\Data\Data.xml','eTender','organisation-location')

        organisation_location.send_keys(organisation-location_data)
        time.sleep(1)

        return browser

    def supplierRegistration(self,browser):
        supplier_register = DataDriver()
        time.sleep(1)
        supplier_register_checkbox_path =supplier_register.readfromXML(folder_path+'\Object\Object.xml','eTender','termsandconditions')
        supplier_register_checkbox = browser.find_elements_by_xpath(supplier_register_checkbox_path)
        time.sleep(1)
        supplier_register_checkbox[1].click()
        time.sleep(1)

        supplier_register_createaccount_path =supplier_register.readfromXML(folder_path+'\Object\Object.xml','eTender','createaccount')
        supplier_register_createaccount = browser.find_element_by_xpath(supplier_register_createaccount_path)
        time.sleep(1)
        supplier_register_createaccount.click()
        time.sleep(10)

        supplier_backtologin_path =supplier_register.readfromXML(folder_path+'\Object\Object.xml','eTender','backtologin')
        supplier_backtologin = browser.find_element_by_xpath(supplier_backtologin_path)
        time.sleep(2)
        supplier_backtologin.click()
        time.sleep(2)
        return browser

    def supplierAuthorisation(self,browser):
        supplier_authorisation = DataDriver()
        time.sleep(1)
        supplier_authorisation_path =supplier_authorisation.readfromXML(folder_path+'\Object\Object.xml','eTender','supplier_authorisation')
        supplier_authorisationmenu = browser.find_element_by_link_text(supplier_authorisation_path)
        time.sleep(1)
        supplier_authorisationmenu.click()
        time.sleep(1)
        self.suppliersearch(browser)
        time.sleep(1)
        return browser

    def supplierAuthorisationLOAD(self,browser):
        supplier_authorisation = DataDriver()
        time.sleep(1)
        supplier_authorisation_path =supplier_authorisation.readfromXML(folder_path+'\Object\Object.xml','eTender','supplier_authorisation')
        supplier_authorisationmenu = browser.find_element_by_link_text(supplier_authorisation_path)
        time.sleep(1)
        supplier_authorisationmenu.click()
        time.sleep(1)
        return browser

    def supplierselection(self,browser):
        supplier_selection1 = DataDriver()
        time.sleep(1)
        supplier_selection_path =supplier_selection1.readfromXML(folder_path+'\Object\Object.xml','eTender','supplier-selection')
        time.sleep(2)
        supplier_selection = browser.find_element_by_xpath(supplier_selection_path)
        time.sleep(2)
        supplier_selection.click()
        time.sleep(2)
        return browser

    def supplierAccept(self,browser):
        supplier_authorisation = DataDriver()
        time.sleep(1)
        supplieraccept = []
        supplier_accept_path =supplier_authorisation.readfromXML(folder_path+'\Object\Object.xml','eTender','supplier-accept')
        supplieraccept = browser.find_elements_by_xpath(supplier_accept_path)

        time.sleep(2)
        supplieraccept[1].click()
        return browser

    def suppliersearch(self,browser):
        supplier_search = DataDriver()
        time.sleep(2)
        supplierslist = []
        time.sleep(2)
        supplier_search_path =supplier_search.readfromXML(folder_path+'\Object\Object.xml','eTender','supplier-search')
        time.sleep(2)
        supplierslist = browser.find_elements_by_xpath(supplier_search_path)
        time.sleep(2)

        supplieremail_data =supplier_search.readfromXML(folder_path+'\Data\Data.xml','eTender','supplier-email1')
        time.sleep(2)
        #supplierslist[1].send_keys(supplieremail_data)
        supplierslist[1].send_keys("t")
        time.sleep(1)
        supplierslist[1].send_keys("e")
        time.sleep(1)
        supplierslist[1].send_keys("s")
        time.sleep(1)
        supplierslist[1].send_keys("t")
        time.sleep(1)
        supplierslist[1].send_keys("@")
        time.sleep(1)
        supplierslist[1].send_keys("e")
        time.sleep(1)
        supplierslist[1].send_keys("te")
        time.sleep(1)
        supplierslist[1].send_keys("nd")
        time.sleep(1)
        supplierslist[1].send_keys("er")
        time.sleep(1)
        supplierslist[1].send_keys(".")
        time.sleep(1)
        supplierslist[1].send_keys("co")
        time.sleep(1)
        supplierslist[1].send_keys("m")
        time.sleep(4)

        supplier_selection_path =supplier_search.readfromXML(folder_path+'\Object\Object.xml','eTender','supplier-selection')
        time.sleep(2)
        supplier_selection = browser.find_element_by_xpath(supplier_selection_path)
        time.sleep(2)
        supplier_selection.click()
        time.sleep(2)
        return browser

    def usersearch(self,browser):
        supplier_search = DataDriver()
        time.sleep(2)
        supplierslist = []
        time.sleep(2)
        supplier_search_path =supplier_search.readfromXML(folder_path+'\Object\Object.xml','eTender','supplier-search')
        time.sleep(2)
        supplierslist = browser.find_elements_by_xpath(supplier_search_path)
        time.sleep(2)

        supplieremail_data =supplier_search.readfromXML(folder_path+'\Data\Data.xml','eTender','supplier-email1')
        time.sleep(2)
        #supplierslist[1].send_keys(supplieremail_data)AutomationTestTwo
        supplierslist[1].send_keys("Auto")
        time.sleep(1)
        supplierslist[1].send_keys("mati")
        time.sleep(1)
        supplierslist[1].send_keys("onTe")
        time.sleep(1)
        supplierslist[1].send_keys("stTwo")
        time.sleep(1)
        supplierslist[1].send_keys("@")
        time.sleep(1)
        supplierslist[1].send_keys("e")
        time.sleep(1)
        supplierslist[1].send_keys("te")
        time.sleep(1)
        supplierslist[1].send_keys("nd")
        time.sleep(1)
        supplierslist[1].send_keys("er")
        time.sleep(1)
        supplierslist[1].send_keys(".")
        time.sleep(1)
        supplierslist[1].send_keys("co")
        time.sleep(1)
        supplierslist[1].send_keys("m")
        time.sleep(4)

        supplier_selection_path =supplier_search.readfromXML(folder_path+'\Object\Object.xml','eTender','supplier-selection')
        time.sleep(2)
        supplier_selection = browser.find_element_by_xpath(supplier_selection_path)
        time.sleep(2)
        supplier_selection.click()
        time.sleep(2)
        return browser

    def userdetails(self,browser):
        Userdetails1 = DataDriver()
        time.sleep(1)
        userdetails_path =Userdetails1.readfromXML(folder_path+'\\Object\\UserProfileObject.xml','eTender','userDetails')
        userdetails_link = browser.find_element_by_link_text(userdetails_path)
        time.sleep(2)
        userdetails_link.click()
        time.sleep(4)
        return browser

    def selectusersmenu(self,browser):
        supplier_usermenu = DataDriver()
        time.sleep(1)
        supplier_list_path =supplier_usermenu.readfromXML(folder_path+'\\Object\\Object.xml','eTender','supplier_list')
        supplier_listmenu = browser.find_element_by_link_text(supplier_list_path)
        time.sleep(2)
        supplier_listmenu.click()
        time.sleep(4)
        return browser


    def supplierDeletion(self,browser):
        supplier_delete = DataDriver()
        time.sleep(2)
        supplier_delete_path =supplier_delete.readfromXML(folder_path+'\\Object\\Object.xml','eTender','supplier-delete')
        supplier_deletion = browser.find_element_by_link_text(supplier_delete_path)
        time.sleep(2)
        supplier_deletion.click()
        time.sleep(2)

        supplier_deleteconfirm_path =supplier_delete.readfromXML(folder_path+'\\Object\\Object.xml','eTender','supplier-deleteconfirm')
        supplier_deleteconfirm = browser.find_element_by_xpath(supplier_deleteconfirm_path)
        time.sleep(1)
        supplier_deleteconfirm.click()
        time.sleep(1)
        return browser

    def organisationmenu(self,browser):
        organisation_menu = DataDriver()
        time.sleep(1)
        organisation_path =organisation_menu.readfromXML(folder_path+'\\Object\\OrgProfileObject.xml','eTender','organisationmenu')
        organisationlist_menu = browser.find_element_by_link_text(organisation_path)
        time.sleep(2)
        organisationlist_menu.click()
        time.sleep(4)
        return browser

    def stagesmenu(self,browser):
        stagesmenu = DataDriver()
        time.sleep(1)
        stages_path =stagesmenu.readfromXML(folder_path+'\Object\OrgProfileObject.xml','eTender','stagesmenu')
        stages = browser.find_element_by_link_text(stages_path)
        stages.click()
        time.sleep(1)
        return browser

    def organisationsearch(self,browser):
        organisation_search = DataDriver()
        time.sleep(2)
        organisationslist = []
        time.sleep(2)
        organisationslist_path =organisation_search.readfromXML(folder_path+'\Object\OrgProfileObject.xml','eTender','organisation-search')
        time.sleep(2)
        organisationslist = browser.find_elements_by_xpath(organisationslist_path)
        time.sleep(2)

        organisation_data =organisation_search.readfromXML(folder_path+'\Data\OrganisationDetails.xml','eTender','orgname')
        time.sleep(2)
        #supplierslist[1].send_keys(supplieremail_data)
        organisationslist[0].send_keys("D")
        time.sleep(3)
        organisationslist[0].send_keys("o")
        time.sleep(3)
        organisationslist[0].send_keys("w")
        time.sleep(3)
        organisationslist[0].send_keys("ne")
        time.sleep(1)
        organisationslist[0].send_keys("rM")
        time.sleep(1)
        organisationslist[0].send_keys("ou")
        time.sleep(1)
        organisationslist[0].send_keys("ch")
        time.sleep(1)
        organisationslist[0].send_keys("el")
        time.sleep(1)
        organisationslist[0].send_keys("T")
        time.sleep(1)
        organisationslist[0].send_keys("e")
        time.sleep(1)
        organisationslist[0].send_keys("st")
        time.sleep(4)

        organisationDetails_path =organisation_search.readfromXML(folder_path+'\Object\OrgProfileObject.xml','eTender','organisationdetails')
        time.sleep(2)
        organisationDetails = browser.find_element_by_link_text(organisationDetails_path)
        time.sleep(2)
        organisationDetails.click()
        time.sleep(2)
        return browser

    def organisationsearchdelete(self,browser):
        organisation_searchdelete = DataDriver()
        time.sleep(2)
        organisationslist = []
        time.sleep(2)
        organisationslist_path =organisation_searchdelete.readfromXML(folder_path+'\Object\OrgProfileObject.xml','eTender','organisation-search')
        time.sleep(2)
        organisationslist = browser.find_elements_by_xpath(organisationslist_path)
        time.sleep(2)

        #organisation_data =organisation_search.readfromXML(folder_path+'\Data\OrganisationDetails.xml','eTender','orgnamedelete')CausewayTest
        #time.sleep(2)
        #supplierslist[1].send_keys(supplieremail_data)
        organisationslist[0].send_keys("C")
        time.sleep(3)
        organisationslist[0].send_keys("a")
        time.sleep(3)
        organisationslist[0].send_keys("u")
        time.sleep(3)
        organisationslist[0].send_keys("se")
        time.sleep(1)
        organisationslist[0].send_keys("wa")
        time.sleep(1)
        organisationslist[0].send_keys("y")
        time.sleep(1)
        organisationslist[0].send_keys("T")
        time.sleep(1)
        organisationslist[0].send_keys("e")
        time.sleep(1)
        organisationslist[0].send_keys("st")
        time.sleep(4)

        organisationdeletelink_path =organisation_searchdelete.readfromXML(folder_path+'\Object\OrgProfileObject.xml','eTender','organisationdeletelink')
        time.sleep(2)
        organisationdeletelink = browser.find_element_by_link_text(organisationdeletelink_path)
        time.sleep(2)
        organisationdeletelink.click()
        time.sleep(2)

        organisationdeleteconfirm_path =organisation_searchdelete.readfromXML(folder_path+'\Object\OrgProfileObject.xml','eTender','organisationdeleteconfirm')
        time.sleep(2)
        organisationdeleteconfirm = browser.find_element_by_xpath(organisationdeleteconfirm_path)
        time.sleep(2)
        organisationdeleteconfirm.click()
        time.sleep(2)
        return browser

    def organisationdetailsclose(self,browser):
        organisationdetails_close = DataDriver()
        time.sleep(1)
        organisationdetailsclose_path =organisationdetails_close.readfromXML(folder_path+'\Object\OrgProfileObject.xml','eTender','organisationdetailsClose')
        time.sleep(1)
        organisationDetailsclose_link = browser.find_element_by_xpath(organisationdetailsclose_path)
        time.sleep(1)
        organisationDetailsclose_link.click()
        time.sleep(1)
        return browser

    def userdetailsclose(self,browser):
        userdetails_close = DataDriver()
        time.sleep(1)
        userdetailsclose_path =userdetails_close.readfromXML(folder_path+'\\Object\\UserProfileObject.xml','eTender','closeuserdetails')
        time.sleep(1)
        userdetailsclose_link = browser.find_element_by_xpath(userdetailsclose_path)
        time.sleep(1)
        userdetailsclose_link.click()
        time.sleep(1)
        return browser
















