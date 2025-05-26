from Modules.Twitch import Send
from Modules.Gambling import coin_flip, roulette
from Modules.Admins import admins

def CommandHandler(irc, CHANNEL, info: tuple):
    command, args, user = info
    user = user.lower()

    # Normal Commands
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
    elif command in ("-shoutout", "-so"):
        if user in admins and args:
            arg = args[0].strip('@')
            Send(irc, CHANNEL, f"You should follow @{arg} on twitch.tv/{arg}")
        else:
            Send(irc, CHANNEL, "You either need to be an Admin, or you forgot to add the channel!")

    # Gamble Commands
    elif command in ("-coinflip", "-cf"):
        Send(irc, CHANNEL, f"Your coin landed on {coin_flip()}")
    elif command == "-roulette":
        Send(irc, CHANNEL, roulette(args[0], 50))



    # Quit Command
    elif command == "-quit":
        Send(irc, CHANNEL, "Goodbye World!")
        return True
    
    return False 