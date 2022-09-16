from dotenv import load_dotenv
import time
import twitter
import os
import scraper

# Load environment variables from .env file
load_dotenv()

# Get consumer/access keys/tokens
_consumer_key = os.environ.get("CONSUMER_KEY")
_consumer_secret = os.environ.get("CONSUMER_SECRET")
_access_token_key = os.environ.get("ACCESS_TOKEN")
_access_token_secret = os.environ.get("ACCESS_SECRET")

# Create instance of Twitter API 
t = twitter.Api(consumer_key=_consumer_key,
                consumer_secret=_consumer_secret,
                access_token_key=_access_token_key,
                access_token_secret=_access_token_secret
                )

# Set Timestamp for Oauth Client
ts = str(time.time() - time.altzone)
t._Api__auth.client.timestamp = ts

# Define __main__ function to be called
def main():
    # Set url and headers
    url = 'https://www.dataroma.com/m/m_activity.php?m=BRK&typ=a'
    HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.81 Safari/537.36 Edg/97.0.1072.69'}

    raw_invst_data = scraper.get_raw_investment_data(url, HEADERS)
    invst_data_list = scraper.get_investment_data_single_qtr('Q2', '2022', raw_invst_data)

    # Post an investment tweet
    t.PostUpdate(invst_data_list[0])

if __name__ == "__main__":
    main()