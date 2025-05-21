import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.title("🎧 Music Streaming Analytics")

# Load dataset
df = pd.read_csv("spotify_tracks.csv")

# Optional: Show some data
st.write(df.head())

