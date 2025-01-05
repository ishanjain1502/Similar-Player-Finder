import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler
from sklearn.metrics.pairwise import cosine_similarity

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

data = pd.read_csv("./players_22.csv/players_22.csv")
selected_features = [ 'short_name' ,'player_positions','pace','shooting' ,'passing' ,'dribbling','defending', 'physic']

if all(feature in data.columns for feature in selected_features):
    X = data[selected_features]
else:
    missing = [feature for feature in selected_features if feature not in data.columns]
    raise ValueError(f"The following features are missing from the dataset: {missing}")

for index, row in data.iterrows():
    positions = row['player_positions'].split(',')
    if positions[0] in ['LW', 'RW', 'CF', 'ST']:
        data.at[index, 'player_positions'] = 'attacker'
    if positions[0] in ['LM', 'RM', 'CM', 'CAM', 'LAF', 'RAF']:
        data.at[index, 'player_positions'] = 'midfielder'
    if positions[0] in ['LB', 'LWB', 'LCB', 'CB', 'RCB', 'RWB', 'RB', 'CDM', 'LDM', 'RDM']:
        data.at[index, 'player_positions'] = 'defender'
    if positions[0] in ['GK']:
        data.at[index, 'player_positions'] = 'goalkeeper'
        
data = data[data['player_positions'] != 'goalkeeper']
df_selected_features = data[selected_features]
print(df_selected_features.shape)

encoder = OneHotEncoder(sparse_output=False)
encoded = encoder.fit_transform(df_selected_features[['player_positions']])
position_feature_names = encoder.get_feature_names_out(['player_positions'])

numerical_features = ['pace','shooting' ,'passing' ,'dribbling','defending', 'physic']
scaler = MinMaxScaler()
numerical_scaled = scaler.fit_transform(data[numerical_features])

combined_features = np.hstack([encoded, numerical_scaled])
feature_names = list(position_feature_names) + numerical_features
combined_df = pd.DataFrame(combined_features, columns=feature_names)
# print(combined_df.head(5))

similarity_matrix = cosine_similarity(combined_features)

# Display similarity matrix for player names
similarity_df = pd.DataFrame(similarity_matrix, index=data['short_name'], columns=data['short_name'])


class PlayerQuery(BaseModel):
    player_positions: str
    speed: float
    physic: float
    defense: float
    dribbling: float
    shooting: float
    passing: float

# Helper Function to Process User Input
def process_user_input(player_positions, speed, physic, defense, dribbling, shooting, passing):
    # Encode player_position and body_type
    user_position_encoded = encoder.transform([[player_positions]])
    # Scale numerical attributes
    user_numerical = scaler.transform([[speed, physic, defense, dribbling, shooting, passing]])
    # Combine all features
    return np.hstack([user_position_encoded, user_numerical])

# Helper Function to Find Similar Players
def find_similar_players(user_features, combined_features, player_names, top_n=3):
    similarities = cosine_similarity(user_features, combined_features).flatten()
    similar_indices = np.argsort(-similarities)[:top_n]
    similar_players_names = df_selected_features.iloc[similar_indices]['short_name'].values
    print('-------------------------------------\n\n\n\n', similar_players_names, '\n\n\n\n-------------------------')
    similar_players_names = similar_players_names.tolist()
    return similar_players_names

# API Endpoint
@app.post("/find_similar_players/")
async def find_players(query: PlayerQuery):
    user_features = process_user_input(
        query.player_positions,
        query.speed,
        query.physic,
        query.defense,
        query.dribbling,
        query.shooting,
        query.passing
    ).reshape(1, -1)
    similar_players = find_similar_players(user_features, combined_features, data['short_name'])
    return {"similar_players": similar_players}