import kaggle
import os
import pandas as pd

def setup_data():
    """Handle all data operations in one place"""
    # Create data directory if needed
    os.makedirs('data', exist_ok=True)
    
    # Download from Kaggle
    def download_data():
        print("Downloading dataset...")
        path = kagglehub.dataset_download("cbhavik/music-taste-recommendation")
        # Move files to data folder
        for file in os.listdir(path):
            os.rename(f"{path}/{file}", f"data/{file}")
        return [f"data/{f}" for f in os.listdir("data")]
    
    # Process data
    def process_data():
        raw_file = [f for f in os.listdir("data") if f.endswith('.csv')][0]
        df = pd.read_csv(f"data/{raw_file}")
        
        # Basic cleaning
        df = df.dropna(subset=['track_name', 'artist'])
        df['duration_min'] = df['duration_ms'] / 60000
        
        # Save processed version
        df.to_csv("data/processed_music.csv", index=False)
        return "data/processed_music.csv"
    
    # Check if processed data exists
    if not os.path.exists("data/processed_music.csv"):
        if not any(f.endswith('.csv') for f in os.listdir("data")):
            download_data()
        return process_data()
    return "data/processed_music.csv"