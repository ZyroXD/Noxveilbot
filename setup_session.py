from instagrapi import Client

cl = Client()

# Replace with your actual Instagram credentials
username = "Your_Username"
password = "Your_Password"

cl.login(username, password)
cl.dump_settings("session.json")
print("Session successfully created and saved to session.json!")

