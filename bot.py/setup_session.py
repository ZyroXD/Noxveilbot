from instagrapi import Client

cl = Client()

# Replace with your actual Instagram credentials
username = "lost.in.h3ll"
password = "Mughees17"

cl.login(username, password)
cl.dump_settings("session.json")
print("Session successfully created and saved to session.json!")

