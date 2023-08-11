import requests
import datetime as dt
from twilio.rest import Client

STOCK = #"<stock symbol>"
COMPANY_NAME = #"<company name>"
ALPHA_API_KEY = #"<alphavantage API key>"
NEWS_API_KEY = #"<newsapi API key>"
TODAY = dt.datetime.today().date()
YESTERDAY = TODAY - dt.timedelta(days=1)
DAY_BEFORE_YESTERDAY = TODAY - dt.timedelta(days=2)
account_sid = #"<twilio account sid>"
auth_token = #"<twilio account auth token>"

stock_price_endpoint = "https://www.alphavantage.co/query"
parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": ALPHA_API_KEY
}

stock_price_response = requests.get(stock_price_endpoint, params=parameters)
stock_price_response.raise_for_status()
stock_data = stock_price_response.json()
yesterday_close = float(stock_data['Time Series (Daily)'][str(YESTERDAY)]['4. close'])
day_before_yesterday_close = float(stock_data['Time Series (Daily)'][str(DAY_BEFORE_YESTERDAY)]['4. close'])
change_percentage = round(((yesterday_close - day_before_yesterday_close) / yesterday_close) * 100, 2)

news_endpoint = "https://newsapi.org/v2/everything"
news_parameters = {
    "q": COMPANY_NAME,
    "from": YESTERDAY,
    "sortBy": "publishedAt",
    "apikey": NEWS_API_KEY
}
news_response = requests.get(news_endpoint, params=news_parameters)
news_response.raise_for_status()
news_data = news_response.json()
articles = news_data['articles'][0:3]


def get_news():
    body_1 = (f"TSLA: 🔺{change_percentage}%\nHeadline: {articles[0]['title']}\nBrief: {articles[0]['description']}"
              f"\nHeadline: {articles[1]['title']}\nBrief: {articles[1]['description']}"
              f"\nHeadline: {articles[2]['title']}\nBrief: {articles[2]['description']}")

    body_2 = (f"TSLA:🔻{change_percentage * -1}%\nHeadline: {articles[0]['title']}\nBrief: {articles[0]['description']}"
              f"\nHeadline: {articles[1]['title']}\nBrief: {articles[1]['description']}"
              f"\nHeadline: {articles[2]['title']}\nBrief: {articles[2]['description']}")
    if change_percentage > 0:
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
            body=body_1,
            from_= #"<your twilio mobile number>",
            to= #<"your mobile number>"
        )
        print(message.status)
    else:
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
            body=body_2,
            from_= #"<your twilio mobile number>",
            to= #<"your mobile number>"
        )
        print(message.status)


get_news()
