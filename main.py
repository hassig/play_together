import requests
import json
import random

# Replace 'YOUR_API_KEY' with your actual Steam API key
API_KEY = "1C23F8402D5691B253A91DF379993D9D"
# Replace 'YOUR_STEAM_ID' with the user's 64-bit SteamID. You can find this ID on a user's Steam profile.
STEAM_ID = "76561197963553194"

# # Set the Steam API for getting game data
# url = f"http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={API_KEY}&steamid={STEAM_ID}&include_appinfo=1&format=json"

# #get request and save response to a variable
# response = requests.get(url)
# #check for errors
# print(response.status_code)
# #convert to JSON and save to another variable
# data = response.json()

# if 'response' in data and 'games' in data['response']:
#     owned_games = data['response']['games']

#     if owned_games:
#         print("Owned Games:")
#         for game in owned_games:
#             print(f"{game['name']} - App ID: {game['appid']}, Playtime (minutes): {game['playtime_forever']}")
#     else:
#         print("No games found for this user.")
# else:
#     print("Unable to retrieve data. Make sure your Steam ID and API key are correct.")

#Getting integer value of total games owned
# totalGames = str(data["response"]["game_count"])

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
# Pick random common game ID from lists
#random_game = random.choice(common_games)

# response = random_game
# games = data

# if common_games:
#     print("Try this game!")
#     random_game = random.choice(common_games)
#     def check_if_multiplayer(random_game):
#         url = f'https://store.steampowered.com/api/appdetails?appids={random_game}'
#         try:
#             response = requests.get(url)
#             data = response.json()
#             if 'success' in data and 'name' in data['response']:
#                 return [data['name']]
#                 play_me = [data['name']]
#         except requests.exceptions.RequestException as e:
#             print(f"Request error: {e}")
#         return play_me
#     print(play_me)

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
        #game_name = data["name"]
            # if 'success' in {app_id}:
            #     return [data['name']]
            # play_me.append(game_name)


#    play_me = check_if_multiplayer(game_name)

    check_if_multiplayer(random_game)


# def check_if_multiplayer(app_id):
#     lst.append(arg)
#     return lst

# print list_at_function_scope(2)
# print list_at_function_scope("qwqwe")


# # Access the 'name' field from the JSON data
# game_name = json_data["game"]["name"]

  #  print(play_me)


    #     except requests.exceptions.RequestException as e:
    #         print(f"Request error: {e}")

    #     return play_me

    # play_me = check_if_multiplayer(random_game)
    # print(play_me)

   # print(random_game)
    #print(random.choice(common_games))
    # for app_id in common_games:
    #     print(f"App ID: {app_id}")
else:
    print("No common games found between these friends.")

#print (common_games)
# if common_games:
#     def check_if_multiplayer(random_game):
#         url = f'https://store.steampowered.com/api/appdetails?appids={random_game}'
#         try:
#             response = requests.get(url)
#             appdata = response.json()
#             if 'response' in appdata and 'games' in appdata['response']:
#                 return [game['name'] for game in appdata['response']['games']]
#         except requests.exceptions.RequestException as e:
#             print(f"Request error: {e}")
#         return []

#     print("Try this game you both own:")
#     for game in common_games:
#         print(f"{game['name']}")

# else:
#     print("No common games found between these friends.")