from Modules.Twitch import Send

def CommandHandler(irc, CHANNEL, info: tuple):
    command, args, user = info

    if command == "-hello":
        Send(irc, CHANNEL, "Hello World!")
    elif command == "-dan":
        Send(irc, CHANNEL, "Dan is so hot!! You should follow him on twitch.tv/danmanplayz where he streams shirtless!")
    elif command == "-umbral":
        Send(irc, CHANNEL, "Umbral is such a cutie patootie!! You should follow him on twitch.tv/umbralaasimar cuz he is such a cutie patootie!")
    elif command == "-user":
        if args:
            Send(irc, CHANNEL, f"{user}, you passed arguments: {' '.join(args)}")
        else:
            Send(irc, CHANNEL, f"{user}")





    elif command == "-quit":
        Send(irc, CHANNEL, "Goodbye World!")
        return True
    
    return False