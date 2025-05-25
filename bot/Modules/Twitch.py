def Send(irc, channel: str, msg: str):
    """
    Sends a message to a specific Twitch IRC channel.

    @param irc (socket): The active IRC socket connection
    @param channel (str): The Twitch channel to send the message to (must start with #)
    @param msg (str): The message text to send

    @return None
    """
    irc.send(f"PRIVMSG {channel} :{msg}\r\n".encode('utf-8'))

def GetUsername(raw: str) -> str:
    """
    Extracts the sender's username from the raw IRC message.

    @param raw (str): Raw IRC PRIVMSG string
    @return username (str)
    """
    return raw.split("!", 1)[0][1:]