from time import sleep
from selenium import webdriver
from pandas import DataFrame
from selenium.webdriver.chrome.options import Options
import os
import glob
import platform
import datetime
import uuid

didnotinit = "Use .initialize_driver() to instantiate a webdriver session. "
log_file_message = "Create and initialize logfile using .create_log_file(bot_name) before logging"

class my_RPA(object):

    """
    Creates an instance of RPA object:

    RPA objects can be used to create a virtual
    assistant that will cary out a series of event-based
    or stricly scheduled taks.

    Use:

    human_resources_bot = my_RPA("Human Resources Bot")
    human_resources_bot.create_log_file()
    human_resources_bot.initialize_driver()
    human_resources_bot.log("WebDriver Initiated")

                    ... ... ...

    Keyword arguments:

    downloads_directory = Directory within downloads
    folder that the RPA's chromedriver will download too.
    Usefull to identify all files downloaded by specific RPA bot.

    """

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
        chop.add_argument('--start-maximized')

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

        """ create log file in autom8_logs folder.
            if bot_name=None automatic ID is assigned to bot. """
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
            bot_name = "Unnamed Bot - %s - %s" %(str(uid), str(datetime.datetime.now()))
            print("Bot Named: Unnamed Bot - %s - %s"%(str(uid), str(datetime.datetime.now())))
        else:
            uid = self.uid
            bot_name = "%s - %s - %s" %(bot_name,str(uid), str(datetime.datetime.now()))
            print("%s - %s - %s"%(bot_name, str(uid), str(datetime.datetime.now())))

        logfile = os.path.join(self.log_path, bot_name+".txt")


        file = open(logfile, mode="w")
        file.write("log file created at %s by user %s.\n"%(str(datetime.datetime.now()), usr))
        file.write("--- --- --- --- --- --- ---\n")
        self.logfile_path = logfile
        today_str = datetime.datetime.today().strftime("%d.%b.%Y")

    def log(self, message):
        """ """

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

    def wait_and_find_element_xpath(self, element, try_times, seconds):
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

    def find_by_tag_and_attr(self, tag, attribute, evaluation_string, sleep_secs):
        sleep(sleep_secs)
        elements = self.driver.find_elements_by_tag_name(tag)
        elements_to_return = []
        for el in elements:
            if el.get_attribute(attribute) == evaluation_string:
                elements_to_return.append(el)
        return elements_to_return
