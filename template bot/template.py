from autom8 import *

def wipe(my_bot):

    my_bot.driver.quit()

def primary_child_function(my_bot):

    """ do some stuff """

    pass

#main function will handle our RPA process
def main():

    #define folder name within downloads
    ddir_foldr_name = "autom8_files"
    #give your bot name
    bot_name = "skynet"
    #instantiate your bot
    my_bot = my_RPA(bot_name=bot_name, downloads_directory=ddir_foldr_name)
    #create a log file
    my_bot.create_log_file()
    #initialize the webdriver
    my_bot.initialize_driver()
    #get url
    url = "https://socket.io/"
    my_bot.get(url)
    #log steps accordingly
    my_bot.log("Conducting Primary Child Function")
    primary_child_function(my_bot=my_bot)
    my_bot.log("Finished Primary Child Function")
    #close url
    my_bot.driver.quit()
    my_bot.log("Process Complete")

#handle exceptions
try:

    main()

except Exception as e:

    print(e)
    #catch any exception and log it
    my_bot.log("Error:")
    my_bot.log(str(e))
    print("error logged please try again")
