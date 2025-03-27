import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import sqlite3

# Load data
df = pd.read_csv("spotify_tracks.csv")

# --- Data Cleaning ---
df = df.dropna()  # Remove missing values
df['duration_min'] = df['duration_ms'] / 60000  # Convert ms to minutes

# --- SQL Integration ---
conn = sqlite3.connect("spotify.db")
df.to_sql("tracks", conn, if_exists="replace", index=False)

# Query: Top 10 popular tracks
query = """
SELECT name, artists, popularity 
FROM tracks 
ORDER BY popularity DESC 
LIMIT 10
"""
top_tracks = pd.read_sql(query, conn)

# --- Visualization ---
plt.figure(figsize=(12, 6))

# Plot 1: Popularity Distribution
plt.subplot(1, 2, 1)
sns.histplot(df['popularity'], bins=30, kde=True)
plt.title("Popularity Distribution")

# Plot 2: Danceability vs. Energy
plt.subplot(1, 2, 2)
sns.scatterplot(data=df, x='danceability', y='energy', hue='explicit', alpha=0.6)
plt.title("Danceability vs. Energy")

plt.tight_layout()
plt.savefig("spotify_insights.png")  # Save for dashboard
plt.show()

# Close SQL connection
conn.close()