"""
Data Extraction Module for Vaccine Hesitancy Research
Extracts data from NFHS-5, Twitter/X, and Google Trends
"""

import pandas as pd
import numpy as np
from pathlib import Path
import os
import requests
from datetime import datetime, timedelta
import time
import json

BASE = Path("projects/vaccine_hesitancy")
DATA_DIR = BASE/"data"
NFHS_DIR = DATA_DIR/"nfhs"
TWITTER_DIR = DATA_DIR/"twitter"
TRENDS_DIR = DATA_DIR/"trends"

def setup_directories():
    """Create necessary directories for data storage"""
    for dir_path in [NFHS_DIR, TWITTER_DIR, TRENDS_DIR]:
        dir_path.mkdir(parents=True, exist_ok=True)

def extract_nfhs_data():
    """Extract NFHS-5 data for vaccine hesitancy analysis"""
    print("🔍 Searching for NFHS-5 vaccine hesitancy data...")

    # NFHS-5 data sources
    nfhs_sources = {
        'vaccination': 'https://dhsprogram.com/pubs/pdf/FR375/FR375.pdf',
        'data_files': 'https://www.dhsprogram.com/data/dataset/India_Standard-DHS_2021.cfm',
        'women_questionnaire': 'https://dhsprogram.com/pubs/pdf/DHSQ8/DHSQ8.pdf'
    }

    # Try to find vaccine-related variables in NFHS-5
    vaccine_variables = [
        'vaccination_status', 'vaccine_hesitant', 'child_vaccination',
        'vaccine_attitude', 'immunization', 'vaccine_refusal'
    ]

    print("📊 NFHS-5 vaccine-related variables to extract:")
    for var in vaccine_variables:
        print(f"  - {var}")

    # Create sample NFHS data structure
    sample_nfhs_data = create_sample_nfhs_data()
    sample_nfhs_data.to_csv(NFHS_DIR/"nfhs5_vaccine_sample.csv", index=False)
    print("✅ Sample NFHS-5 data created. Replace with actual data.")

def create_sample_nfhs_data():
    """Create sample NFHS-5 data structure for testing"""
    np.random.seed(42)
    n_samples = 1000

    states = ['Maharashtra', 'Uttar Pradesh', 'Bihar', 'West Bengal', 'Tamil Nadu',
              'Rajasthan', 'Karnataka', 'Gujarat', 'Andhra Pradesh', 'Odisha']

    data = {
        'state': np.random.choice(states, n_samples),
        'gender': np.random.choice(['Male', 'Female'], n_samples),
        'education': np.random.choice(['No Education', 'Primary', 'Secondary', 'Higher'], n_samples),
        'income': np.random.choice(['Low', 'Middle', 'High'], n_samples),
        'religion': np.random.choice(['Hindu', 'Muslim', 'Christian', 'Sikh', 'Other'], n_samples),
        'age': np.random.randint(18, 65, n_samples),
        'vaccine_hesitant': np.random.choice([0, 1], n_samples, p=[0.7, 0.3]),
        'vaccination_status': np.random.choice([0, 1], n_samples, p=[0.2, 0.8]),
        'rural_urban': np.random.choice(['Rural', 'Urban'], n_samples),
        'wealth_index': np.random.choice(['Poorest', 'Poorer', 'Middle', 'Richer', 'Richest'], n_samples)
    }

    return pd.DataFrame(data)

def extract_twitter_data():
    """Extract Twitter/X data for vaccine sentiment analysis"""
    print("🐦 Extracting Twitter/X data for vaccine sentiment...")

    # Since we don't have Twitter API access, create sample data
    # In production, this would use Tweepy API or fetch from existing datasets

    sample_tweets = create_sample_twitter_data()
    sample_tweets.to_csv(TWITTER_DIR/"vaccine_tweets_india.csv", index=False)
    print("✅ Sample Twitter data created. Replace with actual API data.")

def create_sample_twitter_data():
    """Create sample Twitter data for vaccine sentiment analysis"""
    np.random.seed(42)
    n_tweets = 500

    # Sample vaccine-related tweets in India context
    tweet_templates = [
        "Vaccines are important for public health #VaccineForAll",
        "Not sure about COVID vaccine safety 😟 #VaccineHesitancy",
        "Got my vaccine today! Feeling protected 💉 #VaccinationDrive",
        "Traditional medicine is better than vaccines #AlternativeMedicine",
        "Government should make vaccines mandatory #PublicHealth",
        "Worried about vaccine side effects #VaccineSafety",
        "Proud to be vaccinated! #Vaccinated",
        "Vaccines are a conspiracy #AntiVax",
        "Children need all recommended vaccines #ChildHealth",
        "Vaccine misinformation is dangerous #FactCheck"
    ]

    data = []
    base_date = datetime(2021, 1, 1)

    for i in range(n_tweets):
        tweet = np.random.choice(tweet_templates)
        date = base_date + timedelta(days=np.random.randint(0, 365*3))

        data.append({
            'text': tweet,
            'date': date.strftime('%Y-%m-%d'),
            'user_location': np.random.choice(['Mumbai', 'Delhi', 'Bangalore', 'Chennai', 'Kolkata', 'Hyderabad', 'Pune', 'Ahmedabad'], 1)[0],
            'retweets': np.random.randint(0, 100),
            'likes': np.random.randint(0, 200)
        })

    return pd.DataFrame(data)

def extract_google_trends():
    """Extract Google Trends data for vaccine searches"""
    print("📈 Extracting Google Trends data...")

    # Create sample Google Trends data
    sample_trends = create_sample_trends_data()
    sample_trends.to_csv(TRENDS_DIR/"vaccine_trends_india.csv", index=False)
    print("✅ Sample Google Trends data created.")

def create_sample_trends_data():
    """Create sample Google Trends data"""
    np.random.seed(42)

    # Vaccine-related search terms
    search_terms = ['COVID vaccine', 'vaccine registration', 'vaccine side effects',
                   'vaccine for children', 'COVID vaccine booking']

    data = []
    base_date = datetime(2021, 1, 1)

    for term in search_terms:
        for i in range(365*2):  # 2 years of daily data
            date = base_date + timedelta(days=i)
            # Simulate trend with seasonal patterns and peaks
            trend_value = 20 + 30*np.sin(2*np.pi*i/365) + np.random.normal(0, 10)
            trend_value = max(0, min(100, trend_value))  # Clamp between 0-100

            data.append({
                'date': date.strftime('%Y-%m-%d'),
                'search_term': term,
                'trend_value': int(trend_value),
                'region': 'India'
            })

    return pd.DataFrame(data)

def extract_news_articles():
    """Extract news articles related to vaccine hesitancy"""
    print("📰 Extracting news articles...")

    # This would typically use news APIs like NewsAPI, Google News, etc.
    # For now, create sample data
    sample_news = create_sample_news_data()
    sample_news.to_csv(DATA_DIR/"vaccine_news_articles.csv", index=False)
    print("✅ Sample news data created.")

def create_sample_news_data():
    """Create sample news articles data"""
    news_data = [
        {
            'title': 'Vaccine Hesitancy Remains High in Rural India',
            'source': 'The Hindu',
            'date': '2023-03-15',
            'url': 'https://example.com/news1',
            'content': 'Despite government efforts, vaccine hesitancy continues to be a challenge in rural areas...',
            'sentiment': 'negative'
        },
        {
            'title': 'COVID Vaccination Drive Shows Promising Results',
            'source': 'Times of India',
            'date': '2023-04-20',
            'url': 'https://example.com/news2',
            'content': 'India achieves major milestone in vaccination coverage...',
            'sentiment': 'positive'
        },
        {
            'title': 'Misinformation Spreads on Social Media About Vaccines',
            'source': 'Indian Express',
            'date': '2023-05-10',
            'url': 'https://example.com/news3',
            'content': 'Health experts warn about vaccine misinformation on WhatsApp and Facebook...',
            'sentiment': 'negative'
        }
    ]

    return pd.DataFrame(news_data)

def main():
    """Main function to extract all data sources"""
    print("🚀 Starting data extraction for Vaccine Hesitancy Research...")

    setup_directories()

    # Extract data from different sources
    extract_nfhs_data()
    extract_twitter_data()
    extract_google_trends()
    extract_news_articles()

    print("\n✅ Data extraction complete!")
    print("📁 Data files created in:")
    print(f"  - NFHS: {NFHS_DIR}")
    print(f"  - Twitter: {TWITTER_DIR}")
    print(f"  - Trends: {TRENDS_DIR}")
    print(f"  - News: {DATA_DIR}")

    print("\n📝 Next steps:")
    print("1. Replace sample data with actual datasets")
    print("2. Run: python projects/vaccine_hesitancy/scripts/clean_data.py")
    print("3. Run: python projects/vaccine_hesitancy/run_all.py")

if __name__ == "__main__":
    main()
