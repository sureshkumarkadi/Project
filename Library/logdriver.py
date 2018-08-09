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
sys.path.insert(0,folder_path+"\Library")
from setupenviron import setupValue
class logvalue:
        # create logger

        logger = logging.getLogger("eTender Automation Suite Execution")
        logger.setLevel(logging.DEBUG)
        # create console handler and set level to debug
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ftime = time.mktime(time.localtime())
        ptime=time.strftime("%d-%m-%Y_%H%M%S", time.localtime(ftime))
        path = path= setupValue().logpath
        filename = "Execution Log - {0}".format(ptime)+".log"
        fullpath = os.path.join(path, filename)
        logger.addHandler(logging.FileHandler(fullpath))
        # create formatter
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        # add formatter to ch
        ch.setFormatter(formatter)
        # add ch to logger
        logger.addHandler(ch)
        #return logger
        # "application" code