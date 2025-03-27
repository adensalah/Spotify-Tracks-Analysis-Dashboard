
# 🎵 Spotify Tracks Analysis Dashboard

[**Dashboard Preview**]<img width="1275" alt="Capture_spotify" src="https://github.com/user-attachments/assets/489d9361-af76-45c9-ab7e-72e5cac220a9" />


A data analysis dashboard that visualizes trends in Spotify tracks using Python, Pandas, and Streamlit. Perfect for showcasing data analysis skills in your portfolio.

## 🚀 Features

- **Interactive filters** for year and popularity range
- **Automated date handling** (converts release dates to years)
- **Smart fallback system** when columns are missing
- **Multiple visualization types**:
  - Line charts (for temporal data)
  - Histograms (for distributions)
  - Dynamic rendering based on available data

## 🛠️ Tech Stack

| Component       | Technology |
|----------------|------------|
| **Core**       | Python 3.8+ |
| **Data Processing** | Pandas, NumPy |
| **Visualization** | Matplotlib, Seaborn |
| **Dashboard** | Streamlit |
| **Data Storage** | CSV (SQL optional) |

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/adensalah/Spotify-Tracks-Analysis-Dashboard.git
   cd spotify-analysis
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   *(or manually install: `pandas streamlit matplotlib seaborn`)*

3. **Add your dataset**
   - Place your Spotify data CSV in the project root
   - Default expected name: `spotify_tracks.csv`
   - [Download sample dataset](https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset)

## 🖥️ Usage

```bash
streamlit run dashboard.py
```

The dashboard will open in your default browser at `http://localhost:8501`

## 📊 Customizing for Your Dataset

1. **Check your columns**:
   ```python
   print(df.columns.tolist())
   ```

2. **Update these variables in `dashboard.py`**:
   ```python
   DATE_COLUMN = 'release_date'  # Change to your date column
   MAIN_METRIC = 'popularity'    # Change to your focus metric
   ```

## 📂 Project Structure

```
spotify-analysis/
├── dashboard.py          # Main Streamlit application
├── spotify_tracks.csv    # Dataset (ignored in git)
├── requirements.txt      # Dependencies
├── analysis.ipynb        # Jupyter notebook for exploration (optional)
└── README.md             # This file
```

## 🤝 Contributing

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License
Distributed under the MIT License. See `LICENSE` for more information.

```

