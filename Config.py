import os

# Bot token from @botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN")
# From my.telegram.org/
API_ID = int(os.environ.get("API_ID", "23080322","6451737248:AAHhmMdjgTlsjbWXwVSbn5eoJGaGEQDAnBg"))
API_HASH = os.environ.get("API_HASH","b3611c291bf82d917637d61e4a136535")
# For /log cmd
OWNER_ID = [int(i) for i in os.environ.get("OWNER_ID", "7011929837").split(" ")]
# No time limit for this users
AUTH_USERS = [int(i) for i in os.environ.get("AUTH_USERS", "6023712723").split(" ")]
# Time gap after each request (in seconds)
TIME_GAP = int(os.environ.get("TIME_GAP", "10"))
# Bot channel ID for ForceSub, don't forget to add bot in Bot Channel
UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", False)
