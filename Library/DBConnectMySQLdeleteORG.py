#-------------------------------------------------------------------------------
# Name:     Testing
# Purpose:
#
# Author:      suresh.kumar
#
# Created:     26-12-2016
# Copyright:   (c) suresh.kumar 2016
# Licence:     <Causeway>
#-------------------------------------------------------------------------------
##import MySQLdb
import unittest
import time
import os
import sys

dir_path = os.path.dirname(os.path.realpath(__file__))

folder_path=os.path.abspath(os.path.join(dir_path, os.pardir))


sys.path.insert(0,folder_path+"\Library")
sys.path.insert(0,folder_path+"\Syslibrary")
sys.path.insert(0,folder_path+"\Data")
sys.path.insert(0,folder_path+"\Env")

from datadriven import DataDriver

APIDetails = DataDriver()

##class deleteorganisation(unittest.TestCase):
##
##    def test_deleteitem(self):
##
##        env = APIDetails.readfromXML(folder_path+'\Env\Setup.xml','eTender','env')
##        print env
##
##        if env == 'StageURL':
##            # Open database connection
##            db = MySQLdb.connect("10.3.10.2","etenderuser","password#123","etender" )
##
##            cursor = db.cursor()
##
##            # Prepare SQL query to DELETE a record from the database.
##            sql =  "delete from etender.tender_item where ext_system_id='486203'"
##            try:
##               # Execute the SQL command
##               cursor.execute(sql)
##               db.commit()
##
##            except:
##               print "Error: unable to delete data"
##
##            # disconnect from server
##            db.close()
##            #return browser



##        elif env == 'PreStageURL':
##            # Open database connection
##            db = MySQLdb.connect("bg-etender-db","root","root","etender" )
##
##            cursor = db.cursor()
##
##            # Prepare SQL query to DELETE a record from the database.
##            sql =  "delete from etender.tender_item where ext_system_id='486203'"
##            try:
##               # Execute the SQL command
##               cursor.execute(sql)
##               db.commit()
##
##            except:
##               print "Error: unable to delete data"
##
##            # disconnect from server
##            db.close()
##            #return browser
##
##        elif env == 'MasterURL':
##            # Open database connection
##            db = MySQLdb.connect("10.3.10.2","etenderuser","password#123","etender",3306 )
##
##            cursor = db.cursor()
##
##            # Prepare SQL query to DELETE a record from the database.
##            sql =  "delete from etender.tender_item where ext_system_id='486203'"
##            try:
##               # Execute the SQL command
##               cursor.execute(sql)
##               db.commit()
##
##            except:
##               print "Error: unable to delete data"
##
##            # disconnect from server
##            db.close()
##            #return browser

##    def orgId(self,browser):
##        # Open database connection
##        ##db = MySQLdb.connect("bg-etender-db","root","root","etender" )
##        db = MySQLdb.connect("10.3.10.2:3306","etenderuser","password#123","etender" )
##
##        cursor = db.cursor()
##
##        # Prepare SQL query to DELETE a record from the database.
##        sql =  "delete FROM etender.organisation_type where org_id=(SELECT id FROM etender.organisation where account_name='CausewayTest')"
##        try:
##           # Execute the SQL command
##           cursor.execute(sql)
##           db.commit()
##
##        except:
##           print "Error: unable to delete data"
##
##        # disconnect from server
##        db.close()
##        return browser
##
##    def orguser(self,browser):
##        # Open database connection
##        ##db = MySQLdb.connect("bg-etender-db","root","root","etender" )
##        db = MySQLdb.connect("10.3.10.2:3306","etenderuser","password#123","etender" )
##
##        # prepare a cursor object using cursor() method
##        cursor = db.cursor()
##
##        # Prepare SQL query to DELETE a record from the database.
##        sql =  "delete FROM etender.organisation_user where organisation_id in (select id FROM etender.organisation where account_name='CausewayTest')"
##        try:
##           # Execute the SQL command
##           cursor.execute(sql)
##           db.commit()
##
##        except:
##           print "Error: unable to delete data"
##
##        # disconnect from server
##        db.close()
##        return browser
##
##    def organisation(self,browser):
##        # Open database connection
##        ##db = MySQLdb.connect("bg-etender-db","root","root","etender" )
##        db = MySQLdb.connect("10.3.10.2:3306","etenderuser","password#123","etender" )
##
##        # prepare a cursor object using cursor() method
##        cursor = db.cursor()
##
##        # Prepare SQL query to DELETE a record from the database.
##        sql =  "delete FROM etender.organisation where account_name='CausewayTest'"
##        try:
##           # Execute the SQL command
##           cursor.execute(sql)
##           db.commit()
##
##        except:
##           print "Error: unable to delete data"
##
##        # disconnect from server
##        db.close()
##        return browser
##
##    def deleteuser(self,browser):
##        # Open database connection
##        ##db = MySQLdb.connect("bg-etender-db","root","root","etender" )
##        db = MySQLdb.connect("10.3.10.2:3306","etenderuser","password#123","etender" )
##
##        # prepare a cursor object using cursor() method
##        cursor = db.cursor()
##
##        # Prepare SQL query to DELETE a record from the database.
##        sql =  "delete from etender.user where email='test@etender.com'"
##        try:
##           # Execute the SQL command
##           cursor.execute(sql)
##           db.commit()
##
##        except:
##           print "Error: unable to delete data"
##
##        # disconnect from server
##        db.close()
##        return browser









