import requests
import os
from datetime import *
from twilio.rest import Client

STOCK = "BB"
COMPANY_NAME = '+blackberry AND stock OR limited -mobile -smartphone -mobility -smartphone -smartphones'
ALPHAVANTAGE_KEY = os.environ.get("ALPV_KEY")
NEWS_APIKEY = os.environ.get("NEWS_APIKEY")
TWILIO_KEY = os.environ.get("TWILIO_TOKEN")
TWILIO_SID =

ALPHA_PARAMETER = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "BB",
    "apikey": ALPHAVANTAGE_KEY
}

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

ALPV_response = requests.get("https://www.alphavantage.co/query", params=ALPHA_PARAMETER)
ALPV_response.raise_for_status()
stock_data = ALPV_response.json()
print(stock_data)

# ---------------------------- FUNCTIONS ------------------------------------------


def convert_to_date(x):
    time_today = datetime.now()
    weekday = time_today - timedelta(days=x)
    weekday_dateconfig = f"{weekday.year}-{'{:02d}'.format(weekday.month)}-{'{:02d}'.format(weekday.day)}"

    return weekday_dateconfig


def obtain_value(date1, date2):
    x = convert_to_date(date1)
    y = convert_to_date(date2)
    stock_price_date1 = (stock_data["Time Series (Daily)"][x]['4. close'])
    stock_price_date2 = (stock_data["Time Series (Daily)"][y]['4. close'])
    abs_value = ((float(stock_price_date1) / float(stock_price_date2) * 100) - 100)

    return abs_value


def obtain_newsapi_parameter(date1, date2, keyword):
    parameter = {
        "apiKeY": NEWS_APIKEY,
        "qInTitle": f"{keyword}",
        "from": convert_to_date(date1),
        "to": convert_to_date(date2),
        "language": "en",
        "sortBy": "popularity",
    }

    return parameter


def fetch_articles(news_parameter, number_of_articles):
    news_response = requests.get("https://newsapi.org/v2/everything", params=news_parameter)
    news_response.raise_for_status()
    articles = news_response.json()
    article_list = []
    for _ in range(0, number_of_articles + 1):
        article_list.append(articles['articles'][_])
    print(article_list)

    return article_list

# ---------------------------------------------------------------------------------


time_now = datetime.now()

# test = date(yesterday_raw.year, yesterday_raw.month, yesterday_raw.day)  # Efficient method of approaching problem
# print(test)


if time_now.weekday() == 1:
    percentage = obtain_value(1, 4)
    NEWS_PARAMETER = (obtain_newsapi_parameter(1, 4, COMPANY_NAME))  # Testing to see if strings work.

elif time_now.weekday() == 0:
    percentage = obtain_value(3, 4)
    NEWS_PARAMETER = (obtain_newsapi_parameter(3, 4, COMPANY_NAME))

elif time_now.weekday() == 6:
    percentage = obtain_value(2, 3)
    NEWS_PARAMETER = (obtain_newsapi_parameter(2, 3, COMPANY_NAME))

else:
    percentage = obtain_value(1, 2)
    NEWS_PARAMETER = (obtain_newsapi_parameter(1, 2, COMPANY_NAME))

# 0: Monday, 1: Tuesday, 2: Wednesday, 3: Thursday, 4: Friday, 5: Saturday, 6: Sunday;

# weekday1_close = (stock_data["Time Series (Daily)"][yesterday]['4. close'])
# d_weekday_1_close = (stock_data["Time Series (Daily)"][d_yesterday]['4. close'])
# abs_percentage = abs((float(weekday1_close) / float(d_weekday_1_close) * 100) - 100)

if percentage >= 1 or percentage <= -1:
    if percentage < 0:
        change_symbol = f"🔻{abs(round(percentage, 2))}%"
    else:
        change_symbol = f"🔺{abs(round(percentage, 2))}%"

    # STEP 2: Use https://newsapi.org
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    number_of_wanted_articles = 3
    article_list = fetch_articles(NEWS_PARAMETER, number_of_wanted_articles)

    # STEP 3: Use https://www.twilio.com
    # Send a separate message with the percentage change and each article's title and description to your phone number.

    client = Client(TWILIO_SID, TWILIO_KEY)

    for _ in range(0, number_of_wanted_articles):
        article_msgconfig = f"{STOCK}: {change_symbol}\n" \
                            f"Headline: {article_list[_]['title']}\n\n" \
                            f"Brief: {article_list[_]['description']}"

        message = client.messages.create(
            body=article_msgconfig,
            from_='+16264145685',
            to='+17789530112'
        )



"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""


