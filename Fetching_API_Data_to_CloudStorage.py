import requests
import pandas as pd
import numpy as np
from google.cloud import storage

def fetch_data():
    url = "https://api-football-v1.p.rapidapi.com/v3/players"
    querystring = {"team": "33", "league": "39", "season": "2022"}
    headers = {
        "X-RapidAPI-Key": "b01fb7d4d5msh9d6010d034fce6bp136078jsnfe71045ac5ee",
        "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    return response.json()

def process_data(data):
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

    # Drop unnecessary columns
    df = df.drop(['Position', 'Dribbled Past'], axis=1)

    # Cleaning Weight column
    # Remove 'kg' and convert 'none' to NaN, then convert to numeric
    df['Weight'] = df['Weight'].str.replace(' kg', '').str.replace('kg', '')
    df['Weight'].replace('none', np.nan, inplace=True)
    df['Weight'] = pd.to_numeric(df['Weight'], errors='coerce')

    # Calculate the average weight and replace NaN values with it
    average_weight = df['Weight'].dropna().mean()
    df['Weight'].fillna(average_weight, inplace=True)

    # Cleaning Height column
    # Remove 'cm' and convert 'none' to NaN, then convert to numeric
    df['Height'] = df['Height'].str.replace(' cm', '').str.replace('cm', '')
    df['Height'].replace('none', np.nan, inplace=True)
    df['Height'] = pd.to_numeric(df['Height'], errors='coerce')

    # Calculate the average height and replace NaN values with it
    average_height = df['Height'].dropna().mean()
    df['Height'].fillna(average_height, inplace=True)

    # Replace all other NaN values in the DataFrame with 0
    df.fillna(0, inplace=True)


    return df

def upload_to_gcs(df, bucket_name, destination_blob_name):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    # Save DataFrame to a CSV on memory
    df.to_csv(destination_blob_name, index=False,header=False)

    # Upload the CSV to GCS
    blob.upload_from_filename(destination_blob_name)
    print(f"File {destination_blob_name} uploaded to {bucket_name}.")

def main():
    """
    Main function to orchestrate data fetching, processing, and uploading.
    """
    data = fetch_data()
    df = process_data(data)
    df_cleaned = clean_and_transform_data(df)
    upload_to_gcs(df_cleaned, "2024test", "players_data.csv")

if __name__ == "__main__":
    main()