from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = "24072444"
# -------------------------------------------------------------
API_HASH = "580e1a3e7d0719816feebf595c9166d2"
# --------------------------------------------------------------
BOT_TOKEN = getenv("BOT_TOKEN", None)
MONGO_URL = getenv("MONGO_URL", None)
OWNER_ID = int(getenv("OWNER_ID", "8093150680"))
SUPPORT_GRP = "BOTMINE_SUPPORT"
UPDATE_CHNL = "BOTMINE_TECH"
OWNER_USERNAME = "RADHE_XD"
    
