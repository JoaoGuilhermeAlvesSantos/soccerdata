import requests
import json

API_KEY = "cc56fc5b0d4c32491eb4025982cd42fc"

BASE_URL = "https://v3.football.api-sports.io/fixtures"

HEADERS = {
    "x-apisports-key": API_KEY
}

params = {
    "league": 78,        # Brasileirão Série A
    "season": 2023,      # Temporada
    "from": "2023-01-01",
    "to": "2023-12-31"
}

response = requests.get(BASE_URL, headers=HEADERS, params=params)
data = response.json()

all_matches = []

for match in data.get("response", []):
    home_team = match["teams"]["home"]["name"]
    away_team = match["teams"]["away"]["name"]
    date = match["fixture"]["date"]

    venue = match["fixture"].get("venue", {})
    stadium = venue.get("name", "Desconhecido")
    city = venue.get("city", "")
    local = f"{stadium}, {city}".strip().strip(",")

    all_matches.append({
        "home_team": home_team,
        "away_team": away_team,
        "date": date,
        "local": local
    })

# Saída em JSON
print(json.dumps(all_matches, indent=2, ensure_ascii=False))
# Save the output to a JSON file
output_file = "matches_bundesliga.json"
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(all_matches, f, indent=2, ensure_ascii=False)

print(f"Data has been saved to {output_file}")