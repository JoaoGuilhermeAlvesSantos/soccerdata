import requests
import json

API_KEY = "cc56fc5b0d4c32491eb4025982cd42fc"

BASE_URL = "https://v1.basketball.api-sports.io/games"
HEADERS = {"x-apisports-key": API_KEY}

params = {
    "league": 12,               # NBA
    "season": "2023-2024"       # Temporada
}

response = requests.get(BASE_URL, headers=HEADERS, params=params)
data = response.json()

games = []

for game in data.get("response", []):
    home_team = game["teams"]["home"]["name"]
    away_team = game["teams"]["away"]["name"]
    date = game["date"]

    # Corrigido aqui: pega direto a string `venue`
    local = game.get("venue", "Desconhecido")

    games.append({
        "home_team": home_team,
        "away_team": away_team,
        "date": date,
        "local": local
    })

with open("nba_2023.json", "w", encoding="utf-8") as f:
    json.dump(games, f, indent=2, ensure_ascii=False)

print(f"{len(games)} partidas salvas em 'nba_2023.json'.")
