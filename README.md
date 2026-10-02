Noxveilbot - Instagram Music Note Telegram Bot
Noxveilbot is a single-tenant Telegram bot middleware built with Python (instagrapi and python-telegram-bot). It connects Telegram commands to Instagram's private mobile endpoints, allowing users to search Instagram's global music catalog and automatically post Music Notes to their profile.
Features
 * Full Music Catalog Search: Search millions of tracks available on Instagram.
 * Custom Captions: Attach short text captions (up to 60 characters) above the music.
 * Automated Session Management: Authenticates using serialized session tokens (session.json) to prevent repeated login challenges.
 * Auto-Reconnect Engine: Background execution loop handles temporary network dropouts.
Prerequisites
 * Android Device with Termux (or any server with Python 3.9+)
 * Telegram Bot Token (Obtained via @BotFather on Telegram)
 * Instagram Account
Installation & Setup Guide
Step 1: Install Termux Build Toolsbash
pkg update -y && pkg install python rust clang make python-pillow git nano -y

### Step 2: Install Python Libraries
```bash
python -m pip install -U pip setuptools wheel
python -m pip install --extra-index-url [https://termux-user-repository.github.io/pypi/](https://termux-user-repository.github.io/pypi/) instagrapi python-telegram-bot

Step 3: Clone Repository & Setup Session
git clone [https://github.com/ZyroXD/Noxveilbot.git](https://github.com/ZyroXD/Noxveilbot.git)
cd Noxveilbot
python setup_session.py

Step 4: Run the Bot
Add your Telegram Bot Token inside bot.py, then start the bot:
while true; do python bot.py; sleep 2; done

Telegram Bot Commands
| Command | Usage | Description |
|---|---|---|
| /start | /start | Welcomes user and displays usage rules. |
| /note | /note <song> | <caption text> | Searches music catalog and posts a Music Note with text. |
| /delete_note | /delete_note | Removes active Music Note from your Instagram profile. |
Examples:
 * /note golden brown | hi
 * /note blinding lights | 
Security Notice
Never commit or upload your session.json file or active Telegram Bot Token. Ensure session.json remains listed in .gitignore.

### How to use this in Termux:

1. Open `README.md` in `nano`:
   ```bash
   nano README.md

 * Paste the text above into the file.
 * Save and exit (CTRL \rightarrow o \rightarrow Enter, then CTRL \rightarrow x).
 * Commit and push to GitHub:
   git add README.md
git commit -m "Add detailed README documentation"
git push origin main
