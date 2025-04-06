import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = 27885190
API_HASH = "2fa09a645e1970af43ee3fc6f9ab4f2f"

# Get your token from @BotFather on Telegram.
BOT_TOKEN = "7949387572:AAGyzlzuMKPKKfM0GjiTcOwarqnpBPxAmwQ"

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = "mongodb://multiverseofanime0:ganesh@2025@ac-v7zkpzc-shard-00-00.b13vocg.mongodb.net:27017,ac-v7zkpzc-shard-00-01.b13vocg.mongodb.net:27017,ac-v7zkpzc-shard-00-02.b13vocg.mongodb.net:27017/?replicaSet=atlas-9ez9yo-shard-0&ssl=true&authSource=admin&retryWrites=true&w=majority&appName=Cluster0"

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 60))

# Chat id of a group for logging bot's activities
LOG_GROUP_ID = -1002622690724

# Get this value from @ultron2_robot on Telegram by /id
OWNER_ID = 7508054127

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/rishabhops/alice",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = "https://t.me/+d2wwTwVAbwhjMjA1"
SUPPORT_GROUP = "https://t.me/tempest_kingdom"

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 2145386496))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from Replit
STRING1 = "BQGpfoYAh83yun6XZweHJmGCtVKQYcCd9uznXc9hq8GBYNHv_Pzuugt82IFVOgDA_X4U0UuJTeknas-LLqoAwefA-3LYEYqKxxv8yLEVpttPNXOnGNx8kAWu_4nz0IJOJprPRe_Y0x2iEWtgByYPVKW9J6oFRKAtu6QY9TeIC5d4Gf5HYvH1WMR6Rve4IJlO3mheGGBxFRKDVZVXdASYi3TbK-4lWyfmWLjxT0sMvAPqaNv0vXj-s7nFWfsgbV4NkZtoOTrmytMDEhWOwHVXthIn4Miq3Rv8Sf6xfWMSeOw6RubkHNOTROg353N3uijUJopDvzwMFnEOhFeoQg06mn7TnoMzmQAAAAG_g9BvAA"
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = "https://graph.org/file/56c6a42b2732031e717a7-74d5c0abf0b07c65f9.jpg"

PING_IMG_URL = "https://graph.org/file/56c6a42b2732031e717a7-74d5c0abf0b07c65f9.jpg"

PLAYLIST_IMG_URL = "https://graph.org/file/56c6a42b2732031e717a7-74d5c0abf0b07c65f9.jpg"
STATS_IMG_URL = "https://graph.org/file/56c6a42b2732031e717a7-74d5c0abf0b07c65f9.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/56c6a42b2732031e717a7-74d5c0abf0b07c65f9.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/56c6a42b2732031e717a7-74d5c0abf0b07c65f9.jpg"
STREAM_IMG_URL = "https://graph.org/file/56c6a42b2732031e717a7-74d5c0abf0b07c65f9.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/56c6a42b2732031e717a7-74d5c0abf0b07c65f9.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/56c6a42b2732031e717a7-74d5c0abf0b07c65f9.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/56c6a42b2732031e717a7-74d5c0abf0b07c65f9.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/56c6a42b2732031e717a7-74d5c0abf0b07c65f9.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/56c6a42b2732031e717a7-74d5c0abf0b07c65f9.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )
