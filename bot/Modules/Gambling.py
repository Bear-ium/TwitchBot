import random
from Modules.Twitch import Send

def handle_roulette(irc, channel, user, args):
    """
    Simulates a roulette-style gamble. 1 in 6 chance to lose your bet.

    @param irc (socket): IRC connection to Twitch
    @param channel (str): Target Twitch channel
    @param user (str): Username who invoked the command
    @param args (list): Arguments passed with the command (expects 1 amount)

    @return None
    """
    if len(args) != 1:
        Send(irc, channel, f"@{user} usage: -roulette <amount>")
        return

    try:
        amount = int(args[0])
        if amount <= 0:
            raise ValueError
    except ValueError:
        Send(irc, channel, f"@{user} please enter a valid positive number.")
        return

    # Simulate 1 in 6 chance to lose
    bullet_chamber = random.randint(1, 6)
    if bullet_chamber == 1:
        Send(irc, channel, f"@{user} pulled the trigger and lost {amount} coins!")
    else:
        Send(irc, channel, f"@{user} survived the roulette and keeps their {amount} coins!")