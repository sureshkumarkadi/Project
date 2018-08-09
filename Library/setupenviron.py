#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      mathew.jacob
#
# Created:     31/08/2016
# Copyright:   (c) Causeway Technologies 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import sys
import os
import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
#from selenium.webdriver.firefox.options import Options
dir_path = os.path.dirname(os.path.realpath(__file__))
folder_path=os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0,folder_path+"\Syslibrary")
sys.path.insert(0, folder_path+"\Env")
from datadriven import DataDriver
screenpath = folder_path+"\\Screenshots"
logpath=folder_path+"\\Logs"
reportpath=folder_path+"\\Reports"
downloadpath=folder_path+"\\Downloads"
logpath=folder_path+"\\Logs"

class setupValue:
    screenpath = folder_path+"\\Screenshots"
    logpath=folder_path+"\\Logs"
    reportpath=folder_path+"\\Reports"
    downloadpath=folder_path+"\\Downloads"
    def setupfunction(self):
        envdata=DataDriver()
        envid=envdata.readfromXML(folder_path+'\Env\Setup.xml','eTender','browser')
        if envid=='firefox':
            browser = webdriver.Firefox()
            browser.implicitly_wait(10)
            return browser
        if envid=='ie':
            cap = DesiredCapabilities().INTERNETEXPLORER
            cap['platform'] = "Win10"
            cap['version'] = "11"
            cap['browserName'] = "internet explorer"
            cap['ignoreProtectedModeSettings'] = True
            cap['nativeEvents'] = False
            cap['requireWindowFocus'] = True
            cap['INTRODUCE_FLAKINESS_BY_IGNORING_SECURITY_DOMAINS'] = True
            cap['IGNORE_ZOOM_SETTING']=True
            browser=webdriver.Ie(capabilities=cap, executable_path=r'C:\Selenium\IEDriverServer.exe')
            browser.set_script_timeout(20)
            browser.implicitly_wait(20)
            browser.set_page_load_timeout(20)
            return browser
        if envid=='chrome':
            chromeOptions = webdriver.ChromeOptions()
            prefs = {"download.default_directory" : downloadpath}
            chromeOptions.add_experimental_option("prefs",prefs)
            chromedriver = "C:\Selenium\chromedriver.exe"
            browser = webdriver.Chrome(executable_path=chromedriver,chrome_options=chromeOptions)
            browser.delete_all_cookies()
            browser.implicitly_wait(20)
            browser.set_page_load_timeout(20)
            return browser

        if envid=='headlessChrome':
            chrome_options = Options()
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--window-size=1920x1080")
            chrome_driver = "C:\Selenium\chromedriver.exe"
            browser = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)
            browser.implicitly_wait(10)
            return browser

        if envid=='headlessFirefox':
            firefox_options = Options()
            firefox_options.add_argument("--headless")
            firefox_options.add_argument("--window-size=1920x1080")
            firefox_driver = "C:\Selenium\geckodriver.exe"
            browser = webdriver.Firefox(firefox_options=firefox_options, executable_path=firefox_driver)
            browser.implicitly_wait(10)
            return browser

        if envid=='phantom':
            browser = webdriver.PhantomJS('C:\Selenium\phantomjs.exe')
            browser.implicitly_wait(10)
            return browser

    def folderCreation(self):
        if not os.path.exists(screenpath):
            os.makedirs(setupValue.screenpath)
            time.sleep(1)
        if not os.path.exists(logpath):
            os.makedirs(logpath)
            time.sleep(1)
        reportpath=folder_path+"\Reports"
        if not os.path.exists(reportpath):
            os.makedirs(reportpath)
        if not os.path.exists(downloadpath):
            os.makedirs(downloadpath)