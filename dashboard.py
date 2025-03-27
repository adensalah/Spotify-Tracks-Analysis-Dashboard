import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("🎵 Spotify Tracks Dashboard")

# Load data
df = pd.read_csv("spotify_tracks.csv")

# 1. Check if date column exists
if 'release_date' in df.columns:
    df['year'] = pd.to_datetime(df['release_date']).dt.year
    # Year filter
    selected_year = st.sidebar.slider("Year", 
                                    min_value=int(df['year'].min()),
                                    max_value=int(df['year'].max()),
                                    value=(2010, 2020))
    filtered_df = df[df['year'].between(*selected_year)]
else:
    # Fallback: Filter by popularity
    selected_range = st.sidebar.slider("Popularity Range", 0, 100, (50, 90))
    filtered_df = df[df['popularity'].between(*selected_range)]
    st.warning("No release date found - filtering by popularity instead")

# Visualization
st.subheader("Data Overview")
st.write(filtered_df.head())

# Plot
fig, ax = plt.subplots()
if 'year' in df.columns:
    sns.lineplot(data=filtered_df, x='year', y='popularity', ax=ax)
    ax.set_title("Popularity Over Time")
else:
    sns.histplot(filtered_df['popularity'], bins=20, ax=ax)
    ax.set_title("Popularity Distribution")
st.pyplot(fig)