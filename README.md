1. Termux System & Package Setup Commands
Install System Compiler & Build Dependencies
pkg update -y && pkg install python rust clang make python-pillow git nano -y

 * Details: Updates Termux packages and installs Python, C/Rust compilers (required for building packages), Pillow (image processing), Git (version control), and Nano (text editor).
Upgrade Python Build Tools
python -m pip install -U pip setuptools wheel

 * Details: Upgrades Python's package manager (pip), build tools (setuptools), and wheel generator to their latest versions.
Install Python Libraries via Termux Repository
python -m pip install --extra-index-url https://termux-user-repository.github.io/pypi/ instagrapi python-telegram-bot

 * Details: Installs instagrapi (Instagram Private API framework) and python-telegram-bot (Telegram Bot API wrapper) using pre-built Android wheels to avoid build errors.
Enable Background Execution (Prevent Sleep)
termux-wake-lock

 * Details: Prevents Android's battery saver from putting Termux to sleep or closing network connections when your phone screen turns off.
2. File Creation & Management Commands
Create or Edit bot.py
nano bot.py

 * Details: Opens the bot.py file in the Nano editor so you can paste or modify your main Telegram bot script.
Create or Edit setup_session.py
nano setup_session.py

 * Details: Opens the session creation script used to log into Instagram and generate your session.json file.
Create .gitignore File
nano .gitignore

 * Details: Opens the .gitignore configuration file used to tell Git which sensitive files (like session.json) should never be uploaded to GitHub.
Create README.md File
nano README.md

 * Details: Opens the documentation file used to display repository details, command guides, and setup steps on GitHub.
List All Files (Including Hidden Files)
ls -la

 * Details: Displays every file and folder in your current directory, including hidden configuration files starting with a dot (such as .gitignore).
Remove Broken Directory (If bot.py was made as a folder)
rm -rf bot.py

 * Details: Deletes a directory named bot.py if it was accidentally created as a folder instead of a Python script file.
3. Execution & Bot Operation Commands
Test Network Connectivity to Instagram
ping -c 3 instagram.com

 * Details: Sends 3 test packets to Instagram's servers to verify that your phone's Wi-Fi, Mobile Data, or VPN connection is working properly.
Test Network Connectivity to Telegram
ping -c 3 api.telegram.org

 * Details: Sends 3 test packets to Telegram's API servers to confirm that Telegram is reachable from your network.
Run Instagram Session Authenticator
python setup_session.py

 * Details: Logs into Instagram using your credentials or session ID and exports session cookies to session.json.
Run Telegram Bot (Single Run)
python bot.py

 * Details: Starts your Telegram bot once. Useful for testing initial connectivity and checking for terminal logs.
Run Telegram Bot in Auto-Restart Loop
while true; do python bot.py; sleep 2; done

 * Details: Runs the bot in a continuous background loop. If a network flicker or VPN drop causes bot.py to disconnect, this script automatically restarts it after 2 seconds.
4. Git & GitHub Repository Commands
Set Git Username
git config --global user.name "ZyroXD"

 * Details: Registers your GitHub username (ZyroXD) in your local Git settings.
Set Git Email
git config --global user.email "your_email@example.com"

 * Details: Sets your email address associated with your GitHub commits.
Initialize Local Git Repository
git init

 * Details: Creates a new local Git repository inside your current Termux folder.
Stage All Files for Commit
git add .

 * Details: Prepares all new, edited, and non-ignored files in your folder to be included in the next commit.
Check Git Status
git status

 * Details: Displays staged files (in green) and untracked files (in red). Helps verify that session.json is properly ignored.
Commit Staged Files
git commit -m "Add Instagram Music Note bot scripts"

 * Details: Saves a snapshot of all staged files in your local Git timeline with a custom description message.
Set Main Branch Name
git branch -M main

 * Details: Renames your default local Git branch to main.
Connect Remote GitHub Repository
git remote add origin https://github.com/ZyroXD/Noxveilbot.git

 * Details: Links your local Termux folder to your online GitHub repository (Noxveilbot).
Update Remote GitHub Repository URL
git remote set-url origin https://github.com/ZyroXD/Noxveilbot.git

 * Details: Changes or corrects the remote GitHub URL if it was typed incorrectly in a previous step.
Push Code to GitHub
git push -u origin main

 * Details: Uploads your local committed code to your GitHub repository. (Requires entering your username ZyroXD and Personal Access Token ghp_...).
Force Push Code to GitHub
git push -u origin main --force

 * Details: Overwrites remote files on GitHub with your local code. Useful when setting up a brand-new repository containing default files.
5. Telegram Chat Commands (Typed in Telegram)
Welcome Command
/start
 * Details: Sends a greeting message in Telegram and displays instructions on how to use the bot.
Post Music Note with Text Caption
/note golden brown | hi
 * Details: Searches Instagram's global music database for "golden brown", selects the top matching track, and publishes an Instagram Music Note with the text "hi".
Post Music Note Without Text (Music Only)
/note blinding lights |
 * Details: Searches Instagram for "blinding lights" and posts the song to your Instagram Note without any text overlay.
Delete Current Music Note
/delete_note
 * Details: Instantly removes any active Instagram Note from your profile.
 
