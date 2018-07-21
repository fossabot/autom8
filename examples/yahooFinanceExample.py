from autom8 import *

def wipe(my_bot):
    my_bot.driver.quit()

#defines standard pattern to optain summarized stock data
def get_ticker_data(my_bot, tickers):

    my_data = []

    for ticker in tickers:
        print("ticker: %s"%ticker)
        my_bot.find_by_tag_and_attr(tag="input",
                                    attribute="placeholder",
                                    evaluation_string="Search for news, symbols or companies",
                                    sleep_secs=5)[0].send_keys(ticker)

        my_bot.find_by_tag_and_attr(tag="button",
                                    attribute="class",
                                    evaluation_string="Bdrs(4px) Bdtw(0) Bdw(1px) Bgr(rx) Mstart(5px) Bxz(cb) C(#fff) Ff(ss)! Fz(15px) two-btn_Fz(13px) Lh(32px)! Mend(0)! My(0)! Miw(92px) Px(14px) Py(0) Ta(c) Td(n) Va(t) Zoom Bg(searchBtnBg) Bxsh(customShadowSearchButton)",
                                    sleep_secs=5)[0].click()




        summary_table = my_bot.find_by_tag_and_attr(tag="div",
                                    attribute="class",
                                    evaluation_string="D(ib) W(1/2) Bxz(bb) Pend(12px) Va(t) ie-7_D(i) smartphone_D(b) smartphone_W(100%) smartphone_Pend(0px) smartphone_BdY smartphone_Bdc($c-fuji-grey-c)",
                                    sleep_secs=8)

        summary_table_2 = my_bot.find_by_tag_and_attr(tag="div",
                                    attribute="class",
                                    evaluation_string="D(ib) W(1/2) Bxz(bb) Pstart(12px) Va(t) ie-7_D(i) ie-7_Pos(a) smartphone_D(b) smartphone_W(100%) smartphone_Pstart(0px) smartphone_BdB smartphone_Bdc($c-fuji-grey-c)",
                                    sleep_secs=4)

        [summary_table.append(i) for i in summary_table_2]

        summary_table = [i.text.split("\n") for i in summary_table]

        for i in summary_table:
            my_bot.log(ticker)
            my_bot.log("\n")
            for j in i:
                my_bot.log(j)

        prev_close = summary_table[0][0].replace("Previous Close ", "").replace(",", "")
        open_price = summary_table[0][1].replace("Open ", "")
        day_range = summary_table[0][4].replace("Day's Range ", "").split(" - ")
        fifty_two_week_range = summary_table[0][5].replace("52 Week Range ", "").split(" - ")
        volume = summary_table[0][6].replace("Volume ", "")
        mrkt_cap = summary_table[1][0].replace("Market Cap ", "")
        beta = summary_table[1][1].replace("Beta ", "")
        pe_ratio = summary_table[1][2].replace("PE Ratio (TTM) ", "")
        eps = summary_table[1][3].replace("EPS (TTM)  ", "")
        earning_date = summary_table[1][4].replace("Earnings Date ", "")

        my_dict = {"ticker":ticker,
                   "previous_close":prev_close ,
                   "open_price":open_price ,
                   "day_range_min":day_range[0],
                   "day_range_max":day_range[1],
                   "fifty_two_week_range":fifty_two_week_range,
                   "volume":volume,
                   "mrkt_cap":mrkt_cap,
                   "beta":beta,
                   "pe_ratio":pe_ratio,
                   "eps":eps,
                   "earning_date":earning_date,}

        my_data.append(my_dict)
        my_bot.driver.refresh()

    return my_data

#main function will handle our RPA process
def main():
    #create a new bot instance and initialize the Web Browser automation engine
    my_bot = my_RPA(downloads_directory="Yahoo_Finance_Testing_Bot")
    #create new txt log file for this RPA instance a unique robot id is created for each RPA instance
    my_bot.create_log_file(bot_name="Yahoo Finance Bot")
    my_bot.initialize_driver()
    #define tickers to scrape data from
    tickers = ["F", "AMZN", "GOOG", "NFLX", "TSLA", "FB"]
    my_bot.get("https://finance.yahoo.com/")
    #initiate main function and log errors to error logger
    try:
        #calls primary child function (loops through all tickers)
        all_data = get_ticker_data(my_bot=my_bot, tickers=tickers)
        df = DataFrame(all_data).set_index("ticker")
        df.to_csv(my_bot.downloads_dir)
        wipe(my_bot)
    except Exception as e:
        #catch any exception and log it
        my_bot.log("Error:")
        my_bot.log(" ")
        my_bot.log(str(e))
        print("error logged please try again")



main()
