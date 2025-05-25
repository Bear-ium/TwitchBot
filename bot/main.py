import os
from dotenv import load_dotenv
from Modules.Twitch import Send, GetUsername
from Modules.Network import connect

# === Load secrets from .env ===
load_dotenv()

NICKNAME = os.getenv("BOTNAME")
TOKEN = os.getenv("OAUTH_ID")
CHANNEL = "#MajojoBears"

irc = connect(TOKEN, NICKNAME, CHANNEL)

# === Main Loop ===
while True:
    response = irc.recv(2048).decode('utf-8')

    if response.startswith("PING"):
        irc.send("PONG :tmi.twitch.tv\r\n".encode('utf-8'))
        continue

    print(response.strip())

    if "PRIVMSG" in response:
        parts = response.split(":", 2)
        if len(parts) >= 3:
            message = parts[2].strip().lower()
            #user = GetUsername(response)

            if message == "-hello":
                Send(irc, CHANNEL, "Hello World!")
            elif message == "-dan":
                Send(irc, CHANNEL, "Dan is so hot!! You should follow him on twitch.tv/danmanplayz where he streams shirtless!")
            elif message == "-umbral":
                Send(irc, CHANNEL, "Umbral is such a cutie patootie!! You should follow him on twitch.tv/umbralaasimar cuz he is such a cutie patootie!")