from os import getenv

from dotenv import load_dotenv

load_dotenv()

# get token from .env
DISCORD_BOT_TOKEN = getenv("DISCORD_BOT_TOKEN")


# setting
DISCORD_BOT_NAME = "メイドくん"
DISCORD_BOT_PREFIX = "?"

ROLE_EVERYONE = int(getenv("ROLE_EVERYONE", "800698148452040754"))
