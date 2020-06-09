from collections import Counter
import random

players = 2
packs_per_player = 6
pack_size = 15
pool_size = packs_per_player * pack_size
sealed = True


cards_in_cube = [
    ("White", 50),
    ("Blue", 50),
    ("Black", 50),
    ("Red", 50),
    ("Green", 50),
    ("Land", 50),
    ("Gold", 50),
    ("Colorless", 25),
]

colors, cards = zip(*cards_in_cube)
if sum(cards) < pool_size * players:
    raise Exception("Not enough cards in the cube for the specified number of players")

deck = []
[deck.extend([color] * number) for color, number in cards_in_cube]
random.shuffle(deck)

if sealed:
    for player in range(players):
        player_pool = deck[player * pool_size : (player + 1) * pool_size]
        c = Counter(player_pool)
        print(f"\nPlayer {player+1} Sealed Pool:")
        for color in colors:
            print(f"{color}: {c[color]}")
else:
    for pack in range(players * packs_per_player):
        pack_pool = deck[pack * pack_size : (pack + 1) * pack_size]
        c = Counter(pack_pool)
        print(f"\nPack {pack+1} Contents:")
        for color in colors:
            print(f"{color}: {c[color]}")
