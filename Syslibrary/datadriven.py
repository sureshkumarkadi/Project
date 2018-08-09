#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      mathew.jacob
#
# Created:     18/08/2016
# Copyright:   (c) mathew.jacob 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import xml.etree.ElementTree as ET
class DataDriver():
    def readfromXML(self,filename,rootnode,fnode):
        tree = ET.parse(filename)
        root = tree.getroot()
        for node in root.findall(rootnode):
            rValue=node.find(fnode).text
            #print node1.text
            return rValue

