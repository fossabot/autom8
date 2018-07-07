from time import sleep
from selenium import webdriver
from pandas import DataFrame
from selenium.webdriver.chrome.options import Options
import os
import glob
import platform
import datetime
import uuid
# Gchrome and chrome dirver dependancy. Chrome driver will not work unless regular chrome is installed on machineself.
didnotinit = "Use .initialize_driver() to instantiate a webdriver session. "
log_file_message = "Create and initialize logfile using .create_log_file(bot_name) before logging"

class my_RPA(object):

    def __init__(self,downloads_directory, df=None):
        if df is None:
            print("No DatFrame Provided")
        else:
            self.DataFrame = df

        if platform.system() == "Windows":
            user = os.environ["USERNAME"]
            driver_path = r"C:\chromedriver_win32\chromedriver.exe"
            self.downloads_dir = r"C:\Users\%s\Downloads\%s"%(user, downloads_directory)

        elif platform.system() == "Darwin":
            user = os.environ["LOGNAME"]
            driver_path = "/chromedriver_mac64/chromedriver"
            self.downloads_dir = r"/Users/%s/Downloads/%s"%(user, downloads_directory)

        chop = webdriver.ChromeOptions()
        user = os.environ.get('USERNAME')
        chop.add_argument('log-level=3')

        if platform.system() == "Windows":
            chop.add_argument(r"user-data-dir=C:\Users\\"+user+r"\AppData\Local\Google\Chrome\User Data\Profile 2") #Path to your chrome profile
        elif platform.system() == "Darwin":
                    pass

        chop.add_argument("--start-maximized")
        chop.add_experimental_option("prefs", {
      	"download.default_directory": self.downloads_dir,
     	"download.prompt_for_download": False,
      	"download.directory_upgrade": True,
      	"safebrowsing.enabled": True})
        self.chop = chop
        self.driver_path = driver_path
        self.driver = None
        self.uid = str(uuid.uuid4().hex)
        self.logfile_path = None

    def create_log_file(self, bot_name=None):
        try:
            usr =  os.environ["USERNAME"]
        except:
            usr =  os.environ["LOGNAME"]


        if platform.system() == "Windows":
            self.log_path = "c:\\Users\\%s\\autom8_logs"%usr
        else:
            self.log_path = "/Users/%s/autom8_logs"%usr

        exists = os.path.exists(self.log_path)

        if exists == True:
            print("log directory already created")
        else:
            glob.os.mkdir(self.log_path)
            print("log directory created: %s" %self.log_path)

        if bot_name is None:
            uid = self.uid
            bot_name = "Unnamed Bot - %s" %str(uid)
            print("Bot Named: Unnamed Bot - %s"%uid )
        else:
            uid = self.uid
            bot_name = "%s - %s" %(bot_name,str(uid))
            print("Bot Named: Unnamed Bot - %s"%uid )

        logfile = os.path.join(self.log_path, bot_name+".txt")
        file = open(logfile, mode="w")
        file.write("log file created at %s by user %s.\n"%(str(datetime.datetime.now()), usr))
        file.write("--- --- --- --- --- --- ---\n")
        self.logfile_path = logfile
        today_str = datetime.datetime.today().strftime("%d.%b.%Y")

    def log(self, message):
        if self.logfile_path is None:
            print(log_file_message)
        else:
            with open(self.logfile_path, 'a') as outfile:
                outfile.write("%s - %s\n"%(message, str(datetime.datetime.now())))

    def set_DataFrame(self, df):
        self.DataFrame = df

    def initialize_driver(self):
        self.driver = webdriver.Chrome(self.driver_path, chrome_options = self.chop)

    def get(self, url):
        if self.driver is None:
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
        if self.driver is None:
            print(didnotinit)
        else:
            return self.driver.execute_script(script)
