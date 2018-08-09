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
import sys
import os
import smtplib
#
dir_path = os.path.dirname(os.path.realpath(__file__))
folder_path=os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0,folder_path+"\TestScript")
sys.path.insert(0,folder_path+"\SysLibrary")
sys.path.insert(0,folder_path+"\Library")
from HTMLTestRunner import HTMLTestRunner
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
#
#added on 01/08/17
from plantemplatenotesforallstages import Plantemplatenotesforallstages
from plantemplatenotesupdate import Plantemplatenotesupdate
from plantemplatenotesdelete import Plantemplatenotesdelete
from plantemplatenotesforfirststag import Plantemplatenotesforfirststag
from plantemplatestagnotesupdate import Plantemplatestagnotesupdate
from plantemplatestagnotesdelete import Plantemplatestagnotesdelete
from plantemplateactualforecastdates import Plantemplateactualforecastdates
#
#added on 02/08/17
from plantemplateactualresetplanned import Plantemplateactualresetplanned
from plantemplatestagstatuscompleted import Plantemplatestagstatuscompleted
from warningwhennorates import Warningwhennorates

#added on 25/09/17
from tenderdefaultitem import Tenderdefaultitem
from tenderedititemdefault import Tenderedititemdefault
from tenderadditem import Tenderadditem
from tenderitemupdate import Tenderitemupdate
from tenderitemdelete import Tenderitemdelete
from tenderitemintenderpage import Tenderitemintenderpage
from tenderitemselectcount import Tenderitemselectcount
from tenderlistviewafterdeleteitem import Tenderlistviewafterdeleteitem
from tenderitemsimport import Tenderitemsimport

#added on 06/10/17
from viewnewbillitems import Viewnewbillitems

#added on 10/10/17
from pendingtradefilter import Pendingtradefilter

#added on 05/12/17
from tendercreationBalconiesTrade import TendercreationBalconiesTrade
from tendercreationBalconiesSupplier import TendercreationBalconiesSupplier
from tendercreationBalustradingMaterial import TendercreationBalustradingMaterial
from tendercreationBalustradingTrade import TendercreationBalustradingTrade
from tendercreationBalustradingSupplier import TendercreationBalustradingSupplier
from tendercreationBalconiesMaterial import TendercreationBalconiesMaterial
from tendercreationBalustradingDuplicate import TendercreationBalustradingDuplicate

#added on 06/12/17
from tenderverificationOFF import TenderverificationOFF
from tenderverificationONStatus import TenderverificationONStatus
from tenderverificationONSupplierStatus import TenderverificationONSupplierStatus
from tenderverificationON import TenderverificationON
from tenderverifiedON import TenderverifiedON

#added 08/02/2018
from selectalldocuments import Selectalldocuments
from addhyperlinkdisplayed import Addhyperlinkdisplayed
from hyperlinklabels import Hyperlinklabels
from addURLasFile import AddURLasFile
from documentlinkfileURL import DocumentlinkfileURL
from addInternalURL import AddInternalURL
from internaldocumentlinkfileURL import InternaldocumentlinkfileURL
from addexternalURL import AddexternalURL
from externaldocumentlinkfileURL import ExternaldocumentlinkfileURL

#added 14/02/2018
from invitecolleague import Invitecolleague
from invitecolleaguelink import Invitecolleaguelink
from verifycolleaguelist import Verifycolleaguelist
from invitecolleaguesearch import Invitecolleaguesearch
from invitecolleaguenotinthelist import Invitecolleaguenotinthelist
from invitecolleagueloggeduser import Invitecolleagueloggeduser

#Added on 15/02/2018
from estimatorinvalidpassword import Estimatorinvalidpassword
from invalidloginattemptafter5times import Invalidloginattemptafter5times
from loginattemptafter5mins import Loginattemptafter5mins

#Added on 14/03/2018
from hintinSuperadminonehint import HintinSuperadminonehint
from hintinSuperadmintwohints import HintinSuperadmintwohints
from hintinSuperadminafterLogout import HintinSuperadminafterLogout
from showhintAgaininSuperadmin import ShowhintAgaininSuperadmin
from hintWithoverlayinSuperadmin import HintWithoverlayinSuperadmin

#Added on 27/03/2018
from hintforpathvariable import Hintforpathvariable

#added on 24/10/17
from viewdeleteditemsinestimator import Viewdeleteditemsinestimator
from viewdeleteditemsinsupplier import Viewdeleteditemsinsupplier

#added on 13/10/17
from plantemplatestartasforecastdate import Plantemplatestartasforecastdate
from plantemplateduedateasforecastdate import Plantemplateduedateasforecastdate
from plantemplateAutofillstartasforecastdate import PlantemplateAutofillstartasforecastdate
from plantemplateAutofillduedateasforecastdate import PlantemplateAutofillduedateasforecastdate

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
#
#Added on 26/05/2017
from AT_TenderCreation import TenderCreationClass
from AT_TenderDeletion import TenderDeletionClass
from AT_TenderUpdation import TenderUpdationClass
from AT_ResetTender import TenderResetClass
from AT_BackToTenderlist import TenderList
#
#Added on 20/07/2017
from AT_SupplierLookup import SupplierLookup
#
#Added on 03/07/2017
from AT_TenderSearch import TenderSearchClass
#
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
#Added on 17/10/2017
from AT_StartDateAsForeCast import StartDateAsForecast
from AT_DueDateAsForeCast import DueDateAsForecast
from AT_ExportToExcel import ExportToExcel
from AT_ResponseToExcel import ExportToDetailsExcel
from AT_FootnoteSettings import FootNoteClass
from AT_EmailSetupPageverification import EmailSetupPage
from AT_TenderReturnSaveSettings import TenderVerifySave
from AT_TenderReturnResetSettings import TenderVerifyReset

setup = setupValue()
setup.folderCreation()
setup.folderCreation()
suite = unittest.TestSuite()

#Added on 14/03/2018
##suite.addTest(HintinSuperadminonehint('test_hintinSuperadminonehint'))
##suite.addTest(HintinSuperadmintwohints('test_hintinSuperadmintwohints'))
##suite.addTest(HintinSuperadminafterLogout('test_hintinSuperadminafterLogout'))
##suite.addTest(ShowhintAgaininSuperadmin('test_showhintAgaininSuperadmin'))
##suite.addTest(HintWithoverlayinSuperadmin('test_hintWithoverlayinSuperadmin'))
##
###Added on 27/03/2018
##suite.addTest(Hintforpathvariable('test_hintforpathvariable'))

suite.addTest(Organizationinproject('test_OpenOrganization'))
suite.addTest(UserProfileUI('test_userProfileUI'))
suite.addTest(UserProfilelocationselection('test_UserProfilelocation'))
suite.addTest(UserProfileSaveButton('test_UserProfileSave'))
suite.addTest(UserProfileResetButton('test_ProfileReset'))
suite.addTest(Profilelocationselection('test_Profilelocation'))
suite.addTest(ProfileSaveButton('test_ProfileSave'))
suite.addTest(ProfileResetButton('test_ProfileReset'))
suite.addTest(ProfileOrganizationUI('test_ProfileUI'))
suite.addTest(AddRoletoUserInOrg('test_addroletoUser'))
suite.addTest(RemoveRoletoUserInOrg('test_removeroletoUser'))
suite.addTest(MinimumRoletoUserInOrg('test_minimumroletoUser'))
suite.addTest(AddUserOrganization('test_addUsertoOrg'))
suite.addTest(ResetButtonInAddUser('test_resetButton'))
suite.addTest(RemoveUserOrganization('test_removeUsertoOrg'))
suite.addTest(CancelButtonInAddUser('test_cancelButton'))
suite.addTest(UserSelectionForRole('test_userSelectionverification'))
suite.addTest(SelectUserMessage('test_messageforAddUser'))

#Newly Added scripts
suite.addTest(NotificationTemplateCancel('test_MessageTemplateCancel'))
suite.addTest(NotificationTemplateSave('test_MessageTemplateSave'))
suite.addTest(NotificationMessageTemplate('test_MessageTemplateOption'))
suite.addTest(NotificationMessageOption('test_MessageOption'))

#Added on 26/05/2017
suite.addTest(TenderCreationClass('test_TenderCreationfunction'))
suite.addTest(TenderDeletionClass('test_TenderDeletionfunction'))
suite.addTest(TenderUpdationClass('test_TenderUpdationfunction'))
suite.addTest(TenderResetClass('test_TenderResetfunction'))
suite.addTest(TenderList('test_TenderListfunction'))

#Added on 28/06/2017
suite.addTest(SupplierLookup('test_Supplierfunction'))

#Added on 01/08/2017
suite.addTest(PlanTemplateSelected('test_TemplateSelected'))
suite.addTest(StatusStageCompleted('test_StageCompleted'))
suite.addTest(StatusStageCompletedLate('test_StageCompletedLate'))
suite.addTest(StageOntimeStatus('test_OntimeStatus'))
suite.addTest(ActualDateCancel('test_CancelDate'))

#Added on 17/10/2017
suite.addTest(StartDateAsForecast('test_ForeCastDate'))
suite.addTest(DueDateAsForecast('test_DueCastDate'))
suite.addTest(ExportToExcel('test_ExcelExport'))
suite.addTest(ExportToDetailsExcel('test_ExcelDetailsExport'))

#Added on 01/12/2017

suite.addTest(FootNoteClass('test_FootNote'))
suite.addTest(EmailSetupPage('test_SetupEmailPage'))
suite.addTest(TenderVerifySave('test_TenderReturnSaveVerify'))
suite.addTest(TenderVerifyReset('test_TenderReturnVerifyReset'))

suite.addTest(ResetTaskScheduler('test_TaskSchedulerReset'))
suite.addTest(SaveTaskScheduler('test_TaskSchedulerSave'))
suite.addTest(CreateNewTag('test_newtagcreation'))
suite.addTest(DeleteTag('test_tagdeletion'))
suite.addTest(DuplicateTag('test_duplicatetagverification'))
suite.addTest(NotificationaddUser('test_AddUsernotification'))
suite.addTest(NotificationMinimumUser('test_MinimumUsernotification'))


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
                        description='Test Case Execution Results',
                        dirTestScreenshots=folder_path+'\Screenshots'
                        )
runner.run(suite)
outfile.close()
time.sleep(5)
emailsending=EmailSend()
emailsending.mailSend(fullpath,filename)

