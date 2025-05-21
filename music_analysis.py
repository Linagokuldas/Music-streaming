import pandas as pd
from data_utils import setup_data

def analyze():
    data_path = setup_data()
    df = pd.read_csv(data_path)
    
    print("\n=== Basic Analysis ===")
    print(f"Total tracks: {len(df)}")
    print(f"Top 5 artists:\n{df['artist'].value_counts().head()}")
    
    # Add your analysis here
    # ...

if __name__ == "__main__":
    analyze()