import socket

def IRCConfig(irc, SERVER="irc.chat.twitch.tv", PORT=6667):
    """
    Establishes a TCP connection to Twitch IRC server.

    @param irc (socket): The IRC socket object to connect
    @param SERVER (str): The IRC server address (default: irc.chat.twitch.tv)
    @param PORT (int): The port number to connect on (default: 6667)

    @return None
    """
    irc.connect((SERVER, PORT))


def IRCInfo(irc, TOKEN, NICKNAME, CHANNEL):
    """
    Authenticates and joins a Twitch channel using IRC protocol.

    @param irc (socket): The connected IRC socket
    @param TOKEN (str): The OAuth token used for authentication (starts with 'oauth:')
    @param NICKNAME (str): The Twitch bot's username
    @param CHANNEL (str): The target channel to join (must start with #)

    @return None
    """
    if not NICKNAME or not TOKEN:
        raise ValueError("Missing BOTNAME or OAUTH_ID in environment.")
    
    irc.send(f"PASS {TOKEN}\r\n".encode('utf-8'))
    irc.send(f"NICK {NICKNAME}\r\n".encode('utf-8'))
    irc.send(f"JOIN {CHANNEL}\r\n".encode('utf-8'))


def connect(Token, Nickname, Channel):
    """
    Creates an IRC socket, connects to the Twitch IRC server, and authenticates.

    @param Token (str): The OAuth token for login
    @param Nickname (str): The bot's Twitch username
    @param Channel (str): The target Twitch channel (must start with #)

    @return irc (socket): The fully connected and authenticated IRC socket
    """
    irc = socket.socket()
    IRCConfig(irc)
    IRCInfo(irc, Token, Nickname, Channel)
    
    return irc