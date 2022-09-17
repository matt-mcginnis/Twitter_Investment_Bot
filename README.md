# Twitter_Investment_Bot
This is an API designed to scrape the Dataroma webpage and tweet investment data from some of the biggest fund managers.

## Setup Instructions
Before getting started, you will want to make sure you have the latest version of Python (3.10.7) installed on your machine. You can find instructions to download and install Python [here.](https://www.python.org/downloads/)

In order to run this API, you will need to set up a Twitter Developer account and create a project. Instructions for this can be found [here.](https://developer.twitter.com/en/docs/twitter-api/getting-started/make-your-first-request)

After setting up your Twitter dev account and project, you should have access to a consumer key & secret as well as an access token & secret.

In order to run the API, you will need to create a .env file with the following contents:
```
ACCESS_TOKEN='your_access_token'
ACCESS_SECRET='your_access_secret'
CONSUMER_KEY='your_consumer_key'
CONSUMER_SECRET='your_consumer_secret'
```
This file will be loaded by the API when the API is called.

After your account and project are set up and you have access to the necessary credentials, you can set up a virtual environment to run the API in by executing the following commands in a terminal:
```
python3 -m venv investment_bot_env
source investment_bot_env/bin/activate
pip install -r requirements.txt
```

This allows you to install all the necessary packages to run the API without installing them directly on your machine. To shut down the virtual environment simply run the ```deactivate``` command.

Currently the API is designed to tweet a single investment from the list of investment data scraped for the most recent 13F filing of Berkshire Hathaway. However, this can be modified to tweet all investments (buys, adds, reductions and sells) for an entire quarter or multiple quarters.

## Resources and Acknowledgements
- [**BeautifulSoup**](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#navigating-the-tree)
- [**Twitter Developer**](https://developer.twitter.com/en)
- [**Python**](https://www.python.org/)