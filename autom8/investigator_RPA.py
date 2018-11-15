from autom8 import *
from checkCDriver import CheckCDriver
from selenium.webdriver.common.keys import Keys

CheckCDriver()

topics = ["Donald Trump", "Brexit"]

def main(topics):
    """ Searches for relevent News data and structures it to be saved on disk as a csv file """

    my_bot = my_RPA(bot_name="investigator_bot", downloads_directory = "investigator_bot" )
    #create new txt log file for this RPA instance a unique robot id is created for each RPA instance
    my_bot.create_log_file()
    my_bot.initialize_driver()
    topics_data = []

    try:
        
        for topic in topics:

            my_bot.get("http://www.newslookup.com/")
            search_bar = my_bot.find_by_tag_and_attr(tag="input", attribute="id", evaluation_string="lookup", sleep_secs=0.1)[0]
            search_bar.send_keys(topic, Keys.ENTER)

            #clicks to search time period
            my_bot.find_by_tag_and_attr(tag="button", attribute="id", evaluation_string="timeperiod", sleep_secs=3)[0].click()
            my_bot.find_by_tag_and_attr(tag="a", attribute="id", evaluation_string="tp_720", sleep_secs=3)[0].click()

            my_bot.find_by_tag_and_attr(tag="button", attribute="id", evaluation_string="sort", sleep_secs=3)[0].click()
            my_bot.find_by_tag_and_attr(tag="a", attribute="id", evaluation_string="sort_0", sleep_secs=3)[0].click()

            for i in range(3):
                my_bot.find_by_tag_and_attr(tag="button", attribute="id", evaluation_string="more-btn", sleep_secs=3)[0].click()

            titles = my_bot.find_by_tag_and_attr(tag="a", attribute="class", evaluation_string="title", sleep_secs=2)
            title_texts = [i.text for i in titles]
            title_links = [i.get_attribute("href") for i in titles]

            times = [  i.text for i in 
                my_bot.find_by_tag_and_attr(tag="span", attribute="class", evaluation_string="stime", sleep_secs=0.1)
                ]

            descrips = [ i.text for i in 
                my_bot.find_by_tag_and_attr(tag="p", attribute="class", evaluation_string="desc", sleep_secs=0.1)
                ]

            scraped_success = (len(titles) == len(title_links) == len(title_texts) == len(times) == len(descrips))

            if scraped_success:

                current_page = {}
                current_page["article_title"] = title_texts
                current_page["article_link"] = title_links
                current_page["article_publish"] = times
                current_page["article_description"] = descrips
                topics_data.append(DataFrame(current_page).drop_duplicates())

            else:

                raise Exception("error please check code")

        my_bot.driver.quit()

        destination = my_bot.downloads_dir
        if not os.path.exists(destination):
            os.mkdir(destination)

        for i, df in enumerate(topics_data):
            df.to_csv(destination+r"\%s.csv"%topics[i], encoding="utf-8")
        print("Robot Complete !")

    except Exception as e:
        print("error occured please check logs")
        my_bot.log(e)

if __name__ == "__main__":
    main(topics=topics)