import os
from dotenv import load_dotenv
from Modules.Twitch import GetUsername
from Modules.Network import connect
from Modules.Commands import CommandHandler

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
            full_message = parts[2].strip()
            user = GetUsername(response)

            words = full_message.split()
            # Skip empty message
            if not words:
                continue

            # First word is the command
            command = words[0].lower()
            # The rest are arguments
            args = words[1:]

            kill = CommandHandler(irc, CHANNEL, (command, args, user))

            if kill:
                break