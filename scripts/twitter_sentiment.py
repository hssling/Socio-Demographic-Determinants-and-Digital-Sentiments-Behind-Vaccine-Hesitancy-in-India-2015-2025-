import tweepy, pandas as pd, os
from textblob import TextBlob
from pathlib import Path
from datetime import datetime, timedelta
import re

BASE = Path("projects/vaccine_hesitancy")
OUTT = BASE/"outputs/tables"
OUTT.mkdir(parents=True, exist_ok=True)

def analyze_text(text):
    """Analyze sentiment of text using TextBlob"""
    return TextBlob(str(text)).sentiment.polarity

def clean_text(text):
    """Clean text for better sentiment analysis"""
    text = str(text).lower()
    text = re.sub(r'http\S+', '', text)  # Remove URLs
    text = re.sub(r'@\w+', '', text)     # Remove mentions
    text = re.sub(r'#\w+', '', text)     # Remove hashtags
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    return text.strip()

def fetch_or_load():
    """Load Twitter data and perform sentiment analysis"""
    twdir = BASE/"data/twitter"
    twdir.mkdir(parents=True, exist_ok=True)
    files = list(twdir.glob("*.csv"))

    if files:
        print(f"🐦 Found {len(files)} Twitter data files")
        df = pd.concat([pd.read_csv(f) for f in files], ignore_index=True)
        print(f"📊 Loaded {len(df)} tweets")
    else:
        print("⚠ No Twitter data files found. Run data extraction first:")
        print("  python projects/vaccine_hesitancy/scripts/data_extraction.py")
        return

    # Clean text data
    df["clean_text"] = df["text"].apply(clean_text)

    # Remove empty tweets
    df = df[df["clean_text"].str.len() > 0].copy()

    if len(df) == 0:
        print("⚠ No valid tweets found after cleaning")
        return

    print(f"📝 Analyzing sentiment for {len(df)} tweets...")

    # Analyze sentiment
    df["sentiment"] = df["clean_text"].apply(analyze_text)
    df["label"] = df["sentiment"].apply(lambda x: "positive" if x > 0.1 else "negative" if x < -0.1 else "neutral")

    # Convert date column
    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"], errors='coerce')
    else:
        df["date"] = datetime.now()

    # Create monthly aggregation
    df["month"] = df["date"].dt.to_period("M")
    df["year"] = df["date"].dt.year

    # Create time series summary
    summary = df.groupby("month").agg({
        "sentiment": ["mean", "std", "count"],
        "label": lambda x: x.value_counts().to_dict()
    }).round(3)

    # Flatten column names
    summary.columns = ["_".join(col).strip() for col in summary.columns]
    summary = summary.reset_index()

    # Save results
    df.to_csv(OUTT/"twitter_sentiment_detailed.csv", index=False)
    summary.to_csv(OUTT/"twitter_sentiment_timeseries.csv", index=False)

    print("✅ Sentiment analysis complete!")
    print(f"📈 Average sentiment: {df['sentiment'].mean():.3f}")
    print(f"📊 Sentiment distribution: {df['label'].value_counts().to_dict()}")

    # State-wise analysis if location data available
    if "user_location" in df.columns:
        state_summary = df.groupby("user_location")["sentiment"].mean().round(3)
        state_summary.to_csv(OUTT/"twitter_sentiment_by_state.csv")
        print("✅ State-wise sentiment analysis saved.")

if __name__ == "__main__":
    fetch_or_load()
