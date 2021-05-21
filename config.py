import os

class Config:

    BOT_TOKEN = os.environ["1838688735:AAHj7PMxxDJVebXSpXM_Lhh2FKsw1HcXrao"]                                 # Get From https://t.me/BotFather

    API_ID = int(os.environ["5692055"])                                  # Get from https://my.telegram.org/apps

    API_HASH = os.environ["054513b51d72a347f80535d7520cdfbb"]                                   # Get from https://my.telegram.org/apps

    CLIENT_ID = os.environ["664107408955-coge517i7gvakgarm8h7u0oqp7s1mh5m.apps.googleusercontent.com"]                                 # Get from https://console.developers.google.com/apis/credentials

    CLIENT_SECRET = os.environ["oWCpI3LSI1vjRxPK7RvDPX-b"]                         # Get from https://console.developers.google.com/apis/credentials

    BOT_OWNER = int(os.environ["983480159"])                            # Bot owner's telegram id

    AUTH_USERS = [BOT_OWNER,374321319]+[int(user) for user in os.environ["AUTH_USERS"].split(",") if os.environ["AUTH_USERS"]]
                                                                        # Id of other users who want to use your bot

    CRED_FILE = "auth_token.txt"                                        # Credentials file



