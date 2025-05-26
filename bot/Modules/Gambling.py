import random

errorMsg = "Coin Flip somehow broke? Please tell @MajojoBears on Twitch or @bae.r on Discord to fix this!"

def coin_flip():
    n = random.randint(1,2)
    if n == 1:
        return "Heads"
    elif n == 2:
        return "Tails"
    else:
        return errorMsg

def roulette(amount: int, max: int):
    try:
        amount = int(amount)
    except ValueError:
        return "Invalid amount. Please enter a number."
    
    n = random.randint(1,100)
    win = n <= max
    
    result = (lambda w: f"You win {amount * 2}!" if w else f"You lost {amount}!")(win)
    return result