# Purpose: To execute all smoke test cases
#
# Author:      suresh.kumar
#
# Created:     23-08-2016
#
# Copyright:   (c) Causeway Technologies 2016
#
#-------------------------------------------------------------------------------
import unittest
import time
from HTMLTestRunner import HTMLTestRunner
import sys
import os
import smtplib
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
folder_path=os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0,folder_path+"\TestScript")
sys.path.insert(0,folder_path+"\SysLibrary")
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders

from openbrowser import Browseropen
from setupenviron import setupValue
from subcontractorlogin import Loginsubcontractor
from organisationDetails import detailsofOrganisation
from listOrganisation import Organisationlist
from listProject import Projectlist
from projectforSubcontractor import tradeslistSubcontractor
from tradeColumns import ColumnsinTradeList
from tenderSupplier import Suppliertender
from insertRates import Insertrates
from logout import LogouteTender
from hovermouse import Hovermouse
from dialogboxtoaddnote import Dialogboxtoaddnote
from addingNote import Addingnotes
from deletingNote import Deletingnotes
from tendererdocument import Tendererdocument
from uploaddocument import Uploaddocument
from deletedocument import Deletedocument
from submittender import Submittender
from confirmsubmittender import Confirmsubmittender
from Estimatorlogin import Loginestimator
from projectforEstimator import Estimatorproject
from tenderforEstimator import tradeslistEstimator
from notesinEstimator import Notesinestimator
from reopenTender import Reopentender
from deletingNote import Deletingnotes
from tenderQuickAccess import Tenderquickaccess
from tenderQuickItemAccess import Tenderquickitemaccess
from declinetender import Declinetender
from confirmdeclinetender import Confirmdeclinetender
from declineStatusinEstimator import Declinestatusinestimator
from changepasswordmenu import Changepasswordmenu
from changepasswordform import Changepasswordform
from loginwithchangepassword import Loginwithchangepassword
from RegisteruserTypes import Registerusertypes
from RegisterestimatoruserTypes import Registerestimatorusertypes
from registersuppliernewORG import RegistersuppliernewORG
from registersupplierselectORG import RegistersupplierselectORG
from registerestimatornewORG import RegisterestimatornewORG
from registerestimatorselectORG import RegisterestimatorselectORG
from registerestimatoradminnewORG import RegisterestimatoradminnewORG
from registerestimatoradminselectORG import RegisterestimatoradminselectORG
from viewdocument import Viewdocument
from sendmessagetoestimator import Sendmessagetoestimator
from clearmessage import ClearmessageinEditor
from tendererorganisationinestimator import TendererorganisationinEstimator
from activetendersinestimator import Activetendersinestimator
from estimatorshowvalue import Estimatorshowvalue
from viewpricableitems import Viewpricableitems
from tenderQuickAccessinEstimator import Tenderquickaccessinestimator
from tenderQuickItemAccessinestimator import Tenderquickitemaccessinestimator
from createprojectAPI import Createprojectfromapi
from createtenderAPI import Createtenderfromapi
from tenderdetailsAPI import Createtenderdetialsfromapi
from OrganisationprofilePage import Organisationprofile
from OrganisationprofilePageUpdateName import OrganisationprofileUpdateName
from OrganisationprofilePageValidatedetailsinSuperadmin import OrganisationprofileValidatedetailsinSuperadmin
from UserprofileinEstimator import Userprofileinestimator
from Userprofileinfoupdate import UserProfileinfoupdate
from UserprofilePageValidatedetailsinSuperadmin import UserprofileValidatedetailsinSuperadmin
from createindependentproject import Createindependentproject
from deleteindependentproject import Deleteindependentproject
from updateindependentprojectdetails import Updateindependentproject
from startduedatesinprojectdetails import Startduedateinprojectdetails
from Duplicateindependentproject import duplicateindependentproject
from projecttypeinprojectdetails import Projecttypeinprojectdetails
from projectdetails import Projectdetails
from projectpagination import Projectpagination
from currencyinprojectdetails import Currencyinprojectdetails
from currencyintenderdetails import Currencyintenderdetails
from currencyinprojectsupplierlogin import Currencyinprojectsupplierlogin
from currencyintendersupplierlogin import Currencyintendersupplierlogin
#added on 30/06/17
from tradexsuppliercontact import Tradexsuppliercontact
from selecttradexsuppliercontact import Selecttradexsuppliercontact
from deletetradexsuppliercontact import Deletetradexsuppliercontact
from sendtoenquirysuccessmessage import Sendtoenquirysuccessmessage
from supplierlistundertrade import Supplierlistundertrade

#added on 03/07/17
from currencychangeinprojectUS import CurrencychangeinprojectUS
from currencychangeinprojectEURO import CurrencychangeinprojectEURO
from currencychangeinprojectYEN import CurrencychangeinprojectYEN

#added on 03/07/17
from currencychangeinprojectUS import CurrencychangeinprojectUS
from currencychangeinprojectEURO import CurrencychangeinprojectEURO
from currencychangeinprojectYEN import CurrencychangeinprojectYEN

#added on 25/07/17
from plantemplate import Plantemplate
from plantemplatecreationheading import Plantemplatecreationheading
from plantemplatecreation import Plantemplatecreation
from plantemplatecreationwithstages import Plantemplatecreationwithstages
from plantemplatealertmessage import Plantemplatealertmessage
from plantemplatedeletion import Plantemplatedeletion
from plantemplateupdation import Plantemplateupdation
from plantemplatecount import Plantemplatecount
from plantemplatechoose import Plantemplatechoose

#added on 25/07/17
from plantemplatesave import Plantemplatesave
from plantenderview import Plantenderview

#added on 31/07/17
from plantemplateplanneddates import Plantemplateplanneddates
from plantemplateforecastdates import Plantemplateforecastdates
from plantemplateplannedexclamation import Plantemplateplannedexclamation
from plantemplateforecastexclamation import Plantemplateforecastexclamation
from plantemplatestagdelete import Plantemplatestagdelete
from plantemplatestagaddition import Plantemplatestagaddition
from plantemplatestagadditiondatecheck import Plantemplatestagadditiondatecheck
from plantemplatestagdurationupdation import Plantemplatestagdurationupdation

#added on 01/08/17
from plantemplatenotesforallstages import Plantemplatenotesforallstages
from plantemplatenotesupdate import Plantemplatenotesupdate
from plantemplatenotesdelete import Plantemplatenotesdelete
from plantemplatenotesforfirststag import Plantemplatenotesforfirststag
from plantemplatestagnotesupdate import Plantemplatestagnotesupdate
from plantemplatestagnotesdelete import Plantemplatestagnotesdelete
from plantemplateactualforecastdates import Plantemplateactualforecastdates

#added on 02/08/17
from plantemplateactualresetplanned import Plantemplateactualresetplanned
from plantemplatestagstatuscompleted import Plantemplatestagstatuscompleted
from warningwhennorates import Warningwhennorates

#Pairwiser Staging
from updateprojectdetailsBuildingEnvelopeStaging import UpdateprojectdetailsBuildingEnvelops
from updateprojectdetailsDrainageStaging import UpdateprojectdetailsDrainage
from updateprojectdetailsHighwaysStaging import UpdateprojectdetailsHighways
from updateprojectdetailsHousingStaging import UpdateprojectdetailsHousing
from updateprojectdetailsInfrastructuresStaging import UpdateprojectdetailsInfrastructures
from updateprojectdetailsNoneStaging import UpdateprojectdetailsNone
from updateprojectdetailsOfficesStaging import UpdateprojectdetailsOffices
from updateprojectdetailsRefurbishmentStaging import UpdateprojectdetailsRefurbishment
from updateprojectdetailsSchoolsStaging import UpdateprojectdetailsSchools
from updateprojectdetailsShopfittingStaging import UpdateprojectdetailsShopfitting
from updateprojectdetailsShopsStaging import UpdateprojectdetailsShops
from updateprojectdetailsSportsComplexStaging import UpdateprojectdetailsSportsComplex
from updateprojectdetailsStructuresStaging import UpdateprojectdetailsStructures
from Emailsetup import EmailSend
from AT_AddUsertoOrganization import AddUserOrganization
from AT_AddRoletoUser import AddRoletoUserInOrg
from AT_RemoveRoletoUser import RemoveRoletoUserInOrg
from AT_MinimumRoletoUser import MinimumRoletoUserInOrg
from AT_RemoveUserfromOrganization import RemoveUserOrganization
from AT_CancelAddUsertoOrganization import CancelButtonInAddUser
from AT_UserSelectionforRole import UserSelectionForRole
from AT_ProfilePageUIverification import ProfileOrganizationUI
from AT_ProfileResetfunction import ProfileResetButton
from AT_ProfileSavefunction import ProfileSaveButton
from AT_ProfileLocationSetfunction import Profilelocationselection
from AT_ResetButtonVerification import ResetButtonInAddUser
from AT_SelectUsertoOrganizationMessage import SelectUserMessage
from AT_UserProfileResetfunction import UserProfileResetButton
from AT_UserProfileSavefunction import UserProfileSaveButton
from AT_UserProfileLocationSet import UserProfilelocationselection
from AT_UserProfileUIverification import UserProfileUI
from AT_ProjectOpenOrganization import Organizationinproject
from AT_NotificationAddReceipients import NotificationaddUser
from AT_NotificationMinimumReceipients import NotificationMinimumUser
from AT_CreateNewTag import CreateNewTag
from AT_DeleteTag import DeleteTag
from AT_VerifyDuplicateTag import DuplicateTag
from AT_TaskSchedulerSave import SaveTaskScheduler
from AT_TaskSchedulerReset import ResetTaskScheduler
#Newly added code
from AT_NotificationTemplateSave import NotificationTemplateSave
from AT_NotificationMessageOption import NotificationMessageOption
from AT_NotificationMessageTemplate import NotificationMessageTemplate
from AT_NotificationTemplateCancel import NotificationTemplateCancel

#Added on 26/05/2017
from AT_TenderCreation import TenderCreationClass
from AT_TenderDeletion import TenderDeletionClass
from AT_TenderUpdation import TenderUpdationClass
from AT_ResetTender import TenderResetClass
from AT_BackToTenderlist import TenderList

#Added on 20/07/2017
from AT_SupplierLookup import SupplierLookup

#Added on 03/07/2017
from AT_TenderSearch import TenderSearchClass

#Added 24/07/2017
from AT_CancelPlanTemplate import CancelPlanTemplate
from AT_PreviewPlanTemplate import PreviewPlan
from AT_SelectPlanTemplate import SelectPlanTemplate

#Added 01/08/2017
from AT_PlanTemplateAlreadySelected import PlanTemplateSelected
from AT_StageCompletedStatus import StatusStageCompleted
from AT_StageCompletedLateStatus import StatusStageCompletedLate
from AT_StageOntimeStatus import StageOntimeStatus
from AT_StatusActualDateCancel import ActualDateCancel

setup = setupValue()
setup.folderCreation()
setup.folderCreation()
suite = unittest.TestSuite()


##suite.addTest(Organizationinproject('OpenOrganization'))
##suite.addTest(UserProfileUI('ProfileUI'))
##suite.addTest(UserProfilelocationselection('UserProfilelocation'))
##suite.addTest(UserProfileSaveButton('UserProfileSave'))
##suite.addTest(UserProfileResetButton('ProfileReset'))
##suite.addTest(Profilelocationselection('Profilelocation'))
##suite.addTest(ProfileSaveButton('ProfileSave'))
##suite.addTest(ProfileResetButton('ProfileReset'))
##suite.addTest(ProfileOrganizationUI('ProfileUI'))
##suite.addTest(AddRoletoUserInOrg('addroletoUser'))
##suite.addTest(RemoveRoletoUserInOrg('removeroletoUser'))
##suite.addTest(MinimumRoletoUserInOrg('minimumroletoUser'))
##suite.addTest(AddUserOrganization('addUsertoOrg'))
##suite.addTest(ResetButtonInAddUser('resetButton'))
##suite.addTest(RemoveUserOrganization('removeUsertoOrg'))
##suite.addTest(CancelButtonInAddUser('cancelButton'))
##suite.addTest(UserSelectionForRole('userSelectionverification'))
##suite.addTest(SelectUserMessage('messageforAddUser'))
##suite.addTest(AddRoletoUserInOrg('addroletoUser'))
##suite.addTest(Browseropen('test_openbrowser'))
##suite.addTest(Loginsubcontractor('test_SubcontractorlogineTender'))
##suite.addTest(detailsofOrganisation('test_OrganidetailsofOrganisation'))
##suite.addTest(Organisationlist('test_Organisationlist'))
##suite.addTest(Projectlist('test_Projectlist'))
##suite.addTest(tradeslistSubcontractor('test_tenderdetails'))
##suite.addTest(ColumnsinTradeList('test_ColumnsinTradeList'))
##suite.addTest(Suppliertender('test_suppliertender'))
##suite.addTest(Insertrates('test_Insertrates'))
##suite.addTest(LogouteTender('test_LogouteTender'))
##suite.addTest(Hovermouse('test_hoverMouse'))
##suite.addTest(Dialogboxtoaddnote('test_dialogboxtoAddnote'))
##suite.addTest(Addingnotes('test_addingNotes'))
##suite.addTest(Tendererdocument('test_tendererdocment'))
#suite.addTest(Uploaddocument('test_uploaddocment'))
#uite.addTest(Deletedocument('test_deletedocment'))
##suite.addTest(Submittender('test_submittender'))
##suite.addTest(Confirmsubmittender('test_Confirmsubmittender'))
##suite.addTest(Loginestimator('test_EstimatorlogineTender'))
##suite.addTest(Estimatorproject('test_estimatorproject'))
##suite.addTest(tradeslistEstimator('test_tenderdetails'))
##suite.addTest(Notesinestimator('test_notesinEstimator'))
##suite.addTest(Reopentender('test_reopenTender'))
##suite.addTest(Deletingnotes('test_deletingNotes'))
##suite.addTest(Tenderquickaccess('test_tenderquickaccess'))
##suite.addTest(Tenderquickitemaccess('test_tenderquickitemaccess'))
##suite.addTest(Declinetender('test_declinetender'))
##suite.addTest(Confirmdeclinetender('test_confirmdeclinetender'))
##suite.addTest(Declinestatusinestimator('test_declineStatusinEstiamtor'))
##suite.addTest(Changepasswordmenu('test_changepasswordmenu'))
##suite.addTest(Changepasswordform('test_changepasswordform'))
##suite.addTest(Loginwithchangepassword('test_loginwithchangepassword'))
##suite.addTest(Registerusertypes('test_registerusertypes'))
##suite.addTest(Registerestimatorusertypes('test_registerestimatorusertypes'))
##suite.addTest(RegistersuppliernewORG('test_registersupplierneworg'))
##suite.addTest(RegistersupplierselectORG('test_registersupplierselectorg'))
##suite.addTest(RegisterestimatornewORG('test_registerestimatorneworg'))
##suite.addTest(RegisterestimatorselectORG('test_registerestimatorselectorg'))
##suite.addTest(RegisterestimatoradminnewORG('test_registerestimatoradminneworg'))
##suite.addTest(RegisterestimatoradminselectORG('test_registerestimatoradminselectorg'))
#suite.addTest(Viewdocument('test_viewdocument'))
##suite.addTest(Sendmessagetoestimator('test_sendmessagetoestimator'))
##suite.addTest(ClearmessageinEditor('test_clearmessageineditor'))
##suite.addTest(TendererorganisationinEstimator('test_Tendererorganisationinestimator'))
##suite.addTest(Activetendersinestimator('test_activetendersinEstimator'))
##suite.addTest(Estimatorshowvalue('test_estimatorshowvalue'))
##suite.addTest(Viewpricableitems('test_viewpricableitems'))
##suite.addTest(Tenderquickaccessinestimator('test_tenderquickaccessinestimator'))
##suite.addTest(Tenderquickitemaccessinestimator('test_tenderquickitemaccessinestimator'))
##suite.addTest(Createprojectfromapi('test_createprojectfromapi'))
##suite.addTest(Createtenderfromapi('test_createtenderfromapi'))
##suite.addTest(Createtenderdetialsfromapi('test_createtenderdetialsfromapi'))
##suite.addTest(Organisationprofile('test_Organisationprofile'))
#suite.addTest(OrganisationprofileUpdateName('test_OrganisationprofileupdateName'))
#suite.addTest(OrganisationprofileValidatedetailsinSuperadmin('test_OrganisationprofileValidatedetailsinSuperadmin'))
##suite.addTest(Userprofileinestimator('test_Userprofileinestimator'))
##suite.addTest(UserProfileinfoupdate('test_UserProfileinfoupdate'))
##suite.addTest(UserprofileValidatedetailsinSuperadmin('test_UserprofileValidatedetailsinSuperadmin'))
##suite.addTest(Createindependentproject('test_createindependentproject'))
##suite.addTest(Deleteindependentproject('test_deleteindependentproject'))
##suite.addTest(Updateindependentproject('test_updateindependentproject'))
##suite.addTest(Startduedateinprojectdetails('test_startduedateinprojectdetails'))
##suite.addTest(duplicateindependentproject('test_duplicateindependentproject'))
##
##suite.addTest(Projecttypeinprojectdetails('test_projecttypeinprojectdetails'))
##suite.addTest(Projectdetails('test_Projectdetails'))
##suite.addTest(Projectpagination('test_projectpagination'))
##
### Currency 21/06/17
##suite.addTest(Currencyinprojectdetails('test_currencyinprojectdetails'))
##suite.addTest(Currencyintenderdetails('test_currencyintenderdetails'))
##
### Currency 22/06/17
##suite.addTest(Currencyinprojectsupplierlogin('test_currencyinprojectsupplierlogin'))
##suite.addTest(Currencyintendersupplierlogin('test_currencyintendersupplierlogin'))
##
###added on 30/06/17
##suite.addTest(Tradexsuppliercontact('test_tradexsuppliercontact'))
##suite.addTest(Selecttradexsuppliercontact('test_selecttradexsuppliercontact'))
##suite.addTest(Deletetradexsuppliercontact('test_deletetradexsuppliercontact'))
##suite.addTest(Sendtoenquirysuccessmessage('test_sendtoenquirysuccessmessage'))
##suite.addTest(Supplierlistundertrade('test_supplierlistundertrade'))
##
### Currency 03/07/17
##suite.addTest(CurrencychangeinprojectUS('test_currencychangeinprojectUS'))
##suite.addTest(CurrencychangeinprojectEURO('test_currencychangeinprojectEURO'))
##suite.addTest(CurrencychangeinprojectYEN('test_currencychangeinprojectYEN'))
##
##suite.addTest(ResetTaskScheduler('TaskSchedulerReset'))
##suite.addTest(SaveTaskScheduler('TaskSchedulerSave'))
##suite.addTest(CreateNewTag('newtagcreation'))
##suite.addTest(DeleteTag('tagdeletion'))
##suite.addTest(DuplicateTag('duplicatetagverification'))
##suite.addTest(NotificationaddUser('AddUsernotification'))
##suite.addTest(NotificationMinimumUser('MinimumUsernotification'))
##
###Pairwiser
##suite.addTest(UpdateprojectdetailsBuildingEnvelops('test_updateprojectdetailsBuildingEnvelops'))
##suite.addTest(UpdateprojectdetailsDrainage('test_updateprojectdetailsDrainage'))
##suite.addTest(UpdateprojectdetailsHighways('test_updateprojectdetailsHighways'))
##suite.addTest(UpdateprojectdetailsHousing('test_updateprojectdetailsHousing'))
##suite.addTest(UpdateprojectdetailsInfrastructures('test_updateprojectdetailsInfrastructures'))
##suite.addTest(UpdateprojectdetailsNone('test_updateprojectdetailsNone'))
##suite.addTest(UpdateprojectdetailsOffices('test_updateprojectdetailsOffices'))
##suite.addTest(UpdateprojectdetailsRefurbishment('test_updateprojectdetailsRefurbishment'))
##suite.addTest(UpdateprojectdetailsSchools('test_updateprojectdetailsSchools'))
##suite.addTest(UpdateprojectdetailsShopfitting('test_updateprojectdetailsShopfitting'))
##suite.addTest(UpdateprojectdetailsShops('test_updateprojectdetailsShops'))
##suite.addTest(UpdateprojectdetailsSportsComplex('test_updateprojectdetailsSportsComplex'))
##suite.addTest(UpdateprojectdetailsStructures('test_updateprojectdetailsStructures'))

#added on 25/07/17
suite.addTest(Plantemplate('test_Plantemplate'))
suite.addTest(Plantemplatecreationheading('test_Plantemplatecreationheading'))
suite.addTest(Plantemplatecreation('test_Plantemplatecreation'))
suite.addTest(Plantemplatecreationwithstages('test_Plantemplatecreationwithstages'))
suite.addTest(Plantemplatealertmessage('test_plantemplatealertmessage'))
suite.addTest(Plantemplatedeletion('test_Plantemplatedeletion'))
suite.addTest(Plantemplateupdation('test_Plantemplateupdation'))
suite.addTest(Plantenderview('test_Plantenderview'))
suite.addTest(Plantemplatecount('test_plantemplatecount'))
suite.addTest(Plantemplatechoose('test_plantemplatechoose'))

#added on 31/07/17
suite.addTest(Plantemplateplanneddates('test_Plantemplateplanneddates'))
suite.addTest(Plantemplateplannedexclamation('test_Plantemplateplannedexclamation'))

suite.addTest(Plantemplatestagdelete('test_Plantemplatestagdelete'))
suite.addTest(Plantemplatestagaddition('test_Plantemplatestagaddition'))
suite.addTest(Plantemplatestagadditiondatecheck('test_Plantemplatestagadditiondatecheck'))
suite.addTest(Plantemplatestagdurationupdation('test_Plantemplatestagdurationupdation'))

#added on 30/06/17
##suite.addTest(Tradexsuppliercontact('test_tradexsuppliercontact'))
##suite.addTest(Selecttradexsuppliercontact('test_selecttradexsuppliercontact'))
##suite.addTest(Deletetradexsuppliercontact('test_deletetradexsuppliercontact'))
##suite.addTest(Sendtoenquirysuccessmessage('test_sendtoenquirysuccessmessage'))
##suite.addTest(Supplierlistundertrade('test_supplierlistundertrade'))

# Currency 03/07/17
suite.addTest(CurrencychangeinprojectUS('test_currencychangeinprojectUS'))
suite.addTest(CurrencychangeinprojectEURO('test_currencychangeinprojectEURO'))
suite.addTest(CurrencychangeinprojectYEN('test_currencychangeinprojectYEN'))

suite.addTest(ResetTaskScheduler('TaskSchedulerReset'))
suite.addTest(SaveTaskScheduler('TaskSchedulerSave'))
suite.addTest(CreateNewTag('newtagcreation'))
suite.addTest(DeleteTag('tagdeletion'))
suite.addTest(DuplicateTag('duplicatetagverification'))
suite.addTest(NotificationaddUser('AddUsernotification'))
suite.addTest(NotificationMinimumUser('MinimumUsernotification'))

#added on 25/07/17
suite.addTest(Plantemplatesave('test_Plantemplatesave'))

#added on 25/07/17
suite.addTest(Plantemplate('test_Plantemplate'))
suite.addTest(Plantemplatecreationheading('test_Plantemplatecreationheading'))
suite.addTest(Plantemplatecreation('test_Plantemplatecreation'))
suite.addTest(Plantemplatecreationwithstages('test_Plantemplatecreationwithstages'))
suite.addTest(Plantemplatealertmessage('test_plantemplatealertmessage'))
suite.addTest(Plantemplatedeletion('test_Plantemplatedeletion'))
suite.addTest(Plantemplateupdation('test_Plantemplateupdation'))
suite.addTest(Plantenderview('test_Plantenderview'))
suite.addTest(Plantemplatecount('test_plantemplatecount'))
suite.addTest(Plantemplatechoose('test_plantemplatechoose'))

#added on 31/07/17
suite.addTest(Plantemplateplanneddates('test_Plantemplateplanneddates'))
suite.addTest(Plantemplateforecastdates('test_Plantemplateforecastdates'))
suite.addTest(Plantemplateplannedexclamation('test_Plantemplateplannedexclamation'))
suite.addTest(Plantemplateforecastexclamation('test_Plantemplateforecastexclamation'))
suite.addTest(Plantemplatestagdelete('test_Plantemplatestagdelete'))
suite.addTest(Plantemplatestagaddition('test_Plantemplatestagaddition'))
suite.addTest(Plantemplatestagadditiondatecheck('test_Plantemplatestagadditiondatecheck'))
suite.addTest(Plantemplatestagdurationupdation('test_Plantemplatestagdurationupdation'))

#added on 01/08/17
suite.addTest(Plantemplatenotesforallstages('test_Plantemplatenotesforallstages'))
suite.addTest(Plantemplatenotesupdate('test_Plantemplatenotesupdate'))
suite.addTest(Plantemplatenotesdelete('test_Plantemplatenotesdelete'))
suite.addTest(Plantemplatenotesforfirststag('test_Plantemplatenotesforfirststag'))
suite.addTest(Plantemplatestagnotesupdate('test_Plantemplatestagnotesupdate'))
suite.addTest(Plantemplatestagnotesdelete('test_Plantemplatestagnotesdelete'))

#added on 25/07/17
suite.addTest(Plantemplatesave('test_Plantemplatesave'))

#added on 01/08/17
suite.addTest(Plantemplateactualforecastdates('test_Plantemplateactualforecastdates'))

#added on 02/08/17
suite.addTest(Plantemplateactualresetplanned('test_Plantemplateactualresetplanned'))
suite.addTest(Plantemplatestagstatuscompleted('test_Plantemplatestagstatuscompleted'))
suite.addTest(Warningwhennorates('test_Warningwhennorates'))

suite.addTest(NotificationTemplateCancel('MessageTemplateCancel'))
##suite.addTest(NotificationTemplateSave('MessageTemplateSave'))
##suite.addTest(NotificationMessageTemplate('MessageTemplateOption'))
##suite.addTest(NotificationMessageOption('MessageOption'))

###Added on 26/05/2017
##suite.addTest(TenderCreationClass('TenderCreationfunction'))
##suite.addTest(TenderDeletionClass('TenderDeletionfunction'))
##suite.addTest(TenderUpdationClass('TenderUpdationfunction'))
##suite.addTest(TenderResetClass('TenderResetfunction'))
##suite.addTest(TenderList('TenderListfunction'))
##
##suite.addTest(SupplierLookup('Supplierfunction'))
#Added on 28/06/2017
#Added on 01/08/2017

#Added on 01/08/2017
suite.addTest(PlanTemplateSelected('TemplateSelected'))
suite.addTest(StatusStageCompleted('StageCompleted'))
suite.addTest(StatusStageCompletedLate('StageCompletedLate'))
suite.addTest(StageOntimeStatus('OntimeStatus'))
suite.addTest(ActualDateCancel('CancelDate'))

ftime = time.mktime(time.localtime())
ptime=time.strftime("%d-%m-%Y_%H%M%S", time.localtime(ftime))
filename = 'SmokeTestExecutionReport-{0}.html'.format(ptime)
sfilename = filename
path= setupValue().reportpath
fullpath = os.path.join(path,filename)
if not os.path.exists(os.path.dirname(fullpath)):
    os.makedirs(os.path.dirname(fullpath))
outfile = file(fullpath, 'w+')
runner = HTMLTestRunner(stream=outfile,
                        verbosity=2,
                        title='eTender automation report',
                        description='Test Case Execution Results')
runner.run(suite)
outfile.close()
time.sleep(5)
emailsending=EmailSend()
emailsending.mailSend(fullpath,filename)

