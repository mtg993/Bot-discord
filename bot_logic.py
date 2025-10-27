import random

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password

def coinflip():
    num = random.randint(1,2)
    if num == 1:
        return "Heads"
    else:
        return "Tails"
    
def roll_dice():
    return "the dice is", random.randint(1,6)

def kata_hari_ini():
    kata = ["Jangan menyerah!", "Teruslah berusaha!", "Kamu bisa melakukannya!"]
    return random.choice(kata)

def gen_emodji():
    emodji = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923"]
    return random.choice(emodji)

def bantu():
    bantu = [
        "gen_pass = password generator",
        "coinflip = coin flip",
        "roll_dice = dice roll",
        "kata_hari_ini = kata hari ini",
        "gen_emoji = emoji generator"
    ]
    return "\n".join(bantu)



