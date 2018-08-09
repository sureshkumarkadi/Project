#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      mathew.jacob
#
# Created:     31/08/2016
# Copyright:   (c) mathew.jacob 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import logging
import datetime
import time
import string
import os
import sys
dir_path = os.path.dirname(os.path.realpath(__file__))
folder_path=os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0,folder_path+"\SysLibrary")
sys.path.insert(0,folder_path+"\Library")
from setupenviron import setupValue
logger = logging.getLogger("eTender Automation Suite Execution")
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ftime = time.mktime(time.localtime())
ptime=time.strftime("%d-%m-%Y_%H%M%S", time.localtime(ftime))
path= setupValue().logpath
filename = "Execution Log - {0}".format(ptime)+".log"
fullpath = os.path.join(path, filename)
class logvalue:
        logger = logging.getLogger("eTender Automation Suite Execution")
        logger.setLevel(logging.DEBUG)
        if not os.path.exists(os.path.dirname(fullpath)):
            os.makedirs(os.path.dirname(fullpath))
        logger.addHandler(logging.FileHandler(fullpath))
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        ch.setFormatter(formatter)
        logger.addHandler(ch)


