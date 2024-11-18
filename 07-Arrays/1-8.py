computer_games = [
   "Minecraft", "Fortnite", "Cyberpunk 2077", "The Witcher 3",
   "League of Legends", "Valorant", "Grand Theft Auto V", 
   "Elden Ring", "Apex Legends", "Call of Duty: Warzone"
]

computer_games.sort()

i = 1
index = 0

while index < len(computer_games):
    print(f'{i}. {computer_games[index]}')
    i += 1
    index += 1