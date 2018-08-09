#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      mathew.jacob
#
# Created:     01/09/2016
# Copyright:   (c) Causeway Technologies 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import smtplib
import os
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from datadriven import DataDriver
orgLink=DataDriver()
dir_path = os.path.dirname(os.path.realpath(__file__))
folder_path=os.path.abspath(os.path.join(dir_path, os.pardir))
class EmailSend():
    def mailSend(self,fullpath,sfilename):
        fromaddr = "reisang@etender.com"
        toaddr = "mathew.jacob@causeway.com"
        listvalue=orgLink.readfromXML(folder_path+'\Env\Setup.xml','eTender','env')
        if listvalue.lower()=='StageURL'.lower():
            recipients = ['mathew.jacob@causeway.com','Suresh.Kumar@causeway.com']
        elif listvalue.lower()=='PreStageURL'.lower():
            recipients = ['mathew.jacob@causeway.com','Suresh.Kumar@causeway.com','Reisang.Risom@causeway.com','Nagendra.Reddy@causeway.com']

        elif listvalue.lower()=='MasterURL'.lower():
            recipients = ['mathew.jacob@causeway.com','Suresh.Kumar@causeway.com','Raju.Surapuraju@causeway.com','Reisang.Risom@causeway.com','Andrew.Woolstone@causeway.com','Nagendra.Reddy@causeway.com','Sreeraj.Nair@causeway.com']
        msg = MIMEMultipart('alternative')
        msg['From'] = "automationeTender@etender.com"
        msg['To'] = ", ".join(recipients)
        if listvalue.lower()=='StageURL'.lower():
            msg['Subject'] = "Test Execution Report in Staging for build : "+orgLink.readfromXML(folder_path+'\Data\Data.xml','eTender','buildNo')
        elif listvalue.lower()=='PreStageURL'.lower():
            msg['Subject'] = "Test Execution Report in PreStaging for build : "+orgLink.readfromXML(folder_path+'\Data\Data.xml','eTender','buildNo')
        elif listvalue.lower()=='MasterURL'.lower():
            msg['Subject'] = "Test Execution Report Master build : "+orgLink.readfromXML(folder_path+'\Data\Data.xml','eTender','buildNo')
        body = """\
        <html>
            <head></head>
             <body>
                <p><b>Hi All,</b><br><br>
                  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<b>Attached is the Test Execution Report for <i>eTender</i> build</b><br><br>
                  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<i>Note:To view Screenshot,Make sure use Chrome,IE or Edge</i> <br>
                 <br><b>Thanks,</b><br>
                 <b>Automation team</b>
                </p>
             </body>
         </html>
            """
        msg.attach(MIMEText(body, 'html'))
        path = folder_path+"\Reports"
        filename = 'SmokeTestExecutionReport-01-09-2016_161539.html'
        attachment = open(fullpath,"r+")
        part = MIMEText(body, 'html')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % sfilename)
        msg.attach(part)
        server = smtplib.SMTP("192.168.76.5",25)
        server.login(fromaddr, "password")
        text = msg.as_string()
        server.sendmail(fromaddr, msg['To'].split(","), text)
        server.quit()
