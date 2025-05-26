import random

errorMsg = "Coin Flip somehow broke? Please tell @MajojoBears on Twitch or @bae.r on Discord to fix this!"

def coin_flip():
    """
    Simulates a coin flip, returning either 'Heads' or 'Tails'.

    Uses a random number generator to select one of the two outcomes.

    @return str: "Heads" or "Tails"
    """
    n = random.randint(1,2)
    if n == 1:
        return "Heads"
    elif n == 2:
        return "Tails"
    else:
        return errorMsg

def roulette(amount: int, max: int = 50):
    """
    Simulates a roulette-style gambling game.
    
    A random number from 1 to 100 is generated. If the number is within
    the `max` threshold, the player wins double the amount. Otherwise, they lose it.

    @param amount (int): The amount of currency to bet.
    @param max (int): The win threshold (e.g., 50 means 50% chance to win).

    @return str: A result message indicating win or loss.
    """
    try:
        amount = int(amount)
    except ValueError:
        return "Invalid amount. Please enter a number."
    
    n = random.randint(1,100)
    win = n <= max
    
    result = (lambda w: f"You win {amount * 2}!" if w else f"You lost {amount}!")(win)
    return result