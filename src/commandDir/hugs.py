import random
hugs = [
    "https://c.tenor.com/9e1aE_xBLCsAAAAM/anime-hug.gif",
    "https://c.tenor.com/gKlGEBBkliwAAAAM/anime-yuru-yuri.gif",
    "https://c.tenor.com/TJuvig1CFBQAAAAM/the-pet-girl-of-sakurasou-sakurasou-no-pet-na-kanojo.gif",
    "https://c.tenor.com/gqM9rl1GKu8AAAAM/kitsune-upload-hug.gif",
]

def get_rand_hug():
    random_hug = random.choice(hugs)
    return random_hug