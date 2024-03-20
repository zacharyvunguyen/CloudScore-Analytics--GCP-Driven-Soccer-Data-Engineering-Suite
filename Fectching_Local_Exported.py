import requests
import pandas as pd
import numpy as np
import os

def fetch_data(team_id, league_id, season_year):
    url = "https://api-football-v1.p.rapidapi.com/v3/players"
    querystring = {"team": team_id, "league": league_id, "season": season_year}
    headers = {
        "X-RapidAPI-Key": "b01fb7d4d5msh9d6010d034fce6bp136078jsnfe71045ac5ee",
        "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
    }

    try:
        response = requests.get(url, headers=headers, params=querystring)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def process_data(data):
    if not data or 'response' not in data:
        print("Invalid data or empty response.")
        return pd.DataFrame()

    players_data = []
    for player in data['response']:
        player_info = player['player']
        stats = player['statistics'][0]
        player_data = {
            "Player name": player_info['name'],
            "Nationality": player_info['nationality'],
            "Position": player_info.get('position', 'N/A'),
            "Weight": player_info.get('weight', 'N/A'),
            "Height": player_info.get('height', 'N/A'),
            "Team": stats['team']['name'],
            "League": stats['league']['name'],
            "Appearances": stats['games']['appearences'],
            "Lineups": stats['games']['lineups'],
            "Minutes": stats['games']['minutes'],
            "Goals": stats['goals']['total'],
            "Assists": stats['goals']['assists'],
            "Yellow Cards": stats['cards']['yellow'],
            "Red Cards": stats['cards']['red'],
            "Shots Total": stats['shots']['total'],
            "Shots On": stats['shots']['on'],
            "Passes Total": stats['passes']['total'],
            "Key Passes": stats['passes']['key'],
            "Pass Accuracy": stats['passes']['accuracy'],
            "Tackles Total": stats['tackles']['total'],
            "Blocks": stats['tackles']['blocks'],
            "Interceptions": stats['tackles']['interceptions'],
            "Dribbles Attempts": stats['dribbles']['attempts'],
            "Dribbles Success": stats['dribbles']['success'],
            "Dribbled Past": stats['dribbles']['past'],
            "Fouls Drawn": stats['fouls']['drawn'],
            "Fouls Committed": stats['fouls']['committed'],
            "Duels Total": stats['duels']['total'],
            "Duels Won": stats['duels']['won'],
            "Penalty Scored": stats['penalty']['scored'],
            "Penalty Missed": stats['penalty']['missed'],
            "Penalty Saved": stats['penalty']['saved']
        }
        players_data.append(player_data)
    return pd.DataFrame(players_data)

def clean_and_transform_data(df):
    df = df.drop(['Position', 'Dribbled Past'], axis=1)
    df['Weight'] = df['Weight'].str.replace(' kg', '').str.replace('kg', '').replace('none', np.nan)
    df['Weight'] = pd.to_numeric(df['Weight'], errors='coerce')
    average_weight = df['Weight'].dropna().mean()
    df['Weight'].fillna(average_weight, inplace=True)

    df['Height'] = df['Height'].str.replace(' cm', '').str.replace('cm', '').replace('none', np.nan)
    df['Height'] = pd.to_numeric(df['Height'], errors='coerce')
    average_height = df['Height'].dropna().mean()
    df['Height'].fillna(average_height, inplace=True)

    df.fillna(0, inplace=True)
    return df

def save_to_local(df, local_folder, file_name):
    if not os.path.exists(local_folder):
        os.makedirs(local_folder)

    file_path = os.path.join(local_folder, file_name)
    df.to_csv(file_path, index=False, header=False)
    print(f"File {file_path} saved locally.")

def validate_input(input_str, input_type):
    try:
        if input_type == 'int':
            return int(input_str)
        return str(input_str)
    except ValueError:
        print(f"Invalid input for {input_type}. Please try again.")
        return None

def main():
    team_id = validate_input(input("Enter team ID: "), 'int')
    league_id = validate_input(input("Enter league ID: "), 'int')
    season_year = validate_input(input("Enter season year: "), 'int')

    if team_id is None or league_id is None or season_year is None:
        print("Invalid inputs provided.")
        return

    data = fetch_data(team_id, league_id, season_year)
    if data:
        df = process_data(data)
        if not df.empty:
            df_cleaned = clean_and_transform_data(df)
            file_name = f"players_data_team_{team_id}_league_{league_id}_season_{season_year}.csv"
            save_to_local(df_cleaned, "local_exported_csv", file_name)

if __name__ == "__main__":
    main()
