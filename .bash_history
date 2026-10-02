pkg upgrade
apt upgrade && apt update
pip install instagrapi python-telegram-bot
pkg update -y && pkg install python rust clang make python-pillow -y
python -m pip install -U pip setuptools wheel
python -m pip install --extra-index-url https://termux-user-repository.github.io/pypi/ instagrapi python-telegram-bot
python -c "import instagrapi; import telegram; print('Installed successfully')"
from instagrapi import Client
cl = Client()
# Optional: Set proxy if needed
# cl.set_proxy("http://username:password@proxy_address:port")
username = "YOUR_INSTAGRAM_USERNAME"
password = "YOUR_INSTAGRAM_PASSWORD"
# Perform login and save session settings
cl.login(username, password)
cl.dump_settings("session.json")
print("Session successfully created and saved to session.json")
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from instagrapi import Client
from instagrapi.mixins.note import NoteAudience
# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
# Configuration Constants
TELEGRAM_BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
SESSION_FILE = "session.json"
# Initialize Instagram Client
cl = Client()
try:
except Exception as e:
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
async def post_music_note(update: Update, context: ContextTypes.DEFAULT_TYPE):
async def delete_music_note(update: Update, context: ContextTypes.DEFAULT_TYPE):
if __name__ == "__main__":;     app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
mkdir bot.py
cd bot.py
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from instagrapi import Client
from instagrapi.mixins.note import NoteAudience
# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
# Configuration Constants
TELEGRAM_BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
SESSION_FILE = "session.json"
# Initialize Instagram Client
cl = Client()
try:
except Exception as e:
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
async def post_music_note(update: Update, context: ContextTypes.DEFAULT_TYPE):
async def delete_music_note(update: Update, context: ContextTypes.DEFAULT_TYPE):
if __name__ == "__main__":;     app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
python bot.py
pkg install nano -y
nano bot.py
rm -rf bot.py
nano bot.py
python bot.py
nano bot.py
python bot.py
nano bot.py
python bot.py
nano setup_session.py
python setup_session.py
nano setup_session.py
python setup_session.py
ping -c 3 instagram.com
python setup_session.py
python bot.py
ping -c 3 api.telegram.org
python bot.py
nano bot.py
python bot.py
nano bot.py
python bot.py
while true; do python bot.py; sleep 2; done
