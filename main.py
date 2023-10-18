import requests
import json
import random

# Replace 'YOUR_API_KEY' with your actual Steam API key
API_KEY = "1C23F8402D5691B253A91DF379993D9D"
# Replace 'YOUR_STEAM_ID' with the user's 64-bit SteamID. You can find this ID on a user's Steam profile.
STEAM_ID = "76561197963553194"


#Output total games owned
#print(totalGames)


# Replace with the 64-bit Steam IDs of the two friends
FRIEND_1_STEAM_ID = '76561198006724030'
FRIEND_2_STEAM_ID = '76561198021111520'

# Function to retrieve the list of owned games for a given user
def get_owned_games(steam_id):
    url = f'https://api.steampowered.com/IPlayerService/GetOwnedGames/v1/?key={API_KEY}&steamid={steam_id}&include_appinfo=1&format=json'
    try:
        response = requests.get(url)
        data = response.json()
        if 'response' in data and 'games' in data['response']:
            return [game['appid'] for game in data['response']['games']]
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
    return []

# Get the lists of owned games for each friend
friend_1_games = get_owned_games(FRIEND_1_STEAM_ID)
friend_2_games = get_owned_games(FRIEND_2_STEAM_ID)


# Compare the lists to find common games
common_games = list(set(friend_1_games) & set(friend_2_games))

play_me = []  # Initialize the play_me list

if common_games:
    print("Try this game!")
    random_game = random.choice(common_games)

    def check_if_multiplayer(random_game):
        url = f'https://store.steampowered.com/api/appdetails?appids={random_game}'
        response = requests.get(url)
        data = response.json()
        game_name = data[str(random_game)]['data']['name']
        # data[str(random_game)]['data']['short_description'] for a brief game description
        print(game_name)
        # Check if "multi-player" is present in the "categories" field
        categories = data[str(random_game)]['data']['categories']
        is_multiplayer = any(category['description'] == 'Multi-player' for category in categories)

        if is_multiplayer:
            print("This game is multi-player.")
        else:
            print("This game is NOT multi-player. Try again.")
        return random_game
    check_if_multiplayer(random_game)
else:
    print("No common games found between these friends.")

