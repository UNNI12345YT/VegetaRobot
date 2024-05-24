# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
import json #by ctzfamioy
import os

ARQ_API_URL = "https://arq.hamker.in"
ARQ_API_KEY =  "NFCBDZ-APYXWZ-LINBGL-ARKRKM-ARQ"

def get_user_list(config, key):
    with open('{}/VegetaRobot/{}'.format(os.getcwd(), config),
              'r') as json_file:
        return json.load(json_file)[key]


# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True
    # REQUIRED
    #Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = 27500064   # integer value, dont use ""
    API_HASH = "690dc5633ef234f04f3825a7c1ad0272"
    TOKEN = "wow"  #This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    SQLALCHEMY_DATABASE_URI = "mongodb+srv://HARI_YT:HARI_YT@cluster0.m8x9vc0.mongodb.net/retryWrites=true&w=majority&appName=Cluster0" #Use Your ElephantSQL
    OWNER_ID =  6171681404 # If you dont know, run the bot and do /id in your private chat with it, also an integer
    OWNER_USERNAME = "UNNIdud"
    SUPPORT_CHAT = 'XBOTSUPPORTS'  #Your own group for support, do not add the @
    UPDATES_CHANNEL = 'vegetaUpdates' #Your own channel for Updates of bot, Do not add @
    JOIN_LOGGER = -1002090641762  #Prints any new group the bot is added to, prints just the name and ID.
    REM_BG_API_KEY = "AZb1aLyrziWLUUWNDR7AwMBV"
    EVENT_LOGS = -1002090641762  #Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit
    LOAD = []
    NO_LOAD = ['rss', 'cleaner', 'connection', 'math']
    WEBHOOK = None
    INFOPIC = True
    URL = None
    SPAMWATCH_API = ""  # go to support.spamwat.ch to get key -
    SPAMWATCH_SUPPORT_CHAT = "@SpamWatchSupport"
    BOT_ID = "2128359921"
    
    DRAGONS = get_user_list('elevated_users.json', 'sudos')

    DEV_USERS = get_user_list('elevated_users.json', 'devs')
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = get_user_list('elevated_users.json', 'supports')
    #List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = get_user_list('elevated_users.json', 'tigers')
    WOLVES = get_user_list('elevated_users.json', 'whitelists')
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    WORKERS = 8  # Number of subthreads to use. Set as number of threads your processor uses
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
