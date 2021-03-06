# Purpose: To execute test cases and update result in qTest
#
# Author:      mathew.jacob
#
# Created:     02-02-2018
#
# Copyright:   (c) Causeway Technologies 2016
#
#-------------------------------------------------------------------------------
import time
import sys
import os

#Setup the folder and environment
dir_path = os.path.dirname(os.path.realpath(__file__))
folder_path=os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0,folder_path+"\TestScript")
sys.path.insert(0,folder_path+"\SysLibrary")
sys.path.insert(0,folder_path+"\Library")
#Library fucntions
from setupenviron import setupValue

#setup folders for stroing report and logs
setup = setupValue()
setup.folderCreation()

#Test Cases for execution
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
from tradexsuppliercontact import Tradexsuppliercontact
from selecttradexsuppliercontact import Selecttradexsuppliercontact
from deletetradexsuppliercontact import Deletetradexsuppliercontact
from sendtoenquirysuccessmessage import Sendtoenquirysuccessmessage
from supplierlistundertrade import Supplierlistundertrade
from currencychangeinprojectUS import CurrencychangeinprojectUS
from currencychangeinprojectEURO import CurrencychangeinprojectEURO
from currencychangeinprojectYEN import CurrencychangeinprojectYEN
from plantemplate import Plantemplate
from plantemplatecreationheading import Plantemplatecreationheading
from plantemplatecreation import Plantemplatecreation
from plantemplatecreationwithstages import Plantemplatecreationwithstages
from plantemplatealertmessage import Plantemplatealertmessage
from plantemplatedeletion import Plantemplatedeletion
from plantemplateupdation import Plantemplateupdation
from plantemplatecount import Plantemplatecount
from plantemplatechoose import Plantemplatechoose
from plantemplatesave import Plantemplatesave
from plantenderview import Plantenderview
from plantemplateplanneddates import Plantemplateplanneddates
from plantemplateforecastdates import Plantemplateforecastdates
from plantemplateplannedexclamation import Plantemplateplannedexclamation
from plantemplateforecastexclamation import Plantemplateforecastexclamation
from plantemplatestagdelete import Plantemplatestagdelete
from plantemplatestagaddition import Plantemplatestagaddition
from plantemplatestagadditiondatecheck import Plantemplatestagadditiondatecheck
from plantemplatestagdurationupdation import Plantemplatestagdurationupdation
from plantemplatenotesforallstages import Plantemplatenotesforallstages
from plantemplatenotesupdate import Plantemplatenotesupdate
from plantemplatenotesdelete import Plantemplatenotesdelete
from plantemplatenotesforfirststag import Plantemplatenotesforfirststag
from plantemplatestagnotesupdate import Plantemplatestagnotesupdate
from plantemplatestagnotesdelete import Plantemplatestagnotesdelete
from plantemplateactualforecastdates import Plantemplateactualforecastdates





