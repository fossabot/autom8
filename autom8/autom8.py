from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pandas import read_excel, pivot_table, isnull, DataFrame, read_html, ExcelWriter
from ctypes import windll
from selenium.webdriver.support.ui import Select
import xlwings as xw
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import re
import pyautogui
import os
import pandas as pd
import xlwings as xw
import shutil
import os
from requests import get
from zipfile import ZipFile
import easygui
from dateutil import parser
import glob

didnotinit = "Use .initialize_driver() to instantiate a webdriver session. "

class my_RPA(object):

    def __init__(self, df=None):

        if df == None:
            print("No DatFrame Provided")
        else:
            self.DataFrame = df
        driver_path = r"C:\chromedriver_win32\chromedriver.exe"
        chop = webdriver.ChromeOptions()
        user = os.environ.get('USERNAME')
        chop.add_argument(r"user-data-dir=C:\Users\\"+user+r"\AppData\Local\Google\Chrome\User Data\Profile 2") #Path to your chrome profile
        chop.add_argument("--start-maximized")
        chop.add_experimental_option("prefs", {
      	"download.default_directory": r"C:\CIT RPA\Reports",
     	"download.prompt_for_download": False,
      	"download.directory_upgrade": True,
      	"safebrowsing.enabled": True})
        self.chop = chop
        self.driver_path = driver_path
        self.driver =  None

    def set_DataFrame(df):
        self.DataFrame = df

    def initialize_driver(self):
        self.driver = webdriver.Chrome(self.driver_path, chrome_options = self.chop)

    def get(self, url):
        if self.driver == None:
            print(didnotinit)
        else:
            self.driver.get(url)

    def robust_get_element(self, element, try_times, seconds):

        for i in range(try_times):
            try:
                my_element = self.driver.find_element_by_xpath(element)
                return my_element
            except:
                sleep(seconds)

    def use_javascript(self, script):
        if self.driver == None:
            print(didnotinit)
        else:
            return self.driver.execute_script(script)
