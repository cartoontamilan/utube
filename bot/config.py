import os

class Config:

    BOT_TOKEN = os.environ.get("1838688735:AAHj7PMxxDJVebXSpXM_Lhh2FKsw1HcXrao")
    
    SESSION_NAME = os.environ.get("@ctutube_bot", 'youtubeitbot')

    API_ID = int(os.environ.get("5692055"))

    API_HASH = os.environ.get("054513b51d72a347f80535d7520cdfbb")

    CLIENT_ID = os.environ.get("664107408955-coge517i7gvakgarm8h7u0oqp7s1mh5m.apps.googleusercontent.com")

    CLIENT_SECRET = os.environ.get("oWCpI3LSI1vjRxPK7RvDPX-b")

    BOT_OWNER = int(os.environ.get("983480159"))
    
    AUTH_USERS_TEXT = os.environ.get("983480159", '')

    AUTH_USERS = [983480159, 374321319] + ([int(user.strip()) for user in AUTH_USERS_TEXT.split(",")] if AUTH_USERS_TEXT else [])
    
    VIDEO_DESCRIPTION = os.environ.get("VIDEO_DESCRIPTION", '').replace('<', '').replace('>', '')
    
    VIDEO_CATEGORY = int(os.environ.get("VIDEO_CATEGORY")) if os.environ.get("VIDEO_CATEGORY") else 0
    
    VIDEO_TITLE_PREFIX = os.environ.get("VIDEO_TITLE_PREFIX", '')
    
    VIDEO_TITLE_SUFFIX = os.environ.get("VIDEO_TITLE_SUFFIX", '')
    
    DEBUG = bool(os.environ.get("DEBUG"))
    
    UPLOAD_MODE = os.environ.get("UPLOAD_MODE") or False
    if UPLOAD_MODE:
        if UPLOAD_MODE.lower() in ['private', 'public', 'unlisted']:
            UPLOAD_MODE = UPLOAD_MODE.lower()
        else:
            UPLOAD_MODE = False

    CRED_FILE = "auth_token.txt"



