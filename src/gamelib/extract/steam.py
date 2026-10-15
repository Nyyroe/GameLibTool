import requests
from gamelib import config

OWNED_STEAM_GAMES_URL = "https://api.steampowered.com/IPlayerService/GetOwnedGames/v1/"

def fetch_owned_games(steam_id: str) -> list[dict]:

    # parameters sent to url; include_appinfo means names are included
    params = {"key": config.STEAM_API_KEY, "steamid": steam_id, "include_appinfo": 1, "include_played_free_games": 1, "format": "json"}
    try:
        # store response from GET request
        r = requests.get(OWNED_STEAM_GAMES_URL, params=params, timeout=20)
        r.raise_for_status()
    except requests.exceptions.RequestException:
        # default exceptions will display steam key in the url in the error msg, so we write a custom one
        raise RuntimeError("Unable to reach Steam. Please check your connection, and that your steam key is correct and located in .env (example can be found in .env.example)") from None
    data = r.json()
    data = (data["response"]["games"])

    return data
