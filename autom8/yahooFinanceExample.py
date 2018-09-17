from autom8 import *
from pandas import read_html
from time import sleep
from os import mkdir, environ
import datetime
def wipe(my_bot):
    my_bot.driver.quit()

#defines standard pattern to optain summarized stock data

#main function will handle our RPA process

#create a new bot instance and initialize the Web Browser automation engine
my_bot = my_RPA(downloads_directory="Yaahoo_Finance_Testing_Bot", bot_name="Yahoo Finance Bot")
#create new txt log file for this RPA instance a unique robot id is created for each RPA instance
my_bot.create_log_file()

#define tickers to scrape data from
try:
    mkdir("C:\Users\%s\Desktop\Financial_YAHOO_BOT_Outputs"%(environ["USERNAME"]))
except:
    pass
tickers = ["F", "AMZN", "GOOG", "NFLX", "TSLA", "FB"]
for i in tickers:
    my_bot.initialize_driver()
    my_bot.get("https://finance.yahoo.com/quote/%s"%i)
    page_source = my_bot.driver.page_source
    mydf = read_html(page_source)[-1]
    mydf.columns = ["Indicators", "Values"]
    mydf = mydf.set_index("Indicators")
    mydf["REPORT_DATE"] = str(datetime.datetime.now())
    mydf.to_csv("C:\Users\%s\Desktop\Financial_YAHOO_BOT_Outputs/%s.csv"%(environ["USERNAME"], i))
    sleep(2)
    my_bot.driver.quit()


#initiate main function and log errors to error logger
